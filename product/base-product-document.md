# Product Base Document — Agent Berlin

> This is the single source of truth for what Berlin is at a structural and functional level. Every pitch deck, landing page, sales conversation, feature announcement, and product update should trace back to this document. It defines what Berlin **is**, not who it's for or why they should care — that translation happens downstream.
>
> If something feels missing, update this document first. Never add capabilities to downstream materials that don't exist here.
>
> **Note:** Berlin is the only product from Agentic World, LLC. USOL (Universal Search Optimization Layer) is not a separate product; it is the internal Tools layer that Berlin uses to execute. See `base-usol-document.md` for the internal architecture reference.

---

## Berlin in One Line

> Berlin is an end-to-end SEO/AEO platform — the user talks to it, and it strategizes, sets up execution, and executes.

The alternative to Berlin is hiring an SEO agency or building an in-house SEO team. Berlin is not a workflow builder, not a set of connectors, and not a configuration surface. A user signs in, opens a dashboard, describes their brand and their goals, and Berlin delivers the outcomes — the keyword plan, the published content, the technical fixes, the ongoing monitoring — without the user having to assemble the work themselves.

---

## The Three-Pillar Framework

Berlin is built around the three pillars of any SEO/AEO program: **Strategy** (the plan of what to do and why), **Execution** (implementing the plan), and **Tools** (everything an expert reaches for to execute). The full definition of the framework lives in `framework.md` and is the canonical reference; this document assumes familiarity with it.

Berlin owns all three pillars. Berlin brings best-practice strategy by default — keyword selection, prioritization, what to publish, what to fix. Berlin performs execution — the operational work that would otherwise consume the majority of a human SEO team's time. And Berlin operates its own Tools layer internally, wiring together data sources, crawlers, CMS integrations, and action endpoints so the user never has to think about them.

The user can optionally bring their own strategy. Teams with strong opinions can supply the plan and let Berlin execute against it. Teams that want Berlin to handle everything end-to-end get a strategy generated automatically from best practice and the brand's live data. Either way, the three-pillar abstraction is hidden behind the dashboard — the user experience is a single platform they talk to.

---

## What Berlin Is

### A Dashboard You Talk To

Berlin's interface is a dashboard. The user describes their brand, their market, and their goals. From there, Berlin sets the direction, proposes the work, and executes it. Progress, outputs, and next steps all surface in the dashboard rather than being chased across a dozen tools. There are no workflows to configure and no agents to wire together.

### Strategy by Default, Optional Override

Berlin has domain intelligence about what SEO/AEO strategies work today — what signals matter, how to prioritize across opportunities, how to sequence work so it compounds. By default, Berlin generates the strategy itself, grounded in the brand's live data and in current best practice. A team that prefers to bring its own plan can do so; Berlin will execute against the supplied strategy rather than generating its own. The default path is fully owned by Berlin.

### Execution Done for You

Berlin actually does the operational work. Running audits and producing actionable reports. Monitoring rankings, competitors, and opportunities. Identifying and prioritizing optimization work. Executing content and technical improvements. Tracking performance and surfacing what's changed. The goal is to take approximately 70% of the operational effort off an SEO or marketing team's plate — not by answering questions or generating suggestions, but by producing shipped work.

### Human Oversight

Berlin operates with human oversight. Before taking actions that affect live systems (publishing content, making changes), Berlin surfaces what it intends to do for review. Teams can configure how much oversight they want — from reviewing every action to reviewing only certain categories of work.

---

## The Tools Layer (USOL) — Internal Infrastructure

Berlin runs on top of an internal Tools layer known internally as USOL (Universal Search Optimization Layer). USOL is not a product, is not sold, and is not exposed to users as something to subscribe to or configure. It is the architecture that lets Berlin's agents reach the data sources and action endpoints needed to execute.

The Tools layer provides a first-party data engine — keyword intelligence cached in Berlin's own database, site crawling and competitor monitoring via Snake.blue (the proprietary AI-first crawler), and ranking signal intelligence covering 80+ signals with automated prioritization. It provides a unified data and action layer — single-authentication access to Google Search Console, GA4, Bing Webmaster Tools, CMS platforms, social channels, Google Trends, Google Maps, review platforms, search results data, and a continuously growing list of data sources and action endpoints. It provides semantic page and keyword intelligence — brand and competitor pages and keywords auto-indexed as embeddings, searchable by meaning rather than exact match. And it uses a thin MCP architecture — data retrieval and action execution routed through the infrastructure rather than through the LLM's context window, eliminating hallucination from context overflow.

