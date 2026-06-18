"""Offline smoke test for salesx normalizers, models, and the SDK wiring.

No network. Fixtures mirror the *real* provider responses captured live (LinkedIn/X/
Google/ChatGPT) and the documented shapes (SEO). Run with:

    uv run python tests/smoke.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import salesx  # noqa: E402
from salesx import Salesx  # noqa: E402
from salesx.normalize import close as nc  # noqa: E402
from salesx.normalize import marketing as nm  # noqa: E402

_passed = 0


def check(label, cond):
    global _passed
    if not cond:
        raise AssertionError(f"FAILED: {label}")
    _passed += 1


# --- LinkedIn (real shapes) --------------------------------------------------

li_profile = {"count": 1, "records": [{
    "id": "satyanadella", "name": "Satya Nadella", "first_name": "Satya", "last_name": "Nadella",
    "position": "Chairman and CEO at Microsoft", "about": "As chairman and CEO...",
    "current_company": {"name": "Microsoft", "title": "Chairman and CEO", "company_id": "microsoft"},
    "current_company_name": "Microsoft", "location": "Redmond", "city": "Redmond, Washington, United States",
    "country_code": "US", "followers": 12027690, "connections": 500, "influencer": True,
    "input_url": "https://www.linkedin.com/in/satyanadella/", "url": "https://sa.linkedin.com/in/satyanadella",
    "avatar": "https://media.licdn.com/x.jpg",
    "experience": [{"company": "Microsoft", "company_id": "microsoft", "title": "Chairman and CEO",
                    "location": "Greater Seattle Area", "start_date": "Feb 2014", "end_date": "Present",
                    "url": "https://www.linkedin.com/company/microsoft"}],
    "education": [{"title": "The University of Chicago Booth School of Business",
                   "start_year": "1994", "end_year": "1996", "url": "https://www.linkedin.com/school/x"}],
}]}
p = nm.linkedin_profiles(li_profile)[0]
check("li headline from position", p.headline == "Chairman and CEO at Microsoft")
check("li current_company", p.current_company == "Microsoft" and p.current_title == "Chairman and CEO")
check("li linkedin_url prefers input_url", p.linkedin_url == "https://www.linkedin.com/in/satyanadella/")
check("li experience", p.experience[0].company == "Microsoft" and p.experience[0].end_date == "Present")
check("li education institution", p.education[0].institution.startswith("The University of Chicago"))

li_company = {"records": [{
    "id": "anthropicresearch", "company_id": "74126343", "name": "Anthropic",
    "url": "https://www.linkedin.com/company/anthropicresearch", "website": "https://www.anthropic.com/",
    "website_simplified": "anthropic.com", "description": "Anthropic | ...", "industries": "Research Services",
    "company_size": "501-1,000 employees", "employees_in_linkedin": 4836, "organization_type": "Privately Held",
    "followers": 3810765, "logo": "https://x/logo.png", "crunchbase_url": "https://cb/anthropic",
    "funding": {"last_round_type": "Series E", "last_round_date": "2025", "last_round_raised": "$x", "rounds": 7},
    "investors": ["ICONIQ Capital", "Google"],
}]}
c = nm.linkedin_companies(li_company)[0]
check("li company domain", c.domain == "anthropic.com")
check("li company employee_count", c.employee_count == 4836)
check("li company funding", c.funding.rounds == 7 and c.funding.last_round_type == "Series E")
check("li company investors", c.investors == ["ICONIQ Capital", "Google"])

li_job = {"count": 1, "records": [{
    "job_posting_id": "4427764320", "job_title": "AI/ML Software Engineer", "company_name": "iTradeNetwork, Inc.",
    "company_id": "43580", "company_url": "https://www.linkedin.com/company/itradenetwork",
    "job_location": "San Francisco Bay Area", "country_code": "US", "job_employment_type": "Full-time",
    "job_function": "Engineering and Information Technology", "job_industries": "Software Development",
    "job_seniority_level": "Entry level", "job_posted_date": "2026-06-17T07:51:33.966Z",
    "job_posted_time": "1 day ago", "job_num_applicants": 0, "is_easy_apply": False,
    "job_summary": "ABOUT ITRADENETWORK...", "url": "https://www.linkedin.com/jobs/view/x",
}]}
j = nm.linkedin_jobs(li_job)[0]
check("li job title", j.title == "AI/ML Software Engineer")
check("li job seniority", j.seniority == "Entry level" and j.posted_ago == "1 day ago")

li_post = {"records": [{
    "id": "7470128813885018112", "url": "https://www.linkedin.com/posts/microsoft_x", "post_type": "post",
    "title": "A Formula 1 win...", "headline": "A Formula 1 win...", "post_text": "A Formula 1 win looks like...",
    "date_posted": "2026-06-09T15:04:57.493Z", "num_likes": 1068, "num_comments": 24,
    "user_name": "Microsoft", "user_id": "microsoft", "use_url": "https://www.linkedin.com/company/microsoft",
    "user_followers": 28384143, "hashtags": None, "embedded_links": ["https://msft.it/x"], "video_duration": 32,
}]}
lp = nm.linkedin_posts(li_post)[0]
check("li post likes/comments", lp.likes == 1068 and lp.comments == 24)
check("li post author", lp.author_name == "Microsoft" and lp.author_followers == 28384143)
check("li post hashtags none->[]", lp.hashtags == [] and lp.embedded_links == ["https://msft.it/x"])

# --- X (real shapes) ---------------------------------------------------------

x_profile = {"records": [{
    "id": "4398626122", "x_id": "4398626122", "profile_name": "OpenAI", "url": "https://x.com/openai",
    "biography": "OpenAI's mission...", "location": None, "followers": 4936973, "following": 4,
    "posts_count": 1911, "is_verified": False, "is_business_account": False, "is_government_account": False,
    "date_joined": "2015-12-06T22:51:08.930Z", "profile_image_link": "https://pbs/x.jpg",
}]}
xp = nm.x_profiles(x_profile)[0]
check("x profile name", xp.name == "OpenAI" and xp.id == "4398626122")
check("x profile metrics", xp.followers == 4936973 and xp.posts_count == 1911)

x_post = {"records": [{
    "id": "2001391954014462023", "url": "https://x.com/OpenAI/status/2001391954014462023",
    "description": "That's why we're building...", "user_posted": "OpenAI", "user_id": "4398626122",
    "date_posted": "2025-12-17T20:40:00.000Z", "likes": 484, "replies": 25, "reposts": 27, "quotes": 3,
    "bookmarks": 34, "views": 119122, "is_repost": False, "is_verified": True, "hashtags": None,
}]}
xpost = nm.x_posts(x_post)[0]
check("x post author/engagement", xpost.author == "OpenAI" and xpost.views == 119122 and xpost.quotes == 3)
check("x post bookmarks", xpost.bookmarks == 34 and xpost.is_verified is True)

# --- Search (real shapes) ----------------------------------------------------

gs = nm.google_search({"query": "ai seo platform", "engine": "google", "search_type": "web", "total": 9,
                       "total_results": 118, "results": [{"title": "T", "url": "https://r.com",
                       "snippet": "s", "displayed_link": "r.com › blog"}], "features": {"related_searches": []}})
check("google total vs total_results", gs.total == 9 and gs.total_results == 118)
check("google hit displayed_link + position", gs.results[0].displayed_link == "r.com › blog" and gs.results[0].position == 1)

ai = nm.google_ai_mode({"query": "what is aeo", "markdown": "# AEO",
                        "references": [{"index": 0, "title": "R", "link": "https://ref.com", "source": "Reddit", "snippet": "x"}]})
check("ai answer + citation", ai.answer == "# AEO" and ai.citations[0].url == "https://ref.com" and ai.engine == "google-ai-mode")

gpt = nm.chatgpt_search({"id": "resp_x", "model": "gpt-5.4-mini-2026-03-17", "content": "Anthropic is...",
                        "citations": [{"url": "https://a.com", "title": "Company", "text": "t"}],
                        "usage": {"input_tokens": 8527, "output_tokens": 186, "total_tokens": 8713}})
check("chatgpt content/model", gpt.answer == "Anthropic is..." and gpt.model == "gpt-5.4-mini-2026-03-17")
check("chatgpt usage", gpt.usage["total_tokens"] == 8713)
check("chatgpt citation snippet from text", gpt.citations[0].snippet == "t")

# --- SEO (real shapes; lighthouse documented) --------------------------------

# domain-overview: metrics carry count/etv/cost/movement but NO pos_* buckets.
ov = nm.domain_overview({"target": "anthropic.com", "items": [{"metrics": {"organic": {
    "count": 60150, "etv": 1652993.1, "estimated_paid_traffic_cost": 11462924.4,
    "is_new": 51763, "is_up": 3611, "is_down": 3303, "is_lost": 86751}}}]})
check("seo overview count/etv", ov.organic.count == 60150 and round(ov.organic.etv) == 1652993)
check("seo overview cost+movement", ov.organic.paid_traffic_cost is not None and ov.organic.is_lost == 86751)
check("seo overview pos_* omitted here", ov.organic.pos_1 is None and ov.organic.pos_11_plus is None)

# historical / relevant-pages: metrics DO carry pos_* buckets.
hist = nm.historical_rank_overview({"items": [{"year": 2026, "month": 6, "metrics": {"organic": {
    "pos_1": 1710, "pos_2_3": 1720, "pos_4_10": 3056, "pos_11_20": 5077, "pos_21_30": 7026,
    "pos_31_40": 7472, "pos_41_50": 6916, "pos_51_60": 6754, "pos_61_70": 6327, "pos_71_80": 5803,
    "pos_81_90": 5078, "pos_91_100": 3211, "etv": 1652993.1, "count": 60150, "is_lost": 86751}}}]})
check("seo historical pos_11_plus sums beyond-10",
      hist[0].organic.pos_11_plus == 5077 + 7026 + 7472 + 6916 + 6754 + 6327 + 5803 + 5078 + 3211)
check("seo historical year/month", hist[0].year == 2026 and hist[0].month == 6)

rk = nm.ranked_keywords({"items": [{
    "keyword_data": {"keyword": "2026 agentic coding trends report",
        "keyword_info": {"search_volume": 70, "cpc": 17.66, "competition": 0.6, "competition_level": "MEDIUM"},
        "search_intent_info": {"main_intent": "commercial"}},
    "ranked_serp_element": {"serp_item": {"rank_absolute": 1, "rank_group": 1,
        "domain": "resources.anthropic.com", "url": "https://resources.anthropic.com/x",
        "title": "2026 Agentic Coding Trends Report", "etv": 21.28}}}]})
check("seo ranked core", rk[0].rank == 1 and rk[0].search_volume == 70)
check("seo ranked enriched", rk[0].competition_level == "MEDIUM" and rk[0].domain == "resources.anthropic.com"
      and rk[0].title.startswith("2026 Agentic") and rk[0].intent == "commercial")

ideas = nm.keyword_ideas({"items": [{"keyword": "kling ai",
    "keyword_info": {"search_volume": 135000, "competition_level": "MEDIUM", "competition": 0.58, "cpc": 4.07},
    "keyword_properties": {"keyword_difficulty": 34}}]})
check("seo ideas enriched", ideas[0].difficulty == 34 and ideas[0].competition_level == "MEDIUM")

tech = nm.technologies({"target": "anthropic.com", "domain_rank": 617, "country_iso_code": "US",
    "emails": None, "phone_numbers": None, "social_graph_urls": ["https://twitter.com/AnthropicAI"],
    "technologies": {"content": {"cms": ["Sanity"]}}})
check("seo tech enriched", tech.domain_rank == 617 and tech.country_iso_code == "US"
      and tech.social_graph_urls == ["https://twitter.com/AnthropicAI"] and tech.emails == [])

bulk = nm.bulk_traffic_estimation({"items": [{"target": "openai.com",
    "metrics": {"organic": {"etv": 37184463.1, "count": 177553}}}]})
check("seo bulk", bulk[0].target == "openai.com" and bulk[0].organic.count == 177553)

pages = nm.relevant_pages({"items": [{"page_address": "https://www.anthropic.com/news/x",
    "metrics": {"organic": {"pos_1": 19, "pos_11_20": 307, "pos_21_30": 434, "etv": 22983.1, "count": 3386}}}]})
check("seo pages pos_11_plus", pages[0].page_address.endswith("/news/x") and pages[0].organic.pos_11_plus == 307 + 434)

lh = nm.lighthouse({
    "url": "https://example.com", "strategy": "mobile",
    "analysis_utc_timestamp": "2026-06-18T08:30:00.000Z", "lighthouse_version": "12.0.0",
    "performance_score": 1, "accessibility_score": 0.96, "seo_score": 0.8, "best_practices_score": 0.96,
    "core_web_vitals": {"largest_contentful_paint_ms": 1200.5, "total_blocking_time_ms": 0,
                        "speed_index_ms": 1100.2, "server_response_time_ms": 40.3},
    "field_data": {"url_metrics": {"overall_category": "FAST",
        "interaction_to_next_paint_ms": {"percentile": 180, "category": "FAST"},
        "largest_contentful_paint_ms": {"percentile": 2100, "category": "AVERAGE"}}},
    "opportunities": [{"id": "render-blocking-resources", "title": "Eliminate render-blocking",
        "score": 0.5, "display_value": "Potential savings of 300 ms",
        "estimated_savings_ms": {"lcp": 300, "fcp": 150},
        "offenders": [{"url": "https://x/app.css", "wasted_bytes": 12000, "wasted_ms": 200, "total_bytes": 30000}]}],
    "diagnostics": [{"id": "is-crawlable", "title": "Blocked from indexing", "numeric_value": 811, "numeric_unit": "element"}],
    "third_parties": [{"entity": "Google Fonts", "transfer_size_bytes": 45000, "main_thread_time_ms": 12.4}],
})
check("lh scores 0-1", lh.performance_score == 1 and lh.seo_score == 0.8)
check("lh lab metrics", lh.core_web_vitals.speed_index_ms == 1100.2 and lh.core_web_vitals.server_response_time_ms == 40.3)
check("lh crux INP nested", lh.field_data.url_metrics.interaction_to_next_paint_ms.percentile == 180
      and lh.field_data.url_metrics.interaction_to_next_paint_ms.category == "FAST")
check("lh crux overall", lh.field_data.url_metrics.overall_category == "FAST")
check("lh opportunity", lh.opportunities[0].estimated_savings_ms.lcp == 300
      and lh.opportunities[0].offenders[0].wasted_bytes == 12000)
check("lh diagnostics", lh.diagnostics[0].numeric_value == 811 and lh.diagnostics[0].numeric_unit == "element")
check("lh third_parties", lh.third_parties[0].entity == "Google Fonts" and lh.third_parties[0].transfer_size_bytes == 45000)

# Low-traffic site: field_data omitted entirely — must stay None, not crash.
lh2 = nm.lighthouse({"url": "https://small.com", "strategy": "desktop", "performance_score": 0.7,
                     "core_web_vitals": {"largest_contentful_paint_ms": 2000}})
check("lh field_data absent -> None", lh2.field_data is None and lh2.opportunities == [])

# --- Close CRM ---------------------------------------------------------------

lead = nc.lead({"id": "lead_1", "display_name": "Acme", "url": "https://acme.com", "status_label": "Potential",
                "contacts": [{"id": "c1", "name": "Jane", "emails": [{"email": "jane@acme.com"}], "urls": [{"url": "https://li/j"}]}]})
check("crm lead name from display_name", lead.name == "Acme")
check("crm contact email", lead.contacts[0].emails == ["jane@acme.com"])
note = nc.note({"id": "n1", "lead_id": "lead_1", "note_html": "<p>Great <b>call</b></p>", "date_created": "2026-01-01"})
check("crm note html stripped", note.text == "Great call")
user = nc.user({"id": "u1", "first_name": "Sherin", "last_name": "Thomas", "email": "s@hey.com"})
check("crm user name joined", user.name == "Sherin Thomas")

# --- Serialization + SDK wiring ----------------------------------------------

d = p.to_dict()
check("to_dict drops None", "x_url" not in d and "headline" in d)
check("to_dict nests experience", d["experience"][0]["company"] == "Microsoft")
check("Salesx exported", salesx.Salesx is Salesx)
# Salesx builds without credentials (lazy); sub-client access is what validates.
sx = Salesx.__new__(Salesx)
check("sdk clients exist", hasattr(Salesx, "linkedin") and hasattr(Salesx, "seo") and hasattr(Salesx, "crm"))

print(f"OK — {_passed} checks passed.")
