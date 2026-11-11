# Market

> Canonical reference for the market **AEOxoxo** (aeoxoxo.ai) operates in: the AI-search inflection that creates the demand, the traffic and conversion shift that creates the urgency, the competitor landscape as data, and the external capital signals validating the category.
>
> **What AEOxoxo sells.** An AEO measurement and diagnosis product, delivered as an analyst-delivered consultation report. We measure whether a brand gets recommended in AI answers, diagnose why it does or does not, and hand over a ranked action register. See [`product.md`](product.md) for the offer and [`product/aeo-product-spec.md`](../product/aeo-product-spec.md) for the full specification — including the symptom/cause split and the evidence tiers this file borrows.
>
> **Names.** Brand and entity names are defined once, in [`company.md`](company.md) → *Names and what each one means*. Everything in this file describes AEOxoxo's market.
>
> **Ownership of open items.** Two of the largest questions in this file — market sizing and the ICP — are deliberately unanswered. See **Open decisions** at the end.

---

## How to read the source labels

This file mirrors the evidence discipline in [`product/aeo-product-spec.md`](../product/aeo-product-spec.md) (Appendix). Every quantitative claim carries a tag saying what kind of thing it is. The point is that a vendor's correlational study and a platform's own documentation are not the same class of fact, and a market file that flattens them produces bad decisions.

| Tag | Meaning |
|---|---|
| **[Documented]** | The platform or company states it in its own material. |
| **[Peer-reviewed]** | Published academic work or a controlled benchmark. |
| **[Observational]** | Large-scale measurement, usually by a vendor with an interest in the result. Shows a real pattern; establishes no mechanism. |
| **[Correlational]** | A relationship in data with no isolation of cause. The weakest tier we cite at all. |
| **[Analyst projection]** | A research-firm forecast. Directionally useful, precise to nobody. |
| **[Reported]** | Funding, revenue, valuation and client facts from press coverage or company statements. Believable, rarely audited. |
| **[Unsourced — needs re-citation]** | A number carried forward in our files whose original source was never recorded. Do not use externally until sourced. |
| **[Our observation]** | Ours, with no external source. Never cite as evidence. |

**Rule:** never present a vendor correlational number as an established mechanism, in this file or in anything derived from it.

---

## The AI search inflection: AEO/GEO

The structural shift that creates AEOxoxo's market is the movement of buyer discovery from ranked links to generated answers. Answer Engine Optimization (AEO) and Generative Engine Optimization (GEO) are the disciplines concerned with whether a brand appears — and is recommended — inside those answers. The market for this work did not meaningfully exist before 2024 and is estimated at roughly **$1B in 2025** [Analyst projection].

### The platform shift

- **ChatGPT:** 700M–1B weekly active users; among the most visited sites globally [Reported].
- **Google AI Overviews:** ~2B monthly users across 200+ countries, appearing on roughly **16–25% of U.S. queries** [Reported / Observational — the query-share figure varies by measurement vendor and query set].
- **50% of consumers** say they intentionally seek out AI-powered search engines (McKinsey, Aug 2025) [Observational — survey].
- AI-powered search is projected to influence **$750B in U.S. consumer spending by 2028** (McKinsey) [Analyst projection].
- AI search projected to capture **62%+ of total search volume by 2030** [Unsourced — needs re-citation]. Directionally consistent with the rest, but we cannot stand behind the figure.

### GEO/AEO market projections

Forecasts cluster around **30–50% CAGR**, reaching **$17B+ by the early 2030s** — Intel Market Research projects $17.02B by 2034 at 45.5% CAGR; Dimension Market Research projects $17–34B by 2034 [Analyst projection]. The spread between those two forecasts is itself the finding: nobody knows the size of this market, and the forecasts are being produced faster than the market is being measured.

### Why this matters for AEOxoxo

The problem the shift creates is not "we need more content." It is that **brands cannot tell whether they are being recommended, to whom, or why.** Traditional SEO tools answer a question about ranked links that is decreasingly the question being asked. The first generation of AEO tools answer *whether* a brand appears, on a dashboard, and largely stop there — the diagnosis of *why*, and what to do about it, is left to the customer.

