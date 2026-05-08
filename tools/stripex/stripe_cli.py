#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "click>=8.1",
#   "stripe>=8.0",
#   "rich>=13.7",
# ]
# ///
"""
Stripe CLI - lookup customers, subscriptions, and invoices.

Usage:
    uv run stripe_cli.py [COMMAND] [SUBCOMMAND] [OPTIONS]

Commands:
    customer find --email|--domain|--name  - Find customers by email, domain, or name
    customer show <cus_id>                 - Show customer + all subscriptions
    subscription list [--customer]         - List subscriptions
    subscription show <sub_id>             - Subscription dates, status, plan, amount
    invoice list [--customer]              - List invoices

Examples:
    uv run stripe_cli.py customer find --name "Meena"
    uv run stripe_cli.py customer find --domain reachpsych.com
    uv run stripe_cli.py customer find --email meena@reachpsych.com
    uv run stripe_cli.py customer show cus_Abc123
    uv run stripe_cli.py subscription show sub_1Abc...
    uv run stripe_cli.py invoice list --customer cus_Abc123

Auth:
    Put your *restricted* API key in a .env file beside this script:
        STRIPE_API_KEY=rk_live_xxxxxxxxxxxx
    Generate at: Stripe -> Developers -> API keys -> "Create restricted key".
    Recommended read-only scopes: Customers, Subscriptions, Invoices,
    Plans, Prices, Products.

Why a restricted key (rk_) instead of the secret key (sk_)?
    Smaller blast radius. This CLI only reads. A read-only key can't move money,
    create customers, or modify subscriptions even if it leaks.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import click
import stripe
from rich.console import Console
from rich.table import Table


# =============================================================================
# Configuration
# =============================================================================

console = Console()


def load_api_key() -> str:
    """Load STRIPE_API_KEY from .env in the script's directory."""
    env_path = Path(__file__).parent / ".env"
    if not env_path.exists():
        raise click.ClickException(
            f".env file not found at {env_path}\n"
            "Create one with: STRIPE_API_KEY=rk_live_xxxxx\n"
            "(Generate at Stripe -> Developers -> API keys -> Create restricted key)"
        )
    with env_path.open() as f:
        for line in f:
            line = line.strip()
            if line.startswith("STRIPE_API_KEY="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise click.ClickException("STRIPE_API_KEY not found in .env file")


def init_stripe() -> None:
    """Set the SDK's API key. Called by every command."""
    if not getattr(stripe, "api_key", None):
        stripe.api_key = load_api_key()


# =============================================================================
# Formatting helpers
# =============================================================================


def fmt_ts(ts: Optional[int]) -> str:
    if ts is None:
        return "—"
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def fmt_date(ts: Optional[int]) -> str:
    if ts is None:
        return "—"
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")


def fmt_amount(amount_cents: Optional[int], currency: str = "usd") -> str:
    if amount_cents is None:
        return "—"
    return f"{amount_cents / 100:.2f} {currency.upper()}"


def sg(obj: Any, key: str, default: Any = None) -> Any:
    """Safe-get from a Stripe object or plain dict.

    StripeObject doesn't implement `.get()` and `bool(StripeObject)` is True
    even when empty — so the obvious `obj.get('foo')` pattern blows up. This
    helper falls back to `getattr` for StripeObject and `dict.get` for dicts.
    """
    if obj is None:
        return default
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


def get_period(sub: Any) -> tuple[Optional[int], Optional[int]]:
    """Return (current_period_start, current_period_end).

    In API versions before 2024-09-30 these fields live on the Subscription.
    In newer versions they moved to the subscription's items. We try
    subscription-level first and fall back to the first item.
    """
    start = sg(sub, "current_period_start")
    end = sg(sub, "current_period_end")
    if start and end:
        return start, end
    items_obj = sg(sub, "items")
    items = sg(items_obj, "data", []) if items_obj is not None else []
    if items:
        first = items[0]
        return sg(first, "current_period_start"), sg(first, "current_period_end")
    return None, None


def cust_id_of(obj: Any) -> str:
    """Extract a customer id from a string or a Customer-shaped object."""
    return obj if isinstance(obj, str) else getattr(obj, "id", str(obj))


# =============================================================================
# CLI root
# =============================================================================


@click.group(help="Stripe CLI - read-only lookups for customers and subscriptions.")
def cli() -> None:
    pass


@cli.command(help="Sanity-check the API key (shows account info).")
def me() -> None:
    init_stripe()
    acct = stripe.Account.retrieve()
    console.print(f"[cyan]Account:[/cyan] {acct.id}")
    biz = sg(acct, "business_profile") or {}
    console.print(f"[cyan]Business:[/cyan] {sg(biz, 'name') or '—'}")
    console.print(f"[cyan]Email:[/cyan] {sg(acct, 'email') or '—'}")
    console.print(f"[cyan]Country:[/cyan] {sg(acct, 'country') or '—'}")
    console.print(f"[cyan]Charges enabled:[/cyan] {sg(acct, 'charges_enabled')}")


# =============================================================================
# customer
# =============================================================================


@cli.group(name="customer", help="Customer lookup.")
def customer_group() -> None:
    pass


@customer_group.command(name="find", help="Find customers by email (exact) or domain (substring).")
@click.option("--email", help="Exact email match (uses Stripe Search).")
@click.option("--domain", help="Email domain, e.g. reachpsych.com. Iterates customers client-side.")
@click.option("--limit", default=20, show_default=True, type=int, help="Max results to print.")
def customer_find(email: Optional[str], domain: Optional[str], limit: int) -> None:
    init_stripe()
    if not (email or domain):
        raise click.UsageError("Provide --email or --domain.")
    if email and domain:
        raise click.UsageError("Use --email OR --domain, not both.")

    matches: list[Any] = []

    if email:
        # Stripe Search supports exact email match.
        result = stripe.Customer.search(query=f"email:'{email}'", limit=min(limit, 100))
        matches = list(result)[:limit]
    else:
        # Stripe doesn't support substring search on email natively.
        # Iterate customers and filter client-side. Cheap on small accounts;
        # bound by --limit to avoid scanning forever on large ones.
        domain_l = domain.lower().lstrip("@")
        scanned = 0
        for cust in stripe.Customer.list(limit=100).auto_paging_iter():
            scanned += 1
            cust_email = (cust.email or "").lower()
            if cust_email.endswith("@" + domain_l):
                matches.append(cust)
                if len(matches) >= limit:
                    break
            # Safety valve: don't scan forever.
            if scanned >= 5000:
                console.print(
                    f"[yellow]Warning:[/yellow] scanned {scanned} customers without "
                    f"filling --limit. Stopping. Consider --email instead."
                )
                break

    if not matches:
        click.echo("No customers found.")
        return

    table = Table(title=f"Customers ({len(matches)})", show_lines=False)
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Email")
    table.add_column("Name")
    table.add_column("Created")
    for c in matches:
        table.add_row(c.id, c.email or "—", c.name or "—", fmt_date(c.created))
    console.print(table)


@customer_group.command(name="show", help="Show customer details + all subscriptions.")
@click.argument("customer_id")
def customer_show(customer_id: str) -> None:
    init_stripe()
    cust = stripe.Customer.retrieve(customer_id)
    console.print(f"[cyan]ID:[/cyan] {cust.id}")
    console.print(f"[cyan]Email:[/cyan] {cust.email or '—'}")
    console.print(f"[cyan]Name:[/cyan] {cust.name or '—'}")
    console.print(f"[cyan]Created:[/cyan] {fmt_ts(cust.created)}")
    if cust.description:
        console.print(f"[cyan]Description:[/cyan] {cust.description}")
    # cust.metadata is a StripeObject; bool(StripeObject) is True even when empty.
    # Convert to a real dict via .to_dict(), then check truthiness.
    meta = cust.metadata.to_dict() if cust.metadata is not None else {}
    if meta:
        console.print(f"[cyan]Metadata:[/cyan] {meta}")

    subs = list(
        stripe.Subscription.list(customer=customer_id, status="all", limit=100).auto_paging_iter()
    )
    if not subs:
        console.print("\n[dim]No subscriptions.[/dim]")
        return

    table = Table(title="Subscriptions", show_lines=False)
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Status")
    table.add_column("Started")
    table.add_column("Period end")
    table.add_column("Cancel at")
    table.add_column("Plan")
    table.add_column("Amount")
    for s in subs:
        items = s["items"]["data"]
        price = items[0].price if items else None
        plan_label = (price.nickname or price.id) if price else "—"
        amount = fmt_amount(price.unit_amount, price.currency) if price else "—"
        interval = sg(sg(price, "recurring"), "interval", "") if price else ""
        _, period_end = get_period(s)
        cancel_at = sg(s, "cancel_at")
        table.add_row(
            s.id,
            s.status,
            fmt_date(sg(s, "start_date") or s.created),
            fmt_date(period_end),
            fmt_date(cancel_at) if cancel_at else "—",
            f"{plan_label} ({interval})" if interval else plan_label,
            amount,
        )
    console.print(table)


# =============================================================================
# subscription
# =============================================================================


@cli.group(name="subscription", help="Subscription lookup.")
def subscription_group() -> None:
    pass


@subscription_group.command(name="list", help="List subscriptions, optionally filtered.")
@click.option("--customer", help="Customer ID to filter by.")
@click.option(
    "--status",
    default="all",
    show_default=True,
    help="active, past_due, canceled, trialing, all, etc.",
)
@click.option("--limit", default=20, show_default=True, type=int)
def subscription_list(customer: Optional[str], status: str, limit: int) -> None:
    init_stripe()
    kwargs: dict[str, Any] = {"limit": min(limit, 100), "status": status}
    if customer:
        kwargs["customer"] = customer
    subs = list(stripe.Subscription.list(**kwargs).auto_paging_iter())[:limit]
    if not subs:
        click.echo("No subscriptions found.")
        return

    table = Table(title=f"Subscriptions ({len(subs)})", show_lines=False)
    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Customer", no_wrap=True)
    table.add_column("Status")
    table.add_column("Started")
    table.add_column("Period end")
    for s in subs:
        _, period_end = get_period(s)
        table.add_row(
            s.id,
            cust_id_of(s.customer),
            s.status,
            fmt_date(sg(s, "start_date") or s.created),
            fmt_date(period_end),
        )
    console.print(table)


@subscription_group.command(name="show", help="Show subscription dates, status, plan.")
@click.argument("subscription_id")
def subscription_show(subscription_id: str) -> None:
    init_stripe()
    s = stripe.Subscription.retrieve(
        subscription_id,
        expand=["customer", "items.data.price.product"],
    )

    cust = s.customer
    cust_email = cust.email if not isinstance(cust, str) else "—"
    cust_id = cust_id_of(cust)

    period_start, period_end = get_period(s)

    console.print(f"[cyan]ID:[/cyan] {s.id}")
    console.print(f"[cyan]Customer:[/cyan] {cust_id} ({cust_email})")
    console.print(f"[cyan]Status:[/cyan] {s.status}")
    console.print(f"[cyan]Started:[/cyan] {fmt_ts(sg(s, 'start_date') or s.created)}")
    console.print(f"[cyan]Current period start:[/cyan] {fmt_ts(period_start)}")
    console.print(f"[cyan]Current period end:[/cyan] {fmt_ts(period_end)}")
    if sg(s, "cancel_at_period_end"):
        console.print("[cyan]Cancel at period end:[/cyan] yes")
    if sg(s, "cancel_at"):
        console.print(f"[cyan]Cancel at:[/cyan] {fmt_ts(s.cancel_at)}")
    if sg(s, "canceled_at"):
        console.print(f"[cyan]Canceled at:[/cyan] {fmt_ts(s.canceled_at)}")
    if sg(s, "trial_start"):
        console.print(f"[cyan]Trial:[/cyan] {fmt_date(s.trial_start)} -> {fmt_date(s.trial_end)}")

    items = s["items"]["data"]
    if items:
        console.print("\n[bold]Items:[/bold]")
        for item in items:
            price = item.price
            product = price.product
            product_name = product.name if hasattr(product, "name") else str(product)
            interval = sg(sg(price, "recurring"), "interval") or "one-time"
            qty = sg(item, "quantity", 1)
            console.print(
                f"  - {product_name} | "
                f"{fmt_amount(price.unit_amount, price.currency)} / {interval} "
                f"x {qty}"
            )


# =============================================================================
# invoice
# =============================================================================


@cli.group(name="invoice", help="Invoice lookup.")
def invoice_group() -> None:
    pass


@invoice_group.command(name="list", help="List invoices, optionally filtered by customer.")
@click.option("--customer", help="Customer ID to filter by.")
@click.option("--limit", default=20, show_default=True, type=int)
def invoice_list(customer: Optional[str], limit: int) -> None:
    init_stripe()
    kwargs: dict[str, Any] = {"limit": min(limit, 100)}
    if customer:
        kwargs["customer"] = customer
    invoices = list(stripe.Invoice.list(**kwargs).auto_paging_iter())[:limit]
    if not invoices:
        click.echo("No invoices found.")
        return

    table = Table(title=f"Invoices ({len(invoices)})", show_lines=False)
    table.add_column("Number", style="cyan", no_wrap=True)
    table.add_column("Customer", no_wrap=True)
    table.add_column("Status")
    table.add_column("Date")
    table.add_column("Due")
    table.add_column("Paid")
    for inv in invoices:
        table.add_row(
            inv.number or inv.id,
            cust_id_of(inv.customer),
            inv.status or "—",
            fmt_date(inv.created),
            fmt_amount(inv.amount_due, inv.currency),
            fmt_amount(inv.amount_paid, inv.currency),
        )
    console.print(table)


if __name__ == "__main__":
    cli()
