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

    block add             - Block time. Routes to OOO for full days, schedule
                            overrides for hour-bounded blocks. (See "Block routing"
                            below for details.)
    block list            - List active blocks (OOO entries + schedule overrides)
    block delete <id>     - Remove a block (OOO id, or override date)

    bookings create       - Create a booking on a specific event type
    bookings list         - List bookings (filter by date range, status, attendee)
    bookings cancel <uid> - Cancel a booking by UID

Examples:
    uv run cal_cli.py me
    uv run cal_cli.py block add --in 30m --for 90m
    uv run cal_cli.py block add --start "tomorrow 10am" --end "tomorrow 7pm"
    uv run cal_cli.py block add --start "wed 5:30pm" --end "thu 12pm"
    uv run cal_cli.py bookings create -e 123 --email a@b.com -n "Jane" --start "next mon 10am"
    uv run cal_cli.py bookings list --from today --to "next week"
    uv run cal_cli.py bookings cancel abc123uid --reason "Reschedule"

Block routing:
    Cal.com's OOO endpoint is day-granular (00:00-23:59 only) and can't express
    "block 10am-7pm Tuesday". The hour-granular path is schedule overrides, which
    *replace* the weekly availability for a date with the windows you submit.

    `block add` splits your block into per-day chunks in the schedule's timezone,
    fetches your default schedule, and for each day:
      - if the chunk fully covers that day's available windows -> OOO entry
        (consecutive full-block days are merged into one multi-day OOO)
      - otherwise -> a schedule override that lists the available windows that
        remain after subtracting the block

    Net effect: you specify a time range to block, and the CLI picks the right
    endpoint (or both) under the hood.

Auth:
    Put your API key in a .env file beside this script:
        CAL_API_KEY=cal_live_xxxxxxxxxxxx
    Generate one at: Cal.com -> Settings -> Developer -> API Keys