That gap between measurement and explanation is where AEOxoxo's report sits. See [`product/aeo-product-spec.md`](../product/aeo-product-spec.md) §2.1–2.2 for the symptom/cause split that makes the distinction operational, and the explicit honest position that we can measure symptoms with confidence but cannot yet state which causes drive which symptoms — nor can anyone else.

---

## The traffic and conversion shift

The economics underneath the shift, which is what makes it urgent rather than merely interesting:

- Zero-click searches rose from **56% to 69% in roughly one year**; when AI Overviews appear, organic CTR drops around **61%** [Observational — vendor measurement; original citation not recorded in our files, **needs re-citation**].
- In Google AI Mode, zero-click rates reach approximately **93%** [Observational — vendor].
- AI-referred traffic is growing fast: **+620% YoY across content sites, +752% YoY for e-commerce** (BrightEdge, 2025) [Observational — vendor]. Growth off a small base; the absolute volume remains a fraction of organic search.
- AI-referred traffic is reported to convert at **5–23x** traditional organic rates (**14.2% vs 2.8%**, SEOmator) [Correlational — vendor]. **Treat with care.** This is a selection effect as much as a channel effect: someone arriving from a generated answer has already had their question answered and is further down the funnel. It is a real pattern, not a demonstrated causal property of the channel, and should never be sold as "AI traffic converts 5x better because it is AI traffic."
- **35–45% of Fortune 1000 companies** are said to have dedicated AEO programs, and **42% of B2B marketers** to be shifting budget from SEO to AEO [Unsourced — needs re-citation].

Related peer-reviewed and observational work in [`product/aeo-product-spec.md`](../product/aeo-product-spec.md) is more defensible than most of the above and should be preferred where the two overlap — notably that **~85.7% of URL-grounded citations point to third-party sites** [Observational — 167,551 citations, 128 brands] and that **monthly drift in which domains get cited runs ~40–60%** [Observational — Profound, 80,000 prompts]. The second of those is a market fact as much as a methodological one: it means point-in-time AI-visibility screenshots are not evidence, which is a structural argument for a measured, repeated, analyst-checked product over a dashboard reading.

---

## Key market trends

