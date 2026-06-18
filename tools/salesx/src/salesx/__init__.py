"""salesx — sales tools (LinkedIn, X, Google, ChatGPT, SEO, Close CRM) as one CLI
and one importable SDK.

Each command/method is a thin, direct wrapper over a single backend capability and
returns a canonical dataclass model (so the same layer is usable from a program, not
just the shell). It is deliberately *not* organized around sales phases — composing
these tools into a workflow is the caller's (or the agent prompt's) job.

Programmatic use:

    from salesx import Salesx
    sx = Salesx()
    sx.seo.domain_overview(target="acme.com")     # -> DomainOverview

Layering: providers (raw transport) → normalize (dict→model) → models (the contract)
→ sdk (typed clients) → client.Salesx (facade) → commands (CLI).
"""

from .client import Salesx

__version__ = "0.2.0"

__all__ = ["Salesx", "__version__"]
