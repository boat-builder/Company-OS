"""Close CRM client.

Wraps `https://api.close.com/api/v1` (HTTP basic auth: key as username, empty
password). Returns raw parsed JSON; normalization happens in salesx.normalize.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any, Optional

from ..config import Settings
from .http import request_json

BASE_URL = "https://api.close.com/api/v1"

_STATUS_HINTS = {
    401: "invalid/expired key",
    403: "forbidden",
    404: "not found",
}


class CloseClient:
    def __init__(self, settings: Settings) -> None:
        settings.require_close()
        self._auth = (settings.close_api_key, "")

    def _request(self, method: str, endpoint: str, **kwargs) -> Any:
        return request_json(
            method,
            f"{BASE_URL}/{endpoint.lstrip('/')}",
            provider="close",
            auth=self._auth,
            status_hints=_STATUS_HINTS,
            **kwargs,
        )

    # --- Leads --------------------------------------------------------------

    def create_lead(self, *, name, url=None, description=None, status_id=None, contacts=None) -> Any:
        payload: dict[str, Any] = {"name": name}
        if url:
            payload["url"] = url
        if description:
            payload["description"] = description
        if status_id:
            payload["status_id"] = status_id
        if contacts:
            payload["contacts"] = contacts
        return self._request("POST", "/lead/", json_body=payload)

    def search_leads(self, *, query=None, name=None, status_id=None, limit=10, sort=None) -> Any:
        params: dict[str, Any] = {"_limit": limit}
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
        return self._request("GET", "/lead/", params=params)

    def get_lead(self, lead_id: str) -> Any:
        return self._request("GET", f"/lead/{lead_id}/")

    def update_lead(self, lead_id: str, *, name=None, url=None, description=None, status_id=None) -> Any:
        payload: dict[str, Any] = {}
        if name is not None:
            payload["name"] = name
        if url is not None:
            payload["url"] = url
        if description is not None:
            payload["description"] = description
        if status_id is not None:
            payload["status_id"] = status_id
        return self._request("PUT", f"/lead/{lead_id}/", json_body=payload)

    def delete_lead(self, lead_id: str) -> Any:
        return self._request("DELETE", f"/lead/{lead_id}/")

    # --- Contacts -----------------------------------------------------------

    def create_contact(self, *, lead_id, name, title=None, emails=None, phones=None, urls=None) -> Any:
        payload: dict[str, Any] = {"lead_id": lead_id, "name": name}
        if title:
            payload["title"] = title
        if emails:
            payload["emails"] = [{"email": e, "type": "office"} for e in emails]
        if phones:
            payload["phones"] = [{"phone": p, "type": "office"} for p in phones]
        if urls:
            payload["urls"] = [{"url": u, "type": "url"} for u in urls]
        return self._request("POST", "/contact/", json_body=payload)

    def list_contacts(self, lead_id: str) -> Any:
        return self._request("GET", "/contact/", params={"lead_id": lead_id})

    def get_contact(self, contact_id: str) -> Any:
        return self._request("GET", f"/contact/{contact_id}/")

    def update_contact(self, contact_id: str, *, name=None, title=None) -> Any:
        payload: dict[str, Any] = {}
        if name is not None:
            payload["name"] = name
        if title is not None:
            payload["title"] = title
        return self._request("PUT", f"/contact/{contact_id}/", json_body=payload)

    def delete_contact(self, contact_id: str) -> Any:
        return self._request("DELETE", f"/contact/{contact_id}/")

    # --- Tasks --------------------------------------------------------------

    def create_task(self, *, lead_id, text, due_date=None, assigned_to=None) -> Any:
        if due_date is None:
            due_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        payload: dict[str, Any] = {
            "_type": "lead",
            "lead_id": lead_id,
            "text": text,
            "date": due_date,
        }
        if assigned_to:
            payload["assigned_to"] = assigned_to
        return self._request("POST", "/task/", json_body=payload)

    def list_tasks(self, *, lead_id: Optional[str] = None, is_complete: Optional[bool] = None) -> Any:
        params: dict[str, Any] = {}
        if lead_id:
            params["lead_id"] = lead_id
        if is_complete is not None:
            params["is_complete"] = str(is_complete).lower()
        return self._request("GET", "/task/", params=params)

    def update_task(self, task_id: str, *, text=None, due_date=None, is_complete=None, assigned_to=None) -> Any:
        payload: dict[str, Any] = {}
        if text is not None:
            payload["text"] = text
        if due_date is not None:
            payload["date"] = due_date
        if is_complete is not None:
            payload["is_complete"] = is_complete
        if assigned_to is not None:
            payload["assigned_to"] = assigned_to
        return self._request("PUT", f"/task/{task_id}/", json_body=payload)

    def complete_task(self, task_id: str) -> Any:
        return self.update_task(task_id, is_complete=True)

    def delete_task(self, task_id: str) -> Any:
        return self._request("DELETE", f"/task/{task_id}/")

    # --- Notes --------------------------------------------------------------

    def create_note(self, *, lead_id, note_text) -> Any:
        return self._request("POST", "/activity/note/", json_body={
            "lead_id": lead_id, "note": note_text})

    def list_notes(self, lead_id: str, *, limit: int = 10) -> Any:
        return self._request("GET", "/activity/note/", params={"lead_id": lead_id, "_limit": limit})

    # --- Meta ---------------------------------------------------------------

    def get_me(self) -> Any:
        return self._request("GET", "/me/")

    def list_lead_statuses(self) -> Any:
        return self._request("GET", "/status/lead/")
