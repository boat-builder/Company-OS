# Product Base Document — Agent Berlin

> This is the single source of truth for what Berlin is at a structural and functional level. Every pitch deck, landing page, sales conversation, feature announcement, and product update should trace back to this document. It defines what Berlin **is**, not who it's for or why they should care — that translation happens downstream.
>
> If something feels missing, update this document first. Never add capabilities to downstream materials that don't exist here.
>
> **Note:** Berlin is the only product from Agentic World, LLC. Berlin is a self-contained platform — it is not sold as a layered product, and it is not integrated with as a developer surface.

---

## Berlin in One Line

> Berlin is an end-to-end SEO/AEO platform — the customer connects their domain and accounts, and Berlin strategizes, sets up execution, and executes autonomously. For end customers, the platform is delivered alongside a **Forward Deployed Marketer (FDM)** who owns strategy, reviews output, and owns the relationship.

The alternative to Berlin is hiring an SEO agency. Berlin is not a workflow builder, not a set of connectors, and not a configuration surface. A user signs in, connects their domain and accounts (GSC, GA4, CMS, social, etc.), and Berlin delivers the outcomes — the keyword plan, the published content, the technical fixes, the ongoing monitoring — without the user having to assemble the work themselves. **No conversation is required** for Berlin to execute; the user can talk to Berlin if they want to steer or inspect, but it is optional. (In-house marketing teams aren't a competing alternative — they routinely outsource SEO grunt work to agencies anyway, so the agency comparison still applies.)

### Two Packaged Offerings

Berlin is one product, sold in two packages:

1. **Berlin + FDM (end customers).** The core offering for mid-market and traditional businesses. Platform execution plus an assigned Forward Deployed Marketer who shapes strategy, reviews Berlin's output, owns the customer relationship, and surfaces patterns back into Berlin's default playbooks. FDM is not a premium add-on — it is part of the core offering at this tier.

2. **Berlin for Agencies.** A platform-only version of Berlin sold to SEO/digital agencies running Berlin underneath their own client delivery. This version **does not include an FDM** — the agency provides that layer themselves. Same underlying product, different packaging.

### Pricing Principle (Berlin + FDM)

Berlin + FDM pricing is anchored at roughly **1/4 of what an agency would charge for the same scope of work** — scope-dependent, with the FDM service component being a major driver of tier placement. The pricing model resolves to a four-tier **scope ladder**:

| Scope tier | Agency-equivalent retainer | Berlin price | Example buyer |
|---|---|---|---|
| **Entry** | $1.5K–$2K/mo | **$499** | Local clinic, single-location service business (Reach Psych shape) |
| **Mid** | $4K–$8K/mo | **$999–$1,999** | Bootstrapped SaaS, B2B services with serious SEO scope |
| **Heavy** | $10K–$15K/mo | **$2,500–$4,000** | Mid-market with full-funnel scope, multiple geos |
| **Enterprise** | $20K+/mo | **$5,000+** | Compliance-heavy, multi-brand (miniOrange shape) |

Scope determines the tier; the agency-fraction anchor stays constant across all four. The first paid cohort (Reach Psych, Csuite.so on Berlin + FDM) sits at the Entry tier deliberately — to validate fit and build a clean reference cohort. ARPU expansion comes from **cohort mix shift across the ladder**, not from price increases on existing accounts: a customer at $499 stays at $499 unless their scope materially expands.

Berlin for Agencies pricing is anchored differently — against per-seat platform spend plus tooling subscriptions an agency would otherwise carry. Custom-tiered, taken opportunistically on direct inbound rather than pitched on the public site.

---

## The Three-Pillar Framework

Berlin is built around the three pillars of any SEO/AEO program: **Strategy** (the plan of what to do and why), **Execution** (implementing the plan), and **Tools** (everything an expert reaches for to execute). The full definition of the framework lives in `framework.md` and is the canonical reference; this document assumes familiarity with it.

Berlin owns all three pillars. Berlin brings best-practice strategy by default — keyword selection, prioritization, what to publish, what to fix. Berlin performs execution — the operational work that would otherwise consume the majority of a human SEO team's time. And Berlin operates its own Tools layer internally, wiring together data sources, crawlers, CMS integrations, and action endpoints so the user never has to think about them.

The user can optionally bring their own strategy. Teams with strong opinions can supply the plan and let Berlin execute against it. Teams that want Berlin to handle everything end-to-end get a strategy generated automatically from best practice and the brand's live data. Either way, the three-pillar abstraction is hidden behind the dashboard — the user experience is a single platform they talk to.

---

## What Berlin Is

### A Dashboard That Runs Itself (and That You Can Talk To)

Berlin's interface is a dashboard. Once the customer connects their domain and the accounts Berlin needs to work with (GSC, GA4, CMS, social, etc.), Berlin begins executing on its own — no conversation is required. Progress, outputs, and next steps all surface in the dashboard rather than being chased across a dozen tools. There are no workflows to configure and no agents to wire together.

Customers can talk to Berlin if they want to — to steer strategy, ask for a specific outcome, or inspect reasoning — but it is optional. The default mode is autonomous execution with human review where it matters.

### Strategy by Default, Optional Override

Berlin has domain intelligence about what SEO/AEO strategies work today — what signals matter, how to prioritize across opportunities, how to sequence work so it compounds. By default, Berlin generates the strategy itself, grounded in the brand's live data and in current best practice. A team that prefers to bring its own plan can do so; Berlin will execute against the supplied strategy rather than generating its own. The default path is fully owned by Berlin.

### Execution Done for You

Berlin actually does the operational work. Running audits and producing actionable reports. Monitoring rankings, competitors, and opportunities. Identifying and prioritizing optimization work. Executing content and technical improvements. Tracking performance and surfacing what's changed. The goal is to take approximately 70% of the operational effort off an SEO or marketing team's plate — not by answering questions or generating suggestions, but by producing shipped work.

### Human Oversight

Berlin operates with human oversight. Before taking actions that affect live systems (publishing content, making changes), Berlin surfaces what it intends to do for review. Teams can configure how much oversight they want — from reviewing every action to reviewing only certain categories of work.

### Forward Deployed Marketer (End-Customer Offering)

For end customers on the Berlin + FDM package, an assigned Forward Deployed Marketer works alongside the platform. The FDM shapes strategy, reviews Berlin's output, handles the customer relationship, and surfaces patterns back into Berlin's default strategy and execution playbooks. The FDM is not a consulting bolt-on — they are the human owner of the customer relationship in a model where the platform does the execution. This is the layer that lets Berlin replace an agency relationship cleanly for buyers who expect a human owner, not just software.

The agency-tier version of the product does not include an FDM; agencies provide that layer themselves for their own clients.

---

## The Tools Layer — Internal Infrastructure

Berlin runs on top of an internal Tools layer. It is not a product, is not sold, and is not exposed to users as something to subscribe to or configure. It is the architecture that lets Berlin's agents reach the data sources and action endpoints needed to execute.

The Tools layer provides a first-party data engine — keyword intelligence cached in Berlin's own database, site crawling and competitor monitoring via Snake.blue (the proprietary AI-first crawler), and ranking signal intelligence covering 80+ signals with automated prioritization. It provides a unified data and action layer — single-authentication access to Google Search Console, GA4, Bing Webmaster Tools, CMS platforms, social channels, Google Trends, Google Maps, review platforms, search results data, and a continuously growing list of data sources and action endpoints. It provides semantic page and keyword intelligence — brand and competitor pages and keywords auto-indexed as embeddings, searchable by meaning rather than exact match. And it uses a proprietary data routing architecture so retrieval and action execution happen through the infrastructure rather than through an LLM's context window, eliminating hallucination from context overflow.

These capabilities are real and load-bearing for what Berlin can do. The user never sees them as a product, and they should not be sold or messaged as features. They are the engineering substrate that drives Berlin's unit economics — the reason one FDM can serve more accounts per head than a human-led agency or a Daydream-style Growth Lead can, and the reason Berlin can price at ~1/4 of agency cost without breaking margin. Customers experience all of this indirectly: faster outputs, deeper coverage, lower price point, a single FDM keeping up with their account.

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

### Tools Layer (Engineering Substrate — Not a User-Facing Feature, Not Separately Purchasable)

These items are listed for internal and investor reference only. They are not features Berlin sells, messages, or surfaces in customer pricing pages — they are the substrate underneath the FDM that makes the unit economics work.

| Capability | Description | Status |
| --- | --- | --- |
| **Agentic Runtime** | Custom Go-based runtime running thousands of agent loops concurrently. Built on the founder's prior production AI-runtime work at RedisAI and Lightning.ai. The structural reason one FDM can serve multiple customers in parallel. | Live |
| **Keyword & Page Store** | Comprehensive keyword research, volume, difficulty, ranking data, and page-level data cached in Berlin's own database. Millions of records sit behind a fast query layer agents hit directly — not a vector-search guess and not raw context dumps. | Live |
| **Site Crawling & Competitor Monitoring** | Proprietary AI-first crawler (Snake.blue) running stable, batched crawls at any scale. Keeps site and competitor data fresh and queryable. | Live |
| **Ranking Signal Intelligence** | 80+ ranking signals tracked with automated prioritization. | Live |
| **Unified Data & Action Layer** | Single-authentication access to GSC, GA4, Bing Webmaster Tools, CMS, social, Google Trends, Maps, reviews, and more. | Live & Expanding |
| **Semantic Page & Keyword Intelligence** | Brand and competitor pages/keywords auto-indexed as embeddings, searchable by meaning. | Live |
| **Proprietary Data Routing Architecture** | Data routed through Berlin's infrastructure instead of an LLM context window, eliminating hallucination from context overflow. | Live |
| **Brand Context** | Shared knowledge layer for brand guidelines, terminology, audience details. Available to Berlin's agents as org-wide memory. | Live |
| **Team & Org Management** | Add team members, manage access, share credits. Multiple projects (brands) within the same org. | Live |

---

## How to Use This Document

This is the canonical reference for what Berlin is at a structural and functional level. When crafting messaging for a specific audience:

1. Start from Berlin's core value proposition — an AI-native SEO/AEO agency: an end-to-end platform underneath that owns Strategy, Execution, and Tools, with an assigned Forward Deployed Marketer on top who owns the relationship. Berlin replaces the SEO agency a company would otherwise sign. (In-house marketing teams aren't a competing alternative — they outsource SEO grunt work to agencies anyway.)
2. Reference `framework.md` for the three-pillar framework when the audience needs the structural argument.
3. Translate the structural description into the language of the audience's pain and ambition.
4. Never add a capability that doesn't exist here. If something feels missing, update this document first.

---

_Agentic World, LLC — Internal Foundation Document_
_Last updated: 2026-04-24_
