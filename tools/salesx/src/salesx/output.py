"""Rendering — turn results into JSON (default), a table, or a file.

Default output is canonical JSON because the primary consumer is an agent. `table`
is a human convenience; `raw` is handled by the command (it passes the untouched
provider payload here instead of a model).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional

import click
from rich.console import Console
from rich.table import Table

from .models import Model

console = Console()
err_console = Console(stderr=True)


def to_jsonable(data: Any) -> Any:
    """Recursively convert canonical models to plain JSON-able structures."""
    if isinstance(data, Model):
        return data.to_dict()
    if isinstance(data, dict):
        return {k: to_jsonable(v) for k, v in data.items()}
    if isinstance(data, (list, tuple)):
        return [to_jsonable(v) for v in data]
    return data


def _compact(value: Any) -> str:
    if isinstance(value, (dict, list)):
        text = json.dumps(value, ensure_ascii=False)
        return text if len(text) <= 60 else text[:57] + "..."
    return "" if value is None else str(value)


def _render_table(payload: Any, title: Optional[str]) -> None:
    # List of dicts -> columns from the union of keys (stable order by first row).
    if isinstance(payload, list) and payload and all(isinstance(r, dict) for r in payload):
        columns: list[str] = []
        for row in payload:
            for k in row:
                if k not in columns:
                    columns.append(k)
        table = Table(title=title, show_lines=False, header_style="bold cyan")
        for col in columns:
            table.add_column(col, overflow="fold")
        for row in payload:
            table.add_row(*[_compact(row.get(col)) for col in columns])
        console.print(table)
        return
    # Single dict -> key/value table.
    if isinstance(payload, dict):
        table = Table(title=title, show_header=False, box=None)
        table.add_column("field", style="bold cyan")
        table.add_column("value", overflow="fold")
        for k, v in payload.items():
            table.add_row(k, _compact(v))
        console.print(table)
        return
    # Fallback: just print JSON.
    console.print_json(json.dumps(payload, ensure_ascii=False))


def emit(
    data: Any,
    *,
    fmt: str = "json",
    output: Optional[str] = None,
    raw: bool = False,
    title: Optional[str] = None,
) -> None:
    """Render `data`. If `raw`, `data` is already a plain provider payload."""
    payload = data if raw else to_jsonable(data)

    if output:
        text = payload if isinstance(payload, str) else json.dumps(payload, indent=2, ensure_ascii=False)
        Path(output).write_text(text)
        err_console.print(f"[green]Wrote response to {output}[/green]")
        return

    if isinstance(payload, str):
        click.echo(payload)
        return

    if fmt == "table":
        _render_table(payload, title)
    else:
        console.print_json(json.dumps(payload, ensure_ascii=False))