1. **Measurement is ahead of explanation.** The AEO tool market has converged fast on "track brand mentions across N engines." Almost nobody sells the diagnosis. This is the trend AEOxoxo is built against, and it is also the trend that will close — the incumbents in the head-on bucket have both the capital and the intent to move from monitoring into explanation.
2. **Answers are assembled mostly from third parties.** The majority of grounded citations point off the brand's own domain [Observational]. This relocates the work: a brand cannot fix its AI visibility purely by editing its own site, which is precisely why a diagnosis that spans off-site sources is worth paying an analyst for.
3. **Engine output is volatile.** ~40–60% monthly drift in cited domains [Observational] means visibility is a moving measurement, not a state. Single-shot audits are not defensible evidence; repeated measurement is a cost floor for anyone doing this honestly.
4. **Enterprise budget is moving before enterprise process exists.** Semrush's $50K+/yr customers grew **72% YoY** [Reported]; Conductor added 50+ enterprise AI customers in a single quarter [Reported]. Budget is being allocated to a discipline with no agreed methodology — favourable to a credible analyst-delivered product, and equally favourable to well-funded vendors selling confidence.
5. **The field has no headline number.** Nothing in AEO has become what domain authority was to SEO. Buyers ask for one; nobody has a defensible one (see [`product/aeo-product-spec.md`](../product/aeo-product-spec.md), Open questions #4). Whoever establishes a trusted metric captures the vocabulary of the category.
6. **Owning the data layer still matters.** Continuous crawl, a maintained keyword lake and a versioned page store reduce marginal cost per report and enable longitudinal claims that a per-query API vendor cannot make. See [`engineering.md`](engineering.md).

---

## Competitor landscape

This section is **data**, not positioning. The competitive *frame* — which of these are genuinely head-on against an analyst-delivered measurement and diagnosis report — is an open decision, stated at the end of this file. The bucketing below is descriptive.

### Head-on — AI visibility measurement and AEO/GEO products

These sell against the same buyer need AEOxoxo addresses: *tell me whether AI answers recommend me.* Several are far better capitalised.

| Company | Funding / scale [Reported] | What they do |
|---|---|---|
| **Profound** (tryprofound.com) | $155M total, ~$1B valuation (Sequoia, Kleiner Perkins, Lightspeed); 700+ enterprise customers incl. ~10% of the Fortune 500 | Brand visibility tracking across 10+ AI engines. Publishes large-scale citation research (80K-prompt volatility study; 27M-citation category analysis; 3.25B-citation language study) — research we cite in our own spec. Launched "Profound Agents" for campaign execution. The category's reference point. |
| **Peec AI** (peec.ai) | $21M total, $100M+ valuation (Singular); 1,300+ companies and agencies; **$4M+ ARR in 10 months** | European GEO leader, proprietary UI scraping. Clients incl. Axel Springer, Chanel, n8n, ElevenLabs, TUI. Dashboard-led visibility tracking. |
| **Relixir** | YC S25 | Autonomous GEO agent; scoped to GEO content publishing. |
| **Otterly AI** (otterly.ai) | n/a | AI-answer monitoring; distributed through the Semrush App Center. |
| **GenFlux** | $4.2M seed (Symbolic Capital) | Multi-engine tracking across 8+ AI platforms; analytics-only. |
| **Search Party** | $3.5M seed (Fuse VC) | Maps where AI engines source answers and activates workflows against those sources. Early stage. |

**Reading this bucket honestly:** Profound, Peec and Relixir are not adjacent to AEOxoxo — they are pointed at the same buyer, and Profound in particular is expanding from measurement toward action, which is the direction we occupy. What the differentiation argument rests on is unresolved. It cannot rest on funding or engine coverage, where we lose, and it cannot rest on the existence of measurement, which everything in this table already has. The candidates worth testing — bucket-level resolution, the symptom→cause chain, a confidence-scored action register, the longitudinal competitor field watch, analyst delivery — have not been checked against observed competitor capability. See **Open decisions**.

### Adjacent — content and execution platforms

| Company | Funding / scale [Reported] | What they do |
|---|---|---|
| **AirOps** (airops.com) | $62.1M total, $225M valuation (Greylock, Unusual Ventures, Wing) | Content engineering platform; modular workflows customers compose. Clients incl. Ramp, Webflow, Kayak, Klaviyo, Wiz. |
| **Frase** | Acquired by Copysmith (2022) | ~30,000 customers, plans from $39/mo. Content-centric, down-market. |
| **Maintouch** (maintouch.com) | YC S23, undisclosed | Explicitly anti-agency platform: end-to-end automation of strategy, content, programmatic SEO, link acquisition. No human owner on the customer side. |
| **Gushwork** (gushwork.ai) | $9M seed Feb 2026 (Susquehanna Asia VC lead, with Lightspeed, B Capital, Beenext, Sparrow, 2.2 Capital); ~$11M total | "Agentic AI marketing platform." AI content plus backlinks via a 200–300 partner-site network; subscriptions averaging **$800–$900/month**. |

These sell execution. AEOxoxo sells measurement and diagnosis. The relationship is closer to complementary than competitive today — a customer who buys our action register has to execute it somewhere — though nothing prevents an execution platform from adding diagnosis.

### Incumbent data platforms

The largest budgets in the space, all now shipping AI-visibility features.

| Company | Funding / scale [Reported] | AI posture |
|---|---|---|
| **Semrush** | $443.6M revenue (2025), 117K+ customers; **acquired by Adobe** — announced Nov 2025, expected close H1 2026 | "Semrush One" (Q4 2025) unified the traditional toolkit with an AI Visibility Toolkit. $50K+/yr customers grew 72% YoY. Publishes AEO research (ghost-citation study; backlinks/AI-visibility correlational study). Adobe ownership may slow independent product movement — or fund it heavily. Unknown. |
| **Ahrefs** | ~$149M revenue (2024, 49% YoY growth), bootstrapped | "Brand Radar" for AI-engine mentions, 100M+ prompt database. Publishes correlational AI-visibility research across 75,000 brands. |
| **Conductor** | $210M+ raised; $150M Series A 2021 at $525M valuation | Consolidator of legacy enterprise SEO (ContentKing 2022, Searchmetrics 2023). Forrester Wave Leader Q3 2025. 50+ enterprise AI customers added in Q3 2025 (BlackRock, Four Seasons, TD Bank). |
| **Botify** | $82.6M raised, Series C | Enterprise technical SEO at scale; contracts $75K–$400K+/yr. "PageWorkers" deploy 50+ optimisations per quarter. |

The incumbents' structural advantage is distribution and existing keyword data; their structural weakness is that AI visibility is a feature inside a dashboard sold to an SEO team, not a diagnosis delivered to a decision-maker. Whether that distinction survives contact with a buyer is untested.

### Service businesses building on AI

Not head-on with an analyst-delivered report, but relevant as demand evidence, as potential channel, and as potential buyers of our output.

| Company | Funding / scale [Reported] | Shape |
|---|---|---|
| **Daydream** (withdaydream.com) | $21M total ($15M Series A April 2026, WndrCo lead; First Round Capital, Basis Set Ventures continuing) | Explicitly an "AI-native agency for SEO": proprietary agents plus a dedicated human Growth Lead per customer, done-for-you at agency price points. |
| **Reach / Reach AI Labs** (usereach.ai) | ~$3.6M seed | "Not a tool, not an agency": platform + custom agents + a dedicated senior human per client. Retainers €5K/mo (<€2M revenue) → €7.5K/mo (€2–20M) → €12K/mo (>€20M), 3-month minimum. Clients incl. ColdIQ, Indie Campers, Carro, Fidelidade. |
| **Gushwork** | see above | Hybrid service-to-platform. |
| **Graphite** (graphite.io, Graphite Growth) | No funding on record; services-funded. 120+ people across 15+ countries, 100+ clients. Retainer with a 12-month minimum; pricing unpublished, third-party estimates $10–40K/month | Research-driven growth agency run by Ethan Smith. AEO service covers prompt research, citation-ready content, reputation, technical AEO, and offsite and Reddit work. Analyses data from the client's own tracking tool rather than selling measurement. Clients incl. Webflow, Notion, n8n, HoneyBook, Credit Karma, MasterClass; "Series B through public companies". |
| **Pedowitz Group** (pedowitzgroup.com) | Six-month programmes; published tiers Foundation $100–120K/yr, Growth $145–180K/yr, Enterprise $200K+/yr | B2B marketing agency. Sells an "AXO Diagnostic" (weeks 1–2, 40+ queries across Claude, ChatGPT, Perplexity and Gemini) as the front end of an AEO content-production engagement. |

> **Graphite publishes method, not just service.** Two of its findings bear on our own spec. **Grounding rate:** many prompt-tracking tools force web search, so every response comes back with citations. Unforced, only 58% of ChatGPT responses to entity-comparison prompts showed search evidence, and visibility differed by roughly 20 points on prompts that never search naturally (100 prompts × 100 responses × 2 settings) [Observational — Graphite, Aug 2026]. Their recommendation is to measure the share of runs in which a prompt triggers search, and not to rely on citation-based strategies where that share is low. If it holds, the third-party source map (spec C17) has little to act on for low-grounding prompts; this has not been assessed against the spec. **Sampling:** modelling visibility as Binomial with Wilson intervals, 10 responses per prompt gave a 5.6% mean absolute error, with little gained beyond that [Observational — Graphite, Apr 2026]. The spec lists its ~10-run target as a judgement call; this is a published basis for it. Their AEO proof is thinner than their method: of four published case studies only Webflow is AEO, and the other three are 2018–2023 SEO engagements republished in October 2025 [Documented].
>
> **Pedowitz's AXO Diagnostic, as published.** Eight named modules, of which four measure: problem vocabulary (the client's wording vs the buyer's), symptom-based query presence, persona variance (the same query across three personas) and competitive problem ownership. The other four are remediation, packaging, the LLM panel and trend history. They roll into a 0–100 score, `AXO = AI Presence × 0.38 + Problem Coverage × 0.32 + (100 − Persona Variance) × 0.15 + (100 − Content Gap) × 0.15`, tiered Strong Position (70–100), Developing (45–69) and Critical Gap (0–44) [Documented]. Presence and coverage carry 70% of the score, competitive ownership carries none, and the persona angle is a 15% penalty term. No sampling, repeat-run or measurement definitions are published, and three different versions of the framework appear across their own pages [Our observation].

> **Why Daydream reads as a different category.** Daydream sells continuous done-for-you execution with an embedded human Growth Lead at agency price points; Reach sells the same shape on a monthly retainer. AEOxoxo sells a bounded, analyst-delivered measurement and diagnosis engagement, with no embedded humans and no claim to replace an agency. On that reading both are demand signals and plausible *customers* for a diagnosis they do not want to build. The competitive frame as a whole is unresolved (see **Open decisions**), so treat this as the current reading rather than a settled classification.

### Not competitors

- **DIY stacks** (n8n, Make, Zapier, DataForSEO, raw LLM prompting). Require engineering effort, provide no structured measurement, and cannot produce repeated, controlled runs. They are what a technical marketer does *instead* of buying — a real substitute at the low end, not a competing vendor.
- **In-house teams.** Not a distinct alternative to size; they are the buyer.

### Figures that don't survive checking

Widely repeated and wrong, as of a check on 14 September 2026. Don't carry these into anything external.

- **Daydream.** The "$70M ARR with fewer than 20 employees" figure belongs to OpenArt, a Daydream customer; Daydream's own ARR is not disclosed. A different company also called Daydream (Julie Bornstein's AI e-commerce search, $50M seed, June 2024) is unrelated, so don't merge the funding.
- **Graphite.** `graphite.io` is the growth agency above. `graphite.dev` is a code-review tool (~$52M raised, ~$5.3M ARR). Most "Graphite" revenue and funding figures in the usual databases belong to the code-review company.
- **AirOps.** ~$60–62.5M total, with no round after the November 2025 Series B. Sacra's "May 2026 round of $55.5M" and "$118M total" look like misreadings of a cumulative figure. Claims that AirOps lacks SOC 2 are false; it publishes SOC 2 Type II.
- **Gushwork.** Not a Y Combinator company. The "1000+ companies" headline doesn't reconcile with 300+ paying customers and ~$1.5M ARR as of February 2026; treat the customer count as softer than the revenue.
- **Agency pricing estimates.** Daydream's ~$15K/month and Graphite's $10–40K/month come from competitor-published comparison blogs with their own SEO incentives. Directionally plausible, not vendor-confirmed.

