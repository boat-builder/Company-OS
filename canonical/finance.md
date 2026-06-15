# Finance

> Canonical reference for Berlin's commercial state: revenue model, current traction and metrics, financial state, projections, the fundraise structure, the cap table, and risks/mitigations.
>
> Ephemeral pipeline state lives in `sales/pipeline.md` and is pruned as deals close into the canonical traction count below.

---

## Current State (Snapshot)

- **Cash on hand:** ~$10,000
- **Live MRR:** ~$998 (Reach Psych + Csuite.so at $499/month each; both committed pre-launch and paying from the April 28, 2026 relaunch onward)
- **Legacy MRR:** $0 (all historical paid users on the pre-pivot product have churned)
- **Monthly burn (current build phase):** ~$1,050
  - Cloud infrastructure: ~$250
  - LLM API costs: ~$300
  - Logistics & transportation: ~$300
  - Software subscriptions: ~$200
  - Founder salary: $0 (founder not taking salary during this phase)
- **Runway at current burn (pre-raise):** ~10 months

---

## Revenue Model

- **Subscription with usage-based credits.** Customers subscribe to a tier that includes a base allocation of execution credits (the work Berlin performs on their behalf); additional credits are available on demand. **LLM compute is passed through at cost.**
- **Pricing principle (the anchor):** Berlin's price for any given customer is anchored at approximately **one-quarter of what an agency would charge for the same scope of work.** Scope determines the absolute number; the agency-fraction anchor stays constant. Full pricing detail (4-tier scope ladder + agency-tier channel discount band) lives in `product.md`.
- **Pricing discovery roadmap:** Pricing is being walked up cohort by cohort. The first paid cohort sits at $499/month — deliberately the Entry tier — to validate fit and produce a clean reference cohort. The next tier opens at ~$999/month with expanded scope, and tiers continue climbing until Berlin finds the price ceiling at which inbound volume still supports growth. **Deliberate price discovery cohort by cohort, not "cheap at launch."** The 30-day "match or beat your current agency" guarantee on the public site reinforces the agency-fraction frame explicitly.

### Average contract value (ACV)

First commercial cohort is live at **$499/month** ($5,988/year ACV). Two paying customers on Berlin + FDM (Reach Psych, Csuite.so); miniOrange in DD on the same offering. Blended ARPU is expected to rise as the next cohort opens at $999 and subsequent cohorts climb up the agency-fraction ladder.

### Gross margin

**~80% on core platform infrastructure** (data engine, integrations, execution runtime, crawlers). LLM tokens provided at cost (zero margin) — a strategic decision to maintain pricing parity with native LLM apps and remove adoption friction. Blended gross margin trends toward the 80% infrastructure margin as token costs are amortized across higher-tier customers and continued internal optimization of the agentic runtime drives down per-task token consumption.

### Unit economics

- **CAC:** Not yet measurable at scale. Current customers acquired through founder-led inbound (LinkedIn content, conferences, network). No outbound sales spend to date.
- **LTV:** Too early to calculate.
- **LTV:CAC ratio / payback period:** TBD as customer base scales.

---

## Traction & Metrics

> **Phase:** First commercial cohort committed at launch. Berlin has gone through two repositionings as understanding of the market sharpened — first in late 2025 from a conversational SEO tool to programmable agentic workflow infrastructure; and second in April 2026 to an AI-native SEO/AEO agency (platform + Forward Deployed Marketer) that replaces the SEO agency customers would otherwise sign. The earlier Founding Partner cohort wound down, and one prior agency conversation (CSP Agency) did not close — both surfaced direct evidence that **end customers, not agencies, are the right primary commercial target.** The new platform + FDM offering **publicly relaunched on April 28, 2026** with two customers committed pre-launch at $499/month each. (ICP focus has since been reset to SEO-literate SaaS — see `customers.md`.)

### MRR / ARR

- **Current platform: ~$998 MRR from launch** (~$12K ARR run rate) — two customers committed at launch on Berlin + FDM at $499/month each, both paying from the April 28, 2026 relaunch onward.
- $499/month is the **Entry tier** of Berlin's four-tier scope ladder (Entry $499, Mid $999–$1,999, Heavy $2,500–$4,000, Enterprise $5,000+). Tier placement is scope-driven; subsequent cohorts open at progressively higher tiers as scope and FDM service depth expand.
- **Legacy product:** No active MRR. Berlin had 5 total paid users historically (via Stripe), all on the pre-pivot product targeting a different ICP at legacy pricing (~$49/month avg). All have churned. Total historical revenue from the legacy product: **~$2,000 USD**.

