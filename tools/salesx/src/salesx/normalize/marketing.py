"""Normalize Marketing-backend responses into canonical models.

All mappings were built from real captured responses, except lighthouse — it's built
to the backend's published contract and validated against contract-shaped fixtures,
but the live endpoint still returns 502 pending a backend deploy, so it's not yet
verified end-to-end. The hidden `--raw` flag / raw transport always exposes the full
provider payload if a field isn't surfaced here.
"""

from __future__ import annotations

from typing import Any

from ..models import (
    AnswerResult,
    Citation,
    CoreWebVitals,
    CruxMetric,
    CruxMetrics,
    DomainOverview,
    FieldData,
    KeywordIdea,
    LighthouseDiagnostic,
    LighthouseOffender,
    LighthouseOpportunity,
    LighthouseReport,
    LighthouseSavings,
    LinkedInCompany,
    LinkedInEducation,
    LinkedInExperience,
    LinkedInFunding,
    LinkedInJob,
    LinkedInPost,
    LinkedInProfile,
    RankHistoryPoint,
    RankedKeyword,
    RelevantPage,
    SearchHit,
    SearchResults,
    TechStack,
    ThirdParty,
    TrafficEstimate,
    TrafficMetrics,
    XPost,
    XProfile,
)
from .helpers import as_float, as_int, as_list, domain_of, pick

_POS_BEYOND_10 = (
    "pos_11_20", "pos_21_30", "pos_31_40", "pos_41_50", "pos_51_60",
    "pos_61_70", "pos_71_80", "pos_81_90", "pos_91_100",
)


def _records(resp: Any) -> list:
    """Pull records[] out of a RecordsResponse {count, error_count, duration_ms, records[]}."""
    if isinstance(resp, list):
        return resp
    if isinstance(resp, dict):
        return [r for r in as_list(resp.get("records")) if isinstance(r, dict)]
    return []


# =============================================================================
# LinkedIn
# =============================================================================

def linkedin_profiles(resp: Any) -> list[LinkedInProfile]:
    out = []
    for r in _records(resp):
        cc = r.get("current_company") or {}
        exp = [
            LinkedInExperience(
                company=pick(e, "company"), company_id=pick(e, "company_id"),
                title=pick(e, "title"), location=pick(e, "location"),
                start_date=pick(e, "start_date"), end_date=pick(e, "end_date"),
                url=pick(e, "url"),
            )
            for e in as_list(r.get("experience")) if isinstance(e, dict)
        ]
        edu = [
            LinkedInEducation(
                institution=pick(e, "title", "institute"),
                start_year=pick(e, "start_year"), end_year=pick(e, "end_year"),
                url=pick(e, "url"),
            )
            for e in as_list(r.get("education")) if isinstance(e, dict)
        ]
        out.append(LinkedInProfile(
            id=pick(r, "id", "linkedin_id"),
            name=pick(r, "name"),
            first_name=pick(r, "first_name"),
            last_name=pick(r, "last_name"),
            headline=pick(r, "position", "headline"),
            about=pick(r, "about"),
            current_company=pick(cc, "name") or pick(r, "current_company_name"),
            current_title=pick(cc, "title"),
            location=pick(r, "location"),
            city=pick(r, "city"),
            country_code=pick(r, "country_code"),
            followers=as_int(pick(r, "followers")),
            connections=as_int(pick(r, "connections")),
            influencer=pick(r, "influencer"),
            linkedin_url=pick(r, "input_url", "url"),
            avatar_url=pick(r, "avatar"),
            experience=exp,
            education=edu,
        ))
    return out