---

## On the competitive positioning matrix

**There is no competitive positioning matrix.** Building one honestly requires hands-on evaluation of Profound and Peec; a matrix on capability lines cannot be filled in without inventing scores, and asserting scores from marketing pages would be exactly the kind of claim [`product/aeo-product-spec.md`](../product/aeo-product-spec.md) §2.2 forbids.

Building it credibly means rating Profound, Peec, Relixir, Semrush and Ahrefs on axes such as: resolution of the measurement (single score vs. bucket-level); whether the funnel from eligible → cited → named → recommended is separated at all; whether a symptom is ever traced to a cause; whether confidence in a diagnosis is disclosed; whether competitor change is tracked longitudinally; and whether a human analyst reviews the output. We have opinions about most of those cells and verified evidence for almost none of them.

**Prerequisite:** a hands-on evaluation of at least Profound and Peec against a real brand, producing observed rather than assumed capability data. Listed in **Open decisions**.

---

## Market sizing — to be re-derived

**There is no TAM/SAM/SOM in this file, deliberately.** Market sizing has not been derived for this product. It must be sized against the AEO/GEO market and the analyst-delivered report motion.

What a defensible sizing has to be built from:

- The **AEO/GEO market** specifically — currently ~$1B (2025), forecast to $17B+ by the early 2030s at 30–50% CAGR [Analyst projection]. These are the only top-down figures pointed at the right market, and the forecast spread ($17B to $34B for the same year) means they can frame an argument but cannot carry one.
- A **bottom-up build against the actual motion**: an analyst-delivered consultation report has a per-engagement price, an analyst-time cost floor, and a natural cadence (one-off diagnosis, or a repeated engagement where the longitudinal field watch becomes the value). Volume is bounded by analyst capacity divided by whatever the substrate automates. That build cannot be done before the pricing and the delivery cadence are set — see [`gtm.md`](gtm.md).
- A **defined ICP**, which does not exist yet (below).

