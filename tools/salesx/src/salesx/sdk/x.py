"""Typed X (Twitter) client — returns canonical models."""

from __future__ import annotations

from ..models import XPost, XProfile
from ..normalize import marketing as nm
from ..providers import MarketingClient


class XClient:
    def __init__(self, marketing: MarketingClient) -> None:
        self._m = marketing

    def posts(self, *, urls=None, profiles=None, limit_per_input=None, wait_seconds=None) -> list[XPost]:
        return nm.x_posts(self._m.x_posts(
            urls=urls, profiles=profiles, limit_per_input=limit_per_input, wait_seconds=wait_seconds))

    def profiles(self, *, urls, wait_seconds=None) -> list[XProfile]:
        return nm.x_profiles(self._m.x_profiles(urls=urls, wait_seconds=wait_seconds))
