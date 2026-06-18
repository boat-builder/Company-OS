"""`salesx crm ...` — Close CRM: leads, contacts, tasks, notes, statuses, user."""

from __future__ import annotations

import click

from ..output import emit
from ._shared import output_options, pass_app


@click.group()
def crm() -> None:
    """Close CRM: leads, contacts, tasks, notes, statuses."""


# --- Leads ------------------------------------------------------------------

@crm.group()
def lead() -> None:
    """Manage leads. Output: Lead — id, name, url, description, status_id,
    status_label, contacts[] (Contact)."""


@lead.command("create")
@click.option("--name", "-n", required=True, help="Lead/company name.")
@click.option("--url", "-u", help="Website URL.")
@click.option("--description", "-d", help="Lead description.")
@click.option("--status-id", "-s", help="Status ID (see `crm status list`).")
@output_options
@pass_app
def lead_create(app, name, url, description, status_id, fmt, raw, output):
    """Create a new lead. Output: Lead."""
    kw = dict(name=name, url=url, description=description, status_id=status_id)
    data = app.sx.close.create_lead(**kw) if raw else app.sx.crm.create_lead(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="Lead")


@lead.command("list")
@click.option("--limit", "-l", default=10, help="Max leads to return.")
@click.option("--status-id", "-s", help="Filter by status ID.")
@click.option("--sort", help="Sort field, e.g. date_updated or -date_created.")
@output_options
@pass_app
def lead_list(app, limit, status_id, sort, fmt, raw, output):
    """List leads. Output: Lead[]."""
    kw = dict(limit=limit, status_id=status_id, sort=sort)
    data = app.sx.close.search_leads(**kw) if raw else app.sx.crm.search_leads(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="Leads")


@lead.command("search")
@click.option("--name", "-n", help="Search by lead name.")
@click.option("--query", "-q", help="Raw Close search query.")
@click.option("--status-id", "-s", help="Filter by status ID.")
@click.option("--limit", "-l", default=10, help="Max results.")
@output_options
@pass_app
def lead_search(app, name, query, status_id, limit, fmt, raw, output):
    """Search leads by name, query, or status. Output: Lead[]."""
    if not any([name, query, status_id]):
        raise click.UsageError("Provide at least one of --name, --query, or --status-id.")
    kw = dict(name=name, query=query, status_id=status_id, limit=limit)
    data = app.sx.close.search_leads(**kw) if raw else app.sx.crm.search_leads(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="Leads")


@lead.command("get")
@click.argument("lead_id")
@output_options
@pass_app
def lead_get(app, lead_id, fmt, raw, output):
    """Get a lead (includes contacts). Output: Lead."""
    data = app.sx.close.get_lead(lead_id) if raw else app.sx.crm.get_lead(lead_id)
    emit(data, fmt=fmt, raw=raw, output=output, title="Lead")


@lead.command("update")
@click.argument("lead_id")
@click.option("--name", "-n", help="New lead name.")
@click.option("--url", "-u", help="New website URL.")
@click.option("--description", "-d", help="New description.")
@click.option("--status-id", "-s", help="New status ID.")
@output_options
@pass_app
def lead_update(app, lead_id, name, url, description, status_id, fmt, raw, output):
    """Update a lead's fields. Output: Lead."""
    if not any([name, url, description, status_id]):
        raise click.UsageError("Provide at least one field to update.")
    kw = dict(name=name, url=url, description=description, status_id=status_id)
    data = app.sx.close.update_lead(lead_id, **kw) if raw else app.sx.crm.update_lead(lead_id, **kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="Lead")


@lead.command("delete")
@click.argument("lead_id")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation.")
@pass_app
def lead_delete(app, lead_id, yes):
    """Delete a lead and all its associated data."""
    if not yes:
        try:
            name = app.sx.crm.get_lead(lead_id).name or lead_id
        except Exception:
            name = lead_id
        if not click.confirm(f"Delete lead '{name}' ({lead_id})? This cannot be undone"):
            click.echo("Cancelled.")
            return
    app.sx.crm.delete_lead(lead_id)
    click.echo(click.style(f"Lead {lead_id} deleted.", fg="green"))


