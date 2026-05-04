#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "click>=8.1",
#   "requests>=2.31",
#   "dateparser>=1.2",
#   "rich>=13.7",
#   "tzlocal>=5.2",
# ]
# ///
"""
Cal.com CLI - A command-line interface for managing your personal Cal.com calendar.

Usage:
    uv run cal_cli.py [COMMAND] [OPTIONS]

Commands:
    me                    - Show authenticated user (sanity-check your API key)
    event-types list      - List your event types (find IDs for `bookings create`)

    busy add              - Block time as out-of-office
    busy list             - List your OOO entries
    busy delete <id>      - Remove an OOO entry

    bookings create       - Create a booking on a specific event type
    bookings list         - List bookings (filter by date range, status, attendee)
    bookings cancel <uid> - Cancel a booking by UID

Examples:
    uv run cal_cli.py me
    uv run cal_cli.py busy add --in 30m --for 90m
    uv run cal_cli.py busy add --start "tomorrow 2pm" --end "tomorrow 4pm"
    uv run cal_cli.py bookings create -e 123 --email a@b.com -n "Jane" --start "next mon 10am"
    uv run cal_cli.py bookings list --from today --to "next week"
    uv run cal_cli.py bookings cancel abc123uid --reason "Reschedule"

Auth:
    Put your API key in a .env file beside this script:
        CAL_API_KEY=cal_live_xxxxxxxxxxxx
    Generate one at: Cal.com -> Settings -> Developer -> API Keys
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

import click
import dateparser
import requests
import tzlocal
from rich.console import Console
from rich.table import Table


# =============================================================================
# Configuration
# =============================================================================

BASE_URL = "https://api.cal.com/v2"

# Cal.com versions endpoints independently. Bump these when their docs change.
API_VERSIONS = {
    "me": "2024-08-13",
    "event-types": "2024-06-14",
    "bookings": "2024-08-13",
    "out-of-office": "2024-06-11",
}

console = Console()


def load_api_key() -> str:
    """Load API key from .env file in the script's directory."""
    env_path = Path(__file__).parent / ".env"
    if not env_path.exists():
        raise click.ClickException(
            f".env file not found at {env_path}\n"
            "Create one with: CAL_API_KEY=cal_live_xxxxx\n"
            "(Generate at Cal.com -> Settings -> Developer -> API Keys)"
        )

    with env_path.open() as f:
        for line in f:
            line = line.strip()
            if line.startswith("CAL_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")

    raise click.ClickException("CAL_API_KEY not found in .env file")


def get_api_key() -> str:
    if not hasattr(get_api_key, "_cached_key"):
        get_api_key._cached_key = load_api_key()
    return get_api_key._cached_key


# =============================================================================
# Time parsing
# =============================================================================

_DURATION_RE = re.compile(r"(\d+)\s*([smhd])", re.IGNORECASE)
_DURATION_UNITS = {"s": "seconds", "m": "minutes", "h": "hours", "d": "days"}


def parse_duration(s: str) -> timedelta:
    """Parse '30m', '1h30m', '2h', '90s', '1d' into a timedelta."""
    s = s.strip().lower().replace(" ", "")
    if not s:
        raise click.BadParameter("empty duration")

    matches = _DURATION_RE.findall(s)
    if not matches:
        raise click.BadParameter(
            f"could not parse duration {s!r}. "
            "Use forms like '30m', '1h30m', '2h', '1d'."
        )

    # Make sure we consumed the whole string (no junk like '30x')
    consumed = "".join(f"{n}{u}" for n, u in matches)
    if consumed != s:
        raise click.BadParameter(f"could not parse duration {s!r}")

    kwargs: dict[str, int] = {}
    for value, unit in matches:
        key = _DURATION_UNITS[unit.lower()]
        kwargs[key] = kwargs.get(key, 0) + int(value)
    return timedelta(**kwargs)


