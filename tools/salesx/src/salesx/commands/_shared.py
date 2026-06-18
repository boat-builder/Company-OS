"""Shared plumbing for the command layer.

`AppContext` lazily builds the Salesx facade. `output_options` attaches the
universal output flags. `--raw` exists (returns the untouched provider payload) but
is **hidden** — it isn't shown in `--help` and isn't part of the documented surface,
so agents work with the canonical models by default.
"""

from __future__ import annotations

import json
from typing import Any, Callable, Optional

import click

from ..client import Salesx


class AppContext:
    def __init__(self) -> None:
        self._sx: Optional[Salesx] = None

    @property
    def sx(self) -> Salesx:
        if self._sx is None:
            self._sx = Salesx()
        return self._sx


pass_app = click.make_pass_decorator(AppContext, ensure=True)


def output_options(func: Callable) -> Callable:
    """Attach -f/--format, -o/--output, and a hidden --raw to a leaf command."""
    func = click.option(
        "-o", "--output", "output",
        type=click.Path(dir_okay=False, writable=True),
        help="Write JSON to this file instead of stdout.",
    )(func)
    func = click.option(
        "--raw", is_flag=True, hidden=True,
        help="Internal: emit the untouched provider payload (undocumented).",
    )(func)
    func = click.option(
        "-f", "--format", "fmt",
        type=click.Choice(["json", "table"]), default="json", show_default=True,
        help="Output format.",
    )(func)
    return func


def split_name(full: str) -> dict[str, str]:
    """Split 'First Middle Last' into {first_name, last_name}."""
    parts = full.strip().split()
    if not parts:
        raise click.UsageError("Empty name.")
    if len(parts) == 1:
        return {"first_name": parts[0], "last_name": ""}
    return {"first_name": parts[0], "last_name": " ".join(parts[1:])}


def parse_filters(filters: Optional[str]) -> Any:
    """Parse a --filters value as JSON, falling back to the raw string."""
    if filters is None:
        return None
    try:
        return json.loads(filters)
    except json.JSONDecodeError:
        return filters
