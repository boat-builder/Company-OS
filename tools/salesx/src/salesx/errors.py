"""Error types for salesx.

Everything user-facing inherits from click.ClickException so the CLI prints a
clean one-line message (and exits non-zero) instead of a traceback.
"""

from __future__ import annotations

import click


class SalesxError(click.ClickException):
    """Base class for all salesx errors surfaced to the user."""


class ConfigError(SalesxError):
    """A required credential or setting is missing/invalid."""


class ProviderError(SalesxError):
    """An upstream provider (Marketing backend or Close) returned an error.

    Carries the HTTP status and the raw payload so callers can inspect it, while
    `format_message()` renders a readable summary.
    """

    def __init__(self, provider: str, status: int, detail: str, hint: str = "") -> None:
        self.provider = provider
        self.status = status
        self.detail = detail
        self.hint = hint
        suffix = f" ({hint})" if hint else ""
        super().__init__(f"{provider} HTTP {status}{suffix}\n{detail}".rstrip())