**Blocked on the ICP, which is genuinely open.** No customer profile is asserted anywhere in this file. [`product/aeo-product-spec.md`](../product/aeo-product-spec.md) §3.1 names B2B SaaS at roughly $5–10M ARR across 4–5 engagements — **that is a pilot constraint chosen to make learning tractable, not an ICP claim, and it should not be quoted as one.** The pilots exist partly to produce the evidence an ICP decision needs: who feels the pain acutely, who will pay for diagnosis without bundled execution, and who has a decision-maker for whom "the AI recommends your competitor" is a board-level fact rather than a marketing-team curiosity.

---

## "Why now?"

**What changed.** Answer engines became a primary discovery surface for buyers, and brands lost the instrumentation they had for the previous surface. Rank tracking answers a question about ranked links; it says nothing about whether an assistant recommends you, cites you without naming you, or cautions against you. The measurement gap arrived faster than the tooling.

**Why this was impractical two to three years ago.**

- The surfaces did not carry meaningful volume. AI Overviews and AI Mode did not exist at scale; there was nothing to measure and no budget to measure it.
- The platforms exposed nothing. Search Console's Generative AI Performance report separating AI Mode and AI Overview impressions, Bing's citation-level data and sampled grounding queries, and OpenAI's referral tagging are all recent [Documented] — see [`product/aeo-product-spec.md`](../product/aeo-product-spec.md) A1.
- The research base did not exist. The volatility, citation-source and language studies that make a rigorous methodology arguable were published in 2025–26.
- Running hundreds of prompts repeatedly across engines, crawling every competitor weekly and diffing the results was not economically sensible without the substrate to do it cheaply.

