"""Typed ChatGPT client — returns a canonical AnswerResult."""

from __future__ import annotations

from ..models import AnswerResult
from ..normalize import marketing as nm
from ..providers import MarketingClient


class ChatGPTClient:
    def __init__(self, marketing: MarketingClient) -> None:
        self._m = marketing

    def search(self, *, query, model=None, system_prompt=None, search_context_size=None,
               domain_filter=None, max_tokens=None, reasoning_effort=None,
               include_citations=None, user_location=None) -> AnswerResult:
        result = nm.chatgpt_search(self._m.chatgpt_search(
            query=query, model=model, system_prompt=system_prompt,
            search_context_size=search_context_size, domain_filter=domain_filter,
            max_tokens=max_tokens, reasoning_effort=reasoning_effort,
            include_citations=include_citations, user_location=user_location))
        result.query = query  # response carries no query echo
        return result
