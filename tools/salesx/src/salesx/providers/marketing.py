"""Marketing intelligence backend client.

Thin, complete wrapper over `<host>/api/v1/admin/marketing`. Every endpoint is a
POST with a JSON body that responds synchronously; methods build the body, post it,
and return the raw parsed JSON (normalization happens in salesx.normalize). Each
method drops `None`/empty fields so callers can pass everything and only set values
flow to the wire.
"""

from __future__ import annotations

from typing import Any, Optional

from ..config import Settings
from .http import request_json

API_PREFIX = "/api/v1/admin/marketing"

_STATUS_HINTS = {
    400: "invalid input",
    401: "missing/invalid key",
    403: "blocked account",
    429: "rate limited",
    502: "upstream provider failure",
    503: "capability not configured",
    504: "upstream timeout",
}


def _body(**fields: Any) -> dict[str, Any]:
    """Build a request body from kwargs, dropping None and empty tuples/lists."""
    out: dict[str, Any] = {}
    for key, value in fields.items():
        if value is None:
            continue
        if isinstance(value, (tuple, list)) and len(value) == 0:
            continue
        out[key] = list(value) if isinstance(value, tuple) else value
    return out


class MarketingClient:
    def __init__(self, settings: Settings) -> None:
        settings.require_marketing()
        self._base = settings.marketing_base_url
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        if settings.marketing_auth_style == "x-api-key":
            headers["X-API-Key"] = settings.marketing_api_key
        else:
            headers["Authorization"] = f"Bearer {settings.marketing_api_key}"
        self._headers = headers

    def post(self, path: str, body: dict[str, Any]) -> Any:
        return request_json(
            "POST",
            f"{self._base}{API_PREFIX}{path}",
            provider="marketing",
            headers=self._headers,
            json_body=body,
            status_hints=_STATUS_HINTS,
        )

    # --- LinkedIn -----------------------------------------------------------

    def linkedin_profiles(self, *, urls=None, names=None, limit_per_input=None, wait_seconds=None) -> Any:
        return self.post("/linkedin/profiles", _body(
            urls=urls, names=names, limit_per_input=limit_per_input, wait_seconds=wait_seconds))

    def linkedin_companies(self, *, urls, wait_seconds=None) -> Any:
        return self.post("/linkedin/companies", _body(urls=urls, wait_seconds=wait_seconds))

    def linkedin_jobs(self, *, urls=None, searches=None, limit_per_input=None, wait_seconds=None) -> Any:
        return self.post("/linkedin/jobs", _body(
            urls=urls, searches=searches, limit_per_input=limit_per_input, wait_seconds=wait_seconds))

    def linkedin_posts(self, *, urls=None, profile_urls=None, limit_per_input=None, wait_seconds=None) -> Any:
        return self.post("/linkedin/posts", _body(
            urls=urls, profile_urls=profile_urls, limit_per_input=limit_per_input, wait_seconds=wait_seconds))

    # --- X (Twitter) --------------------------------------------------------

    def x_posts(self, *, urls=None, profiles=None, limit_per_input=None, wait_seconds=None) -> Any:
        return self.post("/x/posts", _body(
            urls=urls, profiles=profiles, limit_per_input=limit_per_input, wait_seconds=wait_seconds))

    def x_profiles(self, *, urls, wait_seconds=None) -> Any:
        return self.post("/x/profiles", _body(urls=urls, wait_seconds=wait_seconds))

    # --- Google -------------------------------------------------------------

    def google_search(self, *, query, country=None, language=None, location=None, max_results=None) -> Any:
        return self.post("/google/search", _body(
            query=query, country=country, language=language, location=location, max_results=max_results))

    def google_ai_mode(self, *, query, country=None, language=None, location=None) -> Any:
        return self.post("/google/ai-mode", _body(
            query=query, country=country, language=language, location=location))

    # --- ChatGPT ------------------------------------------------------------

    def chatgpt_search(self, *, query, model=None, system_prompt=None, search_context_size=None,
                       domain_filter=None, max_tokens=None, reasoning_effort=None,
                       include_citations=None, user_location=None) -> Any:
        return self.post("/chatgpt/search", _body(
            query=query, model=model, system_prompt=system_prompt,
            search_context_size=search_context_size, domain_filter=domain_filter,
            max_tokens=max_tokens, reasoning_effort=reasoning_effort,
            include_citations=include_citations, user_location=user_location))

    # --- SEO ----------------------------------------------------------------

    def seo_ranked_keywords(self, *, target, location_code=None, language_code=None,
                            limit=None, offset=None, order_by=None, filters=None) -> Any:
        return self.post("/seo/ranked-keywords", _body(
            target=target, location_code=location_code, language_code=language_code,
            limit=limit, offset=offset, order_by=order_by, filters=filters))

    def seo_keyword_ideas(self, *, keywords, location_code=None, language_code=None,
                          limit=None, offset=None, order_by=None, filters=None) -> Any:
        return self.post("/seo/keyword-ideas", _body(
            keywords=keywords, location_code=location_code, language_code=language_code,
            limit=limit, offset=offset, order_by=order_by, filters=filters))

    def seo_domain_overview(self, *, target, location_code=None, language_code=None) -> Any:
        return self.post("/seo/domain-overview", _body(
            target=target, location_code=location_code, language_code=language_code))

    def seo_historical_rank_overview(self, *, target, location_code=None, language_code=None,
                                     date_from=None, date_to=None) -> Any:
        return self.post("/seo/historical-rank-overview", _body(
            target=target, location_code=location_code, language_code=language_code,
            date_from=date_from, date_to=date_to))

    def seo_technologies(self, *, target) -> Any:
        return self.post("/seo/technologies", _body(target=target))

    def seo_bulk_traffic_estimation(self, *, targets, location_code=None, language_code=None,
                                    item_types=None) -> Any:
        return self.post("/seo/bulk-traffic-estimation", _body(
            targets=targets, location_code=location_code, language_code=language_code,
            item_types=item_types))

    def seo_relevant_pages(self, *, target, location_code=None, language_code=None,
                           limit=None, offset=None, order_by=None, filters=None) -> Any:
        return self.post("/seo/relevant-pages", _body(
            target=target, location_code=location_code, language_code=language_code,
            limit=limit, offset=offset, order_by=order_by, filters=filters))

    def seo_lighthouse(self, *, url, strategy=None, locale=None) -> Any:
        return self.post("/seo/lighthouse", _body(url=url, strategy=strategy, locale=locale))
