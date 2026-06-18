"""LinkedIn canonical models.

Field selection is curated from the *real* provider responses (captured live, not
the docs): the useful, stable subset of each record is surfaced here, and the noisy
parts (people-also-viewed, raw activity feeds, similar-company lists) are dropped.
The full provider payload is still reachable via the hidden `--raw` flag / the raw
`Salesx.marketing` transport.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .base import Model


@dataclass
class LinkedInExperience(Model):
    company: Optional[str] = None
    company_id: Optional[str] = None
    title: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None        # "Present" when current
    url: Optional[str] = None


@dataclass
class LinkedInEducation(Model):
    institution: Optional[str] = None
    start_year: Optional[str] = None
    end_year: Optional[str] = None
    url: Optional[str] = None


@dataclass
class LinkedInProfile(Model):
    """A person's public LinkedIn profile (`linkedin profiles`)."""

    id: Optional[str] = None              # vanity id, e.g. "satyanadella"
    name: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    headline: Optional[str] = None        # the "position" line
    about: Optional[str] = None
    current_company: Optional[str] = None
    current_title: Optional[str] = None
    location: Optional[str] = None
    city: Optional[str] = None
    country_code: Optional[str] = None
    followers: Optional[int] = None
    connections: Optional[int] = None
    influencer: Optional[bool] = None
    linkedin_url: Optional[str] = None    # the canonical input URL
    avatar_url: Optional[str] = None
    experience: list[LinkedInExperience] = field(default_factory=list)
    education: list[LinkedInEducation] = field(default_factory=list)


@dataclass
class LinkedInFunding(Model):
    last_round_type: Optional[str] = None
    last_round_date: Optional[str] = None
    last_round_raised: Optional[str] = None
    rounds: Optional[int] = None


@dataclass
class LinkedInCompany(Model):
    """A company's public LinkedIn page (`linkedin companies`)."""

    id: Optional[str] = None              # vanity id, e.g. "anthropicresearch"
    company_id: Optional[str] = None      # numeric id
    name: Optional[str] = None
    linkedin_url: Optional[str] = None
    website: Optional[str] = None
    domain: Optional[str] = None          # bare domain (website_simplified)
    description: Optional[str] = None
    about: Optional[str] = None
    slogan: Optional[str] = None
    industries: Optional[str] = None
    company_size: Optional[str] = None    # e.g. "501-1,000 employees"
    employee_count: Optional[int] = None  # employees_in_linkedin
    organization_type: Optional[str] = None
    followers: Optional[int] = None
    logo_url: Optional[str] = None
    crunchbase_url: Optional[str] = None
    funding: Optional[LinkedInFunding] = None
    investors: list[str] = field(default_factory=list)


@dataclass
class LinkedInJob(Model):
    """A LinkedIn job listing (`linkedin jobs`)."""

    id: Optional[str] = None              # job_posting_id
    title: Optional[str] = None
    company: Optional[str] = None
    company_id: Optional[str] = None
    company_url: Optional[str] = None
    location: Optional[str] = None
    country_code: Optional[str] = None
    employment_type: Optional[str] = None
    function: Optional[str] = None
    industries: Optional[str] = None
    seniority: Optional[str] = None
    posted_date: Optional[str] = None     # ISO timestamp
    posted_ago: Optional[str] = None      # e.g. "1 day ago"
    applicants: Optional[int] = None
    is_easy_apply: Optional[bool] = None
    base_salary: Optional[str] = None
    summary: Optional[str] = None
    url: Optional[str] = None


@dataclass
class LinkedInPost(Model):
    """A LinkedIn post (`linkedin posts`)."""

    id: Optional[str] = None
    url: Optional[str] = None
    post_type: Optional[str] = None
    title: Optional[str] = None
    text: Optional[str] = None
    date_posted: Optional[str] = None
    likes: Optional[int] = None
    comments: Optional[int] = None
    author_name: Optional[str] = None
    author_id: Optional[str] = None
    author_url: Optional[str] = None
    author_followers: Optional[int] = None
    hashtags: list[str] = field(default_factory=list)
    embedded_links: list[str] = field(default_factory=list)
    video_duration: Optional[int] = None