# --- Contacts ---------------------------------------------------------------

@crm.group()
def contact() -> None:
    """Manage contacts. Output: Contact — id, lead_id, name, title, emails[],
    phones[], urls[]."""


@contact.command("create")
@click.argument("lead_id")
@click.option("--name", "-n", required=True, help="Contact full name.")
@click.option("--title", "-t", help="Job title.")
@click.option("--email", "-e", multiple=True, help="Email (repeatable).")
@click.option("--phone", "-p", multiple=True, help="Phone (repeatable).")
@click.option("--url", "-u", multiple=True, help="URL, e.g. LinkedIn (repeatable).")
@output_options
@pass_app
def contact_create(app, lead_id, name, title, email, phone, url, fmt, raw, output):
    """Add a contact to a lead. Output: Contact."""
    kw = dict(lead_id=lead_id, name=name, title=title,
              emails=list(email) or None, phones=list(phone) or None, urls=list(url) or None)
    data = app.sx.close.create_contact(**kw) if raw else app.sx.crm.create_contact(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="Contact")


@contact.command("list")
@click.argument("lead_id")
@output_options
@pass_app
def contact_list(app, lead_id, fmt, raw, output):
    """List contacts for a lead. Output: Contact[]."""
    data = app.sx.close.list_contacts(lead_id) if raw else app.sx.crm.list_contacts(lead_id)
    emit(data, fmt=fmt, raw=raw, output=output, title="Contacts")


@contact.command("get")
@click.argument("contact_id")
@output_options
@pass_app
def contact_get(app, contact_id, fmt, raw, output):
    """Get a contact. Output: Contact."""
    data = app.sx.close.get_contact(contact_id) if raw else app.sx.crm.get_contact(contact_id)
    emit(data, fmt=fmt, raw=raw, output=output, title="Contact")


@contact.command("update")
@click.argument("contact_id")
@click.option("--name", "-n", help="New name.")
@click.option("--title", "-t", help="New title.")
@output_options
@pass_app
def contact_update(app, contact_id, name, title, fmt, raw, output):
    """Update a contact. Output: Contact."""
    if not any([name, title]):
        raise click.UsageError("Provide --name or --title.")
    kw = dict(name=name, title=title)
    data = app.sx.close.update_contact(contact_id, **kw) if raw else app.sx.crm.update_contact(contact_id, **kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="Contact")


@contact.command("delete")
@click.argument("contact_id")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation.")
@pass_app
def contact_delete(app, contact_id, yes):
    """Delete a contact."""
    if not yes and not click.confirm(f"Delete contact {contact_id}? This cannot be undone"):
        click.echo("Cancelled.")
        return
    app.sx.crm.delete_contact(contact_id)
    click.echo(click.style(f"Contact {contact_id} deleted.", fg="green"))


# --- Tasks ------------------------------------------------------------------

@crm.group()
def task() -> None:
    """Manage tasks. Output: Task — id, lead_id, text, due_date, is_complete,
    assigned_to."""


@task.command("create")
@click.option("--lead-id", "-l", required=True, help="Lead ID.")
@click.option("--text", "-t", required=True, help="Task text.")
@click.option("--due-date", "-d", help="Due date YYYY-MM-DD (defaults to tomorrow).")
@click.option("--assigned-to", "-a", help="User ID to assign to (defaults to you).")
@output_options
@pass_app
def task_create(app, lead_id, text, due_date, assigned_to, fmt, raw, output):
    """Create a task for a lead. Output: Task."""
    kw = dict(lead_id=lead_id, text=text, due_date=due_date, assigned_to=assigned_to)
    data = app.sx.close.create_task(**kw) if raw else app.sx.crm.create_task(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="Task")


