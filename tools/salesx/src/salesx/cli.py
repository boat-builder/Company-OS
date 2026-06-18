"""salesx — sales tools as one CLI.

Each group wraps one backend; each command wraps one capability and prints a
canonical JSON object (see that command's --help for its exact `Output:` shape).
Composing these into a sales workflow is the caller's job, not the tool's.

Setup
  Put credentials in tools/salesx/.env (copy .env.example) or the environment.
  Commands only need the keys they use:
    MARKETING_API_KEY, MARKETING_BASE_URL   (linkedin, x, google, chatgpt, seo)
    MARKETING_AUTH_STYLE                     (optional: bearer [default] | x-api-key)
    CLOSE_API_KEY                            (crm)

Discovery
  salesx --help                 list groups
  salesx <group> --help         list a group's commands
  salesx <group> <cmd> --help   full flags + the Output: data shape

Output
  Canonical JSON by default; -f table for humans; -o FILE to write to a file.

Programmatic use
  from salesx import Salesx; Salesx().seo.domain_overview(target="acme.com")
"""

from __future__ import annotations

import click

from . import __version__
from .commands import chatgpt, crm, google, linkedin, seo, x


@click.group(help=__doc__)
@click.version_option(version=__version__, prog_name="salesx")
def cli() -> None:
    pass


for _group in (linkedin, x, google, chatgpt, seo, crm):
    cli.add_command(_group)


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
