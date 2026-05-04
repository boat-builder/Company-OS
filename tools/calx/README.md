# calx — Cal.com CLI

A lightweight, scriptable command-line tool for managing your personal [Cal.com](https://cal.com) calendar — block time (OOO), create/cancel/list bookings — without touching the dashboard.

Single Python file, runs via [uv](https://docs.astral.sh/uv/) with no install step (deps are declared inline using PEP 723).

## Setup

### 1. Install `uv` (one-time)

```bash
brew install uv
# or: curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Get a Cal.com API key

1. Go to **Cal.com → Settings → Developer → API Keys**
2. Create a new key. Live keys are prefixed `cal_live_`.
3. Treat it like a password — keep it out of git.

### 3. Configure

Create a `.env` file in this directory:

```
CAL_API_KEY=cal_live_xxxxxxxxxxxxx
```

`.gitignore` already excludes `.env`.

### 4. Verify

```bash
uv run cal_cli.py me
```

The first run will install deps (click, requests, dateparser, rich) into a managed cache. Subsequent runs are instant.

## Why API key, not OAuth?

Cal.com's OAuth flow is built for **multi-tenant platform integrations** — you create an OAuth client, manage user sign-ins, refresh tokens, and scopes. That's overkill for a single-user personal CLI. An API key (`Authorization: Bearer cal_live_…`) is the right fit and is what Cal.com recommends for direct/personal use.

## Usage

```bash
uv run cal_cli.py [COMMAND] [SUBCOMMAND] [OPTIONS]
```

For a smoother experience, alias it in your shell:

```bash
# ~/.zshrc or ~/.bashrc
alias calx="uv run /absolute/path/to/tools/calx/cal_cli.py"
```

Or make it executable (the shebang `#!/usr/bin/env -S uv run --script` does the rest):

```bash
chmod +x cal_cli.py
./cal_cli.py me
```

The examples below assume you've aliased it as `calx`.

### Help

```bash
calx --help
calx busy --help
calx busy add --help
```

---

## Commands

### Sanity check / discovery

```bash
# Confirms your API key works and shows your profile
calx me

# Lists your event types — you'll need an ID for `bookings create`
calx event-types list
```

### Block time (OOO / "busy")

```bash
# Explicit start + end (human-friendly times work)
calx busy add --start "2026-05-05T14:00" --end "2026-05-05T15:30"
calx busy add --start "tomorrow 2pm" --end "tomorrow 4pm"

# Relative: start in 30m, last 90m
calx busy add --in 30m --for 90m

# Relative start, absolute end
calx busy add --in 30m --until "tomorrow 5pm"

# With reason and notes
calx busy add --in 1h --for 2h --reason vacation --notes "Hawaii trip"

# Reasons: unspecified, vacation, travel, sick, public_holiday

# Preview the request without sending
calx busy add --in 30m --for 90m --dry-run

# List & delete
calx busy list
calx busy delete <ooo_id>
```

### Bookings

```bash
# Create
calx bookings create \
  --event-type 123 \
  --email user@example.com \
  --name "John Doe" \
  --start "tomorrow 10am"

# With explicit attendee timezone (defaults to your local tz)
calx bookings create -e 123 --email a@b.com -n "Jane" --start "next mon 10am" \
  --timezone America/New_York

# Add additional guests
calx bookings create -e 123 --email a@b.com -n "Jane" --start "next mon 10am" \
  --guests bob@example.com --guests carol@example.com

# Preview
calx bookings create -e 123 --email a@b.com -n "Jane" --start "tomorrow 10am" --dry-run

# List (filters are optional and combine)
calx bookings list                                       # next 50 upcoming
calx bookings list --status upcoming --limit 20
calx bookings list --from today --to "next week"
calx bookings list --email user@example.com
calx bookings list --name "Jane"

# Cancel
calx bookings cancel <booking_uid>
calx bookings cancel <booking_uid> --reason "Reschedule"
calx bookings cancel <booking_uid> --yes              # skip confirmation
calx bookings cancel <booking_uid> --dry-run          # preview
```

---

## Time parsing

Anywhere a time is accepted (`--start`, `--end`, `--until`, `--from`, `--to`):

- **ISO:** `2026-05-05T14:00`, `2026-05-05`
- **Natural:** `tomorrow 2pm`, `next monday 10am`, `today`, `next week`, `in 2 hours`
- **Hyphenated:** `next-week` (CLI-friendly equivalent of `next week`)

All times are interpreted in your **system's local timezone**, then converted to UTC ISO 8601 before being sent to Cal.com.

Anywhere a duration is accepted (`--in`, `--for`):

- `30m`, `90m`, `1h`, `1h30m`, `2h`, `1d`, `90s`

---

## Project structure

```
tools/calx/
├── .gitignore     # ignores .env
├── README.md      # this file
└── cal_cli.py     # single-file CLI (PEP 723 inline deps)
```

This mirrors the pattern used by [`sales/closecrm/`](../../sales/closecrm/).

---

## Cal.com API reference

- [API v2 introduction](https://cal.com/docs/api-reference/v2/introduction)
- [Bookings — create](https://cal.com/docs/api-reference/v2/bookings/create-a-booking)
- [Bookings — cancel](https://cal.com/docs/api-reference/v2/bookings/cancel-a-booking)
- [Bookings — list](https://cal.com/docs/api-reference/v2/bookings/get-all-bookings)

The endpoint versions are pinned in the `API_VERSIONS` constant near the top of `cal_cli.py`. Cal.com versions endpoints independently — if a call ever 404s with no other obvious cause, bumping the relevant entry there is the first thing to try.

---

## Troubleshooting

**`.env file not found`** — create `.env` in this directory with `CAL_API_KEY=cal_live_xxx`.

**`API error 401`** — invalid/expired key. Regenerate at Cal.com → Settings → Developer → API Keys.

**`API error 404`** — most likely the `cal-api-version` for that endpoint has been bumped on Cal.com's side. Check their docs for the current version of the endpoint and update `API_VERSIONS` in `cal_cli.py`.

**`could not parse time …`** — try a simpler form. ISO (`2026-05-05T14:00`) always works; for natural language `tomorrow 2pm` or `next monday 10am` are reliable.

**`could not parse duration …`** — use number + unit (`s`/`m`/`h`/`d`). `1h30m` works; `1.5h` does not.
