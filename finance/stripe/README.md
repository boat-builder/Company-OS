# Stripe CLI

A command-line interface for managing Stripe products, prices, and customers.

## Setup

### 1. Install Dependencies

```bash
pip install click requests
```

### 2. Configure API Key

Create a `.env` file in the `finance/stripe/` directory:

```
STRIPE_SECRET_KEY=sk_xxxxxxxxxxxxx
```

You can find your API key in the Stripe Dashboard: **Developers > API Keys**

## Usage

```bash
python -m finance.stripe.cli [COMMAND] [SUBCOMMAND] [OPTIONS]
# or from the finance/stripe directory:
python cli.py [COMMAND] [SUBCOMMAND] [OPTIONS]
```

### Get Help

```bash
python cli.py --help
python cli.py product --help
python cli.py product create --help
```

---

## Commands

### Product Management

```bash
# Create a product
python cli.py product create -n "Premium Plan" -d "Our premium offering"
python cli.py product create -n "Enterprise" --no-active -m "tier=enterprise"

# List products
python cli.py product list
python cli.py product list -l 25 --active

# Search products
python cli.py product search -q 'name~"premium"'

# Get product details
python cli.py product get prod_xxx

# Update a product
python cli.py product update prod_xxx -n "Premium Plan v2" --description "Updated plan"
python cli.py product update prod_xxx --no-active

# Delete a product
python cli.py product delete prod_xxx
python cli.py product delete prod_xxx --yes   # skip confirmation
```

### Price Management

```bash
# Create a one-time price ($20.00 USD)
python cli.py price create -p prod_xxx -a 2000 -c usd

# Create a recurring price ($10/month)
python cli.py price create -p prod_xxx -a 1000 -c usd -r month

# Create a quarterly recurring price ($30 every 3 months)
python cli.py price create -p prod_xxx -a 3000 -c usd -r month --interval-count 3

# Create a price with a nickname
python cli.py price create -p prod_xxx -a 5000 -c usd -r year --nickname "Annual Plan"

# List prices
python cli.py price list
python cli.py price list -p prod_xxx --active

# Search prices
python cli.py price search -q 'product:"prod_xxx"'

# Get price details
python cli.py price get price_xxx

# Update a price
python cli.py price update price_xxx --nickname "Monthly Basic"
python cli.py price update price_xxx --no-active
```

### Customer Management

```bash
# Create a customer
python cli.py customer create -n "Jane Doe" -e "jane@example.com" -p "+1-555-1234"
python cli.py customer create -n "Acme Corp" -d "Enterprise account" -m "plan=enterprise"

# List customers
python cli.py customer list
python cli.py customer list -l 25 -e "jane@example.com"

# Search customers
python cli.py customer search -q 'email:"jane@example.com"'
python cli.py customer search -q 'name~"acme"'

# Get customer details
python cli.py customer get cus_xxx

# Update a customer
python cli.py customer update cus_xxx -n "Jane Smith" -e "jane.smith@example.com"

# Delete a customer
python cli.py customer delete cus_xxx
python cli.py customer delete cus_xxx --yes   # skip confirmation
```

### Utilities

```bash
# Verify API key and show account balance
python cli.py whoami
```

---

## Example Workflows

### Set up a new subscription product

```bash
# Create the product
python cli.py product create -n "Pro Plan" -d "Professional tier with all features"
# Copy the prod_xxx ID from output

# Create monthly and annual prices
python cli.py price create -p prod_xxx -a 2900 -c usd -r month --nickname "Pro Monthly"
python cli.py price create -p prod_xxx -a 29000 -c usd -r year --nickname "Pro Annual"

# Verify setup
python cli.py price list -p prod_xxx
```

### Onboard a new customer

```bash
# Create the customer
python cli.py customer create -n "Alice Johnson" -e "alice@company.com" -d "Referred by Bob"

# Verify
python cli.py customer get cus_xxx
```

### Find and update a customer

```bash
python cli.py customer search -q 'email:"alice@company.com"'
python cli.py customer update cus_xxx -p "+1-555-9876" -m "segment=enterprise"
```

### Deactivate a product and its prices

```bash
# List prices for the product
python cli.py price list -p prod_xxx

# Deactivate each price
python cli.py price update price_xxx --no-active
python cli.py price update price_yyy --no-active

# Deactivate the product
python cli.py product update prod_xxx --no-active
```

---

## Metadata

Several commands support arbitrary metadata via the `-m` / `--metadata` flag. Pass metadata as `key=value` pairs (repeatable):

```bash
python cli.py product create -n "Widget" -m "category=hardware" -m "sku=W-001"
python cli.py customer update cus_xxx -m "plan=enterprise" -m "region=us-east"
```

---

## Search Query Syntax

Stripe uses its own search query language. Common patterns:

| Query | Description |
|-------|-------------|
| `name~"premium"` | Name contains "premium" |
| `email:"jane@example.com"` | Exact email match |
| `metadata["key"]:"value"` | Metadata field match |
| `active:"true"` | Active resources only |
| `created>1609459200` | Created after a Unix timestamp |

See [Stripe Search Documentation](https://docs.stripe.com/search) for full syntax.

---

## Extending the CLI

The CLI is built with [Click](https://click.palletsprojects.com/) and organized as a Python package:

```
finance/stripe/
├── cli.py              # Entry point and root group
├── api.py              # StripeAPI client class
└── commands/
    ├── products.py     # Product commands
    ├── prices.py       # Price commands
    └── customers.py    # Customer commands
```

### Adding a new resource

1. Create a new command file in `commands/` (e.g. `subscriptions.py`)
2. Add API methods to the `StripeAPI` class in `api.py`
3. Register the command group in `cli.py` with `cli.add_command()`

---

## Stripe API Reference

- [Stripe API Documentation](https://docs.stripe.com/api)
- [Products API](https://docs.stripe.com/api/products)
- [Prices API](https://docs.stripe.com/api/prices)
- [Customers API](https://docs.stripe.com/api/customers)
- [Search API](https://docs.stripe.com/search)

---

## Troubleshooting

### "STRIPE_SECRET_KEY not found in .env file"

Make sure your `.env` file is in the `finance/stripe/` directory and contains `STRIPE_SECRET_KEY=sk_xxx` (no quotes around the key).

### "API Error (401): Invalid API Key provided"

Your API key may be invalid or expired. Generate a new one in the Stripe Dashboard: **Developers > API Keys**

### "API Error (404): resource missing"

The resource ID doesn't exist. Use `product list`, `price list`, or `customer list` to find valid IDs.

### "API Error (400): ..."

Check the error message — common causes include missing required fields, invalid parameter values, or trying to delete a product that still has active prices.