**What is accelerating adoption.** Enterprise budget is moving to AEO ahead of any agreed methodology; zero-click behaviour is degrading the outcomes marketing teams are measured on; and the volatility of AI answers means the question is never answered once. The last point is a durable demand argument for repeated measurement rather than a one-time audit.

---

## VC validation

Where top-tier capital has deployed in AI search optimisation [all Reported]:

- **Profound** — ~$1B valuation reached in roughly 18 months (Sequoia, Kleiner Perkins, Lightspeed).
- **AirOps** — $225M valuation, Greylock-led.
- **Peec AI** — tripled to $100M+ valuation in four months; $4M+ ARR in ten months.
- **Daydream** — $15M Series A (April 2026, WndrCo lead), $21M total.
- **Reach AI Labs** — ~$3.6M seed.
- **Gushwork** — $9M seed (Feb 2026), ~$11M total.
- **Semrush** — acquired by **Adobe** (announced Nov 2025), the clearest strategic signal that incumbent marketing-software players consider this space structural rather than a feature.
- Total venture funding into AI search infrastructure reported at **$225.8B in 2025** [Reported — a very broad definitional bucket; do not quote as AEO-specific].

**Read this both ways.** It validates that the category is real and being capitalised. It also means AEOxoxo enters a market where the reference vendor is worth ~$1B and the European leader is growing revenue faster than we can. Capital validation and competitive difficulty are the same fact.

