"""`salesx google ...` — Google web search and the AI Mode answer surface."""

from __future__ import annotations

import click

from ..output import emit
from ._shared import output_options, pass_app


@click.group()
def google() -> None:
    """Google web search and the conversational AI Mode surface."""


@google.command("search")
@click.option("--query", required=True, help="Search query.")
@click.option("--country", help='ISO 3166-1 alpha-2, e.g. "us", "de".')
@click.option("--language", help='Two-letter code, e.g. "en".')
@click.option("--location", help='Canonical location, e.g. "Austin,Texas,United States".')
@click.option("--max-results", type=int, help="Cap organic results (1-100).")
@output_options
@pass_app
def search(app, query, country, language, location, max_results, fmt, raw, output):
    """Web search with organic results + SERP features.

    Output: SearchResults — query, engine, search_type, total (rows returned),
    total_results (Google's estimate), features{answer_box, related_searches, ...},
    results[] (title, url, snippet, displayed_link, position).
    """
    kw = dict(query=query, country=country, language=language,
              location=location, max_results=max_results)
    data = app.sx.marketing.google_search(**kw) if raw else app.sx.google.search(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="Google search")


@google.command("ai-mode")
@click.option("--query", required=True, help="Question.")
@click.option("--country", help="ISO 3166-1 alpha-2.")
@click.option("--language", help="Two-letter code.")
@click.option("--location", help="Canonical location name.")
@output_options
@pass_app
def ai_mode(app, query, country, language, location, fmt, raw, output):
    """AI Mode — a markdown answer with cited references.

    Output: AnswerResult — query, engine ("google-ai-mode"), answer (markdown),
    citations[] (title, url, source, snippet).
    """
    kw = dict(query=query, country=country, language=language, location=location)
    data = app.sx.marketing.google_ai_mode(**kw) if raw else app.sx.google.ai_mode(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="Google AI Mode")
