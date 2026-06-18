# salesx

One CLI (and Python SDK) over the sales/marketing tools — **LinkedIn, X, Google,
ChatGPT, SEO, and Close CRM**. Each command wraps one backend capability and returns
canonical JSON.

## Setup

Needs [uv](https://docs.astral.sh/uv/) — no install step, `uv run` handles deps.

```bash
cp .env.example .env    # fill in only the keys you use (Marketing and/or Close)
```

## Use

Everything is discoverable through `--help` — there's no separate manual to read:

```bash
uv run salesx --help                        # the 6 groups
uv run salesx seo --help                    # commands in a group
uv run salesx seo domain-overview --help    # flags + the exact JSON shape returned
```

Each command's `--help` includes an `Output:` block describing its response.
Add `-f table` for human-readable output, or `-o FILE` to save JSON.

## As a library

```python
from salesx import Salesx
Salesx().seo.domain_overview(target="anthropic.com")   # -> a typed model
```
