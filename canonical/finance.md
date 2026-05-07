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
- **Runway at planned go-to-market burn without raise:** ~2 months — making this raise critical

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

> **Phase:** First commercial cohort committed at launch. Berlin has gone through two repositionings as understanding of the market sharpened — first in late 2025 from a conversational SEO tool to programmable agentic workflow infrastructure; and second in April 2026 to an AI-native SEO/AEO agency (platform + Forward Deployed Marketer) that replaces the SEO agency customers would otherwise sign. The earlier Founding Partner cohort wound down, and one prior agency conversation (CSP Agency) did not close — both surfaced direct evidence that **traditional businesses, not agencies, are the right primary commercial target.** The new agency-shaped offering **publicly relaunched on April 28, 2026** with two customers committed pre-launch at $499/month each.

### MRR / ARR

- **Current platform: ~$998 MRR from launch** (~$12K ARR run rate) — two customers committed at launch on Berlin + FDM at $499/month each, both paying from the April 28, 2026 relaunch onward.
- $499/month is the **Entry tier** of Berlin's four-tier scope ladder (Entry $499, Mid $999–$1,999, Heavy $2,500–$4,000, Enterprise $5,000+). Tier placement is scope-driven; subsequent cohorts open at progressively higher tiers as scope and FDM service depth expand.
- **Legacy product:** No active MRR. Berlin had 5 total paid users historically (via Stripe), all on the pre-pivot product targeting a different ICP at legacy pricing (~$49/month avg). All have churned. Total historical revenue from the legacy product: **~$2,000 USD**.

### Customers

- 5 total historical paid users (pre-pivot ICP, all churned)
- **2 paying customers on the current platform** (Reach Psych, Csuite.so) at $499/month each
- **1 enterprise in active due diligence** (miniOrange) on Berlin + FDM

### Active Customers (Detail)

- **Reach Psych** (reachpsych.com) — Clinic in Bangalore. Committed at launch on Berlin + FDM at $499/month; **used v1 through its rough UX and chose to continue on v2 at launch** — direct proof both that the India field motion converts and that customers stay through a rough relaunch when the underlying value lands. Sits in the primary ICP.
- **Csuite.so** — SaaS company. Committed at launch on Berlin + FDM at $499/month. Early signal in the SaaS × Founder discovery cell.
- **miniOrange** (miniorange.com) — Enterprise identity and security. Engaged on Berlin + FDM. Currently in technical/compliance due diligence; actively working through their compliance team toward contract.

### Public-site logos vs. paying customers — disclosure discipline

The agentberlin.ai homepage displays additional logos (brandrep.io, wity.ai, elephantedge.ai, evoqins.com) for marketing purposes — **these are *not* paying customers and should not appear in investor or fundraising materials.** The only paying customers on the current platform are **Reach Psych and Csuite.so**. The Dr. Meena Gnanashekharan testimonial is tied to Reach Psych.

### Pipeline signals (prior Founding Partner engagement)

The earlier Founding Partner cohort (Fliki.ai, BlockSurvey, Search Indicators, Swedish agency partnership in progress, and others) produced the direct buyer signal that drove the April 2026 shift to product + FDM — buyers consistently asked for an assigned human owner alongside the platform rather than "build your own workflows." Those conversations have been reshaped by the new offering; active commercial discussions have narrowed to the customers above.

### Notable customers / logos

Reach Psych, Csuite.so, miniOrange.

### Case studies / testimonials

In progress. Anchored on Reach Psych (live, primary-ICP proof for the India field motion) and miniOrange (once compliance is resolved and contract signs).

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

## Burn Rate Evolution (Post-Raise)

Monthly burn scales in phases as the team grows and revenue offsets costs. The $1M raise lets us hire FDM capacity, India field reps, and a second engineer materially earlier than a smaller plan would allow.

| Period | Key cost additions | Monthly burn |
|--------|-------------------|--------------|
| **Month 1** (round closes, hiring kicks off) | Baseline operating costs only (infra $250, LLM $300, logistics $300, software $200) | ~$1,050 |
| **Month 2** (first wave of hires) | + Founder salary ($1,500) + 1 FDM ($2,500) + 1 India field rep ($1,500) | ~$6,500 |
| **Month 3** | + Full-stack engineer ($2,500) + LLM scaling (~$500) | ~$9,500 |
| **Month 4** | + 2nd FDM ($2,500) + GTM ramp ($1,000) | ~$13,000 |
| **Month 5** | + 2nd field rep ($1,500) + GTM ramp ($2,000) | ~$16,500 |
| **Month 6** | + 3rd FDM ($2,500) + LLM/infra scaling ($1,000) | ~$20,000 |
| **Month 7** | + 2nd engineer ($2,500) + GTM ($1,500) | ~$24,000 |
| **Month 8** | + 3rd field rep ($1,500) + GTM ($1,500) | ~$27,000 |
| **Month 9** | + 4th FDM ($2,500) + GTM ($500) | ~$30,000 |
| **Months 10–12** (steady state) | LLM/infra scaling, software, marginal GTM lift | $32K → $35K |

