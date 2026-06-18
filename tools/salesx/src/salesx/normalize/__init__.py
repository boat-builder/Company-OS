"""Normalizers: raw provider dict -> canonical model.

Imported as namespaces so call sites read clearly:

    from salesx.normalize import marketing as nm, close as nc
    people = nm.linkedin_profiles(resp)
    lead = nc.lead(resp)
"""

from . import close, marketing

__all__ = ["marketing", "close"]
