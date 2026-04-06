"""Price management commands for the Stripe CLI."""

import click

from ..api import StripeAPI, parse_metadata, format_amount


@click.group()
def price():
    """Manage prices in Stripe."""
    pass


def _display_price(p: dict, prefix: str = "  ") -> None:
    """Display a price's details."""
    click.echo(f"{prefix}ID:       {p.get('id')}")
    click.echo(f"{prefix}Product:  {p.get('product')}")

    amount = p.get("unit_amount")
    currency = p.get("currency", "usd")
    if amount is not None:
        click.echo(f"{prefix}Amount:   {format_amount(amount, currency)}")

    recurring = p.get("recurring")
    if recurring:
        interval = recurring.get("interval", "")
        count = recurring.get("interval_count", 1)
        interval_str = f"every {count} {interval}(s)" if count > 1 else interval
        click.echo(f"{prefix}Type:     Recurring ({interval_str})")
    else:
        click.echo(f"{prefix}Type:     One-time")

    active_str = click.style("Yes", fg="green") if p.get("active") else click.style("No", fg="yellow")
    click.echo(f"{prefix}Active:   {active_str}")

    if p.get("nickname"):
        click.echo(f"{prefix}Nickname: {p.get('nickname')}")


@price.command("create")
@click.option("--product", "-p", required=True, help="Product ID to attach the price to")
@click.option("--amount", "-a", required=True, type=int, help="Amount in smallest currency unit (e.g. cents)")
@click.option("--currency", "-c", required=True, help='Currency code (e.g. "usd", "eur")')
@click.option(
    "--recurring-interval", "-r", default=None,
    type=click.Choice(["day", "week", "month", "year"], case_sensitive=False),
    help="Recurring interval (omit for one-time price)",
)
@click.option("--interval-count", default=1, type=int, help="Number of intervals between billings (default: 1)")
@click.option("--nickname", default=None, help="Nickname for the price")
@click.option("--metadata", "-m", multiple=True, help="Metadata key=value pair (repeatable)")
@click.pass_context
def price_create(ctx, product: str, amount: int, currency: str, recurring_interval: str,
                 interval_count: int, nickname: str, metadata: tuple):
    """Create a new price for a product."""
    api: StripeAPI = ctx.obj["api"]
    meta = parse_metadata(metadata)

    result = api.create_price(
        unit_amount=amount,
        currency=currency,
        product_id=product,
        recurring_interval=recurring_interval,
        interval_count=interval_count,
        nickname=nickname,
        metadata=meta or None,
    )

    click.echo(click.style("Price created!", fg="green"))
    _display_price(result)


@price.command("list")
@click.option("--limit", "-l", default=10, help="Maximum number of prices to return")
@click.option("--product", "-p", default=None, help="Filter by product ID")
@click.option("--active/--inactive", default=None, help="Filter by active status")
@click.pass_context
def price_list(ctx, limit: int, product: str, active):
    """List prices with optional filters."""
    api: StripeAPI = ctx.obj["api"]

    result = api.list_prices(limit=limit, product_id=product, active=active)
    prices = result.get("data", [])

    if not prices:
        click.echo("No prices found.")
        return

    click.echo(f"Found {len(prices)} price(s):\n")
    for p in prices:
        amount = p.get("unit_amount")
        currency = p.get("currency", "usd")
        label = format_amount(amount, currency) if amount is not None else "N/A"
        click.echo(f"  {click.style(label, fg='cyan', bold=True)}")
        _display_price(p, prefix="    ")
        click.echo()


@price.command("get")
@click.argument("price_id")
@click.pass_context
def price_get(ctx, price_id: str):
    """Get details for a specific price."""
    api: StripeAPI = ctx.obj["api"]

    p = api.get_price(price_id)

    amount = p.get("unit_amount")
    currency = p.get("currency", "usd")
    label = format_amount(amount, currency) if amount is not None else "Price"
    click.echo(click.style(label, fg="cyan", bold=True))
    _display_price(p)

    meta = p.get("metadata", {})
    if meta:
        click.echo("  Metadata:")
        for k, v in meta.items():
            click.echo(f"    {k}: {v}")


@price.command("update")
@click.argument("price_id")
@click.option("--active/--no-active", default=None, help="Set active status")
@click.option("--nickname", default=None, help="New nickname")
@click.option("--metadata", "-m", multiple=True, help="Metadata key=value pair (repeatable)")
@click.pass_context
def price_update(ctx, price_id: str, active, nickname: str, metadata: tuple):
    """Update a price's fields."""
    api: StripeAPI = ctx.obj["api"]
    meta = parse_metadata(metadata)

    if not any([active is not None, nickname, meta]):
        raise click.UsageError(
            "Please provide at least one field to update "
            "(--active/--no-active, --nickname, or --metadata)"
        )

    result = api.update_price(
        price_id=price_id, active=active, nickname=nickname, metadata=meta or None,
    )

    click.echo(click.style("Price updated!", fg="green"))
    _display_price(result)


@price.command("search")
@click.option("--query", "-q", required=True, help='Stripe search query (e.g. product:"prod_xxx")')
@click.option("--limit", "-l", default=10, help="Maximum number of results")
@click.pass_context
def price_search(ctx, query: str, limit: int):
    """Search prices using Stripe's query syntax."""
    api: StripeAPI = ctx.obj["api"]

    result = api.search_prices(query=query, limit=limit)
    prices = result.get("data", [])

    if not prices:
        click.echo("No prices found matching your search.")
        return

    click.echo(f"Found {len(prices)} price(s):\n")
    for p in prices:
        amount = p.get("unit_amount")
        currency = p.get("currency", "usd")
        label = format_amount(amount, currency) if amount is not None else "N/A"
        click.echo(f"  {click.style(label, fg='cyan', bold=True)}")
        _display_price(p, prefix="    ")
        click.echo()
