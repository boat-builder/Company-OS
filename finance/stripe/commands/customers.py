"""Customer management commands for the Stripe CLI."""

import click

from ..api import StripeAPI, parse_metadata


@click.group()
def customer():
    """Manage customers in Stripe."""
    pass


def _display_customer(c: dict, prefix: str = "  ") -> None:
    """Display a customer's details."""
    click.echo(f"{prefix}ID:          {c.get('id')}")
    click.echo(f"{prefix}Name:        {c.get('name', 'N/A')}")
    click.echo(f"{prefix}Email:       {c.get('email', 'N/A')}")
    if c.get("phone"):
        click.echo(f"{prefix}Phone:       {c.get('phone')}")
    if c.get("description"):
        click.echo(f"{prefix}Description: {c.get('description')}")


@customer.command("create")
@click.option("--name", "-n", default=None, help="Customer name")
@click.option("--email", "-e", default=None, help="Customer email")
@click.option("--phone", "-p", default=None, help="Customer phone number")
@click.option("--description", "-d", default=None, help="Customer description")
@click.option("--metadata", "-m", multiple=True, help="Metadata key=value pair (repeatable)")
@click.pass_context
def customer_create(ctx, name: str, email: str, phone: str, description: str, metadata: tuple):
    """Create a new customer."""
    api: StripeAPI = ctx.obj["api"]
    meta = parse_metadata(metadata)

    result = api.create_customer(
        name=name, email=email, phone=phone, description=description,
        metadata=meta or None,
    )

    click.echo(click.style("Customer created!", fg="green"))
    _display_customer(result)


@customer.command("list")
@click.option("--limit", "-l", default=10, help="Maximum number of customers to return")
@click.option("--email", "-e", default=None, help="Filter by exact email address")
@click.pass_context
def customer_list(ctx, limit: int, email: str):
    """List customers with optional filters."""
    api: StripeAPI = ctx.obj["api"]

    result = api.list_customers(limit=limit, email=email)
    customers = result.get("data", [])

    if not customers:
        click.echo("No customers found.")
        return

    click.echo(f"Found {len(customers)} customer(s):\n")
    for c in customers:
        name = c.get("name") or c.get("email") or "Unnamed"
        click.echo(f"  {click.style(name, fg='cyan', bold=True)}")
        _display_customer(c, prefix="    ")
        click.echo()


@customer.command("get")
@click.argument("customer_id")
@click.pass_context
def customer_get(ctx, customer_id: str):
    """Get details for a specific customer."""
    api: StripeAPI = ctx.obj["api"]

    c = api.get_customer(customer_id)

    name = c.get("name") or c.get("email") or "Unnamed"
    click.echo(click.style(name, fg="cyan", bold=True))
    _display_customer(c)
    click.echo(f"  Created:     {c.get('created', 'N/A')}")

    balance = c.get("balance", 0)
    currency = c.get("currency", "usd")
    if balance != 0 and currency:
        from ..api import format_amount
        click.echo(f"  Balance:     {format_amount(balance, currency)}")

    meta = c.get("metadata", {})
    if meta:
        click.echo("  Metadata:")
        for k, v in meta.items():
            click.echo(f"    {k}: {v}")


@customer.command("update")
@click.argument("customer_id")
@click.option("--name", "-n", default=None, help="New customer name")
@click.option("--email", "-e", default=None, help="New email address")
@click.option("--phone", "-p", default=None, help="New phone number")
@click.option("--description", "-d", default=None, help="New description")
@click.option("--metadata", "-m", multiple=True, help="Metadata key=value pair (repeatable)")
@click.pass_context
def customer_update(ctx, customer_id: str, name: str, email: str, phone: str,
                    description: str, metadata: tuple):
    """Update a customer's fields."""
    api: StripeAPI = ctx.obj["api"]
    meta = parse_metadata(metadata)

    if not any([name, email, phone, description, meta]):
        raise click.UsageError(
            "Please provide at least one field to update "
            "(--name, --email, --phone, --description, or --metadata)"
        )

    result = api.update_customer(
        customer_id=customer_id, name=name, email=email, phone=phone,
        description=description, metadata=meta or None,
    )

    click.echo(click.style("Customer updated!", fg="green"))
    _display_customer(result)


@customer.command("delete")
@click.argument("customer_id")
@click.option("--yes", "-y", is_flag=True, default=False, help="Skip confirmation prompt")
@click.pass_context
def customer_delete(ctx, customer_id: str, yes: bool):
    """Delete a customer."""
    api: StripeAPI = ctx.obj["api"]

    if not yes:
        try:
            c = api.get_customer(customer_id)
            customer_name = c.get("name") or c.get("email") or customer_id
        except Exception:
            customer_name = customer_id
        if not click.confirm(f"Delete customer '{customer_name}' ({customer_id})? This cannot be undone"):
            click.echo("Cancelled.")
            return

    api.delete_customer(customer_id)
    click.echo(click.style(f"Customer {customer_id} deleted.", fg="green"))


@customer.command("search")
@click.option("--query", "-q", required=True, help='Stripe search query (e.g. email:"jane@example.com")')
@click.option("--limit", "-l", default=10, help="Maximum number of results")
@click.pass_context
def customer_search(ctx, query: str, limit: int):
    """Search customers using Stripe's query syntax."""
    api: StripeAPI = ctx.obj["api"]

    result = api.search_customers(query=query, limit=limit)
    customers = result.get("data", [])

    if not customers:
        click.echo("No customers found matching your search.")
        return

    click.echo(f"Found {len(customers)} customer(s):\n")
    for c in customers:
        name = c.get("name") or c.get("email") or "Unnamed"
        click.echo(f"  {click.style(name, fg='cyan', bold=True)}")
        _display_customer(c, prefix="    ")
        click.echo()
