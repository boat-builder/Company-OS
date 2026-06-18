"""CLI command groups — one per provider/resource, flat. No workflow abstraction."""

from .chatgpt import chatgpt
from .crm import crm
from .google import google
from .linkedin import linkedin
from .seo import seo
from .x import x_group as x

__all__ = ["linkedin", "x", "google", "chatgpt", "seo", "crm"]
