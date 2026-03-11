#!/usr/bin/env python3
"""
Close CRM CLI - A command-line interface for interacting with Close CRM.

Usage:
    python close_cli.py [COMMAND] [OPTIONS]

Commands:
    lead create   - Create a new lead
    lead list     - List leads (with optional status/sort filters)
    lead search   - Search leads by name or query
    lead get      - Get details for a specific lead
    lead update   - Update a lead's fields
    lead delete   - Delete a lead

    contact create - Add a contact to a lead
    contact list   - List contacts for a lead
    contact get    - Get contact details
    contact update - Update a contact's fields
    contact delete - Delete a contact

    task create   - Create a new task for a lead
    task list     - List tasks (use --pending for incomplete only, --show-lead for lead names)
    task update   - Update a task's due date, text, or assignee
    task complete - Mark a task as complete
    task delete   - Delete a task

    note create   - Add a note to a lead
    note list     - List notes for a lead

    status list   - List all lead statuses
    whoami        - Show current user information

Examples:
    python close_cli.py lead create -n "Acme Corp" -u "https://acme.com"
    python close_cli.py lead list --status-id stat_xxx --sort -date_updated
    python close_cli.py contact create lead_xxx -n "Jane Doe" -t "CEO" -e "jane@acme.com"
    python close_cli.py note create lead_xxx -t "Had a great intro call"
    python close_cli.py task create --lead-id lead_xxx --text "Follow up"
    python close_cli.py task list --pending --show-lead
"""

import click
import requests
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional


# =============================================================================
# Configuration
# =============================================================================

BASE_URL = "https://api.close.com/api/v1"


