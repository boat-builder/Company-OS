"""Small, defensive helpers shared by the normalizers.

Provider payloads vary (especially the passthrough social records), so every
accessor tolerates missing keys, wrong types, and alternate field names.
"""

from __future__ import annotations

import re
from typing import Any, Optional
from urllib.parse import urlparse

_TAG_RE = re.compile(r"<[^>]+>")


def pick(d: Any, *keys: str) -> Any:
    """Return the first present, non-None value among `keys` in dict `d`."""
    if not isinstance(d, dict):
        return None
    for key in keys:
        if key in d and d[key] is not None:
            return d[key]
    return None


def as_int(value: Any) -> Optional[int]:
    if value is None or isinstance(value, bool):
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def as_float(value: Any) -> Optional[float]:
    if value is None or isinstance(value, bool):
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def as_list(value: Any) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def strip_html(value: Any) -> Optional[str]:
    if not value:
        return None
    return _TAG_RE.sub("", str(value)).strip() or None


def domain_of(url_or_domain: Optional[str]) -> Optional[str]:
    """Reduce a URL or host to a bare registrable-ish domain (drops scheme/www/path)."""
    if not url_or_domain:
        return None
    value = url_or_domain.strip()
    if "//" not in value:
        value = "//" + value
    host = urlparse(value).netloc or ""
    host = host.split("@")[-1].split(":")[0]
    if host.startswith("www."):
        host = host[4:]
    return host or None
