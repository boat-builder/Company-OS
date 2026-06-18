"""Base for all canonical models.

Models are plain dataclasses. `to_dict()` recursively serializes nested models and
drops `None` values, so the JSON an agent receives is a stable, low-noise contract:
a field is either present with a real value or absent because it's unknown. Empty
lists/strings/zeros are kept — they are meaningful ("we looked, found none/zero").
"""

from __future__ import annotations

from dataclasses import dataclass, fields
from typing import Any


def _clean(value: Any) -> Any:
    if isinstance(value, Model):
        return value.to_dict()
    if isinstance(value, dict):
        return {k: _clean(v) for k, v in value.items() if v is not None}
    if isinstance(value, (list, tuple)):
        return [_clean(v) for v in value]
    return value


@dataclass
class Model:
    """Common serialization for every canonical model."""

    def to_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for f in fields(self):
            val = getattr(self, f.name)
            if val is None:
                continue
            out[f.name] = _clean(val)
        return out