By M12 the team is roughly 11 people (4 FDMs, 3 India field reps, 2 engineers, founder, CMO). All hires India-based.

---

## Projections — 12-Month Base Case at $1M Raise

Revenue projection is anchored on **April 2026 actuals** ($998 MRR — 2 customers at $499/month) and assumes two sales-led growth engines:
1. Founder-led and FDM-supported sales into Berlin + FDM (primarily traditional businesses, India field sales as the distinctive channel)
2. Inbound discovery-grid customers (SaaS, eCom, Lead Gen × Founder/CMO) closing as cells convert

The model holds blended ARPU close to the $499 Entry tier through M12 with only modest cohort mix-shift lift toward the Mid tier. **Material walk up the scope ladder is upside, not base case.** ~5% monthly churn is implicit in net customer adds.

| Month | New adds | Total customers | Blended ARPU | MRR |
|-------|----------|-----------------|--------------|-----|
| 1 (Apr '26) | — | 2 *(actual)* | $499 | $998 |
| 2 (May) | 2 | 4 | $499 | $1,996 |
| 3 (Jun) | 3 | 7 | $510 | $3,570 |
| 4 (Jul) | 4 | 11 | $520 | $5,720 |
| 5 (Aug) | 5 | 16 | $540 | $8,640 |
| 6 (Sep) | 7 | 23 | $560 | $12,880 |
| 7 (Oct) | 10 | 33 | $580 | $19,140 |
| 8 (Nov) | 13 | 46 | $600 | $27,600 |
| 9 (Dec) | 17 | 63 | $620 | $39,060 |
| 10 (Jan '27) | 21 | 84 | $635 | $53,340 |
| 11 (Feb) | 26 | 110 | $645 | $70,950 |
| 12 (Mar '27) | 30 | 140 | $655 | $91,700 |

**Month 12 ARR run rate: ~$1.1M.**

ARPU mix shift is modest by design — most customers stay at the $499 Entry tier; the lift from $499 to ~$655 by M12 reflects ~25% of new cohorts entering at Mid-tier scope as FDM service depth expands. If a meaningful share of cohorts walk into Heavy ($2,500–$4,000) or Enterprise ($5,000+) tiers, that's upside above the base case.

---

## Cash Flow Projection

Starting cash: **$1,010,000** ($1M raise + $10K existing). The company reaches **cash-flow positive at month 8**, with a low point of ~$972K at month 7. **Berlin ends month 12 with more cash than was raised** (~$1.1M) — the round funds growth that compounds rather than just buying runway.

| Month | MRR | Monthly burn | Net cash flow | Cash balance |
|-------|-----|--------------|---------------|--------------|
| 0 (start) | — | — | +$1,010,000 | $1,010,000 |
| 1 | $998 | $1,050 | -$52 | $1,009,948 |
| 2 | $1,996 | $6,500 | -$4,504 | $1,005,444 |
| 3 | $3,570 | $9,500 | -$5,930 | $999,514 |
| 4 | $5,720 | $13,000 | -$7,280 | $992,234 |
| 5 | $8,640 | $16,500 | -$7,860 | $984,374 |
| 6 | $12,880 | $20,000 | -$7,120 | $977,254 |
| 7 | $19,140 | $24,000 | -$4,860 | $972,394 |
| 8 | $27,600 | $27,000 | +$600 | $972,994 |
| 9 | $39,060 | $30,000 | +$9,060 | $982,054 |
| 10 | $53,340 | $32,000 | +$21,340 | $1,003,394 |
| 11 | $70,950 | $33,500 | +$37,450 | $1,040,844 |
| 12 | $91,700 | $35,000 | +$56,700 | $1,097,544 |

In a downside scenario (slower customer acquisition, longer enterprise sales cycles, slower hiring ramp), the $1M provides **30+ months of runway** to iterate without fundraising pressure.

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

Berlin has spent ~10 months building product through three pivots with under $1,100/month in expenses and zero outside capital. The infrastructure is live, the product + FDM offering is defined, and the first commercial cohort is paying — Reach Psych and Csuite.so are live at $499/month each, with miniOrange in compliance due diligence. **What's missing is fuel:** the company is transitioning from validation to scale, and current cash reserves (~$10K) support approximately 2 months of operations at planned commercial spend levels.

The category just got validated in April 2026 by **Daydream's $15M Series A** — first institutional Series A in the AI-native SEO agency shape. The next 6–12 months will fill the bucket. **Berlin is the only other operator in this exact shape with paying customers in market today, and it sits in a structurally distinct lane (mid-market and traditional businesses at ~1/4 of agency cost).** This $1M raise funds the FDM capacity, India field sales reps, second engineering hire, and GTM distribution needed to compound that early-mover advantage into category-defining revenue before the lane fills in.

---

## Use of Funds

| Category | Allocation | Amount | Purpose |
|----------|:---------:|:------:|---------|
| **Hiring** | 40% | $400,000 | FDM capacity (4 by M9 — the offering is rate-limited by FDM headcount); India field sales reps (3 by M8); full-stack engineer M3, second engineer (platform / AI infra) M7. All India-based. |
| **GTM & Distribution** | 30% | $300,000 | India field sales operations (travel, on-ground); content production and community growth (r/agent_seo); micro-influencer program with affiliate payouts; SEO newsletter sponsorships; paid acquisition pilots; conferences and meetups; founder-led direct sales into enterprise accounts |
| **Engineering & Infrastructure** | 15% | $150,000 | Platform reliability, execution runtime improvements, expanding integration library, scaling crawlers (Snake.blue), hardening Berlin + FDM offering and Berlin for Agencies SKU, enterprise-readiness work; cloud and LLM infrastructure scaling (mitigated by continued runtime optimization driving per-task token consumption down) |
| **Reserve & Operations** | 15% | $150,000 | Strategic reserve for hiring iteration, unexpected costs, extended runway in downside scenarios; LLC → C-Corp conversion, SAFE legal costs, accounting, insurance, enterprise compliance prep (SOC 2 readiness) |

> Founder salary ($1,500/month) and the hiring/marketing ramp commence as the round closes; until then, funds allocated to these categories are held in reserve, extending runway and ensuring capital efficiency.

---

## Target Runway

Sized to reach **cash-flow positive by month 8**. In the base case, Berlin never exhausts the raise — revenue catches burn by November 2026, and the company **ends month 12 with ~$1.1M in cash (more than was raised)**. In downside, the $1M provides 30+ months of runway.

---

## Milestones This Funding Achieves

| Milestone | Target timeline | Success metric |
|-----------|:--------------:|----------------|
| Resolve miniOrange compliance, convert to paid | Month 1–2 | Contract signed on Berlin + FDM |
| Expand within first cohort | Month 1–3 | Reach Psych and Csuite.so on retention; expansion or upsell signal |
| First wave of FDM + field sales hires | Month 2–4 | 2 FDMs + 2 field reps + 1 engineer onboarded |
| India field sales producing repeat closes | Month 3–5 | 8+ additional traditional-business customers on Berlin + FDM closed via field motion |
| Produce 3–5 publishable customer case studies | Month 3–6 | Named logos with quantified results |
| Publish autonomous affiliate site case study | Month 2–4 | Verifiable organic traffic growth from fully autonomous site |
| Reach $25K MRR | Month 7–8 | ~45 customers; blended ARPU mix shifting toward Mid tier |
| Cash-flow positive | Month 8 | Revenue exceeds monthly burn (~$27.6K MRR vs ~$27K burn) |
| Reach $50K MRR | Month 10 | ~85 customers; clear repeatability on field + inbound motions |
| Seed-ready traction | Month 10–12 | $70K–$92K MRR, ~$1.1M ARR run rate, $1M+ in the bank |

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
  - Repositioned (April 2026) from agentic workflow infrastructure to end-to-end SEO/AEO platform + FDM offering; primary ICP narrowed to traditional businesses, with parallel agency-tier SKU retained but de-emphasized
  - **Public relaunch (April 28, 2026)** with first commercial cohort committed pre-launch: Reach Psych and Csuite.so on Berlin + FDM at $499/month each; ~$998 MRR live from launch

---

## Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| **Incumbents add AI/outcome features** | Medium | High | Berlin is built as an end-to-end outcome platform from day one. Incumbents (Ahrefs, Semrush) are data companies — rebuilding as agent-driven outcome-owning platforms requires fundamental architectural and business-model changes. Speed of execution and founder-market fit are key advantages. |
| **LLM platform risk (OpenAI, Anthropic)** | Low-Medium | Medium | Berlin is LLM-agnostic at the model layer. The agentic runtime can swap underlying models without changing what Berlin does for the customer. |
| **Mid-market adoption speed** | Medium | Medium | First commercial cohort closed at $499/month within weeks of repositioning, miniOrange in DD — early proof of both the field-sales-driven traditional-business motion and the enterprise motion. Buyers compare Berlin + FDM to an agency retainer or a hire — a faster, clearer buying decision than "should we add another SaaS subscription." |
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

_Last updated: 2026-05-07_
