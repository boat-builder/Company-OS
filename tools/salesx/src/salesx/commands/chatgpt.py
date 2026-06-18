"""`salesx chatgpt ...` — web-grounded ChatGPT answer with citations."""

from __future__ import annotations

import click

from ..output import emit
from ._shared import output_options, pass_app


@click.group()
def chatgpt() -> None:
    """Web-grounded ChatGPT answers with citations."""


@chatgpt.command("search")
@click.option("--query", required=True, help="The question.")
@click.option("--model", help="gpt-5.5 | gpt-5.4-mini | gpt-5.4-nano (default gpt-5.4-mini).")
@click.option("--system-prompt", help="Optional system instructions.")
@click.option("--search-context-size", type=click.Choice(["low", "medium", "high"]), help="Grounding context size.")
@click.option("--domain-filter", "domain_filter", multiple=True, help="Restrict grounding to this domain (repeatable).")
@click.option("--max-tokens", type=int, help="Cap response length.")
@click.option("--reasoning-effort", type=click.Choice(["minimal", "low", "medium", "high"]), help="Reasoning effort.")
@click.option("--include-citations/--no-include-citations", "include_citations", default=None, help="Include citations (default true).")
@click.option("--city", help="user_location.city")
@click.option("--region", help="user_location.region")
@click.option("--user-country", help="user_location.country")
@click.option("--timezone", help="user_location.timezone")
@output_options
@pass_app
def search(app, query, model, system_prompt, search_context_size, domain_filter,
           max_tokens, reasoning_effort, include_citations, city, region,
           user_country, timezone, fmt, raw, output):
    """Ask ChatGPT a question with live web grounding.

    Output: AnswerResult — query, engine ("chatgpt"), model, answer (text),
    citations[] (title, url, snippet), usage{input_tokens, output_tokens,
    total_tokens}.
    """
    user_location = {k: v for k, v in {
        "city": city, "region": region, "country": user_country, "timezone": timezone,
    }.items() if v is not None} or None
    kw = dict(query=query, model=model, system_prompt=system_prompt,
              search_context_size=search_context_size, domain_filter=list(domain_filter) or None,
              max_tokens=max_tokens, reasoning_effort=reasoning_effort,
              include_citations=include_citations, user_location=user_location)
    data = app.sx.marketing.chatgpt_search(**kw) if raw else app.sx.chatgpt.search(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="ChatGPT")