def linkedin_companies(resp: Any) -> list[LinkedInCompany]:
    out = []
    for r in _records(resp):
        f = r.get("funding") or {}
        funding = LinkedInFunding(
            last_round_type=pick(f, "last_round_type"),
            last_round_date=pick(f, "last_round_date"),
            last_round_raised=pick(f, "last_round_raised"),
            rounds=as_int(pick(f, "rounds")),
        ) if f else None
        out.append(LinkedInCompany(
            id=pick(r, "id"),
            company_id=pick(r, "company_id"),
            name=pick(r, "name"),
            linkedin_url=pick(r, "url"),
            website=pick(r, "website"),
            domain=pick(r, "website_simplified") or domain_of(pick(r, "website")),
            description=pick(r, "description"),
            about=pick(r, "about", "unformatted_about"),
            slogan=pick(r, "slogan"),
            industries=pick(r, "industries"),
            company_size=pick(r, "company_size"),
            employee_count=as_int(pick(r, "employees_in_linkedin")),
            organization_type=pick(r, "organization_type"),
            followers=as_int(pick(r, "followers")),
            logo_url=pick(r, "logo", "image"),
            crunchbase_url=pick(r, "crunchbase_url"),
            funding=funding,
            investors=[i for i in as_list(r.get("investors")) if isinstance(i, str)],
        ))
    return out


def linkedin_jobs(resp: Any) -> list[LinkedInJob]:
    out = []
    for r in _records(resp):
        out.append(LinkedInJob(
            id=pick(r, "job_posting_id"),
            title=pick(r, "job_title"),
            company=pick(r, "company_name"),
            company_id=pick(r, "company_id"),
            company_url=pick(r, "company_url"),
            location=pick(r, "job_location"),
            country_code=pick(r, "country_code"),
            employment_type=pick(r, "job_employment_type"),
            function=pick(r, "job_function"),
            industries=pick(r, "job_industries"),
            seniority=pick(r, "job_seniority_level"),
            posted_date=pick(r, "job_posted_date"),
            posted_ago=pick(r, "job_posted_time"),
            applicants=as_int(pick(r, "job_num_applicants")),
            is_easy_apply=pick(r, "is_easy_apply"),
            base_salary=pick(r, "base_salary"),
            summary=pick(r, "job_summary"),
            url=pick(r, "url"),
        ))
    return out


def linkedin_posts(resp: Any) -> list[LinkedInPost]:
    out = []
    for r in _records(resp):
        out.append(LinkedInPost(
            id=pick(r, "id"),
            url=pick(r, "url"),
            post_type=pick(r, "post_type"),
            title=pick(r, "title", "headline"),
            text=pick(r, "post_text", "original_post_text"),
            date_posted=pick(r, "date_posted"),
            likes=as_int(pick(r, "num_likes")),
            comments=as_int(pick(r, "num_comments")),
            author_name=pick(r, "user_name"),
            author_id=pick(r, "user_id"),
            author_url=pick(r, "use_url"),
            author_followers=as_int(pick(r, "user_followers")),
            hashtags=as_list(r.get("hashtags")),
            embedded_links=as_list(r.get("embedded_links")),
            video_duration=as_int(pick(r, "video_duration")),
        ))
    return out


# =============================================================================
# X (Twitter)
# =============================================================================

def x_profiles(resp: Any) -> list[XProfile]:
    out = []
    for r in _records(resp):
        out.append(XProfile(
            id=pick(r, "id", "x_id"),
            name=pick(r, "profile_name", "name"),
            url=pick(r, "url"),
            biography=pick(r, "biography"),
            location=pick(r, "location"),
            followers=as_int(pick(r, "followers")),
            following=as_int(pick(r, "following")),
            posts_count=as_int(pick(r, "posts_count")),
            is_verified=pick(r, "is_verified"),
            is_business_account=pick(r, "is_business_account"),
            is_government_account=pick(r, "is_government_account"),
            date_joined=pick(r, "date_joined"),
            external_link=pick(r, "external_link"),
            category=pick(r, "category_name"),
            profile_image=pick(r, "profile_image_link"),
        ))
    return out


