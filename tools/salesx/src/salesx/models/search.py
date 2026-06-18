"""Search & answer-surface canonical models (Google search, AI Mode, ChatGPT).

Curated from real responses. Note: the ChatGPT response carries no `query` echo, so
the SDK injects it onto the model from the request.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

from .base import Model


@dataclass
class SearchHit(Model):
    """One organic result on a SERP."""

    title: Optional[str] = None
    url: Optional[str] = None
    snippet: Optional[str] = None
    displayed_link: Optional[str] = None
    position: Optional[int] = None


@dataclass
class SearchResults(Model):
    """Google web search results (`google search`)."""

    query: Optional[str] = None
    engine: Optional[str] = None
    search_type: Optional[str] = None
    results: list[SearchHit] = field(default_factory=list)
    total: Optional[int] = None            # rows actually returned
    total_results: Optional[int] = None    # Google's "About N results" estimate
    features: dict[str, Any] = field(default_factory=dict)  # answer_box, related_searches, ...


@dataclass
class Citation(Model):
    """A cited source backing a generated answer."""

    title: Optional[str] = None
    url: Optional[str] = None
    source: Optional[str] = None
    snippet: Optional[str] = None


@dataclass
class AnswerResult(Model):
    """A generated, web-grounded answer (Google AI Mode or ChatGPT)."""

    query: Optional[str] = None
    engine: Optional[str] = None           # "google-ai-mode" | "chatgpt"
    model: Optional[str] = None
    answer: Optional[str] = None           # markdown/text content
    citations: list[Citation] = field(default_factory=list)
    usage: dict[str, Any] = field(default_factory=dict)  # token usage (ChatGPT)