---

## Defensibility — what actually holds

The defensibility argument available today rests on the engineering substrate, and it is a narrow claim. Detail in [`engineering.md`](engineering.md).

**What the substrate genuinely provides:**

- **Longitudinal competitor observation.** Crawling entire competitor sites on a weekly cadence and diffing them — every new page, every changed line — is a capability that requires a crawler, a versioned page store and a semantic index to be useful. Tools that do this for a customer's *own* site exist; we know of nothing doing it across an entire competitive set ([`product/aeo-product-spec.md`](../product/aeo-product-spec.md) §2.6). This is the strongest single asset, and its value is time-dependent: the first run is only a baseline.
- **Marginal cost per report.** An owned crawler, keyword lake and page store mean the incremental cost of another client's diagnosis is small once built, which is what allows depth to be priced within reach.
- **Repeated, controlled measurement at cost.** Given ~40–60% monthly citation drift, defensible measurement means many runs per prompt across time. Cost per run determines whether that is affordable or theoretical.

**What the substrate does not provide, and we should not pretend otherwise:**

- A competitor with a competent engineering team can build crawl-and-diff quickly. [`product/aeo-product-spec.md`](../product/aeo-product-spec.md) §2.6 states this directly: the defensible part is **knowing where to look and what a change means**, not the crawling. Describe the capability, never the method.
- Nothing in the substrate is a barrier to Profound or Semrush, who have more capital and existing crawl and keyword infrastructure of their own.
- The compounding asset is the **judgement layer** — the cause taxonomy, the topic and bucket clustering, the accumulated evidence about which causes actually move which symptoms across a portfolio of clients. That is real, it compounds with every engagement, and today it is almost entirely un-accumulated. We have a plan for a moat, not a moat.

**Honest summary:** the substrate lowers cost and enables one capability others do not currently offer. Whether that is a defensibility argument or merely a head start is unresolved and is listed below.

---

## Open decisions

These are decisions, not research tasks. Each blocks something downstream.

1. **Market sizing must be derived from scratch.** Against the AEO/GEO market rather than SEO software, and bottom-up against the analyst-delivered report motion — price per engagement, analyst capacity, repeat cadence. Blocked on pricing ([`gtm.md`](gtm.md)) and on the ICP.

2. **The ICP is undecided and must not be assumed.** The pilot profile in [`product/aeo-product-spec.md`](../product/aeo-product-spec.md) §3.1 is a pilot constraint. The real question is which buyer treats "AI answers recommend your competitor" as a decision-grade fact and will pay for diagnosis without bundled execution. The 4–5 pilots should be run to answer this, and the answer should be written down explicitly rather than inherited from the pilot's convenience sample.

3. **The competitive frame needs restating.** Profound, Peec and Relixir are head-on rather than adjacent — same buyer, same question, substantially more capital. What the differentiation argument rests on is unresolved. **This needs evidence:** a hands-on evaluation of Profound and Peec against a real brand, producing observed capability data. Until that exists, no positioning matrix gets built.

4. **Is the substrate the defensibility argument?** It lowers marginal cost and enables cross-competitor field watch. It is not a barrier to a well-funded competitor, and the genuinely compounding asset — accumulated evidence about which causes move which symptoms — does not exist yet. Decide whether we claim defensibility from the substrate, from the judgement layer we intend to build, or from neither, and say so consistently across [`product.md`](product.md), [`engineering.md`](engineering.md) and [`gtm.md`](gtm.md).

5. **The unsourced numbers.** Several figures in this file (the 62% search-volume projection, the zero-click 56%→69% shift, Fortune 1000 AEO-programme adoption, the 42% B2B budget-shift figure) have no recorded source. Either source them or stop using them. They are currently tagged and must not appear in external material as they stand.

---

_Last updated: 2026-11-11 — added Graphite, Pedowitz Group and the figure corrections from the 14 September 2026 competitor research._
