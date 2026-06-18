"""`salesx seo ...` — search-engine ranking intelligence."""

from __future__ import annotations

import click

from ..output import emit
from ._shared import output_options, parse_filters, pass_app


@click.group()
def seo() -> None:
    """Keyword rankings, related keywords, domain metrics, tech stack, audits."""


@seo.command("ranked-keywords")
@click.option("--target", required=True, help='Domain, e.g. "example.com".')
@click.option("--location-code", type=int, help="Numeric location code (e.g. 2840 = US).")
@click.option("--language-code", help='Two-letter code, e.g. "en".')
@click.option("--limit", type=int, help="Default 100, max 1000.")
@click.option("--offset", type=int, help="Pagination offset.")
@click.option("--order-by", "order_by", multiple=True, help="e.g. keyword_data.keyword_info.search_volume,desc (repeatable).")
@click.option("--filters", help="Upstream filter expression (JSON or raw string).")
@output_options
@pass_app
def ranked_keywords(app, target, location_code, language_code, limit, offset, order_by, filters, fmt, raw, output):
    """Keywords a domain ranks for in Google.

    Output: RankedKeyword[] — keyword, search_volume, cpc, competition,
    competition_level, rank, rank_group, url, domain, title, intent, etv.
    """
    kw = dict(target=target, location_code=location_code, language_code=language_code,
              limit=limit, offset=offset, order_by=list(order_by) or None, filters=parse_filters(filters))
    data = app.sx.marketing.seo_ranked_keywords(**kw) if raw else app.sx.seo.ranked_keywords(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="Ranked keywords")


@seo.command("keyword-ideas")
@click.option("--keyword", "keywords", multiple=True, required=True, help="Seed keyword, 1-200 (repeatable).")
@click.option("--location-code", type=int, help="Numeric location code.")
@click.option("--language-code", help="Two-letter code.")
@click.option("--limit", type=int, help="Default 100, max 1000.")
@click.option("--offset", type=int, help="Pagination offset.")
@click.option("--order-by", "order_by", multiple=True, help="e.g. keyword_info.search_volume,desc (repeatable).")
@click.option("--filters", help="Upstream filter expression (JSON or raw string).")
@output_options
@pass_app
def keyword_ideas(app, keywords, location_code, language_code, limit, offset, order_by, filters, fmt, raw, output):
    """Keywords semantically related to seed keywords.

    Output: KeywordIdea[] — keyword, search_volume, cpc, competition,
    competition_level, difficulty.
    """
    kw = dict(keywords=list(keywords), location_code=location_code, language_code=language_code,
              limit=limit, offset=offset, order_by=list(order_by) or None, filters=parse_filters(filters))
    data = app.sx.marketing.seo_keyword_ideas(**kw) if raw else app.sx.seo.keyword_ideas(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="Keyword ideas")


@seo.command("domain-overview")
@click.option("--target", required=True, help="Domain to analyze.")
@click.option("--location-code", type=int, help="Numeric location code.")
@click.option("--language-code", help="Two-letter code.")
@output_options
@pass_app
def domain_overview(app, target, location_code, language_code, fmt, raw, output):
    """Ranking + traffic metrics for a domain.

    Output: DomainOverview — target, organic (TrafficMetrics: count, etv,
    paid_traffic_cost, is_new, is_up, is_down, is_lost; pos_* buckets are omitted at
    this endpoint), paid (same shape).
    """
    kw = dict(target=target, location_code=location_code, language_code=language_code)
    data = app.sx.marketing.seo_domain_overview(**kw) if raw else app.sx.seo.domain_overview(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="Domain overview")


@seo.command("historical-rank-overview")
@click.option("--target", required=True, help="Domain to analyze.")
@click.option("--location-code", type=int, help="Numeric location code.")
@click.option("--language-code", help="Two-letter code.")
@click.option("--date-from", help="Series start, YYYY-MM-DD.")
@click.option("--date-to", help="Series end, YYYY-MM-DD.")
@output_options
@pass_app
def historical_rank_overview(app, target, location_code, language_code, date_from, date_to, fmt, raw, output):
    """Monthly ranking/traffic (etv) time series — the momentum signal.

    Output: RankHistoryPoint[] — year, month, organic (TrafficMetrics: count, etv,
    paid_traffic_cost, pos_1, pos_2_3, pos_4_10, pos_11_plus, is_new, is_up, is_down,
    is_lost), paid.
    """
    kw = dict(target=target, location_code=location_code, language_code=language_code,
              date_from=date_from, date_to=date_to)
    data = app.sx.marketing.seo_historical_rank_overview(**kw) if raw else app.sx.seo.historical_rank_overview(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="Rank history")