def load_api_key() -> str:
    """Load API key from .env file in the script's directory."""
    env_path = Path(__file__).parent / ".env"
    if not env_path.exists():
        raise click.ClickException(
            f".env file not found at {env_path}\n"
            "Create a .env file with: CLOSE_API_KEY=your_api_key"
        )

    with open(env_path, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("CLOSE_API_KEY="):
                return line.split("=", 1)[1].strip()

    raise click.ClickException("CLOSE_API_KEY not found in .env file")


def get_api_key() -> str:
    """Get API key with caching."""
    if not hasattr(get_api_key, "_cached_key"):
        get_api_key._cached_key = load_api_key()
    return get_api_key._cached_key


# =============================================================================
# API Client
# =============================================================================

class CloseAPI:
    """Simple Close API client."""

    def __init__(self):
        self.api_key = get_api_key()
        self.base_url = BASE_URL

    def _request(self, method: str, endpoint: str, **kwargs) -> dict:
        """Make an authenticated request to the Close API."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.request(
            method,
            url,
            auth=(self.api_key, ""),
            **kwargs
        )

        if not response.ok:
            raise click.ClickException(
                f"API Error ({response.status_code}): {response.text}"
            )

        # DELETE returns 204 No Content
        if response.status_code == 204 or not response.content:
            return {}

        return response.json()

    def get(self, endpoint: str, **kwargs) -> dict:
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> dict:
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs) -> dict:
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> dict:
        return self._request("DELETE", endpoint, **kwargs)

    # -------------------------------------------------------------------------
    # Lead Operations
    # -------------------------------------------------------------------------

    def create_lead(
        self,
        name: str,
        url: Optional[str] = None,
        description: Optional[str] = None,
        status_id: Optional[str] = None,
        contacts: Optional[list] = None,
    ) -> dict:
        """Create a new lead, optionally with inline contacts.

        Args:
            name: Company/lead name.
            url: Website URL.
            description: Free-text description.
            status_id: Lead status ID (from `status list`).
            contacts: List of contact dicts, each with keys like
                      name, title, emails [{email, type}], phones [{phone, type}],
                      urls [{url, type}].
        """
        payload = {"name": name}
        if url:
            payload["url"] = url
        if description:
            payload["description"] = description
        if status_id:
            payload["status_id"] = status_id
        if contacts:
            payload["contacts"] = contacts
        return self.post("/lead/", json=payload)

    def search_leads(
        self,
        query: Optional[str] = None,
        name: Optional[str] = None,
        status_id: Optional[str] = None,
        limit: int = 10,
        sort: Optional[str] = None,
    ) -> dict:
        """Search for leads.

        Args:
            query: Raw Close search query string.
            name: Filter by lead name.
            status_id: Filter by status ID.
            limit: Max results to return.
            sort: Sort field, e.g. 'date_updated' or '-date_created'.
        """
        params = {"_limit": limit}

        queries = []
        if query:
            queries.append(query)
        if name:
            queries.append(f'name:"{name}"')
        if status_id:
            queries.append(f'status_id:"{status_id}"')

        if queries:
            params["query"] = " ".join(queries)
        if sort:
            params["_order_by"] = sort

        return self.get("/lead/", params=params)

    def get_lead(self, lead_id: str) -> dict:
        """Get a single lead by ID."""
        return self.get(f"/lead/{lead_id}/")

    def update_lead(
        self,
        lead_id: str,
        name: Optional[str] = None,
        url: Optional[str] = None,
        description: Optional[str] = None,
        status_id: Optional[str] = None,
    ) -> dict:
        """Update a lead's fields."""
        payload = {}
        if name is not None:
            payload["name"] = name
        if url is not None:
            payload["url"] = url
        if description is not None:
            payload["description"] = description
        if status_id is not None:
            payload["status_id"] = status_id
        return self.put(f"/lead/{lead_id}/", json=payload)

    def delete_lead(self, lead_id: str) -> dict:
        """Delete a lead and all its contacts, tasks, and activities."""
        return self.delete(f"/lead/{lead_id}/")

    # -------------------------------------------------------------------------
    # Contact Operations
    # -------------------------------------------------------------------------

    def create_contact(
        self,
        lead_id: str,
        name: str,
        title: Optional[str] = None,
        emails: Optional[list] = None,
        phones: Optional[list] = None,
        urls: Optional[list] = None,
    ) -> dict:
        """Create a contact under a lead.

        Args:
            lead_id: Parent lead ID.
            name: Contact full name.
            title: Job title.
            emails: List of email strings.
            phones: List of phone strings.
            urls: List of URL strings (e.g. LinkedIn).
        """
        payload = {"lead_id": lead_id, "name": name}
        if title:
            payload["title"] = title
        if emails:
            payload["emails"] = [{"email": e, "type": "office"} for e in emails]
        if phones:
            payload["phones"] = [{"phone": p, "type": "office"} for p in phones]
        if urls:
            payload["urls"] = [{"url": u, "type": "url"} for u in urls]
        return self.post("/contact/", json=payload)

    def list_contacts(self, lead_id: str) -> dict:
        """List all contacts for a lead."""
        return self.get("/contact/", params={"lead_id": lead_id})

    def get_contact(self, contact_id: str) -> dict:
        """Get a single contact by ID."""
        return self.get(f"/contact/{contact_id}/")

    def update_contact(
        self,
        contact_id: str,
        name: Optional[str] = None,
        title: Optional[str] = None,
    ) -> dict:
        """Update a contact's fields."""
        payload = {}
        if name is not None:
            payload["name"] = name
        if title is not None:
            payload["title"] = title
        return self.put(f"/contact/{contact_id}/", json=payload)

    def delete_contact(self, contact_id: str) -> dict:
        """Delete a contact."""
        return self.delete(f"/contact/{contact_id}/")

    # -------------------------------------------------------------------------
    # Task Operations
    # -------------------------------------------------------------------------

    def create_task(
        self,
        lead_id: str,
        text: str,
        due_date: Optional[str] = None,
        assigned_to: Optional[str] = None,
    ) -> dict:
        """Create a task for a lead."""
        if due_date is None:
            due_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

        payload = {
            "_type": "lead",
            "lead_id": lead_id,
            "text": text,
            "date": due_date,
        }

        if assigned_to:
            payload["assigned_to"] = assigned_to

        return self.post("/task/", json=payload)

    def list_tasks(self, lead_id: Optional[str] = None, is_complete: Optional[bool] = None) -> dict:
        """List tasks, optionally filtered by lead and completion status."""
        params = {}
        if lead_id:
            params["lead_id"] = lead_id
        if is_complete is not None:
            params["is_complete"] = str(is_complete).lower()
        return self.get("/task/", params=params)

    def update_task(
        self,
        task_id: str,
        text: Optional[str] = None,
        due_date: Optional[str] = None,
        is_complete: Optional[bool] = None,
        assigned_to: Optional[str] = None,
    ) -> dict:
        """Update a task."""
        payload = {}
        if text is not None:
            payload["text"] = text
        if due_date is not None:
            payload["date"] = due_date
        if is_complete is not None:
            payload["is_complete"] = is_complete
        if assigned_to is not None:
            payload["assigned_to"] = assigned_to
        return self.put(f"/task/{task_id}/", json=payload)

    def complete_task(self, task_id: str) -> dict:
        """Mark a task as complete."""
        return self.update_task(task_id, is_complete=True)

    def delete_task(self, task_id: str) -> dict:
        """Delete a task."""
        return self.delete(f"/task/{task_id}/")

    # -------------------------------------------------------------------------
    # Note / Activity Operations
    # -------------------------------------------------------------------------

    def create_note(self, lead_id: str, note_text: str) -> dict:
        """Create a note on a lead."""
        return self.post("/activity/note/", json={
            "lead_id": lead_id,
            "note": note_text,
        })

    def list_notes(self, lead_id: str, limit: int = 10) -> dict:
        """List notes for a lead."""
        return self.get("/activity/note/", params={
            "lead_id": lead_id,
            "_limit": limit,
        })

    # -------------------------------------------------------------------------
    # User / Organization Operations
    # -------------------------------------------------------------------------

    def get_me(self) -> dict:
        """Get current user info."""
        return self.get("/me/")

    def list_lead_statuses(self) -> dict:
        """List all lead statuses."""
        return self.get("/status/lead/")


# =============================================================================
# CLI Commands
# =============================================================================

@click.group()
@click.version_option(version="0.2.0", prog_name="close-cli")
@click.pass_context
def cli(ctx):
    """
    Close CRM CLI - Manage your Close CRM from the command line.

    Configure your API key in a .env file:

        CLOSE_API_KEY=api_xxxxx

    Run 'close-cli COMMAND --help' for more information on a command.
    """
    ctx.ensure_object(dict)
    ctx.obj["api"] = CloseAPI()


# =============================================================================
# Lead Commands
# =============================================================================

@cli.group()
def lead():
    """Manage leads in Close CRM."""
    pass


@lead.command("create")
@click.option("--name", "-n", required=True, help="Lead/company name")
@click.option("--url", "-u", default=None, help="Website URL")
@click.option("--description", "-d", default=None, help="Lead description")
@click.option("--status-id", "-s", default=None, help="Status ID (see `status list`)")
@click.pass_context
def lead_create(ctx, name: str, url: str, description: str, status_id: str):
    """Create a new lead."""
    api: CloseAPI = ctx.obj["api"]

    result = api.create_lead(
        name=name, url=url, description=description, status_id=status_id,
    )

    click.echo(click.style("Lead created!", fg="green"))
    click.echo(f"  ID:     {result.get('id')}")
    click.echo(f"  Name:   {result.get('display_name')}")
    click.echo(f"  Status: {result.get('status_label')}")
    if result.get("url"):
        click.echo(f"  URL:    {result.get('url')}")


@lead.command("list")
@click.option("--limit", "-l", default=10, help="Maximum number of leads to return")
@click.option("--status-id", "-s", default=None, help="Filter by status ID")
@click.option("--sort", default=None, help="Sort field (e.g. date_updated, -date_created)")
@click.pass_context
def lead_list(ctx, limit: int, status_id: str, sort: str):
    """List leads with optional filters."""
    api: CloseAPI = ctx.obj["api"]

    result = api.search_leads(limit=limit, status_id=status_id, sort=sort)
    leads = result.get("data", [])

    if not leads:
        click.echo("No leads found.")
        return

    click.echo(f"Found {len(leads)} lead(s):\n")
    for lead_data in leads:
        name = lead_data.get("display_name", "Unknown")
        lead_id = lead_data.get("id")
        status = lead_data.get("status_label", "Unknown")
        url = lead_data.get("url", "")

        click.echo(f"  {click.style(name, fg='cyan', bold=True)}")
        click.echo(f"    ID:     {lead_id}")
        click.echo(f"    Status: {status}")
        if url:
            click.echo(f"    URL:    {url}")
        click.echo()


@lead.command("search")
@click.option("--name", "-n", default=None, help="Search by lead name")
@click.option("--query", "-q", default=None, help="Raw Close search query")
@click.option("--status-id", "-s", default=None, help="Filter by status ID")
@click.option("--limit", "-l", default=10, help="Maximum number of results")
@click.pass_context
def lead_search(ctx, name: str, query: str, status_id: str, limit: int):
    """Search for leads by name, query, or status."""
    api: CloseAPI = ctx.obj["api"]

    if not any([name, query, status_id]):
        raise click.UsageError("Please provide at least one of --name, --query, or --status-id")

    result = api.search_leads(name=name, query=query, status_id=status_id, limit=limit)
    leads = result.get("data", [])

    if not leads:
        click.echo("No leads found matching your search.")
        return

    click.echo(f"Found {len(leads)} lead(s):\n")
    for lead_data in leads:
        click.echo(f"  {click.style(lead_data.get('display_name', 'Unknown'), fg='cyan', bold=True)}")
        click.echo(f"    ID:     {lead_data.get('id')}")
        click.echo(f"    Status: {lead_data.get('status_label', 'Unknown')}")
        if lead_data.get("url"):
            click.echo(f"    URL:    {lead_data.get('url')}")
        click.echo()


@lead.command("get")
@click.argument("lead_id")
@click.pass_context
def lead_get(ctx, lead_id: str):
    """Get details for a specific lead."""
    api: CloseAPI = ctx.obj["api"]

    lead_data = api.get_lead(lead_id)

    click.echo(click.style(lead_data.get("display_name", "Unknown"), fg="cyan", bold=True))
    click.echo(f"  ID:          {lead_data.get('id')}")
    click.echo(f"  Status:      {lead_data.get('status_label')}")
    click.echo(f"  URL:         {lead_data.get('url', 'N/A')}")
    click.echo(f"  Description: {lead_data.get('description', 'N/A')}")

    contacts = lead_data.get("contacts", [])
    if contacts:
        click.echo(f"\n  Contacts ({len(contacts)}):")
        for c in contacts:
            click.echo(f"    - {c.get('name', 'Unknown')}")
            if c.get("title"):
                click.echo(f"      Title: {c.get('title')}")
            click.echo(f"      ID:    {c.get('id')}")
            for email in c.get("emails", []):
                click.echo(f"      Email: {email.get('email')}")
            for phone in c.get("phones", []):
                click.echo(f"      Phone: {phone.get('phone')}")
            for url in c.get("urls", []):
                click.echo(f"      URL:   {url.get('url')}")


@lead.command("update")
@click.argument("lead_id")
@click.option("--name", "-n", default=None, help="New lead name")
@click.option("--url", "-u", default=None, help="New website URL")
@click.option("--description", "-d", default=None, help="New description")
@click.option("--status-id", "-s", default=None, help="New status ID")
@click.pass_context
def lead_update(ctx, lead_id: str, name: str, url: str, description: str, status_id: str):
    """Update a lead's fields."""
    api: CloseAPI = ctx.obj["api"]

    if not any([name, url, description, status_id]):
        raise click.UsageError("Please provide at least one field to update (--name, --url, --description, or --status-id)")

    result = api.update_lead(
        lead_id=lead_id, name=name, url=url, description=description, status_id=status_id,
    )

    click.echo(click.style("Lead updated!", fg="green"))
    click.echo(f"  ID:     {result.get('id')}")
    click.echo(f"  Name:   {result.get('display_name')}")
    click.echo(f"  Status: {result.get('status_label')}")
    if result.get("url"):
        click.echo(f"  URL:    {result.get('url')}")


@lead.command("delete")
@click.argument("lead_id")
@click.option("--yes", "-y", is_flag=True, default=False, help="Skip confirmation prompt")
@click.pass_context
def lead_delete(ctx, lead_id: str, yes: bool):
    """Delete a lead and all its associated data."""
    api: CloseAPI = ctx.obj["api"]

    if not yes:
        # Fetch lead name for confirmation
        try:
            lead_data = api.get_lead(lead_id)
            lead_name = lead_data.get("display_name", lead_id)
        except Exception:
            lead_name = lead_id
        if not click.confirm(f"Delete lead '{lead_name}' ({lead_id})? This cannot be undone"):
            click.echo("Cancelled.")
            return

    api.delete_lead(lead_id)
    click.echo(click.style(f"Lead {lead_id} deleted.", fg="green"))


# =============================================================================
# Contact Commands
# =============================================================================

@cli.group()
def contact():
    """Manage contacts in Close CRM."""
    pass


@contact.command("create")
@click.argument("lead_id")
@click.option("--name", "-n", required=True, help="Contact full name")
@click.option("--title", "-t", default=None, help="Job title")
@click.option("--email", "-e", multiple=True, help="Email address (repeatable)")
@click.option("--phone", "-p", multiple=True, help="Phone number (repeatable)")
@click.option("--url", "-u", multiple=True, help="URL, e.g. LinkedIn (repeatable)")
@click.pass_context
def contact_create(ctx, lead_id: str, name: str, title: str, email: tuple, phone: tuple, url: tuple):
    """Add a contact to a lead."""
    api: CloseAPI = ctx.obj["api"]

    result = api.create_contact(
        lead_id=lead_id,
        name=name,
        title=title,
        emails=list(email) if email else None,
        phones=list(phone) if phone else None,
        urls=list(url) if url else None,
    )

    click.echo(click.style("Contact created!", fg="green"))
    click.echo(f"  ID:      {result.get('id')}")
    click.echo(f"  Name:    {result.get('name')}")
    click.echo(f"  Lead ID: {result.get('lead_id')}")
    if result.get("title"):
        click.echo(f"  Title:   {result.get('title')}")
    for e in result.get("emails", []):
        click.echo(f"  Email:   {e.get('email')}")
    for p in result.get("phones", []):
        click.echo(f"  Phone:   {p.get('phone')}")
    for u in result.get("urls", []):
        click.echo(f"  URL:     {u.get('url')}")


@contact.command("list")
@click.argument("lead_id")
@click.pass_context
def contact_list(ctx, lead_id: str):
    """List all contacts for a lead."""
    api: CloseAPI = ctx.obj["api"]

    result = api.list_contacts(lead_id)
    contacts = result.get("data", [])

    if not contacts:
        click.echo("No contacts found for this lead.")
        return

    click.echo(f"Found {len(contacts)} contact(s):\n")
    for c in contacts:
        click.echo(f"  {click.style(c.get('name', 'Unknown'), fg='cyan', bold=True)}")
        click.echo(f"    ID:    {c.get('id')}")
        if c.get("title"):
            click.echo(f"    Title: {c.get('title')}")
        for e in c.get("emails", []):
            click.echo(f"    Email: {e.get('email')}")
        for p in c.get("phones", []):
            click.echo(f"    Phone: {p.get('phone')}")
        for u in c.get("urls", []):
            click.echo(f"    URL:   {u.get('url')}")
        click.echo()


@contact.command("get")
@click.argument("contact_id")
@click.pass_context
def contact_get(ctx, contact_id: str):
    """Get details for a specific contact."""
    api: CloseAPI = ctx.obj["api"]

    c = api.get_contact(contact_id)

    click.echo(click.style(c.get("name", "Unknown"), fg="cyan", bold=True))
    click.echo(f"  ID:      {c.get('id')}")
    click.echo(f"  Lead ID: {c.get('lead_id')}")
    if c.get("title"):
        click.echo(f"  Title:   {c.get('title')}")
    for e in c.get("emails", []):
        click.echo(f"  Email:   {e.get('email')}")
    for p in c.get("phones", []):
        click.echo(f"  Phone:   {p.get('phone')}")
    for u in c.get("urls", []):
        click.echo(f"  URL:     {u.get('url')}")


@contact.command("update")
@click.argument("contact_id")
@click.option("--name", "-n", default=None, help="New contact name")
@click.option("--title", "-t", default=None, help="New job title")
@click.pass_context
def contact_update(ctx, contact_id: str, name: str, title: str):
    """Update a contact's fields."""
    api: CloseAPI = ctx.obj["api"]

    if not any([name, title]):
        raise click.UsageError("Please provide at least one field to update (--name or --title)")

    result = api.update_contact(contact_id=contact_id, name=name, title=title)

    click.echo(click.style("Contact updated!", fg="green"))
    click.echo(f"  ID:    {result.get('id')}")
    click.echo(f"  Name:  {result.get('name')}")
    if result.get("title"):
        click.echo(f"  Title: {result.get('title')}")


@contact.command("delete")
@click.argument("contact_id")
@click.option("--yes", "-y", is_flag=True, default=False, help="Skip confirmation prompt")
@click.pass_context
def contact_delete(ctx, contact_id: str, yes: bool):
    """Delete a contact."""
    api: CloseAPI = ctx.obj["api"]

    if not yes:
        try:
            contact_data = api.get_contact(contact_id)
            contact_name = contact_data.get("name", contact_id)
        except Exception:
            contact_name = contact_id
        if not click.confirm(f"Delete contact '{contact_name}' ({contact_id})? This cannot be undone"):
            click.echo("Cancelled.")
            return

    api.delete_contact(contact_id)
    click.echo(click.style(f"Contact {contact_id} deleted.", fg="green"))


# =============================================================================
# Task Commands
# =============================================================================

@cli.group()
def task():
    """Manage tasks in Close CRM."""
    pass


@task.command("create")
@click.option(
    "--lead-id", "-l",
    required=True,
    help="Lead ID to create the task for (e.g., lead_xxx)"
)
@click.option(
    "--text", "-t",
    required=True,
    help="Task description text"
)
@click.option(
    "--due-date", "-d",
    default=None,
    help="Due date in YYYY-MM-DD format (defaults to tomorrow)"
)
@click.option(
    "--assigned-to", "-a",
    default=None,
    help="User ID to assign the task to (defaults to you)"
)
@click.pass_context
def task_create(ctx, lead_id: str, text: str, due_date: str, assigned_to: str):
    """Create a new task for a lead."""
    api: CloseAPI = ctx.obj["api"]

    result = api.create_task(
        lead_id=lead_id,
        text=text,
        due_date=due_date,
        assigned_to=assigned_to,
    )

    click.echo(click.style("Task created!", fg="green"))
    click.echo(f"  Task ID:  {result.get('id')}")
    click.echo(f"  Lead ID:  {result.get('lead_id')}")
    click.echo(f"  Text:     {result.get('text')}")
    click.echo(f"  Due Date: {result.get('date')}")


@task.command("list")
@click.option("--lead-id", "-l", default=None, help="Filter tasks by lead ID")
@click.option("--pending", "-p", is_flag=True, default=False, help="Show only pending (incomplete) tasks")
@click.option("--show-lead", "-s", is_flag=True, default=False, help="Show lead name for each task")
@click.pass_context
def task_list(ctx, lead_id: str, pending: bool, show_lead: bool):
    """List tasks."""
    api: CloseAPI = ctx.obj["api"]

    is_complete = False if pending else None
    result = api.list_tasks(lead_id=lead_id, is_complete=is_complete)
    tasks = result.get("data", [])

    if not tasks:
        click.echo("No tasks found.")
        return

    # Cache for lead names to avoid duplicate API calls
    lead_cache = {}

    click.echo(f"Found {len(tasks)} task(s):\n")
    for t in tasks:
        status = "Done" if t.get("is_complete") else "Pending"
        status_color = "green" if t.get("is_complete") else "yellow"
        click.echo(f"  [{click.style(status, fg=status_color)}] {t.get('text')}")
        click.echo(f"    ID: {t.get('id')}")
        click.echo(f"    Due: {t.get('date')}")

        if show_lead and t.get("lead_id"):
            task_lead_id = t.get("lead_id")
            if task_lead_id not in lead_cache:
                try:
                    lead_data = api.get_lead(task_lead_id)
                    lead_cache[task_lead_id] = lead_data.get("display_name", "Unknown")
                except Exception:
                    lead_cache[task_lead_id] = "Unknown"
            click.echo(f"    Lead: {lead_cache[task_lead_id]}")

        click.echo()


@task.command("update")
@click.argument("task_id")
@click.option("--text", "-t", default=None, help="New task description text")
@click.option("--due-date", "-d", default=None, help="New due date in YYYY-MM-DD format")
@click.option("--assigned-to", "-a", default=None, help="User ID to reassign the task to")
@click.pass_context
def task_update(ctx, task_id: str, text: str, due_date: str, assigned_to: str):
    """Update a task's details."""
    api: CloseAPI = ctx.obj["api"]

    if not any([text, due_date, assigned_to]):
        raise click.UsageError("Please provide at least one field to update (--text, --due-date, or --assigned-to)")

    result = api.update_task(
        task_id=task_id,
        text=text,
        due_date=due_date,
        assigned_to=assigned_to,
    )

    click.echo(click.style("Task updated!", fg="green"))
    click.echo(f"  Task ID:  {result.get('id')}")
    click.echo(f"  Text:     {result.get('text')}")
    click.echo(f"  Due Date: {result.get('date')}")


@task.command("complete")
@click.argument("task_id")
@click.pass_context
def task_complete(ctx, task_id: str):
    """Mark a task as complete."""
    api: CloseAPI = ctx.obj["api"]

    result = api.complete_task(task_id)

    click.echo(click.style("Task marked as complete!", fg="green"))
    click.echo(f"  Task ID: {result.get('id')}")
    click.echo(f"  Text:    {result.get('text')}")


@task.command("delete")
@click.argument("task_id")
@click.option("--yes", "-y", is_flag=True, default=False, help="Skip confirmation prompt")
@click.pass_context
def task_delete(ctx, task_id: str, yes: bool):
    """Delete a task."""
    api: CloseAPI = ctx.obj["api"]

    if not yes:
        if not click.confirm(f"Delete task {task_id}? This cannot be undone"):
            click.echo("Cancelled.")
            return

    api.delete_task(task_id)
    click.echo(click.style(f"Task {task_id} deleted.", fg="green"))


# =============================================================================
# Note Commands
# =============================================================================

@cli.group()
def note():
    """Manage notes on leads in Close CRM."""
    pass


@note.command("create")
@click.argument("lead_id")
@click.option("--text", "-t", required=True, help="Note text")
@click.pass_context
def note_create(ctx, lead_id: str, text: str):
    """Add a note to a lead."""
    api: CloseAPI = ctx.obj["api"]

    result = api.create_note(lead_id=lead_id, note_text=text)

    click.echo(click.style("Note created!", fg="green"))
    click.echo(f"  ID:      {result.get('id')}")
    click.echo(f"  Lead ID: {result.get('lead_id')}")
    note_html = result.get("note_html", result.get("note", ""))
    # Strip basic HTML for display
    import re
    note_plain = re.sub(r"<[^>]+>", "", note_html) if note_html else ""
    click.echo(f"  Note:    {note_plain[:120]}")


@note.command("list")
@click.argument("lead_id")
@click.option("--limit", "-l", default=10, help="Maximum number of notes to return")
@click.pass_context
def note_list(ctx, lead_id: str, limit: int):
    """List notes for a lead."""
    api: CloseAPI = ctx.obj["api"]

    result = api.list_notes(lead_id=lead_id, limit=limit)
    notes = result.get("data", [])

    if not notes:
        click.echo("No notes found for this lead.")
        return

    import re

    click.echo(f"Found {len(notes)} note(s):\n")
    for n in notes:
        created = n.get("date_created", "Unknown")[:10]
        note_html = n.get("note_html", n.get("note", ""))
        note_plain = re.sub(r"<[^>]+>", "", note_html) if note_html else ""
        preview = note_plain[:100] + ("..." if len(note_plain) > 100 else "")

        click.echo(f"  {click.style(created, fg='cyan')}  {preview}")
        click.echo(f"    ID: {n.get('id')}")
        click.echo()


# =============================================================================
# Status Commands
# =============================================================================

@cli.group()
def status():
    """View lead statuses."""
    pass


@status.command("list")
@click.pass_context
def status_list(ctx):
    """List all lead statuses."""
    api: CloseAPI = ctx.obj["api"]

    result = api.list_lead_statuses()
    statuses = result.get("data", [])

    click.echo("Lead Statuses:\n")
    for s in statuses:
        click.echo(f"  {click.style(s.get('label'), fg='cyan')}")
        click.echo(f"    ID: {s.get('id')}")
        click.echo()


# =============================================================================
# Utility Commands
# =============================================================================

@cli.command("whoami")
@click.pass_context
def whoami(ctx):
    """Show current user information."""
    api: CloseAPI = ctx.obj["api"]

    user = api.get_me()

    click.echo(click.style("Current User:", fg="green", bold=True))
    click.echo(f"  Name:  {user.get('first_name')} {user.get('last_name')}")
    click.echo(f"  Email: {user.get('email')}")
    click.echo(f"  ID:    {user.get('id')}")


# =============================================================================
# Entry Point
# =============================================================================

if __name__ == "__main__":
    cli()