def parse_when(s: str, *, prefer_future: bool = True) -> datetime:
    """Parse human-friendly time into a UTC, timezone-aware datetime.

    Accepts ISO ('2026-05-05T14:00'), natural ('tomorrow 2pm', 'next monday 10am',
    'today', 'next week'), and dash forms ('next-week' -> 'next week').
    Naive results are interpreted in the system's local timezone.
    """
    raw = s.strip()
    # Allow CLI-friendly hyphenated forms like 'next-week'
    normalized = raw.replace("-week", " week").replace("-month", " month")
    # Don't mangle dashes inside ISO dates ('2026-05-05')
    if re.match(r"^\d{4}-\d{2}-\d{2}", raw):
        normalized = raw

    settings = {
        "PREFER_DATES_FROM": "future" if prefer_future else "current_period",
        "RETURN_AS_TIMEZONE_AWARE": True,
    }
    dt = dateparser.parse(normalized, settings=settings)
    if dt is None:
        raise click.BadParameter(
            f"could not parse time {s!r}. "
            "Try '2026-05-05T14:00', 'tomorrow 2pm', or 'next monday 10am'."
        )
    if dt.tzinfo is None:
        # Attach local tz, then convert
        dt = dt.astimezone()
    return dt.astimezone(timezone.utc)


def to_iso_z(dt: datetime) -> str:
    """Format a UTC datetime as ISO 8601 with 'Z' suffix."""
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")


def fmt_local(iso_str: str) -> str:
    """Format a Cal.com ISO timestamp in the local timezone for display."""
    if not iso_str:
        return ""
    try:
        # Handle both '...Z' and '...+00:00'
        s = iso_str.replace("Z", "+00:00")
        dt = datetime.fromisoformat(s).astimezone()
        return dt.strftime("%Y-%m-%d %H:%M %Z").strip()
    except (ValueError, TypeError):
        return iso_str


# =============================================================================
# API client
# =============================================================================


class CalAPI:
    """Cal.com API v2 client."""

    def __init__(self) -> None:
        self.api_key = get_api_key()
        self.base_url = BASE_URL

    def _request(
        self,
        method: str,
        endpoint: str,
        version_key: str,
        **kwargs: Any,
    ) -> dict:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        headers = kwargs.pop("headers", {}) or {}
        headers.setdefault("Authorization", f"Bearer {self.api_key}")
        headers.setdefault("cal-api-version", API_VERSIONS[version_key])
        headers.setdefault("Content-Type", "application/json")

        response = requests.request(method, url, headers=headers, **kwargs)

        if not response.ok:
            raise click.ClickException(
                f"API error {response.status_code} on {method} {endpoint}: "
                f"{response.text}"
            )
        if response.status_code == 204 or not response.content:
            return {}
        try:
            return response.json()
        except ValueError:
            return {"raw": response.text}

    # ----- /me ----------------------------------------------------------------

    def get_me(self) -> dict:
        return self._request("GET", "/me", "me")

    # ----- /event-types -------------------------------------------------------

    def list_event_types(self) -> dict:
        return self._request("GET", "/event-types", "event-types")

    # ----- /bookings ----------------------------------------------------------

    def list_bookings(
        self,
        *,
        status: Optional[str] = None,
        after_start: Optional[str] = None,
        before_end: Optional[str] = None,
        attendee_email: Optional[str] = None,
        attendee_name: Optional[str] = None,
        take: int = 50,
    ) -> dict:
        params: dict[str, Any] = {"take": take}
        if status:
            params["status"] = status
        if after_start:
            params["afterStart"] = after_start
        if before_end:
            params["beforeEnd"] = before_end
        if attendee_email:
            params["attendeeEmail"] = attendee_email
        if attendee_name:
            params["attendeeName"] = attendee_name
        return self._request("GET", "/bookings", "bookings", params=params)

    def create_booking(self, payload: dict) -> dict:
        return self._request("POST", "/bookings", "bookings", json=payload)

    def cancel_booking(self, uid: str, reason: Optional[str] = None) -> dict:
        body = {"cancellationReason": reason} if reason else {}
        return self._request(
            "POST", f"/bookings/{uid}/cancel", "bookings", json=body
        )

    # ----- /out-of-office -----------------------------------------------------

    def create_ooo(self, payload: dict) -> dict:
        return self._request("POST", "/out-of-office", "out-of-office", json=payload)

    def list_ooo(self) -> dict:
        return self._request("GET", "/out-of-office", "out-of-office")

    def delete_ooo(self, ooo_id: str) -> dict:
        return self._request(
            "DELETE", f"/out-of-office/{ooo_id}", "out-of-office"
        )


# =============================================================================
# Output helpers
# =============================================================================