@seo.command("technologies")
@click.option("--target", required=True, help="Domain to analyze.")
@output_options
@pass_app
def technologies(app, target, fmt, raw, output):
    """Technology stack a domain runs on (CMS, analytics, marketing/SEO tooling).

    Output: TechStack — target, domain_rank, last_visited, country_iso_code, emails[],
    phone_numbers[], social_graph_urls[], technologies{category: {subcategory:
    [tech, ...]}}.
    """
    kw = dict(target=target)
    data = app.sx.marketing.seo_technologies(**kw) if raw else app.sx.seo.technologies(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="Tech stack")


@seo.command("bulk-traffic-estimation")
@click.option("--target", "targets", multiple=True, required=True, help="Domain to estimate, 1-1000 (repeatable).")
@click.option("--location-code", type=int, help="Numeric location code.")
@click.option("--language-code", help="Two-letter code.")
@click.option("--item-type", "item_types", multiple=True, help='SERP element type, e.g. "organic", "paid" (repeatable).')
@output_options
@pass_app
def bulk_traffic_estimation(app, targets, location_code, language_code, item_types, fmt, raw, output):
    """Traffic estimates for up to 1,000 domains in one call.

    Output: TrafficEstimate[] — target, organic (count, etv), paid.
    """
    kw = dict(targets=list(targets), location_code=location_code, language_code=language_code,
              item_types=list(item_types) or None)
    data = app.sx.marketing.seo_bulk_traffic_estimation(**kw) if raw else app.sx.seo.bulk_traffic_estimation(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="Traffic estimates")


@seo.command("relevant-pages")
@click.option("--target", required=True, help="Domain to analyze.")
@click.option("--location-code", type=int, help="Numeric location code.")
@click.option("--language-code", help="Two-letter code.")
@click.option("--limit", type=int, help="Default 100, max 1000.")
@click.option("--offset", type=int, help="Pagination offset.")
@click.option("--order-by", "order_by", multiple=True, help="e.g. metrics.organic.etv,desc (repeatable).")
@click.option("--filters", help="Upstream filter expression (JSON or raw string).")
@output_options
@pass_app
def relevant_pages(app, target, location_code, language_code, limit, offset, order_by, filters, fmt, raw, output):
    """A domain's top pages by organic traffic.

    Output: RelevantPage[] — page_address, organic (TrafficMetrics: count, etv,
    paid_traffic_cost, pos_1, pos_2_3, pos_4_10, pos_11_plus, is_*), paid.
    """
    kw = dict(target=target, location_code=location_code, language_code=language_code,
              limit=limit, offset=offset, order_by=list(order_by) or None, filters=parse_filters(filters))
    data = app.sx.marketing.seo_relevant_pages(**kw) if raw else app.sx.seo.relevant_pages(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="Relevant pages")


@seo.command("lighthouse")
@click.option("--url", required=True, help="Page to audit; must be http/https.")
@click.option("--strategy", type=click.Choice(["mobile", "desktop"]), help='"mobile" (default) or "desktop".')
@click.option("--locale", help='BCP-47 locale, e.g. "en-US".')
@output_options
@pass_app
def lighthouse(app, url, strategy, locale, fmt, raw, output):
    """Lighthouse technical-health audit of a single URL (~10-30s, up to ~90s).

    Scores are 0.0-1.0 (x100 to display). Only url, strategy, and core_web_vitals are
    guaranteed; field_data (CrUX real-user data) is absent for low-traffic sites.

    Output: LighthouseReport — url, strategy, analysis_utc_timestamp,
    lighthouse_version, performance_score, accessibility_score, seo_score,
    best_practices_score; core_web_vitals (lab: largest_contentful_paint_ms,
    first_contentful_paint_ms, cumulative_layout_shift, total_blocking_time_ms,
    speed_index_ms, time_to_interactive_ms, server_response_time_ms); field_data
    {url_metrics, origin_metrics} where each is CruxMetrics (overall_category +
    per-metric {percentile, category}); opportunities[] (id, title, description,
    score, display_value, estimated_savings_ms{lcp,fcp}, offenders[]); diagnostics[]
    (id, title, score, numeric_value, numeric_unit); third_parties[] (entity,
    transfer_size_bytes, main_thread_time_ms).
    """
    kw = dict(url=url, strategy=strategy, locale=locale)
    data = app.sx.marketing.seo_lighthouse(**kw) if raw else app.sx.seo.lighthouse(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="Lighthouse")
