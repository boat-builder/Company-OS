"""`salesx x ...` — public X (Twitter) data."""

from __future__ import annotations

import click

from ..output import emit
from ._shared import output_options, pass_app


@click.group(name="x")
def x_group() -> None:
    """Public X (Twitter) posts and profiles."""


@x_group.command("posts")
@click.option("--url", "urls", multiple=True, help="Post (status) URL (repeatable).")
@click.option("--profile", "profile_url", help="Author profile URL to discover posts from.")
@click.option("--start-date", help="Discovery window start, YYYY-MM-DD (with --profile).")
@click.option("--end-date", help="Discovery window end, YYYY-MM-DD (with --profile).")
@click.option("--limit-per-input", type=int, help="Cap posts per profile.")
@click.option("--wait-seconds", type=int, help="Server-side wait cap, 0-600.")
@output_options
@pass_app
def posts(app, urls, profile_url, start_date, end_date, limit_per_input, wait_seconds, fmt, raw, output):
    """Fetch posts by URL, or discover by author profile (optional date window).

    Output: XPost[] — id, url, text, author, author_id, date_posted, likes, replies,
    reposts, quotes, bookmarks, views, is_repost, is_verified, hashtags[], photos[],
    videos[], external_url.
    """
    profiles = None
    if profile_url:
        p = {"url": profile_url}
        if start_date:
            p["start_date"] = start_date
        if end_date:
            p["end_date"] = end_date
        profiles = [p]
    elif start_date or end_date:
        raise click.UsageError("--start-date/--end-date require --profile.")
    if not urls and not profiles:
        raise click.UsageError("Provide --url or --profile.")
    kw = dict(urls=list(urls) or None, profiles=profiles,
              limit_per_input=limit_per_input, wait_seconds=wait_seconds)
    data = app.sx.marketing.x_posts(**kw) if raw else app.sx.x.posts(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="X posts")


@x_group.command("profiles")
@click.option("--url", "urls", multiple=True, required=True, help="Profile URL (repeatable).")
@click.option("--wait-seconds", type=int, help="Server-side wait cap, 0-600.")
@output_options
@pass_app
def profiles(app, urls, wait_seconds, fmt, raw, output):
    """Fetch profiles by URL.

    Output: XProfile[] — id, name, url, biography, location, followers, following,
    posts_count, is_verified, is_business_account, is_government_account,
    date_joined, external_link, category, profile_image.
    """
    kw = dict(urls=list(urls), wait_seconds=wait_seconds)
    data = app.sx.marketing.x_profiles(**kw) if raw else app.sx.x.profiles(**kw)
    emit(data, fmt=fmt, raw=raw, output=output, title="X profiles")
