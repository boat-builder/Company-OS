# marketingx — Marketing API CLI

A lightweight, scriptable command-line tool over the internal **Marketing API** — social (LinkedIn, X), search (Google, ChatGPT), and SEO data behind one key-authed, vendor-neutral contract.

Single Python file, runs via [uv](https://docs.astral.sh/uv/) with no install step (deps are declared inline using PEP 723). Mirrors the pattern used by [`tools/stripex/`](../stripex/) and [`tools/calx/`](../calx/).

## What it covers

Every documented endpoint is wrapped as a subcommand:

| Group | Command | Endpoint |
| --- | --- | --- |
| `linkedin` | `profiles` | `POST /linkedin/profiles` — people by URL or name |
| `linkedin` | `companies` | `POST /linkedin/companies` — company pages by URL |
| `linkedin` | `jobs` | `POST /linkedin/jobs` — jobs by URL or keyword/location search |
| `linkedin` | `posts` | `POST /linkedin/posts` — posts by URL or author profile |
| `x` | `posts` | `POST /x/posts` — posts by URL or author profile (date window) |
| `x` | `profiles` | `POST /x/profiles` — profiles by URL |
| `google` | `search` | `POST /google/search` — web search + SERP features |
| `google` | `ai-mode` | `POST /google/ai-mode` — AI Mode markdown answer + references |
| `chatgpt` | `search` | `POST /chatgpt/search` — web-grounded ChatGPT answer + citations |
| `seo` | `ranked-keywords` | `POST /seo/ranked-keywords` — keywords a domain ranks for |
| `seo` | `keyword-ideas` | `POST /seo/keyword-ideas` — related keyword expansion |
| `seo` | `domain-overview` | `POST /seo/domain-overview` — domain ranking/traffic metrics |

The API is **POST-only, JSON in/JSON out, synchronous**. The CLI builds the request body from flags, posts it, and prints the JSON response.

## Setup

### 1. Install `uv` (one-time)

```bash
brew install uv
# or: curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Configure

Create a `.env` file in this directory (there's a `.env.example` to copy):

```
MARKETING_API_KEY=mk_live_xxxxxxxxxxxxx
MARKETING_BASE_URL=https://your-backend-host
```

- **`MARKETING_API_KEY`** — your personal key from the *Marketing API Key* card in the admin UI. It authenticates as you; treat it like a password. `.gitignore` already excludes `.env`.
- **`MARKETING_BASE_URL`** — the backend host. The CLI appends `/api/v1/admin/marketing` itself, so just give the host (e.g. `https://api.internal.example`).
- **`MARKETING_AUTH_STYLE`** *(optional)* — `bearer` (default) sends `Authorization: Bearer <key>`; set to `x-api-key` to send `X-API-Key: <key>` instead.

Environment variables override the `.env` file, so the same script works in CI / sandboxes where the key is injected as an env var.

### 3. Verify

```bash
uv run marketing_cli.py google search --query "hello world" --max-results 3
```

The first run installs deps (click, requests, rich) into a managed cache. Subsequent runs are instant.

## Usage

```bash
uv run marketing_cli.py [GROUP] [COMMAND] [OPTIONS]
```

For a smoother experience, alias it (or `chmod +x marketing_cli.py` and rely on the shebang):

```bash
# ~/.zshrc or ~/.bashrc
alias marketingx="uv run /absolute/path/to/tools/marketingx/marketing_cli.py"
```

The examples below assume you've aliased it as `marketingx`.

### Help

```bash
marketingx --help
marketingx linkedin --help
marketingx linkedin jobs --help
```

---

## Commands

### LinkedIn

```bash
# People profiles by URL
marketingx linkedin profiles --url https://www.linkedin.com/in/satyanadella/

# Discover profiles by name (repeat --name for several)
marketingx linkedin profiles --name "Satya Nadella" --limit-per-input 5

# Company pages
marketingx linkedin companies --url https://www.linkedin.com/company/microsoft/

# Jobs by keyword/location search
marketingx linkedin jobs --keyword "product manager" --location Berlin --limit-per-input 20

# Jobs by direct URL
marketingx linkedin jobs --url https://www.linkedin.com/jobs/view/123456789/

# Recent posts from an author profile
marketingx linkedin posts --profile-url https://www.linkedin.com/in/satyanadella/ --limit-per-input 10
```

### X (Twitter)

```bash
# Posts from an author profile within a date window
marketingx x posts --profile https://x.com/openai --start-date 2026-01-01 --limit-per-input 20

# Specific posts by URL
marketingx x posts --url https://x.com/openai/status/123

# Profiles
marketingx x profiles --url https://x.com/openai
```

### Google

```bash
# Web search
marketingx google search --query "best running shoes 2026" --country us --max-results 10

# AI Mode (markdown answer with cited references)
marketingx google ai-mode --query "how do carbon-plate running shoes work"
```

### ChatGPT

```bash
marketingx chatgpt search --query "What did Anthropic release most recently?" --search-context-size medium

# With options
marketingx chatgpt search --query "latest AI news" \
  --model gpt-5.5 --reasoning-effort high \
  --domain-filter anthropic.com --domain-filter openai.com
```

### SEO

```bash
# Keywords a domain ranks for
marketingx seo ranked-keywords --target anthropic.com --location-code 2840 --language-code en --limit 50

# Related keyword ideas (repeat --keyword for several seeds)
marketingx seo keyword-ideas --keyword "running shoes" --keyword "trail shoes" --location-code 2840 --limit 50

# Domain ranking/traffic overview
marketingx seo domain-overview --target anthropic.com --location-code 2840 --language-code en
```

---

## Common options on every command

| Option | Purpose |
| --- | --- |
| `--body '<json>'` | Raw JSON request body. Flags are merged **on top** of it (flags win). Use this to express anything the flags don't cover — e.g. multiple `searches` (LinkedIn jobs) or multiple `profiles` (X posts) in a single request. |
| `--raw` | Print the response verbatim, no pretty-printing or coloring. Handy for piping into `jq`. |
| `-o, --output FILE` | Write the JSON response to a file instead of stdout. |

### The `--body` escape hatch

Convenience flags cover the common single-input path. For everything else, pass the body directly — for example, several LinkedIn job searches at once:

```bash
marketingx linkedin jobs --body '{
  "searches": [
    {"keyword": "product manager", "location": "Berlin"},
    {"keyword": "data scientist", "location": "Munich", "remote": "true"}
  ],
  "limit_per_input": 20
}'
```

Pipe to `jq`:

```bash
marketingx seo ranked-keywords --target anthropic.com --location-code 2840 --raw \
  | jq '.items[].keyword_data.keyword'
```

---

## Notes on API behaviour

**Latency.** LinkedIn/X discovery jobs may take ~10–70s; Google/ChatGPT/SEO usually return in a few seconds. The HTTP read timeout is set high (660s) to accommodate a server-side `wait_seconds` of up to 600.

**`wait_seconds`.** Most endpoints accept `--wait-seconds` (0–600, where 0 = server default) to cap how long the server waits for upstream providers before returning.

**Errors are surfaced verbatim.** The CLI maps the documented status codes to readable messages and prints the server's error payload:

| Code | Meaning |
| --- | --- |
| 400 | invalid input |
| 401 | missing/invalid key |
| 403 | blocked account |
| 502 | upstream provider failure |
| 503 | capability not configured |

**Response shapes.** LinkedIn/X endpoints return a `RecordsResponse` (`{ count, error_count, duration_ms, records[] }`) where records are passthrough provider objects. Google/ChatGPT/SEO return their own documented shapes. The CLI does not reshape responses — what the API returns is what you get.

---

## Project structure

```
tools/marketingx/
├── .env.example     # template — copy to .env and fill in
├── .gitignore       # ignores .env and __pycache__
├── README.md        # this file
└── marketing_cli.py # single-file CLI (PEP 723 inline deps)
```

---

## Troubleshooting

**`MARKETING_API_KEY not set` / `MARKETING_BASE_URL not set`** — create `.env` in this directory (copy `.env.example`) or export the variables in your shell.

**`HTTP 401 (missing/invalid key)`** — re-copy your key from the Marketing API Key card; confirm it isn't expired or revoked.

**`HTTP 403 (blocked account)`** — your account is blocked from the API; contact whoever administers the Marketing API.

**`HTTP 502 (upstream provider failure)`** — the upstream social/search/SEO provider failed. Usually transient; retry.

**`HTTP 503 (capability not configured)`** — that capability isn't enabled on the backend. The endpoint exists but isn't wired up for your environment.

**Request timed out** — LinkedIn/X jobs can be slow; retry, or reduce scope (`--limit-per-input`, fewer inputs).