"""

from __future__ import annotations

import json
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional
from zoneinfo import ZoneInfo

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
    "schedules": "2024-06-11",
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

    # ----- /me/ooo ------------------------------------------------------------
    # Cal.com renamed the OOO endpoints from /out-of-office to /me/ooo.

    def create_ooo(self, payload: dict) -> dict:
        return self._request("POST", "/me/ooo", "out-of-office", json=payload)

    def list_ooo(self) -> dict:
        return self._request("GET", "/me/ooo", "out-of-office")

    def delete_ooo(self, ooo_id: str) -> dict:
        return self._request(
            "DELETE", f"/me/ooo/{ooo_id}", "out-of-office"
        )

    # ----- /schedules ---------------------------------------------------------

    def get_default_schedule(self) -> dict:
        return self._request("GET", "/schedules/default", "schedules")

    def update_schedule(self, schedule_id: int, payload: dict) -> dict:
        return self._request(
            "PATCH", f"/schedules/{schedule_id}", "schedules", json=payload
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
# Block planning (pure functions; no I/O)
#
# A "block" is a wall-clock time range the user wants to mark unavailable.
# Cal.com offers two endpoints with different granularities:
#
#   * /me/ooo - day-level only. Anything you POST gets normalized to
#     00:00-23:59 UTC of the start/end date. Good for "I'm out Tue-Thu."
#   * PATCH /schedules/{id}.overrides - per-date windows that REPLACE the
#     weekly availability for that date. Good for "block 10am-7pm Tuesday."
#
# The planner splits a block into per-day chunks in the schedule's timezone,
# classifies each chunk as either "fully covers all available windows on
# that day" (-> OOO) or "leaves some availability" (-> override with the
# remaining windows), then groups consecutive full-block days into single
# multi-day OOO ranges.
# =============================================================================


def hhmm_to_minutes(hhmm: str) -> int:
    """'10:30' -> 630."""
    h, m = hhmm.split(":")
    return int(h) * 60 + int(m)


def minutes_to_hhmm(m: int) -> str:
    """630 -> '10:30'. Caps at 23:59 (Cal.com's max valid endTime)."""
    m = max(0, min(m, 24 * 60 - 1))
    return f"{m // 60:02d}:{m % 60:02d}"


def split_block_into_local_days(
    start_utc: datetime, end_utc: datetime, tz: ZoneInfo
) -> list[tuple[str, int, int]]:
    """Split a UTC datetime range into per-local-day chunks.

    Returns: list of (date_iso, start_minute_of_day, end_minute_of_day).
    end_minute is in [1, 1440]; 1440 means "through end of that local day."
    """
    start_local = start_utc.astimezone(tz)
    end_local = end_utc.astimezone(tz)
    chunks: list[tuple[str, int, int]] = []
    cursor = start_local
    while cursor < end_local:
        next_midnight = (cursor + timedelta(days=1)).replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        chunk_end = min(next_midnight, end_local)
        date_iso = cursor.date().isoformat()
        start_min = cursor.hour * 60 + cursor.minute
        if chunk_end.date() != cursor.date():
            end_min = 24 * 60  # spans through midnight
        else:
            end_min = chunk_end.hour * 60 + chunk_end.minute
        chunks.append((date_iso, start_min, end_min))
        cursor = chunk_end
    return chunks


def windows_for_weekday(schedule: dict, weekday_name: str) -> list[tuple[int, int]]:
    """Return the weekly availability windows for a given weekday name."""
    out: list[tuple[int, int]] = []
    for entry in schedule.get("availability", []) or []:
        if weekday_name in (entry.get("days") or []):
            out.append(
                (
                    hhmm_to_minutes(entry["startTime"]),
                    hhmm_to_minutes(entry["endTime"]),
                )
            )
    return sorted(out)


def overrides_for_date(schedule: dict, date_iso: str) -> list[tuple[int, int]]:
    """Return any existing override windows for a specific date."""
    out: list[tuple[int, int]] = []
    for ov in schedule.get("overrides", []) or []:
        if ov.get("date") == date_iso:
            out.append(
                (hhmm_to_minutes(ov["startTime"]), hhmm_to_minutes(ov["endTime"]))
            )
    return sorted(out)


def effective_windows(schedule: dict, date_iso: str) -> list[tuple[int, int]]:
    """Return the *effective* available windows on a date.

    If an override exists for that date, it replaces the weekly schedule for
    that date (per Cal.com semantics). Otherwise weekly availability applies.
    """
    existing = overrides_for_date(schedule, date_iso)
    if existing:
        return existing
    weekday = date.fromisoformat(date_iso).strftime("%A")
    return windows_for_weekday(schedule, weekday)


def subtract_block(
    windows: list[tuple[int, int]], block_start: int, block_end: int
) -> list[tuple[int, int]]:
    """Subtract [block_start, block_end] from each window. Returns remaining windows."""
    out: list[tuple[int, int]] = []
    for w_start, w_end in windows:
        if block_end <= w_start or block_start >= w_end:
            out.append((w_start, w_end))  # no overlap
            continue
        if w_start < block_start:
            out.append((w_start, block_start))
        if block_end < w_end:
            out.append((block_end, w_end))
    return out


def classify_day(
    schedule: dict, date_iso: str, block_start: int, block_end: int
) -> dict:
    """Decide what to do with a single day's chunk of the block.

    Returns dict with keys:
      date, type ('full'|'partial'|'noop'), original_windows, remaining_windows
    """
    original = effective_windows(schedule, date_iso)
    if not original:
        # Day already had no availability (e.g., Sunday with no schedule entry).
        # Block is a no-op for this day.
        return {
            "date": date_iso,
            "type": "noop",
            "original_windows": [],
            "remaining_windows": [],
        }
    remaining = subtract_block(original, block_start, block_end)
    if not remaining:
        # Block fully covers all available windows -> use OOO for this day.
        return {
            "date": date_iso,
            "type": "full",
            "original_windows": original,
            "remaining_windows": [],
        }
    return {
        "date": date_iso,
        "type": "partial",
        "original_windows": original,
        "remaining_windows": remaining,
    }


def group_consecutive_full_days(
    classifications: list[dict],
) -> list[tuple[date, date]]:
    """Collapse runs of consecutive 'full' days into (start_date, end_date) ranges."""
    groups: list[tuple[date, date]] = []
    current: Optional[tuple[date, date]] = None
    for c in classifications:
        if c["type"] == "full":
            d = date.fromisoformat(c["date"])
            if current is None:
                current = (d, d)
            elif d == current[1] + timedelta(days=1):
                current = (current[0], d)
            else:
                groups.append(current)
                current = (d, d)
        else:
            if current is not None:
                groups.append(current)
                current = None
    if current is not None:
        groups.append(current)
    return groups


def merge_overrides(
    existing: list[dict], new_per_date: dict[str, list[tuple[int, int]]]
) -> list[dict]:
    """Drop existing overrides on affected dates; add new ones. Stable-sort the result."""
    affected = set(new_per_date.keys())
    out = [
        {"date": o["date"], "startTime": o["startTime"], "endTime": o["endTime"]}
        for o in (existing or [])
        if o.get("date") not in affected
    ]
    for date_iso, windows in new_per_date.items():
        for w_start, w_end in windows:
            out.append(
                {
                    "date": date_iso,
                    "startTime": minutes_to_hhmm(w_start),
                    "endTime": minutes_to_hhmm(w_end),
                }
            )
    out.sort(key=lambda o: (o["date"], o["startTime"]))
    return out


def plan_block(
    schedule: dict, start_utc: datetime, end_utc: datetime
) -> dict:
    """Compute the full plan for a block. Returns:
      {
        timezone, classifications,
        ooo_groups: [(start_date, end_date), ...],
        partial_overrides: {date_iso: [(start_min, end_min), ...]},
      }
    """
    tz_name = schedule.get("timeZone") or "UTC"
    tz = ZoneInfo(tz_name)
    chunks = split_block_into_local_days(start_utc, end_utc, tz)
    classifications = [
        classify_day(schedule, date_iso, b_start, b_end)
        for date_iso, b_start, b_end in chunks
    ]
    ooo_groups = group_consecutive_full_days(classifications)
    partial: dict[str, list[tuple[int, int]]] = {
        c["date"]: c["remaining_windows"]
        for c in classifications
        if c["type"] == "partial"
    }
    return {
        "timezone": tz_name,
        "classifications": classifications,
        "ooo_groups": ooo_groups,
        "partial_overrides": partial,
    }


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


# ----- block -----------------------------------------------------------------


VALID_OOO_REASONS = {"unspecified", "vacation", "travel", "sick", "public_holiday"}


@cli.group("block")
def block_group() -> None:
    """Block time on your calendar (smart-routes between OOO and schedule overrides).

    See the module docstring's "Block routing" section for details on how the
    OOO-vs-override decision is made.
    """


def _format_window(start_min: int, end_min: int) -> str:
    return f"{minutes_to_hhmm(start_min)}-{minutes_to_hhmm(end_min)}"


def _print_plan(plan: dict, dest_tz: str) -> None:
    """Human-readable summary of what `block add` is about to do."""
    click.echo(click.style(f"Plan (timezone: {dest_tz}):", fg="cyan", bold=True))
    if plan["ooo_groups"]:
        click.echo("  OOO entries to create:")
        for s, e in plan["ooo_groups"]:
            if s == e:
                click.echo(f"    - {s.isoformat()} (full day)")
            else:
                click.echo(f"    - {s.isoformat()} -> {e.isoformat()} (full days)")
    if plan["partial_overrides"]:
        click.echo("  Schedule overrides to write:")
        for date_iso, windows in sorted(plan["partial_overrides"].items()):
            if not windows:
                click.echo(f"    - {date_iso}: (no remaining availability)")
            else:
                w_str = ", ".join(_format_window(s, e) for s, e in windows)
                click.echo(f"    - {date_iso}: available {w_str}")
    noops = [c for c in plan["classifications"] if c["type"] == "noop"]
    if noops:
        click.echo(
            "  No-op days (no availability to begin with): "
            + ", ".join(c["date"] for c in noops)
        )
    if not plan["ooo_groups"] and not plan["partial_overrides"]:
        click.echo("  Nothing to do.")


@block_group.command("add")
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
    help="Reason (only attached to OOO entries; ignored for override-only blocks).",
)
@click.option("--notes", default=None, help="Optional notes (OOO only).")
@click.option("--dry-run", is_flag=True, help="Print the plan without sending.")
@click.pass_context
def cmd_block_add(
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
    """Block a time range. Provide --start/--end, --in/--for, or --in/--until."""
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

    api = get_api(ctx)
    schedule = unwrap(api.get_default_schedule()) or {}
    if not schedule.get("id"):
        raise click.ClickException(
            "no default schedule found; create one in Cal.com first"
        )

    plan = plan_block(schedule, start, end)
    _print_plan(plan, plan["timezone"])

    if dry_run:
        click.echo(click.style("[dry-run] no changes sent.", fg="yellow"))
        return

    if not plan["ooo_groups"] and not plan["partial_overrides"]:
        return

    # 1. OOO writes (one POST per consecutive group)
    created_ooo_ids: list[str] = []
    schedule_tz = ZoneInfo(plan["timezone"])
    for group_start, group_end in plan["ooo_groups"]:
        # Send the local-day boundaries as UTC ISO. Cal.com normalizes to
        # 00:00-23:59 UTC of the *date* anyway, so the exact times are advisory.
        start_local = datetime.combine(group_start, datetime.min.time(), tzinfo=schedule_tz)
        # End of last day at 23:59:59 local
        end_local = datetime.combine(
            group_end, datetime.max.time().replace(microsecond=0), tzinfo=schedule_tz
        )
        payload: dict[str, Any] = {
            "start": to_iso_z(start_local),
            "end": to_iso_z(end_local),
            "reason": reason,
        }
        if notes:
            payload["notes"] = notes
        result = unwrap(api.create_ooo(payload)) or {}
        if isinstance(result, dict) and result.get("id") is not None:
            created_ooo_ids.append(str(result["id"]))

    # 2. Schedule override write (single PATCH covering all partial-day dates)
    wrote_overrides = False
    if plan["partial_overrides"]:
        merged = merge_overrides(
            schedule.get("overrides") or [], plan["partial_overrides"]
        )
        # Cal.com PATCH replaces the overrides array wholesale, so we send the
        # full merged list.
        update_payload = {"overrides": merged}
        api.update_schedule(int(schedule["id"]), update_payload)
        wrote_overrides = True

    click.echo(click.style("Block applied.", fg="green"))
    if created_ooo_ids:
        click.echo(f"  OOO entries created: {', '.join(created_ooo_ids)}")
    if wrote_overrides:
        dates = sorted(plan["partial_overrides"].keys())
        click.echo(f"  Schedule overrides written for: {', '.join(dates)}")


@block_group.command("list")
@click.pass_context
def cmd_block_list(ctx: click.Context) -> None:
    """List active blocks (OOO entries + schedule overrides)."""
    api = get_api(ctx)

    # OOO entries
    ooo_data = unwrap(api.list_ooo()) or []
    if not isinstance(ooo_data, list):
        ooo_data = ooo_data.get("entries") or ooo_data.get("oooEntries") or []

    # Overrides (from default schedule)
    schedule = unwrap(api.get_default_schedule()) or {}
    overrides = schedule.get("overrides") or []

    if not ooo_data and not overrides:
        click.echo("No active blocks.")
        return

    table = Table(title="Blocks", show_lines=False)
    table.add_column("Type", style="magenta", no_wrap=True)
    table.add_column("ID / Date", style="cyan", no_wrap=True)
    table.add_column("When")
    table.add_column("Detail")

    for ooo in ooo_data:
        when = (
            f"{fmt_local(ooo.get('start', ''))} -> {fmt_local(ooo.get('end', ''))}"
        )
        detail_parts = []
        if ooo.get("reason"):
            detail_parts.append(str(ooo["reason"]))
        if ooo.get("notes"):
            detail_parts.append(str(ooo["notes"]))
        table.add_row(
            "ooo",
            f"ooo:{ooo.get('id', '')}",
            when,
            " | ".join(detail_parts),
        )

    # Group overrides by date so each date shows up as one row.
    by_date: dict[str, list[dict]] = {}
    for ov in overrides:
        by_date.setdefault(ov["date"], []).append(ov)
    for date_iso in sorted(by_date.keys()):
        windows = sorted(by_date[date_iso], key=lambda o: o["startTime"])
        windows_str = ", ".join(
            f"{o['startTime']}-{o['endTime']}" for o in windows
        )
        table.add_row(
            "override",
            f"override:{date_iso}",
            date_iso,
            f"available {windows_str}",
        )

    console.print(table)
    click.echo(
        click.style(
            "(delete with `block delete <id>`. IDs are e.g. `ooo:72424` or "
            "`override:2026-05-06`.)",
            dim=True,
        )
    )


@block_group.command("delete")
@click.argument("block_id")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation.")
@click.pass_context
def cmd_block_delete(ctx: click.Context, block_id: str, yes: bool) -> None:
    """Delete a block. ID can be `ooo:<id>`, `override:<date>`, a bare numeric
    OOO id, or a bare `YYYY-MM-DD` date (treated as override)."""
    api = get_api(ctx)

    # Disambiguate the ID.
    is_override = False
    target: str
    if block_id.startswith("ooo:"):
        target = block_id.split(":", 1)[1]
    elif block_id.startswith("override:"):
        is_override = True
        target = block_id.split(":", 1)[1]
    elif re.fullmatch(r"\d{4}-\d{2}-\d{2}", block_id):
        is_override = True
        target = block_id
    elif block_id.isdigit():
        target = block_id
    else:
        raise click.UsageError(
            f"unrecognized block id {block_id!r}. Use `ooo:<id>` or "
            "`override:YYYY-MM-DD` (or list with `block list`)."
        )

    if is_override:
        # Validate date
        try:
            date.fromisoformat(target)
        except ValueError as e:
            raise click.UsageError(f"invalid override date {target!r}: {e}")

        if not yes and not click.confirm(
            f"Delete schedule override(s) for {target}?"
        ):
            click.echo("Cancelled.")
            return

        schedule = unwrap(api.get_default_schedule()) or {}
        if not schedule.get("id"):
            raise click.ClickException("no default schedule found")
        existing = schedule.get("overrides") or []
        remaining = [o for o in existing if o.get("date") != target]
        if len(remaining) == len(existing):
            click.echo(f"No override found for {target}.")
            return
        api.update_schedule(
            int(schedule["id"]),
            {
                "overrides": [
                    {
                        "date": o["date"],
                        "startTime": o["startTime"],
                        "endTime": o["endTime"],
                    }
                    for o in remaining
                ]
            },
        )
        click.echo(click.style(f"Override(s) for {target} deleted.", fg="green"))
        return

    # OOO path
    if not yes and not click.confirm(f"Delete OOO entry {target}?"):
        click.echo("Cancelled.")
        return
    api.delete_ooo(target)
    click.echo(click.style(f"OOO entry {target} deleted.", fg="green"))


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
