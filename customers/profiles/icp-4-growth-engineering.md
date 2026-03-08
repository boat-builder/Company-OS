# ICP 4 — Growth Engineering / Marketing Ops Teams Inside SaaS

> **Living document.** Base thesis below. Append new intel (interviews, social signals, objections, wins) as you learn it.

---

## Quick Stats

| Field | Detail |
|-------|--------|
| **Segment** | Growth Eng / Marketing Ops at SaaS companies |
| **Core Pain** | Fragmented SEO data; brittle scripts; AI search not instrumented |
| **Value Hook** | Programmable infrastructure; replace custom scripts; API-first |
| **Top Roles** | Growth Engineer, Head of Marketing Ops |
| **Buying Signal** | Dev time savings; reduce marketing requests |

---

## Key Pain Points

- **SEO data is fragmented across sources that don't talk to each other.** GSC, GA4, rank trackers, crawl data, and CRM data all live in different systems. Joining them requires bespoke scripts that are brittle and expensive to maintain.
- **Building internal SEO tooling for the marketing team is a recurring distraction.** Every time marketing wants a new report or automation, it becomes an engineering task. That's time away from product work.
- **Measurement is getting harder as AI Overviews and zero-click results multiply.** Standard metrics (clicks, impressions, rankings) are increasingly misleading. The team knows it but doesn't have better instrumentation yet.
- **Workflows that were automated once break without warning.** API changes, auth token expiry, data schema changes — maintaining custom SEO scripts is a hidden ongoing cost.
- **AI search introduces a new measurement surface they haven't instrumented yet.** Where does the brand appear in AI-generated answers? How does it compare to competitors? No existing tooling answers this cleanly.
- **Marketing ops teams are expected to build infrastructure, not just reports.** Point solutions aren't enough. They need something that plugs into their existing data layer and scales with org complexity.

---

## Core Value Proposition

This platform maps directly to how Growth Engineering / Marketing Ops already thinks: unified data layer, API-first access, programmable workflows. The unified data access layer (GSC, GA4, Bing, keyword data, crawl data) replaces a patchwork of scripts and gives a single queryable interface for all SEO data — with the platform handling auth and normalization. The workflow builder lets them create the automated SEO processes marketing needs without writing and maintaining custom code. The LLM integration is also compelling here: if they're building AI-powered internal tools, the platform's tool layer lets them expose SEO data to those apps natively. And as their org scales (team management, project/brand management), the infrastructure grows with them.

**In short:** replace a pile of brittle scripts with programmable, maintainable SEO infrastructure.

---

## Assumptions About Their Priorities

- **Reliability and infrastructure quality come first.** They will probe the technical depth of the platform before anything else. Flaky APIs or inconsistent data quality will kill the evaluation.
- **API access and data layer flexibility are more important than UI.** They'll likely explore what's queryable before they touch the workflow builder.
- **They're trying to reduce the volume of one-off marketing requests.** A workflow the marketing team can run themselves is worth more than a report they have to generate on demand.
- **They think in systems, not features.** They want to know how the platform fits into their existing stack, not a list of what it can do in isolation.
- **Cost is justified by developer time saved or tooling consolidated.** The ROI story is hours-per-month reclaimed from custom scripts + subscriptions eliminated.

---

## Ideal Roles

- **Growth Engineer / Marketing Engineer** — Primary user and evaluator; cares deeply about API quality and data layer reliability.
- **Head of Marketing Operations** — Owns the marketing data stack; decision-maker on infrastructure tools.
- **Revenue Operations Manager** — Interested in SEO-to-pipeline attribution; values clean data integration.
- **Data Engineer (Marketing)** — Technical evaluator; will probe schema, API limits, and maintainability.
- **Director of Demand Generation** — Cares about SEO as a channel but doesn't want to manage scripts; executive sponsor.

---

## Content & Messaging Notes

> _Add notes here as you test social posts, hooks, and angles that resonate or fall flat._

---

## Discovery Intel

> _Log insights from conversations, interviews, replies, DMs, etc._

| Date | Source | Insight |
|------|--------|---------|
| | | |

---

## Objections Heard

> _Track objections and how you've responded._

| Objection | Response / Reframe |
|-----------|--------------------|
| | |

---

## Open Questions

> _Things you still want to validate about this ICP._

- [ ] Do they consider SEO infrastructure their problem to own, or do they hand it off to an SEO tool vendor?
- [ ] What does their current SEO script/maintenance burden look like in hours per month?
- [ ] Are they already exploring exposing SEO data to internal LLM apps?
