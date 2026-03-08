#!/usr/bin/env python3
"""
Close CRM CLI - A command-line interface for interacting with Close CRM.

Usage:
    python close_cli.py [COMMAND] [OPTIONS]

Commands:
    task create   - Create a new task for a lead
    task list     - List tasks (use --pending for incomplete only, --show-lead for lead names)
    task update   - Update a task's due date, text, or assignee
    task complete - Mark a task as complete
    lead list     - List all leads
    lead search   - Search leads by name or query
    lead get      - Get details for a specific lead
    status list   - List all lead statuses
    whoami        - Show current user information

Examples:
    python close_cli.py task create --lead-id lead_xxx --text "Follow up"
    python close_cli.py task list --pending --show-lead
    python close_cli.py task update task_xxx --due-date 2026-01-20
    python close_cli.py task complete task_xxx
    python close_cli.py lead search --name "Acme"
    python close_cli.py lead list
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

        return response.json()

    def get(self, endpoint: str, **kwargs) -> dict:
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs) -> dict:
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs) -> dict:
        return self._request("PUT", endpoint, **kwargs)

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

    # -------------------------------------------------------------------------
    # Lead Operations
    # -------------------------------------------------------------------------

    def search_leads(
        self,
        query: Optional[str] = None,
        name: Optional[str] = None,
        status_id: Optional[str] = None,
        limit: int = 10,
    ) -> dict:
        """Search for leads."""
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

        return self.get("/lead/", params=params)

    def get_lead(self, lead_id: str) -> dict:
        """Get a single lead by ID."""
        return self.get(f"/lead/{lead_id}/")

    # -------------------------------------------------------------------------
    # User/Organization Operations
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
@click.version_option(version="0.1.0", prog_name="close-cli")
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


# -----------------------------------------------------------------------------
# Task Commands
# -----------------------------------------------------------------------------

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

    click.echo(click.style("Task created successfully!", fg="green"))
    click.echo(f"  Task ID:  {result.get('id')}")
    click.echo(f"  Lead ID:  {result.get('lead_id')}")
    click.echo(f"  Text:     {result.get('text')}")
    click.echo(f"  Due Date: {result.get('date')}")


@task.command("list")
@click.option(
    "--lead-id", "-l",
    default=None,
    help="Filter tasks by lead ID"
)
@click.option(
    "--pending", "-p",
    is_flag=True,
    default=False,
    help="Show only pending (incomplete) tasks"
)
@click.option(
    "--show-lead", "-s",
    is_flag=True,
    default=False,
    help="Show lead name for each task"
)
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
@click.option(
    "--text", "-t",
    default=None,
    help="New task description text"
)
@click.option(
    "--due-date", "-d",
    default=None,
    help="New due date in YYYY-MM-DD format"
)
@click.option(
    "--assigned-to", "-a",
    default=None,
    help="User ID to reassign the task to"
)
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

    click.echo(click.style("Task updated successfully!", fg="green"))
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


# -----------------------------------------------------------------------------
# Lead Commands
# -----------------------------------------------------------------------------

@cli.group()
def lead():
    """Manage leads in Close CRM."""
    pass


@lead.command("list")
@click.option(
    "--limit", "-n",
    default=10,
    help="Maximum number of leads to return"
)
@click.pass_context
def lead_list(ctx, limit: int):
    """List all leads."""
    api: CloseAPI = ctx.obj["api"]

    result = api.search_leads(limit=limit)
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
@click.option(
    "--name", "-n",
    default=None,
    help="Search by lead name"
)
@click.option(
    "--query", "-q",
    default=None,
    help="Raw search query"
)
@click.option(
    "--limit", "-l",
    default=10,
    help="Maximum number of results"
)
@click.pass_context
def lead_search(ctx, name: str, query: str, limit: int):
    """Search for leads."""
    api: CloseAPI = ctx.obj["api"]

    if not name and not query:
        raise click.UsageError("Please provide --name or --query")

    result = api.search_leads(name=name, query=query, limit=limit)
    leads = result.get("data", [])

    if not leads:
        click.echo("No leads found matching your search.")
        return

    click.echo(f"Found {len(leads)} lead(s):\n")
    for lead_data in leads:
        name = lead_data.get("display_name", "Unknown")
        lead_id = lead_data.get("id")
        status = lead_data.get("status_label", "Unknown")

        click.echo(f"  {click.style(name, fg='cyan', bold=True)}")
        click.echo(f"    ID:     {lead_id}")
        click.echo(f"    Status: {status}")
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
            for email in c.get("emails", []):
                click.echo(f"      Email: {email.get('email')}")
            for phone in c.get("phones", []):
                click.echo(f"      Phone: {phone.get('phone')}")


# -----------------------------------------------------------------------------
# Status Commands
# -----------------------------------------------------------------------------

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


# -----------------------------------------------------------------------------
# Utility Commands
# -----------------------------------------------------------------------------

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
