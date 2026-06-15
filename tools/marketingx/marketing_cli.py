#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "click>=8.1",
#   "requests>=2.31",
#   "rich>=13.7",
# ]
# ///
"""
Marketing API CLI - social, search, and SEO intelligence behind one key.

A thin, scriptable wrapper over the internal Marketing API. Every endpoint is a
POST with a JSON body that responds synchronously; this CLI builds that body for
you from flags (and lets you override/extend it with --body), posts it, and
prints the JSON response.

Usage:
    uv run marketing_cli.py [GROUP] [COMMAND] [OPTIONS]

Groups & commands:
    linkedin profiles    --url | --name           People profiles by URL or name
    linkedin companies   --url                     Company pages by URL
    linkedin jobs        --url | --keyword ...      Job listings by URL or search
    linkedin posts       --url | --profile-url      Posts by URL or author profile

    x posts              --url | --profile          X posts by URL or author profile
    x profiles           --url                       X profiles by URL

    google search        --query                     Web search + SERP features
    google ai-mode       --query                     AI Mode markdown answer + refs

    chatgpt search       --query                     Web-grounded ChatGPT answer

    seo ranked-keywords  --target                    Keywords a domain ranks for
    seo keyword-ideas    --keyword                    Related keyword expansion
    seo domain-overview  --target                    Domain ranking/traffic metrics

Every command also accepts:
    --body '<json>'   Raw request body (merged under the flags; flags win).
                      Use this to express anything the flags don't cover, e.g.
                      multiple `searches` or `profiles` in one request.
    --raw             Print the response as-is (no pretty-printing / coloring).
    -o, --output FILE Write the JSON response to FILE instead of stdout.

Examples:
    uv run marketing_cli.py linkedin profiles --url https://www.linkedin.com/in/satyanadella/
    uv run marketing_cli.py linkedin jobs --keyword "product manager" --location Berlin --limit-per-input 20
    uv run marketing_cli.py x posts --profile https://x.com/openai --start-date 2026-01-01
    uv run marketing_cli.py google search --query "best running shoes 2026" --country us --max-results 10
    uv run marketing_cli.py google ai-mode --query "how do carbon-plate running shoes work"
    uv run marketing_cli.py chatgpt search --query "What did Anthropic release most recently?"
    uv run marketing_cli.py seo ranked-keywords --target anthropic.com --location-code 2840 --limit 50
    uv run marketing_cli.py seo keyword-ideas --keyword "running shoes" --keyword "trail shoes"

Auth:
    Put your personal key and the backend host in a .env file beside this script:
        MARKETING_API_KEY=mk_live_xxxxxxxxxxxx
        MARKETING_BASE_URL=https://your-backend-host
    The key authenticates as you — treat it like a password. It is sent as
    `Authorization: Bearer <key>` (set MARKETING_AUTH_STYLE=x-api-key to send it
    as the `X-API-Key` header instead).

Errors (surfaced verbatim from the API):
    400 invalid input · 401 missing/invalid key · 403 blocked account ·
    502 upstream provider failure · 503 capability not configured.

Latency:
    LinkedIn/X jobs may take ~10-70s; Google/ChatGPT/SEO usually return in a few
    seconds. The HTTP timeout is generous (see REQUEST_TIMEOUT) to accommodate
    server-side `wait_seconds` of up to 600.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any, Callable, Optional

import click
import requests
from rich.console import Console


# =============================================================================
# Configuration
# =============================================================================

console = Console()
err_console = Console(stderr=True)

API_PREFIX = "/api/v1/admin/marketing"

# wait_seconds can be up to 600; give the socket comfortable headroom on top.
REQUEST_TIMEOUT = (10, 660)  # (connect, read) seconds


def _read_env_file() -> dict[str, str]:
    """Parse the .env beside this script into a dict (no external deps)."""
    env_path = Path(__file__).parent / ".env"
    values: dict[str, str] = {}
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, val = line.split("=", 1)
            values[key.strip()] = val.strip().strip('"').strip("'")
    return values


def load_config() -> tuple[str, str, str]:
    """Return (api_key, base_url, auth_style).

    Environment variables take precedence over the .env file so the CLI works
    in CI / sandboxes where secrets are injected as env vars.
    """
    file_env = _read_env_file()

    def pick(name: str, default: str = "") -> str:
        return os.environ.get(name) or file_env.get(name, default)

    api_key = pick("MARKETING_API_KEY")
    base_url = pick("MARKETING_BASE_URL")
    auth_style = pick("MARKETING_AUTH_STYLE", "bearer").lower()

    if not api_key:
        raise click.ClickException(
            "MARKETING_API_KEY not set.\n"
            "Add it to a .env file beside this script (or export it):\n"
            "    MARKETING_API_KEY=mk_live_xxxxx\n"
            "Get your key from the Marketing API Key card in the admin UI."
        )
    if not base_url:
        raise click.ClickException(
            "MARKETING_BASE_URL not set.\n"
            "Add the backend host to .env (or export it):\n"
            "    MARKETING_BASE_URL=https://your-backend-host"
        )
    return api_key, base_url.rstrip("/"), auth_style


def post(path: str, body: dict[str, Any]) -> Any:
    """POST a JSON body to the Marketing API and return the parsed response.

    Translates the documented status codes into readable CLI errors.
    """
    api_key, base_url, auth_style = load_config()
    url = f"{base_url}{API_PREFIX}{path}"

    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    if auth_style == "x-api-key":
        headers["X-API-Key"] = api_key
    else:
        headers["Authorization"] = f"Bearer {api_key}"

    try:
        resp = requests.post(url, json=body, headers=headers, timeout=REQUEST_TIMEOUT)
    except requests.exceptions.Timeout:
        raise click.ClickException(
            f"Request to {path} timed out. LinkedIn/X jobs can take up to ~70s "
            "(or longer with a high wait_seconds); try again or lower the scope."
        )
    except requests.exceptions.RequestException as exc:
        raise click.ClickException(f"Network error calling {url}: {exc}")

    if resp.status_code >= 400:
        hint = {
            400: "invalid input",
            401: "missing/invalid key",
            403: "blocked account",
            502: "upstream provider failure",
            503: "capability not configured",
        }.get(resp.status_code, "request failed")
        # Surface the server's error payload if there is one.
        detail = resp.text.strip()
        try:
            detail = json.dumps(resp.json(), indent=2)
        except ValueError:
            pass
        raise click.ClickException(
            f"HTTP {resp.status_code} ({hint}) from {path}\n{detail}"
        )

    if not resp.content:
        return {}
    try:
        return resp.json()
    except ValueError:
        return resp.text


def emit(data: Any, raw: bool, output: Optional[str]) -> None:
    """Print or save a JSON response."""
    text = (
        data
        if isinstance(data, str)
        else json.dumps(data, indent=2, ensure_ascii=False)
    )
    if output:
        Path(output).write_text(text if isinstance(text, str) else str(text))
        err_console.print(f"[green]Wrote response to {output}[/green]")
        return
    if raw:
        click.echo(text)
    else:
        # rich pretty-prints JSON with syntax highlighting; fall back to plain.
        if isinstance(data, str):
            click.echo(data)
        else:
            console.print_json(text)


def parse_body(body: Optional[str]) -> dict[str, Any]:
    """Parse a --body JSON string into a dict (or {} if not given)."""
    if not body:
        return {}
    try:
        parsed = json.loads(body)
    except json.JSONDecodeError as exc:
        raise click.UsageError(f"--body is not valid JSON: {exc}")
    if not isinstance(parsed, dict):
        raise click.UsageError("--body must be a JSON object.")
    return parsed


def overlay(base: dict[str, Any], **fields: Any) -> dict[str, Any]:
    """Overlay non-None fields onto base (mutating + returning base).

    Empty tuples (from repeatable options the user didn't pass) and None are
    skipped so flags only override --body when actually provided.
    """
    for key, value in fields.items():
        if value is None:
            continue
        if isinstance(value, tuple) and len(value) == 0:
            continue
        base[key] = list(value) if isinstance(value, tuple) else value
    return base


def split_name(full: str) -> dict[str, str]:
    """Split 'First Middle Last' into {first_name, last_name}."""
    parts = full.strip().split()
    if not parts:
        raise click.UsageError("Empty --name.")
    if len(parts) == 1:
        return {"first_name": parts[0], "last_name": ""}
    return {"first_name": parts[0], "last_name": " ".join(parts[1:])}


# =============================================================================
# Shared decorators
# =============================================================================


def output_options(func: Callable) -> Callable:
    """Attach --body, --raw, -o/--output to a command."""
    func = click.option(
        "--body",
        "body",
        help="Raw JSON request body; flags are merged on top of it.",
    )(func)
    func = click.option(
        "--raw",
        is_flag=True,
        help="Print the response verbatim (no pretty-printing).",
    )(func)
    func = click.option(
        "-o",
        "--output",
        "output",
        type=click.Path(dir_okay=False, writable=True),
        help="Write the JSON response to this file.",
    )(func)
    return func


def run(path: str, body: dict[str, Any], raw: bool, output: Optional[str]) -> None:
    emit(post(path, body), raw, output)


# =============================================================================
# CLI root
# =============================================================================


@click.group(
    help="Marketing API CLI - LinkedIn, X, Google, ChatGPT, and SEO intelligence."
)
def cli() -> None:
    pass


# =============================================================================
# linkedin
# =============================================================================


@cli.group(name="linkedin", help="Public LinkedIn profiles, companies, jobs, posts.")
def linkedin_group() -> None:
    pass


@linkedin_group.command(name="profiles", help="Fetch people profiles by URL, or discover by name.")
@click.option("--url", "urls", multiple=True, help="Profile URL to fetch (repeatable).")
@click.option("--name", "names", multiple=True, help='Name to discover, e.g. "Satya Nadella" (repeatable).')
@click.option("--limit-per-input", type=int, help="Cap results per discovery input.")
@click.option("--wait-seconds", type=int, help="Server-side wait cap, 0-600 (0 = default).")
@output_options
def linkedin_profiles(urls, names, limit_per_input, wait_seconds, body, raw, output):
    payload = parse_body(body)
    name_objs = tuple(split_name(n) for n in names) if names else ()
    overlay(
        payload,
        urls=urls,
        names=name_objs,
        limit_per_input=limit_per_input,
        wait_seconds=wait_seconds,
    )
    if not payload.get("urls") and not payload.get("names"):
        raise click.UsageError("Provide at least one --url or --name (or supply --body).")
    run("/linkedin/profiles", payload, raw, output)


@linkedin_group.command(name="companies", help="Fetch company pages by URL.")
@click.option("--url", "urls", multiple=True, help="Company page URL (repeatable).")
@click.option("--wait-seconds", type=int, help="Server-side wait cap, 0-600.")
@output_options
def linkedin_companies(urls, wait_seconds, body, raw, output):
    payload = parse_body(body)
    overlay(payload, urls=urls, wait_seconds=wait_seconds)
    if not payload.get("urls"):
        raise click.UsageError("Provide at least one --url (or supply --body).")
    run("/linkedin/companies", payload, raw, output)


@linkedin_group.command(name="jobs", help="Fetch jobs by URL, or discover by keyword/location.")
@click.option("--url", "urls", multiple=True, help="Job listing URL (repeatable).")
@click.option("--keyword", help="Search keyword (effectively the only required search field).")
@click.option("--location", help="Search location, e.g. Berlin.")
@click.option("--country", help="Country filter.")
@click.option("--time-range", help="Time range filter.")
@click.option("--job-type", help="Job type filter.")
@click.option("--experience-level", help="Experience level filter.")
@click.option("--remote", help="Remote filter.")
@click.option("--company", help="Company filter.")
@click.option("--limit-per-input", type=int, help="Cap results per search.")
@click.option("--wait-seconds", type=int, help="Server-side wait cap, 0-600.")
@output_options
def linkedin_jobs(
    urls, keyword, location, country, time_range, job_type, experience_level,
    remote, company, limit_per_input, wait_seconds, body, raw, output,
):
    payload = parse_body(body)
    search = overlay(
        {},
        keyword=keyword, location=location, country=country, time_range=time_range,
        job_type=job_type, experience_level=experience_level, remote=remote, company=company,
    )
    searches = (search,) if search else ()
    overlay(payload, urls=urls, searches=searches,
            limit_per_input=limit_per_input, wait_seconds=wait_seconds)
    if not payload.get("urls") and not payload.get("searches"):
        raise click.UsageError("Provide --url or a search (--keyword ...), or supply --body.")
    run("/linkedin/jobs", payload, raw, output)


@linkedin_group.command(name="posts", help="Fetch posts by URL, or discover recent posts by author.")
@click.option("--url", "urls", multiple=True, help="Post URL (repeatable).")
@click.option("--profile-url", "profile_urls", multiple=True, help="Author profile URL to discover posts from (repeatable).")
@click.option("--limit-per-input", type=int, help="Cap posts per profile.")
@click.option("--wait-seconds", type=int, help="Server-side wait cap, 0-600.")
@output_options
def linkedin_posts(urls, profile_urls, limit_per_input, wait_seconds, body, raw, output):
    payload = parse_body(body)
    overlay(payload, urls=urls, profile_urls=profile_urls,
            limit_per_input=limit_per_input, wait_seconds=wait_seconds)
    if not payload.get("urls") and not payload.get("profile_urls"):
        raise click.UsageError("Provide --url or --profile-url (or supply --body).")
    run("/linkedin/posts", payload, raw, output)


# =============================================================================
# x (twitter)
# =============================================================================


@cli.group(name="x", help="Public X (Twitter) posts and profiles.")
def x_group() -> None:
    pass


@x_group.command(name="posts", help="Fetch posts by URL, or discover by author profile.")
@click.option("--url", "urls", multiple=True, help="Post (status) URL (repeatable).")
@click.option("--profile", "profile_url", help="Author profile URL to discover posts from.")
@click.option("--start-date", help="Discovery window start, YYYY-MM-DD (with --profile).")
@click.option("--end-date", help="Discovery window end, YYYY-MM-DD (with --profile).")
@click.option("--limit-per-input", type=int, help="Cap posts per profile.")
@click.option("--wait-seconds", type=int, help="Server-side wait cap, 0-600.")
@output_options
def x_posts(urls, profile_url, start_date, end_date, limit_per_input, wait_seconds, body, raw, output):
    payload = parse_body(body)
    profiles: tuple = ()
    if profile_url:
        profiles = (overlay({"url": profile_url}, start_date=start_date, end_date=end_date),)
    elif start_date or end_date:
        raise click.UsageError("--start-date/--end-date require --profile.")
    overlay(payload, urls=urls, profiles=profiles,
            limit_per_input=limit_per_input, wait_seconds=wait_seconds)
    if not payload.get("urls") and not payload.get("profiles"):
        raise click.UsageError("Provide --url or --profile (or supply --body).")
    run("/x/posts", payload, raw, output)


@x_group.command(name="profiles", help="Fetch X profiles by URL.")
@click.option("--url", "urls", multiple=True, help="Profile URL (repeatable).")
@click.option("--wait-seconds", type=int, help="Server-side wait cap, 0-600.")
@output_options
def x_profiles(urls, wait_seconds, body, raw, output):
    payload = parse_body(body)
    overlay(payload, urls=urls, wait_seconds=wait_seconds)
    if not payload.get("urls"):
        raise click.UsageError("Provide at least one --url (or supply --body).")
    run("/x/profiles", payload, raw, output)


# =============================================================================
# google
# =============================================================================


@cli.group(name="google", help="Google web search and the AI Mode surface.")
def google_group() -> None:
    pass


@google_group.command(name="search", help="Google web search with organic results + SERP features.")
@click.option("--query", required=False, help="Search query.")
@click.option("--country", help='ISO 3166-1 alpha-2, e.g. "us", "de".')
@click.option("--language", help='Two-letter code, e.g. "en".')
@click.option("--location", help='Canonical location name, e.g. "Austin,Texas,United States".')
@click.option("--max-results", type=int, help="Cap organic results (1-100).")
@output_options
def google_search(query, country, language, location, max_results, body, raw, output):
    payload = parse_body(body)
    overlay(payload, query=query, country=country, language=language,
            location=location, max_results=max_results)
    if not payload.get("query"):
        raise click.UsageError("--query is required (or supply --body with a query).")
    run("/google/search", payload, raw, output)


@google_group.command(name="ai-mode", help="Google AI Mode - markdown answer with cited references.")
@click.option("--query", required=False, help="Question.")
@click.option("--country", help="ISO 3166-1 alpha-2.")
@click.option("--language", help="Two-letter code.")
@click.option("--location", help="Canonical location name.")
@output_options
def google_ai_mode(query, country, language, location, body, raw, output):
    payload = parse_body(body)
    overlay(payload, query=query, country=country, language=language, location=location)
    if not payload.get("query"):
        raise click.UsageError("--query is required (or supply --body with a query).")
    run("/google/ai-mode", payload, raw, output)


# =============================================================================
# chatgpt
# =============================================================================


@cli.group(name="chatgpt", help="Web-grounded ChatGPT answer with citations.")
def chatgpt_group() -> None:
    pass


@chatgpt_group.command(name="search", help="Ask ChatGPT a question with live web grounding.")
@click.option("--query", required=False, help="The question.")
@click.option("--model", help="gpt-5.5 | gpt-5.4-mini | gpt-5.4-nano (default gpt-5.4-mini).")
@click.option("--system-prompt", help="Optional system instructions.")
@click.option("--search-context-size", type=click.Choice(["low", "medium", "high"]), help="Grounding context size.")
@click.option("--domain-filter", "domain_filter", multiple=True, help="Restrict grounding to this domain (repeatable).")
@click.option("--max-tokens", type=int, help="Cap response length.")
@click.option("--reasoning-effort", type=click.Choice(["minimal", "low", "medium", "high"]), help="Reasoning effort.")
@click.option("--include-citations/--no-include-citations", "include_citations", default=None, help="Include citations (default true).")
@click.option("--city", help="user_location.city")
@click.option("--region", help="user_location.region")
@click.option("--user-country", help="user_location.country")
@click.option("--timezone", help="user_location.timezone")
@output_options
def chatgpt_search(
    query, model, system_prompt, search_context_size, domain_filter, max_tokens,
    reasoning_effort, include_citations, city, region, user_country, timezone,
    body, raw, output,
):
    payload = parse_body(body)
    user_location = overlay({}, city=city, region=region, country=user_country, timezone=timezone)
    overlay(
        payload,
        query=query, model=model, system_prompt=system_prompt,
        search_context_size=search_context_size, domain_filter=domain_filter,
        max_tokens=max_tokens, reasoning_effort=reasoning_effort,
        include_citations=include_citations,
        user_location=(user_location or None),
    )
    if not payload.get("query"):
        raise click.UsageError("--query is required (or supply --body with a query).")
    run("/chatgpt/search", payload, raw, output)


# =============================================================================
# seo
# =============================================================================


@cli.group(name="seo", help="Search-engine ranking intelligence.")
def seo_group() -> None:
    pass


def _parse_filters(filters: Optional[str]) -> Any:
    if filters is None:
        return None
    try:
        return json.loads(filters)
    except json.JSONDecodeError:
        # The API accepts arbitrary upstream filter expressions; pass through as-is.
        return filters


@seo_group.command(name="ranked-keywords", help="Keywords a domain ranks for in Google.")
@click.option("--target", required=False, help='Domain, e.g. "example.com".')
@click.option("--location-code", type=int, help="Numeric location code (e.g. 2840 = US).")
@click.option("--language-code", help='Two-letter code, e.g. "en".')
@click.option("--limit", type=int, help="Default 100, max 1000.")
@click.option("--offset", type=int, help="Pagination offset.")
@click.option("--order-by", "order_by", multiple=True, help='e.g. "keyword_data.keyword_info.search_volume,desc" (repeatable).')
@click.option("--filters", help="Optional upstream filter expression (JSON or raw string).")
@output_options
def seo_ranked_keywords(target, location_code, language_code, limit, offset, order_by, filters, body, raw, output):
    payload = parse_body(body)
    overlay(payload, target=target, location_code=location_code, language_code=language_code,
            limit=limit, offset=offset, order_by=order_by, filters=_parse_filters(filters))
    if not payload.get("target"):
        raise click.UsageError("--target is required (or supply --body with a target).")
    run("/seo/ranked-keywords", payload, raw, output)


@seo_group.command(name="keyword-ideas", help="Keywords semantically related to seed keywords.")
@click.option("--keyword", "keywords", multiple=True, help="Seed keyword, 1-200 (repeatable).")
@click.option("--location-code", type=int, help="Numeric location code.")
@click.option("--language-code", help="Two-letter code.")
@click.option("--limit", type=int, help="Default 100, max 1000.")
@click.option("--offset", type=int, help="Pagination offset.")
@click.option("--order-by", "order_by", multiple=True, help='e.g. "keyword_info.search_volume,desc" (repeatable).')
@click.option("--filters", help="Optional upstream filter expression (JSON or raw string).")
@output_options
def seo_keyword_ideas(keywords, location_code, language_code, limit, offset, order_by, filters, body, raw, output):
    payload = parse_body(body)
    overlay(payload, keywords=keywords, location_code=location_code, language_code=language_code,
            limit=limit, offset=offset, order_by=order_by, filters=_parse_filters(filters))
    if not payload.get("keywords"):
        raise click.UsageError("Provide at least one --keyword (or supply --body with keywords).")
    run("/seo/keyword-ideas", payload, raw, output)


@seo_group.command(name="domain-overview", help="Ranking + traffic metrics for a domain.")
@click.option("--target", required=False, help="Domain to analyze.")
@click.option("--location-code", type=int, help="Numeric location code.")
@click.option("--language-code", help="Two-letter code.")
@output_options
def seo_domain_overview(target, location_code, language_code, body, raw, output):
    payload = parse_body(body)
    overlay(payload, target=target, location_code=location_code, language_code=language_code)
    if not payload.get("target"):
        raise click.UsageError("--target is required (or supply --body with a target).")
    run("/seo/domain-overview", payload, raw, output)


if __name__ == "__main__":
    cli()
