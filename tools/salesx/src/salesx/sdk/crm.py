"""Typed Close CRM client — returns canonical models.

Flat method names (`create_lead`, `list_contacts`, …) keep the SDK and the CLI in
lock-step. Mutations return the affected model; deletes return None.
"""

from __future__ import annotations

from typing import Optional

from ..models import Contact, Lead, LeadStatus, Note, Task, User
from ..normalize import close as nc
from ..providers import CloseClient


class CrmClient:
    def __init__(self, close: CloseClient) -> None:
        self._c = close

    # Leads
    def create_lead(self, *, name, url=None, description=None, status_id=None, contacts=None) -> Lead:
        return nc.lead(self._c.create_lead(
            name=name, url=url, description=description, status_id=status_id, contacts=contacts))

    def search_leads(self, *, query=None, name=None, status_id=None, limit=10, sort=None) -> list[Lead]:
        return nc.leads(self._c.search_leads(
            query=query, name=name, status_id=status_id, limit=limit, sort=sort))

    def get_lead(self, lead_id: str) -> Lead:
        return nc.lead(self._c.get_lead(lead_id))

    def update_lead(self, lead_id: str, *, name=None, url=None, description=None, status_id=None) -> Lead:
        return nc.lead(self._c.update_lead(
            lead_id, name=name, url=url, description=description, status_id=status_id))

    def delete_lead(self, lead_id: str) -> None:
        self._c.delete_lead(lead_id)

    # Contacts
    def create_contact(self, *, lead_id, name, title=None, emails=None, phones=None, urls=None) -> Contact:
        return nc.contact(self._c.create_contact(
            lead_id=lead_id, name=name, title=title, emails=emails, phones=phones, urls=urls))

    def list_contacts(self, lead_id: str) -> list[Contact]:
        return nc.contacts(self._c.list_contacts(lead_id))

    def get_contact(self, contact_id: str) -> Contact:
        return nc.contact(self._c.get_contact(contact_id))

    def update_contact(self, contact_id: str, *, name=None, title=None) -> Contact:
        return nc.contact(self._c.update_contact(contact_id, name=name, title=title))

    def delete_contact(self, contact_id: str) -> None:
        self._c.delete_contact(contact_id)

    # Tasks
    def create_task(self, *, lead_id, text, due_date=None, assigned_to=None) -> Task:
        return nc.task(self._c.create_task(
            lead_id=lead_id, text=text, due_date=due_date, assigned_to=assigned_to))

    def list_tasks(self, *, lead_id: Optional[str] = None, is_complete: Optional[bool] = None) -> list[Task]:
        return nc.tasks(self._c.list_tasks(lead_id=lead_id, is_complete=is_complete))

    def update_task(self, task_id: str, *, text=None, due_date=None, assigned_to=None) -> Task:
        return nc.task(self._c.update_task(task_id, text=text, due_date=due_date, assigned_to=assigned_to))

    def complete_task(self, task_id: str) -> Task:
        return nc.task(self._c.complete_task(task_id))

    def delete_task(self, task_id: str) -> None:
        self._c.delete_task(task_id)

    # Notes
    def create_note(self, *, lead_id, note_text) -> Note:
        return nc.note(self._c.create_note(lead_id=lead_id, note_text=note_text))

    def list_notes(self, lead_id: str, *, limit=10) -> list[Note]:
        return nc.notes(self._c.list_notes(lead_id, limit=limit))

    # Meta
    def list_statuses(self) -> list[LeadStatus]:
        return nc.statuses(self._c.list_lead_statuses())

    def whoami(self) -> User:
        return nc.user(self._c.get_me())