### Customers

- 5 total historical paid users (pre-pivot ICP, all churned)
- **2 paying customers on the current platform** (Reach Psych, Csuite.so) at $499/month each
- **1 enterprise in active due diligence** (miniOrange) on Berlin + FDM

### Active Customers (Detail)

- **Reach Psych** (reachpsych.com) — Clinic in Bangalore. Committed at launch on Berlin + FDM at $499/month; **used v1 through its rough UX and chose to continue on v2 at launch** — proof that customers stay through a rough relaunch when the underlying value lands. Acquired under earlier positioning; predates the June 2026 ICP reset.
- **Csuite.so** — SaaS company. Committed at launch on Berlin + FDM at $499/month. The one live account that sits inside the current SaaS focus.
- **miniOrange** (miniorange.com) — Enterprise identity and security. Engaged on Berlin + FDM. Currently in technical/compliance due diligence; actively working through their compliance team toward contract.

### Public-site logos vs. paying customers — disclosure discipline

The agentberlin.ai homepage displays additional logos (brandrep.io, wity.ai, elephantedge.ai, evoqins.com) for marketing purposes — **these are *not* paying customers and should not appear in investor or fundraising materials.** The only paying customers on the current platform are **Reach Psych and Csuite.so**. The Dr. Meena Gnanashekharan testimonial is tied to Reach Psych.

### Pipeline signals (prior Founding Partner engagement)

The earlier Founding Partner cohort (Fliki.ai, BlockSurvey, Search Indicators, Swedish agency partnership in progress, and others) produced the direct buyer signal that drove the April 2026 shift to product + FDM — buyers consistently asked for an assigned human owner alongside the platform rather than "build your own workflows." Those conversations have been reshaped by the new offering; active commercial discussions have narrowed to the customers above.

### Notable customers / logos

Reach Psych, Csuite.so, miniOrange.

### Case studies / testimonials

In progress. Anchored on Reach Psych (live) and miniOrange (once compliance is resolved and contract signs).

---

## Flagship Case (Substrate Proof) — 2.5M Pages, 12,000 Broken URLs, 15 Hours

The clearest demonstration of Berlin's engineering substrate working in practice — **and the result that drove the April 2026 repositioning.**

An e-commerce operator running a **2.5 million page catalogue across 6 countries** had **12,000 soft 404s** — pages returning a 200 status but serving nothing. Redirects had to stay within each country's site (a 200K+ row routing problem with country-aware constraints). Berlin's agents mapped the full link graph, classified each broken URL, and produced a country-aware redirect report in **15 hours**. A traditional agency had previously scoped the same work at **6 months and 600+ engineering hours**.

| Dimension | Traditional Agency Scope | Berlin |
|---|---|---|
| Pages audited | 2,500,000 | 2,500,000 |
| Broken URLs classified | 12,000 | 12,000 |
| Scoped delivery time | ~6 months | **15 hours** |
| Engineering hours | 600+ | **< 15** |
| Country-aware routing | Manual | **Automated** |

**What this proves and why it matters:**

This work was delivered as a **pilot underneath an agency** running Berlin against their own client work — **substrate proof, not commercial traction**, and explicitly the result that taught us to *be* the agency rather than power one. The April 2026 repositioning to Berlin + FDM came directly from this case. The substrate (Snake.blue crawl, cached data, proprietary data routing architecture, ranking-signal coverage) is the structural reason one Berlin FDM ships agency-scoped outcomes in agency-fraction time — that's where the **~1/4 of agency cost pricing anchor** comes from, not from a discount strategy.

---

## Burn Rate & Projections

The earlier post-raise burn schedule, 12-month revenue projection, and cash-flow projection have been retired. They were built on the now-defunct assumptions — a multi-wave India field-sales + multi-FDM hiring plan and the discovery-grid GTM — that no longer hold after the June 2026 ICP reset (see `customers.md`). There is no current detailed burn rate or hiring-schedule plan beyond the present build-phase burn (~$1,050/month, above) and the immediate plan to **hire 2 FDMs**. Updated projections will be rebuilt once the SaaS experiments produce a validated ICP; no replacement figures are recorded here in the meantime.

