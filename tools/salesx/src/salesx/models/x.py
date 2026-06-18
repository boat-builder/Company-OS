"""X (Twitter) canonical models, curated from real provider responses."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from .base import Model


@dataclass
class XProfile(Model):
    """A public X profile (`x profiles`)."""

    id: Optional[str] = None
    name: Optional[str] = None            # profile_name
    url: Optional[str] = None
    biography: Optional[str] = None
    location: Optional[str] = None
    followers: Optional[int] = None
    following: Optional[int] = None
    posts_count: Optional[int] = None
    is_verified: Optional[bool] = None
    is_business_account: Optional[bool] = None
    is_government_account: Optional[bool] = None
    date_joined: Optional[str] = None
    external_link: Optional[str] = None
    category: Optional[str] = None        # category_name
    profile_image: Optional[str] = None


@dataclass
class XPost(Model):
    """A public X post (`x posts`)."""

    id: Optional[str] = None
    url: Optional[str] = None
    text: Optional[str] = None            # description
    author: Optional[str] = None          # user_posted
    author_id: Optional[str] = None       # user_id
    date_posted: Optional[str] = None
    likes: Optional[int] = None
    replies: Optional[int] = None
    reposts: Optional[int] = None
    quotes: Optional[int] = None
    bookmarks: Optional[int] = None
    views: Optional[int] = None
    is_repost: Optional[bool] = None
    is_verified: Optional[bool] = None
    hashtags: list[str] = field(default_factory=list)
    photos: list[str] = field(default_factory=list)
    videos: list[str] = field(default_factory=list)
    external_url: Optional[str] = None
