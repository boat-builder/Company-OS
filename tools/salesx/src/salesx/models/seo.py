"""SEO canonical models.

SEO is the core of Berlin's pitch, so these flatten the upstream's deeply-nested
DataForSEO-style forms into flat, predictable records. Built from real captured
responses, except LighthouseReport — modeled from the backend's published contract
(the live endpoint still 502s pending a backend deploy, so it's not yet verified live).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

from .base import Model


@dataclass
class RankedKeyword(Model):
    """A keyword a domain ranks for (from `seo ranked-keywords`)."""

    keyword: Optional[str] = None
    search_volume: Optional[int] = None
    cpc: Optional[float] = None
    competition: Optional[float] = None
    competition_level: Optional[str] = None  # LOW | MEDIUM | HIGH
    rank: Optional[int] = None            # absolute SERP position
    rank_group: Optional[int] = None
    url: Optional[str] = None             # the ranking page on the target
    domain: Optional[str] = None          # host of the ranking page
    title: Optional[str] = None           # SERP result title
    intent: Optional[str] = None          # main search intent (informational/commercial/...)
    etv: Optional[float] = None           # estimated traffic value for this keyword


@dataclass
class KeywordIdea(Model):
    """A keyword semantically related to seeds (from `seo keyword-ideas`)."""

    keyword: Optional[str] = None
    search_volume: Optional[int] = None
    cpc: Optional[float] = None
    competition: Optional[float] = None
    competition_level: Optional[str] = None  # LOW | MEDIUM | HIGH
    difficulty: Optional[int] = None      # keyword_properties.keyword_difficulty


@dataclass
class TrafficMetrics(Model):
    """Organic/paid traffic counts, value, and movement for a slice.

    `pos_*` rank buckets are present on the time-series / per-page endpoints
    (historical-rank-overview, relevant-pages) and absent on domain-overview /
    bulk-traffic-estimation (so they're omitted there). `is_*` are period-over-period
    movement counts — momentum signals.
    """

    count: Optional[int] = None
    etv: Optional[float] = None           # estimated traffic value
    paid_traffic_cost: Optional[float] = None  # estimated_paid_traffic_cost (ad-spend equivalent)
    pos_1: Optional[int] = None
    pos_2_3: Optional[int] = None
    pos_4_10: Optional[int] = None
    pos_11_plus: Optional[int] = None
    is_new: Optional[int] = None
    is_up: Optional[int] = None
    is_down: Optional[int] = None
    is_lost: Optional[int] = None


@dataclass
class DomainOverview(Model):
    """Ranking + traffic snapshot for a domain (from `seo domain-overview`)."""

    target: Optional[str] = None
    organic: Optional[TrafficMetrics] = None
    paid: Optional[TrafficMetrics] = None


@dataclass
class RankHistoryPoint(Model):
    """One month in a domain's ranking/traffic time series."""

    year: Optional[int] = None
    month: Optional[int] = None
    organic: Optional[TrafficMetrics] = None
    paid: Optional[TrafficMetrics] = None


@dataclass
class TechStack(Model):
    """Technology stack a domain runs on (from `seo technologies`)."""

    target: Optional[str] = None
    domain_rank: Optional[int] = None
    last_visited: Optional[str] = None
    country_iso_code: Optional[str] = None
    emails: list[str] = field(default_factory=list)
    phone_numbers: list[str] = field(default_factory=list)
    social_graph_urls: list[str] = field(default_factory=list)
    # category -> subcategory -> [tech, ...], passed through (structure is upstream's)
    technologies: dict[str, Any] = field(default_factory=dict)


@dataclass
class TrafficEstimate(Model):
    """Traffic estimate for one domain (from `seo bulk-traffic-estimation`)."""

    target: Optional[str] = None
    organic: Optional[TrafficMetrics] = None
    paid: Optional[TrafficMetrics] = None


@dataclass
class RelevantPage(Model):
    """A top page by organic traffic (from `seo relevant-pages`)."""

    page_address: Optional[str] = None
    organic: Optional[TrafficMetrics] = None
    paid: Optional[TrafficMetrics] = None


@dataclass
class CoreWebVitals(Model):
    """Lab metrics from the Lighthouse run (the response's `core_web_vitals`).

    All fields are individually optional (omitted when not measured). Note INP is a
    field-only metric and lives under field_data, not here.
    """

    largest_contentful_paint_ms: Optional[float] = None
    first_contentful_paint_ms: Optional[float] = None
    cumulative_layout_shift: Optional[float] = None
    total_blocking_time_ms: Optional[float] = None
    speed_index_ms: Optional[float] = None
    time_to_interactive_ms: Optional[float] = None
    server_response_time_ms: Optional[float] = None


@dataclass
class CruxMetric(Model):
    """A single CrUX real-user metric: a percentile and its bucket."""

    percentile: Optional[float] = None
    category: Optional[str] = None        # FAST | AVERAGE | SLOW


@dataclass
class CruxMetrics(Model):
    """CrUX field metrics for a URL or origin (real-user data)."""

    overall_category: Optional[str] = None
    largest_contentful_paint_ms: Optional[CruxMetric] = None
    first_contentful_paint_ms: Optional[CruxMetric] = None
    cumulative_layout_shift: Optional[CruxMetric] = None
    interaction_to_next_paint_ms: Optional[CruxMetric] = None
    time_to_first_byte_ms: Optional[CruxMetric] = None


@dataclass
class FieldData(Model):
    """CrUX real-user data — absent entirely for low-traffic sites (normal)."""

    url_metrics: Optional[CruxMetrics] = None
    origin_metrics: Optional[CruxMetrics] = None


@dataclass
class LighthouseSavings(Model):
    lcp: Optional[float] = None           # estimated LCP savings, ms
    fcp: Optional[float] = None           # estimated FCP savings, ms


@dataclass
class LighthouseOffender(Model):
    url: Optional[str] = None
    wasted_bytes: Optional[int] = None
    wasted_ms: Optional[float] = None
    total_bytes: Optional[int] = None


@dataclass
class LighthouseOpportunity(Model):
    """An actionable fix with estimated savings (`opportunities`)."""

    id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    score: Optional[float] = None
    display_value: Optional[str] = None
    estimated_savings_ms: Optional[LighthouseSavings] = None
    offenders: list[LighthouseOffender] = field(default_factory=list)


@dataclass
class LighthouseDiagnostic(Model):
    """An issue without a precise savings number (`diagnostics`)."""

    id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    score: Optional[float] = None
    display_value: Optional[str] = None
    numeric_value: Optional[float] = None
    numeric_unit: Optional[str] = None


@dataclass
class ThirdParty(Model):
    """Per-entity third-party resource rollup (`third_parties`)."""

    entity: Optional[str] = None
    transfer_size_bytes: Optional[int] = None
    main_thread_time_ms: Optional[float] = None


@dataclass
class LighthouseReport(Model):
    """Lighthouse technical-health audit of a URL (from `seo lighthouse`).

    Only url, strategy, and the core_web_vitals container are guaranteed; everything
    else is omitted when not measured. Scores are 0.0-1.0 (multiply by 100 to display).
    """

    url: Optional[str] = None
    strategy: Optional[str] = None        # "mobile" | "desktop"
    analysis_utc_timestamp: Optional[str] = None
    lighthouse_version: Optional[str] = None
    performance_score: Optional[float] = None      # 0.0-1.0
    accessibility_score: Optional[float] = None
    seo_score: Optional[float] = None
    best_practices_score: Optional[float] = None
    core_web_vitals: Optional[CoreWebVitals] = None
    field_data: Optional[FieldData] = None
    opportunities: list[LighthouseOpportunity] = field(default_factory=list)
    diagnostics: list[LighthouseDiagnostic] = field(default_factory=list)
    third_parties: list[ThirdParty] = field(default_factory=list)