def emit_dry_run(method: str, endpoint: str, body: dict) -> None:
    click.echo(click.style(f"[dry-run] {method} {endpoint}", fg="yellow", bold=True))
    click.echo(json.dumps(body, indent=2))


def unwrap(resp: dict) -> Any:
    """Cal.com wraps payloads as {status, data}. Return data if present."""
    if isinstance(resp, dict) and "data" in resp:
        return resp["data"]
    return resp


# =============================================================================
# CLI
# =============================================================================


@click.group()
@click.version_option(version="0.1.0", prog_name="calx")
@click.pass_context
def cli(ctx: click.Context) -> None:
    """
    calx - Lightweight CLI for managing your Cal.com calendar.

    Configure your API key in a .env file beside this script:

        CAL_API_KEY=cal_live_xxxxx

    Run 'calx COMMAND --help' for details on a command.
    """
    ctx.ensure_object(dict)
    # Lazy-init API: --help shouldn't require an API key.
    ctx.obj["_api"] = None


def get_api(ctx: click.Context) -> CalAPI:
    if ctx.obj.get("_api") is None:
        ctx.obj["_api"] = CalAPI()
    return ctx.obj["_api"]


# ----- me --------------------------------------------------------------------


@cli.command("me")
@click.pass_context
def cmd_me(ctx: click.Context) -> None:
    """Show the authenticated user's profile."""
    api = get_api(ctx)
    me = unwrap(api.get_me()) or {}
    click.echo(click.style("Authenticated as:", fg="green", bold=True))
    click.echo(f"  ID:       {me.get('id')}")
    click.echo(f"  Username: {me.get('username')}")
    click.echo(f"  Email:    {me.get('email')}")
    if me.get("timeZone"):
        click.echo(f"  TimeZone: {me.get('timeZone')}")


# ----- event-types -----------------------------------------------------------


@cli.group("event-types")
def event_types_group() -> None:
    """Inspect your event types."""


@event_types_group.command("list")
@click.pass_context
def cmd_event_types_list(ctx: click.Context) -> None:
    """List your event types (use the IDs for `bookings create`)."""
    api = get_api(ctx)
    data = unwrap(api.list_event_types()) or []
    # API may return {eventTypeGroups: [...]} or a flat list. Handle both.
    rows: list[dict] = []
    if isinstance(data, list):
        rows = data
    elif isinstance(data, dict) and "eventTypeGroups" in data:
        for group in data["eventTypeGroups"]:
            rows.extend(group.get("eventTypes") or [])

    if not rows:
        click.echo("No event types found.")
        return

    table = Table(title="Event Types", show_lines=False)
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Title")
    table.add_column("Slug")
    table.add_column("Length")
    for et in rows:
        table.add_row(
            str(et.get("id", "")),
            str(et.get("title", "") or et.get("name", "")),
            str(et.get("slug", "")),
            f"{et.get('lengthInMinutes') or et.get('length', '')}m",
        )
    console.print(table)


# ----- busy ------------------------------------------------------------------


VALID_OOO_REASONS = {"unspecified", "vacation", "travel", "sick", "public_holiday"}


@cli.group("busy")
def busy_group() -> None:
    """Block time as out-of-office (OOO)."""


