#!/usr/bin/env python3
"""
Stripe CLI - A command-line interface for managing Stripe resources.

Usage:
    python cli.py [COMMAND] [OPTIONS]

Commands:
    product create   - Create a new product
    product list     - List products
    product get      - Get product details
    product update   - Update a product
    product delete   - Delete a product
    product search   - Search products

    price create     - Create a new price for a product
    price list       - List prices
    price get        - Get price details
    price update     - Update a price
    price search     - Search prices

    customer create  - Create a new customer
    customer list    - List customers
    customer get     - Get customer details
    customer update  - Update a customer
    customer delete  - Delete a customer
    customer search  - Search customers

    whoami           - Verify API key and show account balance

Examples:
    python cli.py product create -n "Premium Plan" -d "Our premium offering"
    python cli.py price create -p prod_xxx -a 2000 -c usd -r month
    python cli.py customer create -n "Jane Doe" -e "jane@example.com"
    python cli.py customer search -q 'email:"jane@example.com"'
"""

import click

from .api import format_amount
from .commands.products import product
from .commands.prices import price
from .commands.customers import customer


class LazyAPI:
    """Lazy wrapper that only initializes StripeAPI on first attribute access."""

    def __init__(self):
        self._api = None

    def _init(self):
        if self._api is None:
            from .api import StripeAPI
            self._api = StripeAPI()

    def __getattr__(self, name):
        if name.startswith("_"):
            raise AttributeError(name)
        self._init()
        return getattr(self._api, name)


@click.group()
@click.version_option(version="0.1.0", prog_name="stripe-cli")
@click.pass_context
def cli(ctx):
    """
    Stripe CLI - Manage Stripe products, prices, and customers.

    Configure your API key in a .env file:

        STRIPE_SECRET_KEY=sk_xxxxx

    Run 'stripe-cli COMMAND --help' for more information on a command.
    """
    ctx.ensure_object(dict)
    # Lazy initialization — API key is only loaded when a command actually
    # calls an API method, so --help works without a .env file.
    ctx.obj["api"] = LazyAPI()


# Register command groups
cli.add_command(product)
cli.add_command(price)
cli.add_command(customer)


@cli.command("whoami")
@click.pass_context
def whoami(ctx):
    """Verify API key and show account balance."""
    api: StripeAPI = ctx.obj["api"]

    balance = api.get_balance()

    click.echo(click.style("API Key Valid!", fg="green", bold=True))
    click.echo()

    available = balance.get("available", [])
    if available:
        click.echo("  Available Balance:")
        for b in available:
            amount = b.get("amount", 0)
            currency = b.get("currency", "usd")
            click.echo(f"    {format_amount(amount, currency)}")

    pending = balance.get("pending", [])
    if pending:
        click.echo("  Pending Balance:")
        for b in pending:
            amount = b.get("amount", 0)
            currency = b.get("currency", "usd")
            click.echo(f"    {format_amount(amount, currency)}")


if __name__ == "__main__":
    cli()