---

## The Round — Two Tranches

Berlin is raising in two tranches:

### 1. $50K angel/bridge round — open now

- **Price:** $50K-for-1% (effective **$5M post-money cap**) — half the seed cap, structured as an early-trust discount for angels who commit before the seed opens.
- **Status:** $25K committed of $50K open (May 2026). Use the existing commit as social proof when closing remaining angels.
- **Hard ceiling for any single angel:** 0.5% (i.e., max $25K-equivalent check on this tranche).
- **External labeling:** call this "angel round" or "bridge" — **never "friends & family."** Likewise, the $1M tranche below is "seed," not "pre-seed."
- **Structural fairness rule:** any non-cash variants (e.g., services-for-equity) convert into the same SAFE at the same cap as cash angels — never at a different price. **Do NOT price an angel-round services SAFE at the $10M seed cap** — that breaks the angel-round discount logic and creates an explainability problem with cash angels who paid the $5M-cap price.
- **Services-for-equity anchor:** when a contributor wants to convert services into the angel SAFE, use **$5/hr internal rate × hours delivered**, true-up quarterly into SAFE units at the $5M cap. The 0.5% per-angel ceiling holds regardless of how the rate or hours are framed — that's the walk-away wall.

### 2. $1M pre-seed/seed — opens after the angel tranche closes

- **Amount:** $1,000,000
- **Instrument:** SAFE (post-money)
- **Valuation cap:** $10M post-money
- **Implied dilution:** 10% (industry-standard pre-seed dilution for AI-native vertical SaaS in 2026)
- **Discount:** None
- **Pro rata rights:** Yes
- **Minimum check size:** $50,000

The angel cap is set deliberately at **2x the seed price** as the early-trust discount.

---

## Why Now — The Funding Inflection

Berlin has spent ~10 months building product through three pivots with under $1,100/month in expenses and zero outside capital. The infrastructure is live, the product + FDM offering is defined, and the first commercial cohort is paying — Reach Psych and Csuite.so are live at $499/month each, with miniOrange in compliance due diligence. **What's missing is fuel:** the company is transitioning from validation to scale, and current cash reserves (~$10K) support roughly 10 months at the present build-phase burn — but not the hiring and GTM investment scaling requires.

The category just got validated in April 2026 by **Daydream's $15M Series A** — first institutional Series A in the AI-native SEO agency shape. The next 6–12 months will fill the bucket. **Berlin is the only other operator in this exact shape with paying customers in market today, and it sits in a structurally distinct lane (platform + FDM at ~1/4 of agency cost).** This $1M raise funds the FDM capacity, engineering, and GTM distribution needed to compound that early-mover advantage into category-defining revenue before the lane fills in.

---

## Use of Funds

| Category | Allocation | Amount | Purpose |
|----------|:---------:|:------:|---------|
| **Hiring** | 40% | $400,000 | FDM capacity — the offering is rate-limited by FDM headcount; the immediate plan is to **hire 2 FDMs**, plus engineering capacity. |
| **GTM & Distribution** | 30% | $300,000 | Content production and community growth (r/agent_seo); micro-influencer program with affiliate payouts; SEO newsletter sponsorships; paid acquisition pilots; conferences and meetups; founder-led direct sales |
| **Engineering & Infrastructure** | 15% | $150,000 | Platform reliability, execution runtime improvements, expanding integration library, scaling crawlers (Snake.blue), hardening Berlin + FDM offering and Berlin for Agencies SKU, enterprise-readiness work; cloud and LLM infrastructure scaling (mitigated by continued runtime optimization driving per-task token consumption down) |
| **Reserve & Operations** | 15% | $150,000 | Strategic reserve for hiring iteration, unexpected costs, extended runway in downside scenarios; LLC → C-Corp conversion, SAFE legal costs, accounting, insurance, enterprise compliance prep (SOC 2 readiness) |

> Founder salary ($1,500/month) and the hiring/marketing ramp commence as the round closes; until then, funds allocated to these categories are held in reserve, extending runway and ensuring capital efficiency.

