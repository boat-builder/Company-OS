"""Shared HTTP plumbing for provider clients.

One place that issues requests, applies a generous timeout, and turns HTTP error
responses into readable ProviderErrors carrying the upstream payload.
"""

from __future__ import annotations

import json
from typing import Any, Optional

import requests

from ..errors import ProviderError

# Marketing's `wait_seconds` can be up to 600; give the socket headroom on top.
DEFAULT_TIMEOUT = (10, 660)  # (connect, read) seconds


def request_json(
    method: str,
    url: str,
    *,
    provider: str,
    headers: Optional[dict] = None,
    auth: Optional[tuple] = None,
    json_body: Optional[dict] = None,
    params: Optional[dict] = None,
    timeout: tuple = DEFAULT_TIMEOUT,
    status_hints: Optional[dict[int, str]] = None,
) -> Any:
    """Issue a request and return parsed JSON, or raise ProviderError.

    `status_hints` maps HTTP status codes to a short human hint appended to the
    error (e.g. {401: "missing/invalid key"}).
    """
    try:
        resp = requests.request(
            method,
            url,
            headers=headers,
            auth=auth,
            json=json_body,
            params=params,
            timeout=timeout,
        )
    except requests.exceptions.Timeout as exc:
        raise ProviderError(
            provider, 0,
            f"Request to {url} timed out. Discovery/audit jobs can be slow; "
            "retry or reduce scope.",
        ) from exc
    except requests.exceptions.RequestException as exc:
        raise ProviderError(provider, 0, f"Network error calling {url}: {exc}") from exc

    if resp.status_code >= 400:
        detail = resp.text.strip()
        try:
            detail = json.dumps(resp.json(), indent=2, ensure_ascii=False)
        except ValueError:
            pass
        hint = (status_hints or {}).get(resp.status_code, "")
        raise ProviderError(provider, resp.status_code, detail, hint)

    if not resp.content:
        return {}
    try:
        return resp.json()
    except ValueError:
        return resp.text