def x_posts(resp: Any) -> list[XPost]:
    out = []
    for r in _records(resp):
        out.append(XPost(
            id=pick(r, "id"),
            url=pick(r, "url"),
            text=pick(r, "description"),
            author=pick(r, "user_posted", "name"),
            author_id=pick(r, "user_id"),
            date_posted=pick(r, "date_posted"),
            likes=as_int(pick(r, "likes")),
            replies=as_int(pick(r, "replies")),
            reposts=as_int(pick(r, "reposts")),
            quotes=as_int(pick(r, "quotes")),
            bookmarks=as_int(pick(r, "bookmarks")),
            views=as_int(pick(r, "views")),
            is_repost=pick(r, "is_repost"),
            is_verified=pick(r, "is_verified"),
            hashtags=as_list(r.get("hashtags")),
            photos=as_list(r.get("photos")),
            videos=as_list(r.get("videos")),
            external_url=pick(r, "external_url"),
        ))
    return out


# =============================================================================
# Search & answers
# =============================================================================

def google_search(resp: Any) -> SearchResults:
    if not isinstance(resp, dict):
        return SearchResults()
    hits = []
    for i, r in enumerate(as_list(resp.get("results"))):
        if not isinstance(r, dict):
            continue
        hits.append(SearchHit(
            title=pick(r, "title"),
            url=pick(r, "url", "link"),
            snippet=pick(r, "snippet", "description"),
            displayed_link=pick(r, "displayed_link"),
            position=as_int(pick(r, "position", "rank")) or (i + 1),
        ))
    return SearchResults(
        query=pick(resp, "query"),
        engine=pick(resp, "engine") or "google",
        search_type=pick(resp, "search_type"),
        results=hits,
        total=as_int(resp.get("total")),
        total_results=as_int(resp.get("total_results")),
        features=resp.get("features") or {},
    )


def google_ai_mode(resp: Any) -> AnswerResult:
    if not isinstance(resp, dict):
        return AnswerResult()
    citations = [
        Citation(title=pick(r, "title"), url=pick(r, "link", "url"),
                 source=pick(r, "source"), snippet=pick(r, "snippet"))
        for r in as_list(resp.get("references")) if isinstance(r, dict)
    ]
    return AnswerResult(
        query=pick(resp, "query"),
        engine="google-ai-mode",
        answer=pick(resp, "markdown", "text"),
        citations=citations,
    )


def chatgpt_search(resp: Any) -> AnswerResult:
    """Note: response has no `query` field — the SDK injects it from the request."""
    if not isinstance(resp, dict):
        return AnswerResult()
    citations = [
        Citation(title=pick(r, "title"), url=pick(r, "url", "link"),
                 snippet=pick(r, "text", "snippet"))
        for r in as_list(resp.get("citations")) if isinstance(r, dict)
    ]
    return AnswerResult(
        query=pick(resp, "query"),
        engine="chatgpt",
        model=pick(resp, "model"),
        answer=pick(resp, "content", "answer"),
        citations=citations,
        usage=resp.get("usage") or {},
    )


# =============================================================================
# SEO  (verified live, except lighthouse — see module docstring)
# =============================================================================

def _traffic_metrics(m: Any) -> TrafficMetrics | None:
    if not isinstance(m, dict):
        return None
    beyond = [as_int(m.get(k)) for k in _POS_BEYOND_10 if m.get(k) is not None]
    pos_11_plus = sum(v for v in beyond if v is not None) if beyond else None
    return TrafficMetrics(
        count=as_int(m.get("count")), etv=as_float(m.get("etv")),
        paid_traffic_cost=as_float(m.get("estimated_paid_traffic_cost")),
        pos_1=as_int(m.get("pos_1")), pos_2_3=as_int(m.get("pos_2_3")),
        pos_4_10=as_int(m.get("pos_4_10")), pos_11_plus=pos_11_plus,
        is_new=as_int(m.get("is_new")), is_up=as_int(m.get("is_up")),
        is_down=as_int(m.get("is_down")), is_lost=as_int(m.get("is_lost")),
    )