@busy_group.command("add")
@click.option("--start", "start_str", help="Start time (e.g. '2026-05-05T14:00', 'tomorrow 2pm').")
@click.option("--end", "end_str", help="End time (e.g. 'tomorrow 4pm').")
@click.option("--in", "in_dur", help="Start in DURATION from now (e.g. '30m', '1h30m').")
@click.option("--for", "for_dur", help="Duration from start (e.g. '90m', '2h'). Pairs with --in or --start.")
@click.option("--until", "until_str", help="End at this time. Pairs with --in or --start.")
@click.option(
    "--reason",
    type=click.Choice(sorted(VALID_OOO_REASONS)),
    default="unspecified",
    show_default=True,
    help="OOO reason.",
)
@click.option("--notes", default=None, help="Optional notes.")
@click.option("--dry-run", is_flag=True, help="Print the request without sending.")
@click.pass_context
def cmd_busy_add(
    ctx: click.Context,
    start_str: Optional[str],
    end_str: Optional[str],
    in_dur: Optional[str],
    for_dur: Optional[str],
    until_str: Optional[str],
    reason: str,
    notes: Optional[str],
    dry_run: bool,
) -> None:
    """Block time. Provide --start/--end, or --in/--for, or --in/--until."""
    if start_str and in_dur:
        raise click.UsageError("use either --start or --in, not both")
    if not start_str and not in_dur:
        raise click.UsageError("provide --start or --in")

    if start_str:
        start = parse_when(start_str)
    else:
        start = datetime.now(timezone.utc) + parse_duration(in_dur)  # type: ignore[arg-type]

    end_inputs = sum(bool(x) for x in (end_str, for_dur, until_str))
    if end_inputs == 0:
        raise click.UsageError("provide --end, --for, or --until")
    if end_inputs > 1:
        raise click.UsageError("provide only one of --end, --for, --until")

    if end_str:
        end = parse_when(end_str)
    elif for_dur:
        end = start + parse_duration(for_dur)
    else:
        end = parse_when(until_str)  # type: ignore[arg-type]

    if end <= start:
        raise click.UsageError("end must be after start")

    payload: dict[str, Any] = {
        "start": to_iso_z(start),
        "end": to_iso_z(end),
        "reason": reason,
    }
    if notes:
        payload["notes"] = notes

    if dry_run:
        emit_dry_run("POST", "/v2/out-of-office", payload)
        return

    api = get_api(ctx)
    result = unwrap(api.create_ooo(payload))
    click.echo(click.style("OOO entry created.", fg="green"))
    if isinstance(result, dict):
        click.echo(f"  ID:     {result.get('id')}")
        click.echo(f"  Start:  {fmt_local(result.get('start', payload['start']))}")
        click.echo(f"  End:    {fmt_local(result.get('end', payload['end']))}")
        click.echo(f"  Reason: {result.get('reason', reason)}")


@busy_group.command("list")
@click.pass_context
def cmd_busy_list(ctx: click.Context) -> None:
    """List your OOO entries."""
    api = get_api(ctx)
    data = unwrap(api.list_ooo()) or []
    if not isinstance(data, list):
        data = data.get("entries") or data.get("oooEntries") or []
    if not data:
        click.echo("No OOO entries.")
        return

    table = Table(title="Out of Office", show_lines=False)
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Start")
    table.add_column("End")
    table.add_column("Reason")
    table.add_column("Notes")
    for ooo in data:
        table.add_row(
            str(ooo.get("id", "")),
            fmt_local(ooo.get("start", "")),
            fmt_local(ooo.get("end", "")),
            str(ooo.get("reason", "") or ""),
            str(ooo.get("notes", "") or ""),
        )
    console.print(table)


@busy_group.command("delete")
@click.argument("ooo_id")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation.")
@click.pass_context
def cmd_busy_delete(ctx: click.Context, ooo_id: str, yes: bool) -> None:
    """Delete an OOO entry by ID."""
    if not yes and not click.confirm(f"Delete OOO entry {ooo_id}?"):
        click.echo("Cancelled.")
        return
    api = get_api(ctx)
    api.delete_ooo(ooo_id)
    click.echo(click.style(f"OOO entry {ooo_id} deleted.", fg="green"))


# ----- bookings --------------------------------------------------------------


@cli.group("bookings")
def bookings_group() -> None:
    """Create, list, and cancel bookings."""


