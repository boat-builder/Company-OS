"""Product management commands for the Stripe CLI."""

import click

from ..api import StripeAPI, parse_metadata


@click.group()
def product():
    """Manage products in Stripe."""
    pass


@product.command("create")
@click.option("--name", "-n", required=True, help="Product name")
@click.option("--description", "-d", default=None, help="Product description")
@click.option("--active/--no-active", default=None, help="Whether the product is active (default: active)")
@click.option("--metadata", "-m", multiple=True, help="Metadata key=value pair (repeatable)")
@click.pass_context
def product_create(ctx, name: str, description: str, active, metadata: tuple):
    """Create a new product."""
    api: StripeAPI = ctx.obj["api"]
    meta = parse_metadata(metadata)

    result = api.create_product(
        name=name, description=description, active=active, metadata=meta or None,
    )

    click.echo(click.style("Product created!", fg="green"))
    click.echo(f"  ID:          {result.get('id')}")
    click.echo(f"  Name:        {result.get('name')}")
    if result.get("description"):
        click.echo(f"  Description: {result.get('description')}")
    active_str = click.style("Yes", fg="green") if result.get("active") else click.style("No", fg="yellow")
    click.echo(f"  Active:      {active_str}")


@product.command("list")
@click.option("--limit", "-l", default=10, help="Maximum number of products to return")
@click.option("--active/--inactive", default=None, help="Filter by active status")
@click.pass_context
def product_list(ctx, limit: int, active):
    """List products with optional filters."""
    api: StripeAPI = ctx.obj["api"]

    result = api.list_products(limit=limit, active=active)
    products = result.get("data", [])

    if not products:
        click.echo("No products found.")
        return

    click.echo(f"Found {len(products)} product(s):\n")
    for p in products:
        click.echo(f"  {click.style(p.get('name', 'Unnamed'), fg='cyan', bold=True)}")
        click.echo(f"    ID:          {p.get('id')}")
        active_str = click.style("Yes", fg="green") if p.get("active") else click.style("No", fg="yellow")
        click.echo(f"    Active:      {active_str}")
        if p.get("description"):
            click.echo(f"    Description: {p.get('description')}")
        click.echo()


@product.command("get")
@click.argument("product_id")
@click.pass_context
def product_get(ctx, product_id: str):
    """Get details for a specific product."""
    api: StripeAPI = ctx.obj["api"]

    p = api.get_product(product_id)

    click.echo(click.style(p.get("name", "Unnamed"), fg="cyan", bold=True))
    click.echo(f"  ID:          {p.get('id')}")
    active_str = click.style("Yes", fg="green") if p.get("active") else click.style("No", fg="yellow")
    click.echo(f"  Active:      {active_str}")
    click.echo(f"  Description: {p.get('description', 'N/A')}")
    click.echo(f"  Created:     {p.get('created', 'N/A')}")

    if p.get("default_price"):
        click.echo(f"  Default Price: {p.get('default_price')}")

    meta = p.get("metadata", {})
    if meta:
        click.echo("  Metadata:")
        for k, v in meta.items():
            click.echo(f"    {k}: {v}")


@product.command("update")
@click.argument("product_id")
@click.option("--name", "-n", default=None, help="New product name")
@click.option("--description", "-d", default=None, help="New description")
@click.option("--active/--no-active", default=None, help="Set active status")
@click.option("--metadata", "-m", multiple=True, help="Metadata key=value pair (repeatable)")
@click.pass_context
def product_update(ctx, product_id: str, name: str, description: str, active, metadata: tuple):
    """Update a product's fields."""
    api: StripeAPI = ctx.obj["api"]
    meta = parse_metadata(metadata)

    if not any([name, description, active is not None, meta]):
        raise click.UsageError(
            "Please provide at least one field to update "
            "(--name, --description, --active/--no-active, or --metadata)"
        )

    result = api.update_product(
        product_id=product_id, name=name, description=description,
        active=active, metadata=meta or None,
    )

    click.echo(click.style("Product updated!", fg="green"))
    click.echo(f"  ID:          {result.get('id')}")
    click.echo(f"  Name:        {result.get('name')}")
    if result.get("description"):
        click.echo(f"  Description: {result.get('description')}")
    active_str = click.style("Yes", fg="green") if result.get("active") else click.style("No", fg="yellow")
    click.echo(f"  Active:      {active_str}")


@product.command("delete")
@click.argument("product_id")
@click.option("--yes", "-y", is_flag=True, default=False, help="Skip confirmation prompt")
@click.pass_context
def product_delete(ctx, product_id: str, yes: bool):
    """Delete a product."""
    api: StripeAPI = ctx.obj["api"]

    if not yes:
        try:
            p = api.get_product(product_id)
            product_name = p.get("name", product_id)
        except Exception:
            product_name = product_id
        if not click.confirm(f"Delete product '{product_name}' ({product_id})? This cannot be undone"):
            click.echo("Cancelled.")
            return

    api.delete_product(product_id)
    click.echo(click.style(f"Product {product_id} deleted.", fg="green"))


@product.command("search")
@click.option("--query", "-q", required=True, help='Stripe search query (e.g. name~"premium")')
@click.option("--limit", "-l", default=10, help="Maximum number of results")
@click.pass_context
def product_search(ctx, query: str, limit: int):
    """Search products using Stripe's query syntax."""
    api: StripeAPI = ctx.obj["api"]

    result = api.search_products(query=query, limit=limit)
    products = result.get("data", [])

    if not products:
        click.echo("No products found matching your search.")
        return

    click.echo(f"Found {len(products)} product(s):\n")
    for p in products:
        click.echo(f"  {click.style(p.get('name', 'Unnamed'), fg='cyan', bold=True)}")
        click.echo(f"    ID:          {p.get('id')}")
        active_str = click.style("Yes", fg="green") if p.get("active") else click.style("No", fg="yellow")
        click.echo(f"    Active:      {active_str}")
        if p.get("description"):
            click.echo(f"    Description: {p.get('description')}")
        click.echo()
