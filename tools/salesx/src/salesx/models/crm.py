"""CRM canonical models (Close leads, contacts, tasks, notes, statuses, user).

These deliberately hide Close's quirks (`display_name`, `note_html`, the `date`
field on tasks) behind stable names, so the rest of salesx — and agents — never
has to know Close's wire format.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .base import Model


@dataclass
class Contact(Model):
    """A CRM contact (a person reachable on a lead)."""

    id: Optional[str] = None
    lead_id: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    emails: list[str] = field(default_factory=list)
    phones: list[str] = field(default_factory=list)
    urls: list[str] = field(default_factory=list)


@dataclass
class Lead(Model):
    """A CRM lead (the company-level record in Close)."""

    id: Optional[str] = None
    name: Optional[str] = None
    url: Optional[str] = None
    description: Optional[str] = None
    status_id: Optional[str] = None
    status_label: Optional[str] = None
    contacts: list[Contact] = field(default_factory=list)


@dataclass
class Task(Model):
    id: Optional[str] = None
    lead_id: Optional[str] = None
    text: Optional[str] = None
    due_date: Optional[str] = None
    is_complete: Optional[bool] = None
    assigned_to: Optional[str] = None


@dataclass
class Note(Model):
    id: Optional[str] = None
    lead_id: Optional[str] = None
    text: Optional[str] = None             # HTML stripped to plain text
    created_at: Optional[str] = None


@dataclass
class LeadStatus(Model):
    id: Optional[str] = None
    label: Optional[str] = None


@dataclass
class User(Model):
    id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