@bookings_group.command("create")
@click.option("--event-type", "-e", "event_type", type=int, required=True, help="Event type ID.")
@click.option("--email", required=True, help="Attendee email.")
@click.option("--name", "-n", required=True, help="Attendee name.")
@click.option("--start", "start_str", required=True, help="Start time (e.g. 'tomorrow 10am').")
@click.option(
    "--timezone",
    "tz",
    default=None,
    help="Attendee timezone IANA name (e.g. 'America/New_York'). Defaults to your local tz.",
)
@click.option("--guests", multiple=True, help="Additional guest emails (repeatable).")
@click.option("--dry-run", is_flag=True, help="Print the request without sending.")
@click.pass_context
def cmd_bookings_create(
    ctx: click.Context,
    event_type: int,
    email: str,
    name: str,
    start_str: str,
    tz: Optional[str],
    guests: tuple[str, ...],
    dry_run: bool,
) -> None:
    """Create a booking on an event type."""
    start = parse_when(start_str)
    if tz is None:
        # Cal.com requires IANA zone names (e.g. 'Asia/Kolkata'), not abbrevs.
        tz = str(tzlocal.get_localzone_name() or "UTC")

    payload: dict[str, Any] = {
        "start": to_iso_z(start),
        "eventTypeId": event_type,
        "attendee": {
            "name": name,
            "email": email,
            "timeZone": tz,
        },
    }
    if guests:
        payload["guests"] = list(guests)

    if dry_run:
        emit_dry_run("POST", "/v2/bookings", payload)
        return

    api = get_api(ctx)
    result = unwrap(api.create_booking(payload))
    click.echo(click.style("Booking created.", fg="green"))
    if isinstance(result, dict):
        click.echo(f"  UID:    {result.get('uid')}")
        click.echo(f"  Title:  {result.get('title', '')}")
        click.echo(f"  Start:  {fmt_local(result.get('start', payload['start']))}")
        click.echo(f"  End:    {fmt_local(result.get('end', ''))}")
        click.echo(f"  Status: {result.get('status', '')}")


@bookings_group.command("list")
@click.option("--from", "from_str", default=None, help="Earliest start (e.g. 'today').")
@click.option("--to", "to_str", default=None, help="Latest end (e.g. 'next week').")
@click.option(
    "--status",
    type=click.Choice(["upcoming", "recurring", "past", "cancelled", "unconfirmed"]),
    default=None,
    help="Filter by booking status.",
)
@click.option("--email", default=None, help="Filter by attendee email.")
@click.option("--name", default=None, help="Filter by attendee name.")
@click.option("--limit", default=20, show_default=True, help="Max results.")
@click.pass_context
def cmd_bookings_list(
    ctx: click.Context,
    from_str: Optional[str],
    to_str: Optional[str],
    status: Optional[str],
    email: Optional[str],
    name: Optional[str],
    limit: int,
) -> None:
    """List bookings."""
    api = get_api(ctx)
    after_start = to_iso_z(parse_when(from_str)) if from_str else None
    before_end = to_iso_z(parse_when(to_str)) if to_str else None

    resp = api.list_bookings(
        status=status,
        after_start=after_start,
        before_end=before_end,
        attendee_email=email,
        attendee_name=name,
        take=limit,
    )
    data = unwrap(resp) or []
    # Some Cal.com responses return {bookings: [...]} or a list directly
    if isinstance(data, dict):
        data = data.get("bookings") or data.get("data") or []
    if not data:
        click.echo("No bookings found.")
        return

    table = Table(title="Bookings", show_lines=False)
    table.add_column("Time", style="cyan")
    table.add_column("Attendee")
    table.add_column("Event")
    table.add_column("Status")
    table.add_column("UID", no_wrap=True)
    for b in data:
        attendees = b.get("attendees") or []
        first = attendees[0] if attendees else {}
        attendee_str = (
            f"{first.get('name', '')} <{first.get('email', '')}>"
            if first
            else ""
        )
        table.add_row(
            fmt_local(b.get("start", "")),
            attendee_str,
            str(b.get("title", "") or b.get("eventType", {}).get("title", "")),
            str(b.get("status", "")),
            str(b.get("uid", "")),
        )
    console.print(table)


@bookings_group.command("cancel")
@click.argument("booking_uid")
@click.option("--reason", default=None, help="Cancellation reason.")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation.")
@click.option("--dry-run", is_flag=True, help="Print the request without sending.")
@click.pass_context
def cmd_bookings_cancel(
    ctx: click.Context,
    booking_uid: str,
    reason: Optional[str],
    yes: bool,
    dry_run: bool,
) -> None:
    """Cancel a booking by UID."""
    body: dict[str, Any] = {}
    if reason:
        body["cancellationReason"] = reason

    if dry_run:
        emit_dry_run("POST", f"/v2/bookings/{booking_uid}/cancel", body)
        return

    if not yes and not click.confirm(f"Cancel booking {booking_uid}?"):
        click.echo("Cancelled.")
        return

    api = get_api(ctx)
    api.cancel_booking(booking_uid, reason=reason)
    click.echo(click.style(f"Booking {booking_uid} cancelled.", fg="green"))


# =============================================================================
# Entry point
# =============================================================================

if __name__ == "__main__":
    cli()