@task.command("list")
@click.option("--lead-id", "-l", help="Filter by lead ID.")
@click.option("--pending", "-p", is_flag=True, help="Only pending (incomplete) tasks.")
@output_options
@pass_app
def task_list(app, lead_id, pending, fmt, raw, output):
    """List tasks. Output: Task[]."""
    kw = dict(lead_id=lead_id, is_complete=False if pending else None)
    data = app.sx.close.list_tasks(**kw) if raw else app.sx.crm.list_tasks(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="Tasks")


@task.command("update")
@click.argument("task_id")
@click.option("--text", "-t", help="New text.")
@click.option("--due-date", "-d", help="New due date YYYY-MM-DD.")
@click.option("--assigned-to", "-a", help="Reassign to user ID.")
@output_options
@pass_app
def task_update(app, task_id, text, due_date, assigned_to, fmt, raw, output):
    """Update a task. Output: Task."""
    if not any([text, due_date, assigned_to]):
        raise click.UsageError("Provide at least one field to update.")
    kw = dict(text=text, due_date=due_date, assigned_to=assigned_to)
    data = app.sx.close.update_task(task_id, **kw) if raw else app.sx.crm.update_task(task_id, **kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="Task")


@task.command("complete")
@click.argument("task_id")
@output_options
@pass_app
def task_complete(app, task_id, fmt, raw, output):
    """Mark a task complete. Output: Task."""
    data = app.sx.close.complete_task(task_id) if raw else app.sx.crm.complete_task(task_id)
    emit(data, fmt=fmt, raw=raw, output=output, title="Task")


@task.command("delete")
@click.argument("task_id")
@click.option("--yes", "-y", is_flag=True, help="Skip confirmation.")
@pass_app
def task_delete(app, task_id, yes):
    """Delete a task."""
    if not yes and not click.confirm(f"Delete task {task_id}? This cannot be undone"):
        click.echo("Cancelled.")
        return
    app.sx.crm.delete_task(task_id)
    click.echo(click.style(f"Task {task_id} deleted.", fg="green"))


# --- Notes ------------------------------------------------------------------

@crm.group()
def note() -> None:
    """Manage notes on leads. Output: Note — id, lead_id, text, created_at."""


@note.command("create")
@click.argument("lead_id")
@click.option("--text", "-t", required=True, help="Note text.")
@output_options
@pass_app
def note_create(app, lead_id, text, fmt, raw, output):
    """Add a note to a lead. Output: Note."""
    if raw:
        emit(app.sx.close.create_note(lead_id=lead_id, note_text=text), fmt=fmt, raw=raw, output=output)
    else:
        emit(app.sx.crm.create_note(lead_id=lead_id, note_text=text), fmt=fmt, output=output, title="Note")


@note.command("list")
@click.argument("lead_id")
@click.option("--limit", "-l", default=10, help="Max notes to return.")
@output_options
@pass_app
def note_list(app, lead_id, limit, fmt, raw, output):
    """List notes for a lead. Output: Note[]."""
    data = app.sx.close.list_notes(lead_id, limit=limit) if raw else app.sx.crm.list_notes(lead_id, limit=limit)
    emit(data, fmt=fmt, raw=raw, output=output, title="Notes")


# --- Meta -------------------------------------------------------------------

@crm.group()
def status() -> None:
    """Lead statuses. Output: LeadStatus — id, label."""


@status.command("list")
@output_options
@pass_app
def status_list(app, fmt, raw, output):
    """List all lead statuses (with IDs for filtering). Output: LeadStatus[]."""
    data = app.sx.close.list_lead_statuses() if raw else app.sx.crm.list_statuses()
    emit(data, fmt=fmt, raw=raw, output=output, title="Lead statuses")


@crm.command("whoami")
@output_options
@pass_app
def whoami(app, fmt, raw, output):
    """Show the current authenticated Close user. Output: User — id, name, email."""
    data = app.sx.close.get_me() if raw else app.sx.crm.whoami()
    emit(data, fmt=fmt, raw=raw, output=output, title="User")
