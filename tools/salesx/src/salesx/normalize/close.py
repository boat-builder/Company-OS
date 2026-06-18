"""Normalize Close CRM responses into canonical CRM models."""

from __future__ import annotations

from typing import Any

from ..models import Contact, Lead, LeadStatus, Note, Task, User
from .helpers import as_list, pick, strip_html


def _data(resp: Any) -> list:
    """Close list endpoints wrap results in {data: [...]}; accept a bare list too."""
    if isinstance(resp, list):
        return resp
    if isinstance(resp, dict):
        return as_list(resp.get("data"))
    return []


def contact(rec: Any) -> Contact:
    d = rec if isinstance(rec, dict) else {}
    return Contact(
        id=pick(d, "id"),
        lead_id=pick(d, "lead_id"),
        name=pick(d, "name"),
        title=pick(d, "title"),
        emails=[e.get("email") for e in as_list(d.get("emails")) if isinstance(e, dict) and e.get("email")],
        phones=[p.get("phone") for p in as_list(d.get("phones")) if isinstance(p, dict) and p.get("phone")],
        urls=[u.get("url") for u in as_list(d.get("urls")) if isinstance(u, dict) and u.get("url")],
    )


def lead(rec: Any) -> Lead:
    d = rec if isinstance(rec, dict) else {}
    return Lead(
        id=pick(d, "id"),
        name=pick(d, "display_name", "name"),
        url=pick(d, "url"),
        description=pick(d, "description"),
        status_id=pick(d, "status_id"),
        status_label=pick(d, "status_label"),
        contacts=[contact(c) for c in as_list(d.get("contacts"))],
    )


def leads(resp: Any) -> list[Lead]:
    return [lead(r) for r in _data(resp)]


def contacts(resp: Any) -> list[Contact]:
    return [contact(r) for r in _data(resp)]


def task(rec: Any) -> Task:
    d = rec if isinstance(rec, dict) else {}
    return Task(
        id=pick(d, "id"),
        lead_id=pick(d, "lead_id"),
        text=pick(d, "text"),
        due_date=pick(d, "date", "due_date"),
        is_complete=d.get("is_complete"),
        assigned_to=pick(d, "assigned_to"),
    )


def tasks(resp: Any) -> list[Task]:
    return [task(r) for r in _data(resp)]


def note(rec: Any) -> Note:
    d = rec if isinstance(rec, dict) else {}
    return Note(
        id=pick(d, "id"),
        lead_id=pick(d, "lead_id"),
        text=strip_html(pick(d, "note_html", "note")),
        created_at=pick(d, "date_created"),
    )


def notes(resp: Any) -> list[Note]:
    return [note(r) for r in _data(resp)]


def status(rec: Any) -> LeadStatus:
    d = rec if isinstance(rec, dict) else {}
    return LeadStatus(id=pick(d, "id"), label=pick(d, "label"))


def statuses(resp: Any) -> list[LeadStatus]:
    return [status(r) for r in _data(resp)]


def user(resp: Any) -> User:
    d = resp if isinstance(resp, dict) else {}
    name = " ".join(p for p in [d.get("first_name"), d.get("last_name")] if p) or None
    return User(id=pick(d, "id"), name=name, email=pick(d, "email"))
