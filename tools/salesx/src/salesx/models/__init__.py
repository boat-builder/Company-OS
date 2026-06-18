"""Canonical models — the stable data contract salesx emits (and the SDK returns).

Import from here:

    from salesx.models import LinkedInProfile, XProfile, SearchResults, DomainOverview, Lead
"""

from .base import Model
from .crm import Contact, Lead, LeadStatus, Note, Task, User
from .linkedin import (
    LinkedInCompany,
    LinkedInEducation,
    LinkedInExperience,
    LinkedInFunding,
    LinkedInJob,
    LinkedInPost,
    LinkedInProfile,
)
from .search import AnswerResult, Citation, SearchHit, SearchResults
from .seo import (
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
    RankHistoryPoint,
    RankedKeyword,
    RelevantPage,
    TechStack,
    ThirdParty,
    TrafficEstimate,
    TrafficMetrics,
)
from .x import XPost, XProfile

__all__ = [
    "Model",
    # LinkedIn
    "LinkedInProfile", "LinkedInExperience", "LinkedInEducation",
    "LinkedInCompany", "LinkedInFunding", "LinkedInJob", "LinkedInPost",
    # X
    "XProfile", "XPost",
    # Search / answers
    "SearchHit", "SearchResults", "Citation", "AnswerResult",
    # SEO
    "RankedKeyword", "KeywordIdea", "TrafficMetrics", "DomainOverview",
    "RankHistoryPoint", "TechStack", "TrafficEstimate", "RelevantPage",
    # SEO — Lighthouse
    "LighthouseReport", "CoreWebVitals", "CruxMetric", "CruxMetrics", "FieldData",
    "LighthouseOpportunity", "LighthouseDiagnostic", "ThirdParty",
    "LighthouseOffender", "LighthouseSavings",
    # CRM
    "Contact", "Lead", "Task", "Note", "LeadStatus", "User",
]
