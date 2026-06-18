"""Typed LinkedIn client — returns canonical models."""

from __future__ import annotations

from ..models import LinkedInCompany, LinkedInJob, LinkedInPost, LinkedInProfile
from ..normalize import marketing as nm
from ..providers import MarketingClient


class LinkedInClient:
    def __init__(self, marketing: MarketingClient) -> None:
        self._m = marketing

    def profiles(self, *, urls=None, names=None, limit_per_input=None, wait_seconds=None) -> list[LinkedInProfile]:
        return nm.linkedin_profiles(self._m.linkedin_profiles(
            urls=urls, names=names, limit_per_input=limit_per_input, wait_seconds=wait_seconds))

    def companies(self, *, urls, wait_seconds=None) -> list[LinkedInCompany]:
        return nm.linkedin_companies(self._m.linkedin_companies(urls=urls, wait_seconds=wait_seconds))

    def jobs(self, *, urls=None, searches=None, limit_per_input=None, wait_seconds=None) -> list[LinkedInJob]:
        return nm.linkedin_jobs(self._m.linkedin_jobs(
            urls=urls, searches=searches, limit_per_input=limit_per_input, wait_seconds=wait_seconds))

    def posts(self, *, urls=None, profile_urls=None, limit_per_input=None, wait_seconds=None) -> list[LinkedInPost]:
        return nm.linkedin_posts(self._m.linkedin_posts(
            urls=urls, profile_urls=profile_urls, limit_per_input=limit_per_input, wait_seconds=wait_seconds))
