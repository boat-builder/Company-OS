# Product

> Canonical reference for what Berlin **is** at a structural and functional level — the three-pillar framework, the two packaged offerings, the dashboard experience, the Tools layer underneath, the feature reference, and the pricing principle. Every pitch deck, landing page, sales conversation, feature announcement, and product update should trace back to this document.
>
> **If something feels missing, update this document first.** Never add capabilities to downstream materials that don't exist here.
>
> **Note:** Berlin is the only product from Agentic World, LLC. Berlin is a self-contained platform — not sold as a layered product, not integrated with as a developer surface.

---

## Berlin in One Line

> Berlin is an end-to-end SEO/AEO platform — the customer connects their domain and accounts, and Berlin strategizes, sets up execution, and executes autonomously. For end customers, the platform is delivered alongside a **Forward Deployed Marketer (FDM)** who owns strategy, reviews output, and owns the relationship.

The alternative to Berlin is **hiring an SEO agency**. Berlin is not a workflow builder, not a set of connectors, and not a configuration surface. A user signs in, connects their domain and accounts (GSC, GA4, CMS, social, etc.), and Berlin delivers the outcomes — keyword plan, published content, technical fixes, ongoing monitoring — without the user having to assemble the work themselves. **No conversation is required** for Berlin to execute; the user can talk to Berlin if they want to steer or inspect, but it is optional.

