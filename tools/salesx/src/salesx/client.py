"""The Salesx facade — the entry point for both the CLI and programmatic use.

    from salesx import Salesx
    sx = Salesx()                                  # reads env / .env
    profiles = sx.linkedin.profiles(urls=[url])    # -> list[LinkedInProfile]
    overview = sx.seo.domain_overview(target="acme.com")
    lead = sx.crm.create_lead(name="Acme")

Provider transports are built lazily, so constructing `Salesx` never checks
credentials; only touching `.linkedin`/`.seo`/… (Marketing) or `.crm` (Close)
validates the keys it needs. The raw transports are also exposed (`sx.marketing`,
`sx.close`) for the rare case you want the untouched provider payload.
"""

from __future__ import annotations

from typing import Optional

from .config import Settings, load_settings
from .providers import CloseClient, MarketingClient
from .sdk import (
    ChatGPTClient,
    CrmClient,
    GoogleClient,
    LinkedInClient,
    SeoClient,
    XClient,
)


class Salesx:
    def __init__(self, settings: Optional[Settings] = None) -> None:
        self._settings = settings or load_settings()
        self._marketing: Optional[MarketingClient] = None
        self._close: Optional[CloseClient] = None

    @property
    def settings(self) -> Settings:
        return self._settings

    # Raw transports (lazy; validate credentials on first use).
    @property
    def marketing(self) -> MarketingClient:
        if self._marketing is None:
            self._marketing = MarketingClient(self._settings)
        return self._marketing

    @property
    def close(self) -> CloseClient:
        if self._close is None:
            self._close = CloseClient(self._settings)
        return self._close

    # Typed clients (return models).
    @property
    def linkedin(self) -> LinkedInClient:
        return LinkedInClient(self.marketing)

    @property
    def x(self) -> XClient:
        return XClient(self.marketing)

    @property
    def google(self) -> GoogleClient:
        return GoogleClient(self.marketing)

    @property
    def chatgpt(self) -> ChatGPTClient:
        return ChatGPTClient(self.marketing)

    @property
    def seo(self) -> SeoClient:
        return SeoClient(self.marketing)

    @property
    def crm(self) -> CrmClient:
        return CrmClient(self.close)