def ranked_keywords(resp: Any) -> list[RankedKeyword]:
    out = []
    for item in as_list((resp or {}).get("items")):
        if not isinstance(item, dict):
            continue
        kd = item.get("keyword_data") or {}
        ki = kd.get("keyword_info") or {}
        intent = (kd.get("search_intent_info") or {}).get("main_intent")
        rse = item.get("ranked_serp_element") or {}
        serp = rse.get("serp_item") if isinstance(rse.get("serp_item"), dict) else rse
        serp = serp if isinstance(serp, dict) else {}
        out.append(RankedKeyword(
            keyword=pick(kd, "keyword"),
            search_volume=as_int(ki.get("search_volume")),
            cpc=as_float(ki.get("cpc")),
            competition=as_float(ki.get("competition")),
            competition_level=pick(ki, "competition_level"),
            rank=as_int(pick(serp, "rank_absolute")),
            rank_group=as_int(pick(serp, "rank_group")),
            url=pick(serp, "url"),
            domain=pick(serp, "domain"),
            title=pick(serp, "title"),
            intent=intent,
            etv=as_float(serp.get("etv")),
        ))
    return out


def keyword_ideas(resp: Any) -> list[KeywordIdea]:
    out = []
    for item in as_list((resp or {}).get("items")):
        if not isinstance(item, dict):
            continue
        ki = item.get("keyword_info") or {}
        kp = item.get("keyword_properties") or {}
        out.append(KeywordIdea(
            keyword=pick(item, "keyword"),
            search_volume=as_int(ki.get("search_volume")),
            cpc=as_float(ki.get("cpc")),
            competition=as_float(ki.get("competition")),
            competition_level=pick(ki, "competition_level"),
            difficulty=as_int(kp.get("keyword_difficulty")),
        ))
    return out


def domain_overview(resp: Any) -> DomainOverview:
    items = as_list((resp or {}).get("items"))
    metrics = (items[0].get("metrics") if items and isinstance(items[0], dict) else None) or {}
    return DomainOverview(
        target=pick(resp or {}, "target"),
        organic=_traffic_metrics(metrics.get("organic")),
        paid=_traffic_metrics(metrics.get("paid")),
    )


def historical_rank_overview(resp: Any) -> list[RankHistoryPoint]:
    out = []
    for item in as_list((resp or {}).get("items")):
        if not isinstance(item, dict):
            continue
        metrics = item.get("metrics") or {}
        out.append(RankHistoryPoint(
            year=as_int(item.get("year")), month=as_int(item.get("month")),
            organic=_traffic_metrics(metrics.get("organic")),
            paid=_traffic_metrics(metrics.get("paid")),
        ))
    return out


def technologies(resp: Any) -> TechStack:
    d = resp if isinstance(resp, dict) else {}
    return TechStack(
        target=pick(d, "target"),
        domain_rank=as_int(d.get("domain_rank")),
        last_visited=pick(d, "last_visited"),
        country_iso_code=pick(d, "country_iso_code"),
        emails=as_list(d.get("emails")),
        phone_numbers=as_list(d.get("phone_numbers")),
        social_graph_urls=as_list(d.get("social_graph_urls")),
        technologies=d.get("technologies") or {},
    )


def bulk_traffic_estimation(resp: Any) -> list[TrafficEstimate]:
    out = []
    for item in as_list((resp or {}).get("items")):
        if not isinstance(item, dict):
            continue
        metrics = item.get("metrics") or {}
        out.append(TrafficEstimate(
            target=pick(item, "target"),
            organic=_traffic_metrics(metrics.get("organic")),
            paid=_traffic_metrics(metrics.get("paid")),
        ))
    return out


def relevant_pages(resp: Any) -> list[RelevantPage]:
    out = []
    for item in as_list((resp or {}).get("items")):
        if not isinstance(item, dict):
            continue
        metrics = item.get("metrics") or {}
        out.append(RelevantPage(
            page_address=pick(item, "page_address", "page"),
            organic=_traffic_metrics(metrics.get("organic")),
            paid=_traffic_metrics(metrics.get("paid")),
        ))
    return out


def _crux_metric(m: Any) -> CruxMetric | None:
    if not isinstance(m, dict):
        return None
    return CruxMetric(percentile=as_float(m.get("percentile")), category=pick(m, "category"))