---

## Target Runway

The detailed month-by-month runway model was retired with the burn and projection tables above (it depended on the now-defunct India field-sales + multi-wave hiring plan). At the present build-phase burn (~$1,050/month), existing cash is ~10 months of runway; the $1M raise is sized to fund the FDM hires, engineering, and GTM needed to scale. A refreshed runway model will be rebuilt alongside updated projections once the SaaS experiments produce a validated ICP.

---

## Milestones This Funding Achieves

| Milestone | Target timeline | Success metric |
|-----------|:--------------:|----------------|
| Resolve miniOrange compliance, convert to paid | Month 1–2 | Contract signed on Berlin + FDM |
| Expand within first cohort | Month 1–3 | Reach Psych and Csuite.so on retention; expansion or upsell signal |
| Hire 2 FDMs | Month 2–4 | 2 FDMs onboarded; delivery capacity expanded |
| Validate the SaaS ICP hypothesis | Month 2–5 | Consistent pattern across ≥5 qualified SaaS conversations (see `customers.md` promotion criteria) |
| Produce 3–5 publishable customer case studies | Month 3–6 | Named logos with quantified results |
| Publish autonomous affiliate site case study | Month 2–4 | Verifiable organic traffic growth from fully autonomous site |

---

## Cap Table & Legal

### Current Ownership

| Shareholder | Ownership | Type | Notes |
|-------------|:---------:|------|-------|
| Sherin Thomas | 100% | Sole Member, LLC | Founder & CEO |

The company is **100% founder-owned** with no outside investors, no outstanding SAFEs, no convertible notes, and no option pool. The cap table is completely clean. *(In progress: $50K angel/bridge tranche at $5M cap — $25K soft-circled / committed of $50K open as of May 2026, not yet executed.)*

### Entity Structure

- **Current entity:** Agentic World, LLC — Delaware LLC. Full details in `company.md`.
- **C-Corp conversion:** TBD — open to investor guidance. Founder is prepared to convert to Delaware C-Corp if required by lead investor or accelerator. SAFE documents can include a conversion covenant.

### Investor History

- **Prior fundraising:** None — fully bootstrapped to date
- **Existing investors:** None (angel tranche in progress)
- **Outstanding SAFEs / convertible notes:** None executed yet ($25K soft-circled)
- **Advisor equity / grants:** None

### Equity & Option Pool

- **Current option pool:** None
- **Planned option pool:** 10% reserved for future hires and advisors, established at C-Corp conversion
- **409A valuation:** N/A (LLC; 409A completed at C-Corp conversion if applicable)

### Intellectual Property

- **IP ownership:** All IP created by the sole founder and assigned to Agentic World, LLC. No third-party contributors.
- **IP assignments complete:** Yes — sole founder is sole member of the LLC.
- **Open-source dependencies:** Standard permissive licenses (MIT, Apache 2.0). No copyleft (GPL) in production code.
- **Third-party IP / licensing:** DataForSEO API (commercial), LLM provider APIs (OpenAI, Anthropic) under standard commercial terms.
- **Patents:** None.

### Legal Matters

- **Pending litigation:** None
- **Regulatory considerations:** Berlin's crawler infrastructure collects publicly available web data only. GDPR and CCPA compliance addressed through (1) crawling only publicly accessible pages, (2) respecting robots.txt, (3) no collection of personal data, (4) data processing within standard cloud infrastructure with appropriate security controls. Formal compliance documentation to be completed as part of enterprise readiness.
- **Material contracts:** DataForSEO API subscription. Active paid customer agreements with Reach Psych and Csuite.so on Berlin + FDM at $499/month each. Standard cloud infrastructure agreements. Earlier Founding Partner design-partner arrangements (non-binding) have wound down.
- **Terms of service / privacy policy:** Drafted and live on site. To be reviewed by legal counsel as part of enterprise readiness and fundraise preparation.

---

## Social Proof & Milestones