(In-house marketing teams aren't a competing alternative — they routinely outsource SEO grunt work to agencies anyway, so the agency comparison still applies.)

---

## Why the SEO Problem Got Harder (Substrate for Positioning)

Doing SEO/AEO well in 2026 is roughly **10x harder than it was three years ago**.

- The **old surface area** was Google's blue links.
- The **new surface area** covers every AI search engine (ChatGPT, Perplexity, Claude, Google's AI Mode), plus a long list of activities that weren't on traditional SEO checklists — managing review velocity without tripping Google's spam filters, building authority signals across multiple platforms, brand presence in the places LLMs cite from (Reddit, LinkedIn, etc.), and dozens of evolving techniques.
- **None of this is documented by Google or OpenAI.** The playbook is undocumented and evolves week by week.
- Agencies and in-house teams don't have the bandwidth to run experiments and figure out what's actually working right now. Berlin does, and that experimentation work is **core to the roadmap** — it's a substrate the platform is built around, not a feature.

---

## The Three-Pillar Framework

Any real-world SEO/AEO program decomposes into three pillars: **Strategy**, **Execution**, and **Tools**. The pillars are useful because they make it precise which parts of the work a given product or person actually owns — and which parts get passed off elsewhere.

### Strategy

Strategy is the plan: what to do and why. It's the selection of keywords and topics to pursue, the prioritization of opportunities, the decisions about what to publish, what to fix, what to ignore, and what sequence to do it in. Strategy is where an SEO program either compounds or spins. **Strategy produces a plan; it does not produce shipped work.**

### Execution

Execution is the human expert using the tools to implement the strategy. The operational grunt work: running the audit, drafting the brief, writing or editing the page, pushing it through the CMS, configuring the redirect, pulling the GSC report, updating the dashboard, chasing the broken link. **Execution is where most of the hours in an SEO program actually go**, and it's the part that is hardest to outsource cleanly because it requires constant small judgment calls informed by context.

### Tools

Tools is everything the executing expert reaches for. Not only SaaS like Semrush or Ahrefs — also the browser, the CMS, crawlers, data sources (Google Search Console, GA4, Google Trends, Google Maps, review platforms, Bing Webmaster Tools), social platforms, and a long tail of specialized utilities. Some have first-class APIs; many don't. **A lot of what makes execution slow is moving between tools and reconciling their outputs.**

### How Berlin Maps Onto the Framework

Berlin owns **all three pillars**. The user arrives at a dashboard, talks to Berlin, and Berlin delivers outcomes. Strategy comes baked in by default: Berlin picks keywords, sets priorities, and decides what to publish and what to fix, drawing on best practice and on the brand's live data. Execution happens inside Berlin — the operational work is done by the platform rather than by a person clicking through ten tabs. Tools are wired in as internal infrastructure; the user never sees or manages them.

The three-pillar abstraction is hidden from the end user. What they see is a platform they talk to. The user can optionally bring their own strategy — a team with strong opinions can supply the plan and let Berlin execute against it — but if they don't, Berlin supplies one. **The Tools pillar is internal architecture inside Berlin — not a product that is sold or integrated with separately.**

The practical implication: Berlin is positioned against **hiring an SEO agency**, not against workflow builders or AI dev tools. A customer is choosing between "hire an agency that will own Strategy, Execution, and Tools" and "use Berlin, where an FDM and the platform underneath own all three."

---

## Two Packaged Offerings

Berlin is one product, sold in two packages:

1. **Berlin + FDM (end customers).** The core offering for mid-market and traditional businesses. Platform execution plus an assigned Forward Deployed Marketer who shapes strategy, reviews Berlin's output, owns the customer relationship, and surfaces patterns back into Berlin's default playbooks. **FDM is not a premium add-on — it is part of the core offering at this tier.**

2. **Berlin for Agencies.** A platform-only version sold to SEO/digital agencies running Berlin underneath their own client delivery. This version **does not include an FDM** — the agency provides that layer themselves. Same underlying product, different packaging.

Full FDM model lives in `team.md`.

---

## What Berlin Is — Capability Surfaces

### A Dashboard That Runs Itself (and That You Can Talk To)

Berlin's interface is a dashboard. Once the customer connects their domain and the accounts Berlin needs (GSC, GA4, CMS, social, etc.), Berlin begins executing on its own — **no conversation is required**. Progress, outputs, and next steps surface in the dashboard rather than being chased across a dozen tools. There are no workflows to configure and no agents to wire together.

Customers can talk to Berlin if they want — to steer strategy, ask for a specific outcome, or inspect reasoning — but it is optional. The default mode is autonomous execution with human review where it matters.

### Strategy by Default, Optional Override

Berlin has domain intelligence about what SEO/AEO strategies work today — what signals matter, how to prioritize across opportunities, how to sequence work so it compounds. By default, Berlin generates the strategy itself, grounded in the brand's live data and current best practice. A team that prefers to bring its own plan can do so; Berlin will execute against the supplied strategy. **The default path is fully owned by Berlin.**

### Execution Done for You

Berlin actually does the operational work — running audits, monitoring rankings, identifying and prioritizing optimization, executing content and technical improvements, tracking performance, surfacing what's changed. The goal is to take approximately **70% of the operational effort** off an SEO or marketing team's plate — not by answering questions or generating suggestions, but by producing **shipped work**.

A concrete shape of this in practice: **Berlin runs a full site audit in under an hour — the same audit takes a typical agency three days.** Berlin then schedules the fixes, executes most of them automatically, and continuously monitors for regressions and new issues. Anything that genuinely cannot be automated is where the FDM steps in.

### Human Oversight

Berlin operates with human oversight. Before taking actions that affect live systems (publishing content, making changes), Berlin surfaces what it intends to do for review. Teams can configure how much oversight they want — from reviewing every action to reviewing only certain categories of work.

### Forward Deployed Marketer (End-Customer Offering)

For end customers on the Berlin + FDM package, an assigned FDM works alongside the platform. The FDM shapes strategy, reviews Berlin's output, handles the customer relationship, and surfaces patterns back into Berlin's default playbooks. **The FDM is not a consulting bolt-on — they are the human owner of the customer relationship in a model where the platform does the execution.** This is the layer that lets Berlin replace an agency relationship cleanly for buyers who expect a human owner, not just software.

The agency-tier version of the product does not include an FDM; agencies provide that layer themselves for their own clients. Full model spec in `team.md`.

---

## The Tools Layer — Internal Infrastructure

Berlin runs on top of an internal Tools layer. It is **not a product, is not sold, and is not exposed to users** as something to subscribe to or configure. It is the architecture that lets Berlin's agents reach the data sources and action endpoints needed to execute.

The Tools layer provides:

- A **first-party data engine** — keyword intelligence cached in Berlin's own database, site crawling and competitor monitoring via **Snake.blue** (the proprietary AI-first crawler), and ranking signal intelligence covering 80+ signals with automated prioritization.
- A **unified data and action layer** — single-authentication access to Google Search Console, GA4, Bing Webmaster Tools, CMS platforms, social channels, Google Trends, Google Maps, review platforms, search results data, and a continuously growing list of data sources and action endpoints.
- **Semantic page and keyword intelligence** — brand and competitor pages and keywords auto-indexed as embeddings, searchable by meaning rather than exact match.
- A **proprietary data routing architecture** — retrieval and action execution happen through the infrastructure rather than through an LLM's context window, eliminating hallucination from context overflow.

These capabilities are real and load-bearing for what Berlin can do. The user never sees them as a product, and they should not be sold or messaged as features. They are the **engineering substrate that drives Berlin's unit economics** — the reason one FDM can serve more accounts per head than a human-led agency or a Daydream-style Growth Lead can, and the reason Berlin can price at ~1/4 of agency cost without breaking margin. Customers experience all of this indirectly: faster outputs, deeper coverage, lower price point, a single FDM keeping up with their account.

---

## The Engineering Moat (Investor / Internal Reference)

For investor and internal context, the substrate decomposes into:

- **Go-based agentic runtime.** Custom-built in Go to run thousands of agent loops concurrently — a concurrency ceiling typical Python orchestration frameworks cannot reach. Built on the founder's prior production AI-runtime work at RedisAI and Lightning.ai. Structural reason one Berlin FDM can serve multiple customers in parallel without queueing or degraded latency.
- **Proprietary crawl (Snake.blue).** AI-first crawler. Stable, batched crawls at any scale; brand and competitor data fresh and queryable without depending on external infrastructure.
- **Queryable keyword and page store.** Millions of keywords and pages behind a fast query layer that agents hit directly — not a vector-search guess and not raw context dumps. Keyword intelligence sourced from providers like Semrush and DataForSEO; pages come from Snake.blue. Customers never need their own third-party subscriptions; data costs compound down over time as the cache grows.
- **Proprietary data routing architecture.** Naive agentic tool-use fills the LLM's context window and degrades reliability as operations scale. Berlin's data routing layer (inspired by 2024 codemode research) routes data through the unified data layer instead — reliability holds across long, multi-source agentic work that breaks other AI-assisted tools mid-flow.
- **80+ ranking-signal coverage.** Automated signal capture and prioritization across the lifecycle, so the FDM doesn't burn cycles assembling them by hand.

Together this substrate is *why* Berlin can offer agency-equivalent scope at ~1/4 of agency cost without breaking margin — and *why* the platform underneath the FDM is genuinely autonomous-capable, leaving latent self-serve optionality for the future without it being a current focus.

---

## Operational Infrastructure

- **Scheduling** — work runs without human initiation (monitoring, reporting, recurring audits).
- **Report Center** — centralized collection point for all outputs Berlin produces.
- **Review Center** — human-in-the-loop approval before actions execute.
- **Sharing & governance** — work shared across the organization, standardized delivery across clients and projects.
- **Brand context, team and org management, permissions, and governance** — all at the platform level.

This infrastructure is what makes Berlin operational — it runs continuously, not only when someone is actively using it.

---

## Feature Reference

A flat reference of Berlin's capabilities. These are all parts of one product; the Tools-layer capabilities are internal infrastructure that Berlin uses, not separately purchasable features.

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

Listed for internal and investor reference only. Not features Berlin sells, messages, or surfaces in customer pricing pages.

| Capability | Description | Status |
| --- | --- | --- |
| **Agentic Runtime** | Custom Go-based runtime running thousands of agent loops concurrently. Built on prior production AI-runtime work at RedisAI and Lightning.ai. The structural reason one FDM can serve multiple customers in parallel. | Live |
| **Keyword & Page Store** | Comprehensive keyword research, volume, difficulty, ranking data, and page-level data cached in Berlin's own database. Millions of records sit behind a fast query layer agents hit directly. | Live |
| **Site Crawling & Competitor Monitoring** | Proprietary AI-first crawler (Snake.blue) running stable, batched crawls at any scale. Keeps site and competitor data fresh and queryable. | Live |
| **Ranking Signal Intelligence** | 80+ ranking signals tracked with automated prioritization. | Live |
| **Unified Data & Action Layer** | Single-authentication access to GSC, GA4, Bing Webmaster Tools, CMS, social, Google Trends, Maps, reviews, and more. | Live & Expanding |
| **Semantic Page & Keyword Intelligence** | Brand and competitor pages/keywords auto-indexed as embeddings, searchable by meaning. | Live |
| **Proprietary Data Routing Architecture** | Data routed through Berlin's infrastructure instead of an LLM context window, eliminating hallucination from context overflow. | Live |
| **Brand Context** | Shared knowledge layer for brand guidelines, terminology, audience details. Available to Berlin's agents as org-wide memory. | Live |
| **Team & Org Management** | Add team members, manage access, share credits. Multiple projects (brands) within the same org. | Live |

---

## Pricing — Berlin + FDM (End Customers)

Berlin + FDM pricing is anchored at roughly **1/4 of what an agency would charge for the same scope of work** — scope-dependent, with the FDM service component as a major driver of tier placement. The pricing model resolves to a four-tier **scope ladder**:

| Scope tier | Agency-equivalent retainer | Berlin price | Example buyer |
|---|---|---|---|
| **Entry** | $1.5K–$2K/mo | **$499** | Local clinic, single-location service business (Reach Psych shape) |
| **Mid** | $4K–$8K/mo | **$999–$1,999** | Bootstrapped SaaS, B2B services with serious SEO scope |
| **Heavy** | $10K–$15K/mo | **$2,500–$4,000** | Mid-market with full-funnel scope, multiple geos |
| **Enterprise** | $20K+/mo | **$5,000+** | Compliance-heavy, multi-brand (miniOrange shape) |

**Scope determines the tier; the agency-fraction anchor stays constant across all four.** The first paid cohort (Reach Psych, Csuite.so) sits at the Entry tier deliberately — to validate fit and build a clean reference cohort. **ARPU expansion comes from cohort mix shift across the ladder, not from price increases on existing accounts**: a customer at $499 stays at $499 unless their scope materially expands.

### India market exception

Local agencies in India charge ~₹60K/month (~$630). Berlin's $499 is **not** 1/4 of agency cost in this market. When competing locally, lead with marketer-to-client ratio (1:10–15 vs 1:4–8) and AI search authority work, not price. (Sales playbook: `sales.md`.)

---

## Pricing — Berlin for Agencies

Berlin for Agencies is anchored differently — against the **per-seat platform spend plus tooling subscriptions** an agency would otherwise carry, not against a retainer multiple. Custom-tiered, taken opportunistically on direct inbound rather than pitched on the public site.

When an agency engages, Berlin offers a **channel partner discount band** off list price. The band exists so the discount level is principled rather than negotiated from scratch each time, and so deeper discounts are explicitly tied to volume or strategic commitments.

| Anchor | Discount | Conditions |
|---|---|---|
| **Open** | **25% off list** | Standard channel partner pricing — offered to any agency engaging on Berlin for Agencies. No commitments required. |
| **Target** | **35–40% off list** | Locked for 18 months. Tied to volume commitment (e.g., 5 paid client seats by M6, 10 by M12). Discount steps back to 25% if volume floor isn't met. |
| **Floor** | **50% off list** | Only with bundled commitments — geographic exclusivity for 12 months, or a 12-month case study + co-marketing commitment. |
| **Walk** | Below 50% | Below 50% off list, Berlin walks. Below that, Berlin is underwriting the agency's customer acquisition with its own equity. |

**Structural rules that apply across the band:**

- The discount applies to **platform list price only**. LLM pass-through is at cost and is **non-negotiable** — never discounted, never bundled.
- **MFN-back clause:** if Berlin offers any other agency a deeper discount on equivalent volume, the agency on this contract gets matched.
- **No MFN-forward:** the agency does not get future product additions or new SKUs at the same discount rate.
- **Annual renewal subject to volume.** No perpetual lock. The discount level rebases each year against the partner's actual volume.
- **Enterprise-tier carve-out:** Heavy/Enterprise customer seats (corresponding to Heavy/Enterprise scope tiers on the Berlin + FDM ladder) carve out to a smaller discount of 15–20% — full channel rates would erode unit economics on those seats.

**Reference points used to set this band:** standard reseller 15–25%; premier/volume 25–35%; white-label 35–50%. Berlin's open at 25% sits at the top of the standard reseller range; the 50% floor is the white-label ceiling. Below that, Berlin walks.

---

## How to Use This Document

When crafting messaging for a specific audience:

1. Start from Berlin's core value proposition — an AI-native SEO/AEO agency: end-to-end platform underneath that owns Strategy, Execution, and Tools, with an assigned FDM on top who owns the relationship. **Berlin replaces the SEO agency a company would otherwise sign.**
2. Reference the three-pillar framework when the audience needs the structural argument.
3. Translate the structural description into the language of the audience's pain and ambition.
4. **Never add a capability that doesn't exist here.** If something feels missing, update this document first.

---

_Last updated: 2026-05-07_