def _crux_metrics(m: Any) -> CruxMetrics | None:
    if not isinstance(m, dict):
        return None
    return CruxMetrics(
        overall_category=pick(m, "overall_category"),
        largest_contentful_paint_ms=_crux_metric(m.get("largest_contentful_paint_ms")),
        first_contentful_paint_ms=_crux_metric(m.get("first_contentful_paint_ms")),
        cumulative_layout_shift=_crux_metric(m.get("cumulative_layout_shift")),
        interaction_to_next_paint_ms=_crux_metric(m.get("interaction_to_next_paint_ms")),
        time_to_first_byte_ms=_crux_metric(m.get("time_to_first_byte_ms")),
    )


def lighthouse(resp: Any) -> LighthouseReport:
    d = resp if isinstance(resp, dict) else {}
    cwv = d.get("core_web_vitals") or {}

    field_data = None
    fd = d.get("field_data")
    if isinstance(fd, dict):
        field_data = FieldData(
            url_metrics=_crux_metrics(fd.get("url_metrics")),
            origin_metrics=_crux_metrics(fd.get("origin_metrics")),
        )

    opportunities = []
    for o in as_list(d.get("opportunities")):
        if not isinstance(o, dict):
            continue
        sav = o.get("estimated_savings_ms")
        opportunities.append(LighthouseOpportunity(
            id=pick(o, "id"), title=pick(o, "title"), description=pick(o, "description"),
            score=as_float(o.get("score")), display_value=pick(o, "display_value"),
            estimated_savings_ms=LighthouseSavings(
                lcp=as_float(sav.get("lcp")), fcp=as_float(sav.get("fcp")),
            ) if isinstance(sav, dict) else None,
            offenders=[
                LighthouseOffender(
                    url=pick(x, "url"), wasted_bytes=as_int(x.get("wasted_bytes")),
                    wasted_ms=as_float(x.get("wasted_ms")), total_bytes=as_int(x.get("total_bytes")),
                )
                for x in as_list(o.get("offenders")) if isinstance(x, dict)
            ],
        ))

    diagnostics = [
        LighthouseDiagnostic(
            id=pick(x, "id"), title=pick(x, "title"), description=pick(x, "description"),
            score=as_float(x.get("score")), display_value=pick(x, "display_value"),
            numeric_value=as_float(x.get("numeric_value")), numeric_unit=pick(x, "numeric_unit"),
        )
        for x in as_list(d.get("diagnostics")) if isinstance(x, dict)
    ]

    third_parties = [
        ThirdParty(
            entity=pick(x, "entity"), transfer_size_bytes=as_int(x.get("transfer_size_bytes")),
            main_thread_time_ms=as_float(x.get("main_thread_time_ms")),
        )
        for x in as_list(d.get("third_parties")) if isinstance(x, dict)
    ]

    return LighthouseReport(
        url=pick(d, "url"),
        strategy=pick(d, "strategy"),
        analysis_utc_timestamp=pick(d, "analysis_utc_timestamp"),
        lighthouse_version=pick(d, "lighthouse_version"),
        performance_score=as_float(d.get("performance_score")),
        accessibility_score=as_float(d.get("accessibility_score")),
        seo_score=as_float(d.get("seo_score")),
        best_practices_score=as_float(d.get("best_practices_score")),
        core_web_vitals=CoreWebVitals(
            largest_contentful_paint_ms=as_float(cwv.get("largest_contentful_paint_ms")),
            first_contentful_paint_ms=as_float(cwv.get("first_contentful_paint_ms")),
            cumulative_layout_shift=as_float(cwv.get("cumulative_layout_shift")),
            total_blocking_time_ms=as_float(cwv.get("total_blocking_time_ms")),
            speed_index_ms=as_float(cwv.get("speed_index_ms")),
            time_to_interactive_ms=as_float(cwv.get("time_to_interactive_ms")),
            server_response_time_ms=as_float(cwv.get("server_response_time_ms")),
        ),
        field_data=field_data,
        opportunities=opportunities,
        diagnostics=diagnostics,
        third_parties=third_parties,
    )
