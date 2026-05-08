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

If you want richer access (e.g. for `customer show` to surface bank/card details, or to read account-level info), grant those Read scopes too. The CLI only ever calls read endpoints.

A restricted key (`rk_`) was chosen over a secret key (`sk_`) deliberately — this CLI only reads. A read-only key can't move money, create customers, or modify subscriptions even if it leaks.

### 3. Configure

Create a `.env` file in this directory:

```
STRIPE_API_KEY=rk_live_xxxxxxxxxxxxx
```

`.gitignore` already excludes `.env`. There's a `.env.example` checked in as a placeholder.

### 4. Verify

```bash
uv run stripe_cli.py customer find --name "test"
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

### Find a customer

`customer find` accepts exactly one of `--email`, `--domain`, or `--name`. All three go through the Stripe Search API — no client-side iteration, no scanning.

```bash
# Exact email match — email:'foo@bar.com'
stripex customer find --email meena@reachpsych.com

# Email domain (case-insensitive substring against the @domain suffix) — email~'@reachpsych.com'
stripex customer find --domain reachpsych.com

# Customer name (case-insensitive substring) — name~'meena'
stripex customer find --name "Meena"

# Limit results (default 20)
stripex customer find --domain gmail.com --limit 5
```

If `--domain` returns nothing, the customer's billing email may be on a different domain than expected — try `--name` instead.

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
# 1. Find the customer (try name first — most reliable when you know who they are)
stripex customer find --name "Meena"

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

**Search supports both exact and substring on string fields.** Stripe's Search query language has `field:'value'` (exact match) and `field~'value'` (case-insensitive substring) for `email` and `name`. `stripex` uses both: `--email` is exact, `--domain` and `--name` are substring.

**`StripeObject` is not a dict.** It supports `obj["key"]` but not `obj.get("key")`, and `bool(empty_obj)` is `True`. The CLI uses an internal `sg(obj, key, default)` helper to paper over that. If you extend the CLI and access fields that may be missing, use `sg` rather than `.get`.

**Restricted keys can be scoped tighter or wider.** If you ever want to prevent this CLI from seeing certain resources, leave those permissions at "None" when creating the key. The CLI only ever calls Customer, Subscription, Invoice, Plan, Price, and Product endpoints — no Account, no Charges, no PaymentMethods.

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

**`No customers found` for `--domain` but they're definitely there** — their billing email may be on a different domain than expected (e.g. `gmail.com` rather than the company domain). Try `--name` with their first or last name.

**Stripe Search returns no result but you can see them in the dashboard** — Stripe's Search index lags writes by a few seconds. Brand-new customers may not appear immediately.
