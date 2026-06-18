"""`salesx linkedin ...` — public LinkedIn data."""

from __future__ import annotations

import click

from ..output import emit
from ._shared import output_options, pass_app, split_name


@click.group()
def linkedin() -> None:
    """Public LinkedIn profiles, companies, jobs, and posts."""


@linkedin.command("profiles")
@click.option("--url", "urls", multiple=True, help="Profile URL to fetch (repeatable).")
@click.option("--name", "names", multiple=True, help='Name to discover, e.g. "Satya Nadella" (repeatable).')
@click.option("--limit-per-input", type=int, help="Cap results per discovery input.")
@click.option("--wait-seconds", type=int, help="Server-side wait cap, 0-600.")
@output_options
@pass_app
def profiles(app, urls, names, limit_per_input, wait_seconds, fmt, raw, output):
    """Fetch people profiles by URL, or discover them by name.

    Output: LinkedInProfile[] — id, name, first_name, last_name, headline, about,
    current_company, current_title, location, city, country_code, followers,
    connections, influencer, linkedin_url, avatar_url, experience[] (company,
    title, location, start_date, end_date, url), education[] (institution,
    start_year, end_year, url).
    """
    name_objs = [split_name(n) for n in names] if names else None
    if not urls and not name_objs:
        raise click.UsageError("Provide --url or --name.")
    kw = dict(urls=list(urls) or None, names=name_objs,
              limit_per_input=limit_per_input, wait_seconds=wait_seconds)
    data = app.sx.marketing.linkedin_profiles(**kw) if raw else app.sx.linkedin.profiles(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="LinkedIn profiles")


@linkedin.command("companies")
@click.option("--url", "urls", multiple=True, required=True, help="Company page URL (repeatable).")
@click.option("--wait-seconds", type=int, help="Server-side wait cap, 0-600.")
@output_options
@pass_app
def companies(app, urls, wait_seconds, fmt, raw, output):
    """Fetch company pages by URL.

    Output: LinkedInCompany[] — id, company_id, name, linkedin_url, website,
    domain, description, about, slogan, industries, company_size, employee_count,
    organization_type, followers, logo_url, crunchbase_url, funding (last_round_type,
    last_round_date, last_round_raised, rounds), investors[].
    """
    kw = dict(urls=list(urls), wait_seconds=wait_seconds)
    data = app.sx.marketing.linkedin_companies(**kw) if raw else app.sx.linkedin.companies(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="LinkedIn companies")


@linkedin.command("jobs")
@click.option("--url", "urls", multiple=True, help="Job listing URL (repeatable).")
@click.option("--keyword", help="Search keyword (the only effectively-required search field).")
@click.option("--location", help="Search location, e.g. Berlin.")
@click.option("--country", help="Country filter.")
@click.option("--time-range", help="Time range filter.")
@click.option("--job-type", help="Job type filter.")
@click.option("--experience-level", help="Experience level filter.")
@click.option("--remote", help="Remote filter.")
@click.option("--company", help="Company filter.")
@click.option("--limit-per-input", type=int, help="Cap results per search.")
@click.option("--wait-seconds", type=int, help="Server-side wait cap, 0-600.")
@output_options
@pass_app
def jobs(app, urls, keyword, location, country, time_range, job_type, experience_level,
         remote, company, limit_per_input, wait_seconds, fmt, raw, output):
    """Fetch job listings by URL, or discover them by keyword/location.

    Output: LinkedInJob[] — id, title, company, company_id, company_url, location,
    country_code, employment_type, function, industries, seniority, posted_date,
    posted_ago, applicants, is_easy_apply, base_salary, summary, url.
    """
    search = {k: v for k, v in {
        "keyword": keyword, "location": location, "country": country,
        "time_range": time_range, "job_type": job_type,
        "experience_level": experience_level, "remote": remote, "company": company,
    }.items() if v is not None}
    if not urls and not search:
        raise click.UsageError("Provide --url or a search (--keyword ...).")
    kw = dict(urls=list(urls) or None, searches=[search] if search else None,
              limit_per_input=limit_per_input, wait_seconds=wait_seconds)
    data = app.sx.marketing.linkedin_jobs(**kw) if raw else app.sx.linkedin.jobs(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="LinkedIn jobs")


@linkedin.command("posts")
@click.option("--url", "urls", multiple=True, help="Post URL (repeatable).")
@click.option("--profile-url", "profile_urls", multiple=True, help="Author profile URL to discover posts from (repeatable).")
@click.option("--limit-per-input", type=int, help="Cap posts per profile.")
@click.option("--wait-seconds", type=int, help="Server-side wait cap, 0-600.")
@output_options
@pass_app
def posts(app, urls, profile_urls, limit_per_input, wait_seconds, fmt, raw, output):
    """Fetch posts by URL, or discover recent posts by author profile.

    Output: LinkedInPost[] — id, url, post_type, title, text, date_posted, likes,
    comments, author_name, author_id, author_url, author_followers, hashtags[],
    embedded_links[], video_duration.
    """
    if not urls and not profile_urls:
        raise click.UsageError("Provide --url or --profile-url.")
    kw = dict(urls=list(urls) or None, profile_urls=list(profile_urls) or None,
              limit_per_input=limit_per_input, wait_seconds=wait_seconds)
    data = app.sx.marketing.linkedin_posts(**kw) if raw else app.sx.linkedin.posts(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="LinkedIn posts")
