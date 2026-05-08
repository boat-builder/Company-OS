# stripex — Stripe CLI

A lightweight, scriptable command-line tool for read-only lookups against [Stripe](https://stripe.com) — find a customer by email or domain, see when their subscription started and when it renews, list invoices — without opening the Stripe dashboard.

Single Python file, runs via [uv](https://docs.astral.sh/uv/) with no install step (deps are declared inline using PEP 723).

## Setup

### 1. Install `uv` (one-time)

```bash
brew install uv
# or: curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Create a restricted API key

1. Go to **Stripe → Developers → API keys → Create restricted key**.
2. Give it a name like `stripex-readonly`.
3. Set every permission to **None** except these, which should be **Read**:
   - Customers
   - Subscriptions
   - Invoices
   - Plans
   - Prices
   - Products
4. Copy the key (starts with `rk_live_` or `rk_test_`).

A restricted key (`rk_`) was chosen over a secret key (`sk_`) deliberately — this CLI only reads. A read-only key can't move money, create customers, or modify subscriptions even if it leaks.

### 3. Configure

Create a `.env` file in this directory:

```
STRIPE_API_KEY=rk_live_xxxxxxxxxxxxx
```

`.gitignore` already excludes `.env`. There's a `.env.example` checked in as a placeholder.

### 4. Verify

```bash
uv run stripe_cli.py me
```

The first run will install deps (click, stripe, rich) into a managed cache. Subsequent runs are instant.

## Why an API key, not `stripe login`?

Stripe's official CLI auths via a browser-based pairing flow that writes a session token to `~/.config/stripe/config.toml`. The session expires periodically and re-auth requires a browser — awkward for use from a sandboxed environment or scripts. A restricted API key in `.env` works everywhere, doesn't expire, and has a smaller blast radius than a full secret key.

## Usage

```bash
uv run stripe_cli.py [COMMAND] [SUBCOMMAND] [OPTIONS]
```

For a smoother experience, alias it in your shell:

```bash
# ~/.zshrc or ~/.bashrc
alias stripex="uv run /absolute/path/to/tools/stripex/stripe_cli.py"
```

Or make it executable (the shebang `#!/usr/bin/env -S uv run --script` does the rest):

```bash
chmod +x stripe_cli.py
./stripe_cli.py me
```

The examples below assume you've aliased it as `stripex`.

### Help

```bash
stripex --help
stripex customer --help
stripex customer find --help
```

---

## Commands

### Sanity check

```bash
# Confirms your API key works and shows your account
stripex me
```

### Find a customer

```bash
# Exact email (uses Stripe Search)
stripex customer find --email meena@reachpsych.com

# By domain (Stripe Search doesn't support email substrings, so this
# iterates customers and filters client-side)
stripex customer find --domain reachpsych.com

# Limit results (default 20)
stripex customer find --domain reachpsych.com --limit 5
```

### Show a customer + their subscriptions

```bash
stripex customer show cus_AbC123xyz
```

This is usually all you need — it prints customer details and a table of all subscriptions including start date, renewal date, plan, and amount.

### Subscriptions

```bash
# List subscriptions for a customer
stripex subscription list --customer cus_AbC123xyz

# All active subscriptions across the account
stripex subscription list --status active

# Full details for one subscription (start date, current period start/end,
# cancel_at, plan, items)
stripex subscription show sub_1Abc...
```

### Invoices

```bash
# Invoices for a customer
stripex invoice list --customer cus_AbC123xyz

# Recent invoices across the account
stripex invoice list --limit 50
```

---

## Typical workflow: "when does X's subscription end?"

```bash
# 1. Find the customer
stripex customer find --domain reachpsych.com

# 2. Pipe the cus_id into customer show — gives you everything in one go
stripex customer show cus_AbC123xyz
```

The `Subscriptions` table in `customer show` includes:

- **Started** — original subscription start date
- **Period end** — current period end (renewal date for active subs; expiry for canceled-at-period-end)
- **Cancel at** — explicit cancellation date if set
- **Plan / Amount** — what they're paying

For a full timestamped breakdown of one subscription:

```bash
stripex subscription show <sub_id>
```

---

## Project structure

```
tools/stripex/
├── .env.example  # template — copy to .env and fill in
├── .gitignore    # ignores .env
├── README.md     # this file
└── stripe_cli.py # single-file CLI (PEP 723 inline deps)
```

This mirrors the pattern used by [`tools/calx/`](../calx/).

---

## Notes on Stripe API behaviour

**Period fields moved.** In API versions before 2024-09-30, `current_period_start`/`current_period_end` lived on the Subscription object. In newer versions they moved to subscription items. `stripex` checks both locations so it works regardless of the API version your account is pinned to.

**Email substring search isn't a thing.** Stripe's Search API supports exact match on `email` (e.g. `email:'foo@bar.com'`), but no `LIKE` / wildcard. That's why `--domain` falls back to iterating customers — fine for accounts up to a few thousand, slow beyond that. If you ever hit the safety stop at 5000 customers scanned, switch to `--email`.

**Restricted keys can be scoped tighter.** If you ever want to prevent this CLI from seeing certain resources (e.g. payment methods, payouts), just leave those permissions at "None" when creating the key. The CLI only ever calls Customer, Subscription, Invoice, Account, Plan, Price, and Product endpoints.

---

## Stripe API reference

- [API keys overview](https://stripe.com/docs/keys)
- [Customer Search](https://stripe.com/docs/search)
- [Subscriptions API](https://stripe.com/docs/api/subscriptions)
- [Subscription period fields migration (2024-09-30)](https://stripe.com/docs/upgrades#2024-09-30.acacia)

---

## Troubleshooting

**`.env file not found`** — create `.env` in this directory with `STRIPE_API_KEY=rk_live_xxx`.

**`Invalid API Key provided`** — copy the key again. Restricted keys start with `rk_live_` or `rk_test_`. If you see `sk_`, that's the full secret key — works but has more privilege than this CLI needs.

**`No such permission` / 401 on a specific endpoint** — your restricted key is missing a Read scope. Edit the key at Stripe → Developers → API keys → click the key → tick the missing permission.

**`No customers found` for `--domain` but they're definitely there** — the customer may have a different email domain than expected (e.g. `gmail.com` rather than the company domain). Try `--email` with their actual email.

**`scanned 5000 customers without filling --limit`** — the safety stop. The customer probably doesn't exist; double-check spelling, or use `--email` if you know it.
