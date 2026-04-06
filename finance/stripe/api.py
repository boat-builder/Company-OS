"""
Stripe API client for the Stripe CLI.

Handles authentication, HTTP requests, and all resource operations
for Products, Prices, and Customers.
"""

import click
import requests
from pathlib import Path
from typing import Optional


# =============================================================================
# Configuration
# =============================================================================

BASE_URL = "https://api.stripe.com/v1"


def load_api_key() -> str:
    """Load API key from .env file in the script's directory."""
    env_path = Path(__file__).parent / ".env"
    if not env_path.exists():
        raise click.ClickException(
            f".env file not found at {env_path}\n"
            "Create a .env file with: STRIPE_SECRET_KEY=sk_xxxxx"
        )

    with open(env_path, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("STRIPE_SECRET_KEY="):
                return line.split("=", 1)[1].strip()

    raise click.ClickException("STRIPE_SECRET_KEY not found in .env file")


def get_api_key() -> str:
    """Get API key with caching."""
    if not hasattr(get_api_key, "_cached_key"):
        get_api_key._cached_key = load_api_key()
    return get_api_key._cached_key


# =============================================================================
# Helpers
# =============================================================================

def format_amount(amount_cents: int, currency: str) -> str:
    """Format an amount in smallest currency unit to a display string.

    Example: format_amount(2000, "usd") -> "$20.00 USD"
    """
    amount = amount_cents / 100
    currency_upper = currency.upper()
    if currency.lower() == "usd":
        return f"${amount:,.2f} {currency_upper}"
    return f"{amount:,.2f} {currency_upper}"


def parse_metadata(metadata_pairs: tuple) -> dict:
    """Parse metadata key=value pairs from CLI input.

    Args:
        metadata_pairs: Tuple of "key=value" strings from Click's multiple option.

    Returns:
        Dict of metadata keys to values.
    """
    if not metadata_pairs:
        return {}
    result = {}
    for pair in metadata_pairs:
        if "=" not in pair:
            raise click.BadParameter(
                f"Invalid metadata format: '{pair}'. Use key=value format."
            )
        key, value = pair.split("=", 1)
        result[key.strip()] = value.strip()
    return result


# =============================================================================
# API Client
# =============================================================================

class StripeAPI:
    """Stripe API client using Bearer token authentication."""

    def __init__(self):
        self.api_key = get_api_key()
        self.base_url = BASE_URL

    def _request(self, method: str, endpoint: str, **kwargs) -> dict:
        """Make an authenticated request to the Stripe API."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {self.api_key}"

        response = requests.request(method, url, headers=headers, **kwargs)

        if not response.ok:
            try:
                err = response.json().get("error", {})
                msg = err.get("message", response.text)
            except (ValueError, AttributeError):
                msg = response.text
            raise click.ClickException(f"API Error ({response.status_code}): {msg}")

        if response.status_code == 204 or not response.content:
            return {}

        return response.json()

    def get(self, endpoint: str, **kwargs) -> dict:
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> dict:
        return self._request("POST", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> dict:
        return self._request("DELETE", endpoint, **kwargs)

    def _flatten_metadata(self, metadata: dict) -> dict:
        """Convert a metadata dict to Stripe's form-encoded format.

        Example: {"foo": "bar"} -> {"metadata[foo]": "bar"}
        """
        return {f"metadata[{k}]": v for k, v in metadata.items()}

    # -------------------------------------------------------------------------
    # Product Operations
    # -------------------------------------------------------------------------

    def create_product(
        self,
        name: str,
        description: Optional[str] = None,
        active: Optional[bool] = None,
        metadata: Optional[dict] = None,
    ) -> dict:
        """Create a new product."""
        data = {"name": name}
        if description is not None:
            data["description"] = description
        if active is not None:
            data["active"] = str(active).lower()
        if metadata:
            data.update(self._flatten_metadata(metadata))
        return self.post("/products", data=data)

    def list_products(self, limit: int = 10, active: Optional[bool] = None) -> dict:
        """List products with optional filters."""
        params = {"limit": limit}
        if active is not None:
            params["active"] = str(active).lower()
        return self.get("/products", params=params)

    def get_product(self, product_id: str) -> dict:
        """Retrieve a single product by ID."""
        return self.get(f"/products/{product_id}")

    def update_product(
        self,
        product_id: str,
        name: Optional[str] = None,
        description: Optional[str] = None,
        active: Optional[bool] = None,
        metadata: Optional[dict] = None,
    ) -> dict:
        """Update an existing product."""
        data = {}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        if active is not None:
            data["active"] = str(active).lower()
        if metadata:
            data.update(self._flatten_metadata(metadata))
        return self.post(f"/products/{product_id}", data=data)

    def delete_product(self, product_id: str) -> dict:
        """Delete a product."""
        return self.delete(f"/products/{product_id}")

    def search_products(self, query: str, limit: int = 10) -> dict:
        """Search products using Stripe's search query syntax."""
        return self.get("/products/search", params={"query": query, "limit": limit})

    # -------------------------------------------------------------------------
    # Price Operations
    # -------------------------------------------------------------------------

    def create_price(
        self,
        unit_amount: int,
        currency: str,
        product_id: str,
        recurring_interval: Optional[str] = None,
        interval_count: int = 1,
        nickname: Optional[str] = None,
        active: Optional[bool] = None,
        metadata: Optional[dict] = None,
    ) -> dict:
        """Create a new price for a product."""
        data = {
            "unit_amount": str(unit_amount),
            "currency": currency,
            "product": product_id,
        }
        if recurring_interval:
            data["recurring[interval]"] = recurring_interval
            data["recurring[interval_count]"] = str(interval_count)
        if nickname is not None:
            data["nickname"] = nickname
        if active is not None:
            data["active"] = str(active).lower()
        if metadata:
            data.update(self._flatten_metadata(metadata))
        return self.post("/prices", data=data)

    def list_prices(
        self,
        limit: int = 10,
        product_id: Optional[str] = None,
        active: Optional[bool] = None,
    ) -> dict:
        """List prices with optional filters."""
        params = {"limit": limit}
        if product_id is not None:
            params["product"] = product_id
        if active is not None:
            params["active"] = str(active).lower()
        return self.get("/prices", params=params)

    def get_price(self, price_id: str) -> dict:
        """Retrieve a single price by ID."""
        return self.get(f"/prices/{price_id}")

    def update_price(
        self,
        price_id: str,
        active: Optional[bool] = None,
        nickname: Optional[str] = None,
        metadata: Optional[dict] = None,
    ) -> dict:
        """Update an existing price."""
        data = {}
        if active is not None:
            data["active"] = str(active).lower()
        if nickname is not None:
            data["nickname"] = nickname
        if metadata:
            data.update(self._flatten_metadata(metadata))
        return self.post(f"/prices/{price_id}", data=data)

    def search_prices(self, query: str, limit: int = 10) -> dict:
        """Search prices using Stripe's search query syntax."""
        return self.get("/prices/search", params={"query": query, "limit": limit})

    # -------------------------------------------------------------------------
    # Customer Operations
    # -------------------------------------------------------------------------

    def create_customer(
        self,
        name: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        description: Optional[str] = None,
        metadata: Optional[dict] = None,
    ) -> dict:
        """Create a new customer."""
        data = {}
        if name is not None:
            data["name"] = name
        if email is not None:
            data["email"] = email
        if phone is not None:
            data["phone"] = phone
        if description is not None:
            data["description"] = description
        if metadata:
            data.update(self._flatten_metadata(metadata))
        return self.post("/customers", data=data)

    def list_customers(
        self,
        limit: int = 10,
        email: Optional[str] = None,
    ) -> dict:
        """List customers with optional filters."""
        params = {"limit": limit}
        if email is not None:
            params["email"] = email
        return self.get("/customers", params=params)

    def get_customer(self, customer_id: str) -> dict:
        """Retrieve a single customer by ID."""
        return self.get(f"/customers/{customer_id}")

    def update_customer(
        self,
        customer_id: str,
        name: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        description: Optional[str] = None,
        metadata: Optional[dict] = None,
    ) -> dict:
        """Update an existing customer."""
        data = {}
        if name is not None:
            data["name"] = name
        if email is not None:
            data["email"] = email
        if phone is not None:
            data["phone"] = phone
        if description is not None:
            data["description"] = description
        if metadata:
            data.update(self._flatten_metadata(metadata))
        return self.post(f"/customers/{customer_id}", data=data)

    def delete_customer(self, customer_id: str) -> dict:
        """Delete a customer."""
        return self.delete(f"/customers/{customer_id}")

    def search_customers(self, query: str, limit: int = 10) -> dict:
        """Search customers using Stripe's search query syntax."""
        return self.get("/customers/search", params={"query": query, "limit": limit})

    # -------------------------------------------------------------------------
    # Account / Utility
    # -------------------------------------------------------------------------

    def get_balance(self) -> dict:
        """Get account balance to verify API key."""
        return self.get("/balance")