These capabilities are real and load-bearing for what Berlin can do. The point is that the user never sees them as a product. They experience Berlin as a platform that works; the Tools layer is the reason it works.

For the internal architecture reference — what USOL does, how it's structured, how Berlin's agents interact with it — see `base-usol-document.md`.

---

## Operational Infrastructure

Berlin includes infrastructure for managing ongoing SEO/AEO operations.

Scheduling lets work run without human initiation — monitoring, reporting, recurring audits. The Report Center is a centralized collection point for all outputs Berlin produces. The Review Center provides human-in-the-loop approval before actions execute. Sharing and governance let work be shared across the organization, with standardized delivery across clients and projects. Brand context, team and org management, permissions, and governance live at the platform level.

This infrastructure makes Berlin operational — it runs continuously, not only when someone is actively using it.

---

## Feature Reference

A flat reference of Berlin's capabilities. These are all parts of one product; the Tools-layer capabilities below are internal infrastructure that Berlin uses, not separately purchasable features.

### Dashboard and Agent

| Feature | Description | Status |
| --- | --- | --- |
| **Dashboard Interface** | The user-facing surface for Berlin. The user talks to Berlin here; Berlin surfaces plans, work, outputs, and status. | Live |
| **Strategy Engine** | Berlin generates the SEO/AEO strategy by default from the brand's live data and current best practice. Users can optionally supply their own strategy. | Live |
| **Execution Engine** | Berlin performs the operational work end-to-end — audits, content, technical fixes, reporting, monitoring. | Live |
| **Report Center** | Centralized collection of all outputs Berlin produces. | Live |
| **Review Center** | Human-in-the-loop approval before actions execute. | Live |
| **Scheduling** | Work runs on a schedule without human initiation. | Live |
| **Sharing & Governance** | Work can be shared and standardized across teams, clients, and projects. | Live |

### Tools Layer (Internal Infrastructure — Not a Separately Purchasable Product)

| Capability | Description | Status |
| --- | --- | --- |
| **Keyword Intelligence** | Comprehensive keyword research, volume, difficulty, and ranking data cached in Berlin's own database. | Live |
| **Site Crawling & Competitor Monitoring** | Proprietary crawlers (Snake.blue) keeping site and competitor data fresh and queryable. | Live |
| **Ranking Signal Intelligence** | 80+ ranking signals tracked with automated prioritization. | Live |
| **Unified Data & Action Layer** | Single-authentication access to GSC, GA4, Bing Webmaster Tools, CMS, social, Google Trends, Maps, reviews, and more. | Live & Expanding |
| **Semantic Page & Keyword Intelligence** | Brand and competitor pages/keywords auto-indexed as embeddings, searchable by meaning. | Live |
| **Thin MCP Architecture** | Data routed through the infrastructure instead of the LLM context window, eliminating hallucination from context overflow. | Live |
| **Brand Context** | Shared knowledge layer for brand guidelines, terminology, audience details. Available to Berlin's agents as org-wide memory. | Live |
| **Team & Org Management** | Add team members, manage access, share credits. Multiple projects (brands) within the same org. | Live |

---

## How to Use This Document

This is the canonical reference for what Berlin is at a structural and functional level. When crafting messaging for a specific audience:

1. Start from Berlin's core value proposition — an end-to-end SEO/AEO platform that owns Strategy, Execution, and Tools, and is the alternative to hiring an SEO team or agency.
2. Reference `framework.md` for the three-pillar framework when the audience needs the structural argument.
3. Reference `base-usol-document.md` only for internal architecture conversations; do not surface USOL as a product name to customers.
4. Translate the structural description into the language of the audience's pain and ambition.
5. Never add a capability that doesn't exist here. If something feels missing, update this document first.

---

_Agentic World, LLC — Internal Foundation Document_
_Last updated: 2026-04-23_