- **Press / media:** Thought-leadership content on agentic SEO gaining traction with industry influencers; 16K+ impressions on a single LinkedIn post picked up by SEO and AI community voices.
- **Awards / recognitions:** None yet.
- **Accelerator participation:** None yet — evaluating accelerator programs as part of fundraise strategy.
- **Notable milestones achieved:**
  - Intelligence infrastructure built (80+ ranking signals, automated prioritization, GSC/GA integrations)
  - End-to-end SEO/AEO execution stack live
  - Proprietary data routing architecture live
  - Integrated keyword database (sourced from leading providers, cached in own DB) and proprietary crawlers operational
  - Repositioned (April 2026) from agentic workflow infrastructure to end-to-end SEO/AEO platform + FDM offering, with parallel agency-tier SKU retained but de-emphasized (ICP focus subsequently reset to SEO-literate SaaS in June 2026 — see `customers.md`)
  - **Public relaunch (April 28, 2026)** with first commercial cohort committed pre-launch: Reach Psych and Csuite.so on Berlin + FDM at $499/month each; ~$998 MRR live from launch

---

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **Incumbents add AI/outcome features** | Medium | High | Berlin is built as an end-to-end outcome platform from day one. Incumbents (Ahrefs, Semrush) are data companies — rebuilding as agent-driven outcome-owning platforms requires fundamental architectural and business-model changes. Speed of execution and founder-market fit are key advantages. |
| **LLM platform risk (OpenAI, Anthropic)** | Low-Medium | Medium | Berlin is LLM-agnostic at the model layer. The agentic runtime can swap underlying models without changing what Berlin does for the customer. |
| **Adoption speed** | Medium | Medium | First commercial cohort closed at $499/month within weeks of repositioning, miniOrange in DD — early proof of the platform + FDM motion. Buyers compare Berlin + FDM to an agency retainer or a hire — a faster, clearer buying decision than "should we add another SaaS subscription." |
| **AI search landscape evolving rapidly** | High | Medium | Berlin's architecture treats strategy and execution as first-class with the underlying tool layer swappable — as AI search evolves, Berlin updates default playbooks without customers having to rebuild anything. Proprietary crawl, integrated keyword data, and AEO/GEO coverage position us ahead. |
| **Data privacy / crawler compliance** | Low-Medium | Medium | Crawlers only access publicly available data, respect robots.txt, collect no personal information. GDPR/CCPA compliance roadmap in progress for enterprise readiness. |
| **Key-person risk** | Low-Medium | High | Leadership has expanded beyond the single founder — Rhea David has joined as CMO. Additional GTM and engineering hires planned with this raise. Product architecture is modular and well-documented; founder has track record of operating lean and shipping through multiple pivots. |
| **Fundamental shift in how the web works** | Medium | High | Regardless of medium, users will always need to search for and purchase things; brands will always need to be discoverable. Berlin's architecture is outcome-first, not SEO-mechanic-first — strategy and execution layers are decoupled from any particular search engine's ranking algorithm. Can retarget toward whatever the web becomes (agent-to-agent commerce, conversational discovery) without a fundamental rebuild. |
| **AI-native competitors expand into end-to-end SEO/AEO** | Medium | High | Profound has begun expanding beyond monitoring into execution; Peec AI, Relixir, Search Party could follow. **Mitigation:** these platforms are monitoring-first and content-first by architecture — expanding to cover strategy, full execution, and the underlying tool layer is fundamentally different from bolting on an "agents" feature. The same architectural constraint that limits incumbents applies here. |

---

## Referenced State

- **Ephemeral pipeline state:** `sales/pipeline.md` — active deals in motion that haven't yet promoted to canonical traction count above.
- **Funding-page deck:** `finance/funding-page/index.html` — investor-facing HTML deck. **SYNC CHECK:** when figures here change, verify the deck reflects the same numbers (the deck is a curated subset, not a parity copy).

---

_Last updated: 2026-06-04 (ICP reset) — retired the India field-sales motion and the defunct forward models (post-raise burn schedule, 12-month revenue projection, cash-flow projection) that depended on it and on the multi-wave hiring plan; there is no current detailed burn/hiring plan beyond present build-phase burn (~$1,050/mo) and the plan to **hire 2 FDMs**. Reconciled use-of-funds, target runway, milestones, traction notes, why-now, and risks to the June 2026 SaaS-focused ICP reset (see `customers.md`). Round structure, cap table, and legal unchanged. No replacement projection figures were invented._

_2026-05-07 — prior version._
