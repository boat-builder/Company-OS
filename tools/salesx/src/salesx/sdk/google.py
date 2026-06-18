"""Typed Google client — returns canonical models."""

from __future__ import annotations

from ..models import AnswerResult, SearchResults
from ..normalize import marketing as nm
from ..providers import MarketingClient


class GoogleClient:
    def __init__(self, marketing: MarketingClient) -> None:
        self._m = marketing

    def search(self, *, query, country=None, language=None, location=None, max_results=None) -> SearchResults:
        return nm.google_search(self._m.google_search(
            query=query, country=country, language=language, location=location, max_results=max_results))

    def ai_mode(self, *, query, country=None, language=None, location=None) -> AnswerResult:
        result = nm.google_ai_mode(self._m.google_ai_mode(
            query=query, country=country, language=language, location=location))
        result.query = result.query or query
        return result
