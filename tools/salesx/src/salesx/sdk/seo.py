"""Typed SEO client — returns canonical models."""

from __future__ import annotations

from ..models import (
    DomainOverview,
    KeywordIdea,
    LighthouseReport,
    RankHistoryPoint,
    RankedKeyword,
    RelevantPage,
    TechStack,
    TrafficEstimate,
)
from ..normalize import marketing as nm
from ..providers import MarketingClient


class SeoClient:
    def __init__(self, marketing: MarketingClient) -> None:
        self._m = marketing

    def ranked_keywords(self, *, target, location_code=None, language_code=None,
                        limit=None, offset=None, order_by=None, filters=None) -> list[RankedKeyword]:
        return nm.ranked_keywords(self._m.seo_ranked_keywords(
            target=target, location_code=location_code, language_code=language_code,
            limit=limit, offset=offset, order_by=order_by, filters=filters))

    def keyword_ideas(self, *, keywords, location_code=None, language_code=None,
                      limit=None, offset=None, order_by=None, filters=None) -> list[KeywordIdea]:
        return nm.keyword_ideas(self._m.seo_keyword_ideas(
            keywords=keywords, location_code=location_code, language_code=language_code,
            limit=limit, offset=offset, order_by=order_by, filters=filters))

    def domain_overview(self, *, target, location_code=None, language_code=None) -> DomainOverview:
        return nm.domain_overview(self._m.seo_domain_overview(
            target=target, location_code=location_code, language_code=language_code))

    def historical_rank_overview(self, *, target, location_code=None, language_code=None,
                                 date_from=None, date_to=None) -> list[RankHistoryPoint]:
        return nm.historical_rank_overview(self._m.seo_historical_rank_overview(
            target=target, location_code=location_code, language_code=language_code,
            date_from=date_from, date_to=date_to))

    def technologies(self, *, target) -> TechStack:
        return nm.technologies(self._m.seo_technologies(target=target))

    def bulk_traffic_estimation(self, *, targets, location_code=None, language_code=None,
                                item_types=None) -> list[TrafficEstimate]:
        return nm.bulk_traffic_estimation(self._m.seo_bulk_traffic_estimation(
            targets=targets, location_code=location_code, language_code=language_code, item_types=item_types))

    def relevant_pages(self, *, target, location_code=None, language_code=None,
                       limit=None, offset=None, order_by=None, filters=None) -> list[RelevantPage]:
        return nm.relevant_pages(self._m.seo_relevant_pages(
            target=target, location_code=location_code, language_code=language_code,
            limit=limit, offset=offset, order_by=order_by, filters=filters))

    def lighthouse(self, *, url, strategy=None, locale=None) -> LighthouseReport:
        return nm.lighthouse(self._m.seo_lighthouse(url=url, strategy=strategy, locale=locale))
