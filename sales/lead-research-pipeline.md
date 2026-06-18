# Lead Research Pipeline — Discover → Qualify → Enrich → CRM

**Purpose.** A repeatable, tool-agnostic instruction set for an AI agent that takes a lightly-specified *target* and turns it into a CRM record: it discovers the company and the right people, qualifies them against an ICP supplied at runtime, and — if they fit — enriches them with the raw material needed to write a personalized DM. This document is self-contained: the full SEO/AEO profiling workflow is embedded here (Stage B), so you do not need any other file to run the pipeline.

**How to use this.** Treat everything below as your operating manual. The *target* and the *context* (ICP, business model, segment, geography, known competitors) arrive in the user prompt — they are not hardcoded here. Map whatever tools you have (web/SERP search, an AI answer engine, an SEO/Labs data provider, LinkedIn/X lookups, plain HTTP, a CRM) onto the capabilities described. Calibrate every threshold to the segment and to the target's own competitors, never to absolute numbers.

**The four stages, and when each runs:**

1. **Discover / prospecting** — resolve the target to a company + domain, find its web/social footprint, map the people, and identify the marketing/SEO decision-maker(s). *Always runs.*
2. **Qualify / filter** — judge ICP fit using the runtime ICP draft, the discovery findings, and the embedded SEO/AEO profile. *Always runs.* Stop the deep, expensive work the moment cheap signals clearly disqualify.
3. **Enrich** — read the decision-maker(s) deeply and pull the hooks needed to craft a DM. *Only runs if the qualification verdict is a fit (strong or partial).*
4. **CRM write** — persist everything gathered. *Always runs — qualified or not — so a "no" is recorded and not re-researched later.*

Be cost-aware throughout: pull cheap, high-signal data first; only go deep once the target looks plausibly in-ICP.

***

## 0. Inputs — assume almost nothing is given; derive the rest

**The input will be unstructured and sparse.** In practice you will get little more than a **target** — often just a company name, a domain, a person's name, or a LinkedIn/X URL, sometimes dropped in as a messy line of text. Do **not** expect the fields below to be stated, not even the "optional" ones. Your job is to **figure them out yourself** from the company's own pages and the open internet before you start qualifying. Only two things might come from the prompt; everything else you derive.

**What may come from the prompt:**

* **Target (the one thing you can usually count on)** — a company name, domain, person name, or LinkedIn/X URL, possibly buried in free text. Extract it, then **resolve it to a single canonical company + root domain** (if given a person, resolve to the company they currently work at). This resolution is step one of Stage A.

* **ICP definition (sometimes given, sometimes not)** — who counts as a good fit; the qualification yardstick. If the prompt supplies one, read it carefully and judge against *it*. If it doesn't, fall back to the standing ICP for Berlin (see `seo-literate-ai-using-saas-teams.md`) and say which you used.

**What you must derive (do not wait to be told):**

* **Business model / segment** — *figure this out from the company's own site.* Read the homepage, About/About-us, product, and pricing pages and infer whether they're B2B SaaS, a dev tool, ecommerce, a marketplace, local services, media, etc. This sets what "normal" looks like for every SEO threshold, so derive it before any calibration. (Stage A2.)

* **Geography / language / target audience** — *infer from the business.* Who do they sell to and where? Read their positioning, pricing currency, language, and any location cues; if unclear, search the web to confirm the market they operate in. Use the derived market to set the location/language for SEO data. State the market you concluded and why; only default to US (English) if you truly can't tell, and say so.

* **Competitors** — *discover them; never assume they'll be handed to you.* Understand the business's problem statement first, then **search the internet for the keywords or prompts a buyer with that problem would use** — scoped to the same geography and the same target audience — and see who shows up. Corroborate with an AI answer engine (Stage B, Phase B7). The competitor set you derive is the yardstick for qualification.

* **Goal / output expectations** — if the prompt hints at one ("just qualify", "draft DM angles", "add to CRM"), honor it; otherwise run the full pipeline.

**Operating rule:** treat a sparse prompt as normal, not as a blocker. Resolve the target, read the company to understand the business, derive segment / geography / audience / competitors from what you find, and only then qualify. Don't stop to ask for details you can research yourself.

***

## 1. The capabilities you need

This pipeline assumes you can obtain the following kinds of data. Use whatever tool fulfils each capability; the labels below are the expected *concepts*, not literal output keys — confirm exact field names against whatever tool you actually use.

### Company & people research

| Capability                       | Technique / data to obtain                                                                 | Pull this for…                                  |
| :------------------------------- | :----------------------------------------------------------------------------------------- | :---------------------------------------------- |
| Company resolution               | Web search for the official site of a name/person; resolve to root domain                  | the canonical company + domain                  |
| Company website & "About"        | HTTP GET / read the homepage, About, product, pricing, blog                                 | what they do, who they sell to, positioning     |
| Company LinkedIn page            | LinkedIn lookup of the company                                                              | headcount, description, employees list          |
| Company X/Twitter profile        | Web / X search for the company handle                                                       | voice, activity, whether they're present at all |
| People at the company            | LinkedIn employees list; read names, titles, tenure                                        | org shape, finding the decision-maker           |
| Founder / leader X profiles      | Google or Google AI Mode search for a named person's X handle                              | personal voice, interests, recent posts         |
| Missing-profile discovery        | Google Search or Google AI Mode search to fill gaps (e.g. "find the X profile of <name>")  | closing holes in the person/company map         |

### SEO / AEO data (drives qualification, Stage B)

| Capability                          | Technique / data to obtain                                                                | Pull this for…                           |
| :---------------------------------- | :---------------------------------------------------------------------------------------- | :--------------------------------------- |
| Page footprint                      | Web search for `site:<domain>` and read the total-results count                           | scale of indexed content                 |
| Web search + SERP features          | A web/SERP search for the target's terms                                                  | SERP presence, features, snippets        |
| AI-answer visibility & citations    | Query an AI answer engine (AI overview, or an LLM with search) and read its cited sources | competitor discovery, AEO visibility     |
| Domain organic overview             | An SEO data source: traffic, traffic value, domain rank, # keywords                       | traffic, traffic value, rank, # keywords |
| Ranked keywords                     | An SEO data source: keywords a domain ranks for, with positions                           | ranking quality, intent, branded share   |
| Keyword ideas / demand              | An SEO data source: related keyword ideas and volumes                                     | content opportunity / TAM of demand      |
| Historical rank overview            | An SEO data source: traffic/keyword history over time                                     | momentum: growing vs flat vs declining   |
| Backlink summary                    | An SEO data source: referring domains, backlinks, authority, spam                         | authority / off-page investment          |
| Core Web Vitals / page health       | A Lighthouse-style audit of key pages                                                     | technical health                         |
| Detected technologies               | A tech-stack lookup for the domain                                                        | stack & SEO/AEO tooling maturity         |
| Sitemap & `llms.txt` presence       | Plain HTTP GET of `<domain>/sitemap.xml` and `<domain>/llms.txt`                          | content inventory + AEO awareness        |

### CRM

| Capability        | Technique / data to obtain                                | Pull this for…                          |
| :---------------- | :-------------------------------------------------------- | :-------------------------------------- |
| CRM upsert        | Create/update a company + contact record (tool-agnostic)  | persisting the result of every run      |

**Notes that apply everywhere:**

* **Specify the market.** SEO data is market-specific — set location and language to the segment/geo from the prompt. A global SaaS may warrant checking more than one market.
* **Read only the fields you need.** When a tool returns large responses, extract just the specific fields each phase calls for.
* Treat every traffic/keyword figure as a **modeled estimate**, not ground truth. Use them comparatively (target vs competitor vs segment), where estimation error mostly cancels out.
* **Be cost-aware.** Pull the cheap, high-signal data first; go deep only once the target looks plausibly in-ICP.

***

## Stage A — Discover / Prospecting

**Goal:** turn a sparse target into a structured map of *the company* and *the people who own the SEO/AEO decision*, plus enough surface understanding to qualify them. This stage gathers facts; it does not yet judge fit.

### A1 — Resolve the company

Resolve the target (name / domain / person / LinkedIn URL) to a single **canonical company and root domain**. If you were given a person, find the company they currently work at and resolve that. Record the resolved domain — every later phase keys off it.

### A2 — Read the company's own pages, and derive the business context

Read the homepage, **About/About-us**, product, pricing, and blog. This is where you **derive the inputs the prompt didn't give you** (Section 0). Capture and explicitly conclude:
* **What the company does** and **its problem statement** — the buyer pain it solves, in plain language. You'll reuse this to find competitors (B7).
* **Business model / segment** — infer it (B2B SaaS, dev tool, ecommerce, marketplace, local services, media, etc.). This sets every SEO threshold downstream.
* **Target audience & geography/language** — who they sell to and where, inferred from positioning, pricing currency, language, and location cues. Confirm with a web search if unclear.
* **Apparent stage/size** and positioning language.

The About and pricing pages are usually the richest sources. Record what you concluded and the evidence for it — these derived values drive calibration in Stage B.

### A3 — Map the company's social footprint

Find and record:

* **Company LinkedIn page** — description, headcount band, and the employees list.
* **Company X/Twitter profile** — does one exist at all, and is it active. (Absence is itself a signal.)

If a profile isn't immediately found, use **Google Search or Google AI Mode search** to locate it before concluding it doesn't exist.

### A4 — Identify the people, then the decision-maker

From the LinkedIn employees list (names + titles + tenure), identify **who owns marketing / SEO / AEO**. This is typically a **founder**, a **marketing/growth lead**, or **both** — capture both when both plausibly own it. You are looking for the person a DM should actually go to.

### A5 — Find the decision-maker's personal profiles

For each identified decision-maker, find both their **LinkedIn** and their **X/Twitter** profile. LinkedIn surfaces the person (name + role + detail); use those details plus **Google / Google AI Mode search** to find their **X handle**, which LinkedIn won't give you directly. Record the profile URLs. Deep reading of these profiles happens later, in Stage C — here you only need to locate them.

**Stage A output (carry forward):** resolved company + domain; what they do / who they serve; company LinkedIn + X; the list of relevant people; the identified decision-maker(s) with their LinkedIn + X URLs; any profile you searched for but could not find (note the gap).

***

## Stage B — Qualify / Filter (ICP fit + embedded SEO/AEO profile)

**Goal:** decide whether the target matches the **ICP supplied at runtime**, using (a) the Stage A findings and (b) the SEO/AEO profile built below. Run the phases in order; **stop early and mark "not in ICP"** the moment cheap signals clearly disqualify (e.g. effectively zero organic footprint when the ICP requires "already doing real SEO"). Calibrate every threshold to the segment and to the target's competitors, never to absolute numbers.

> The runtime ICP is the yardstick. Map each phase's evidence back to the ICP's specific criteria (vertical, revenue/size, "doing real SEO", AI usage, team shape, buyer literacy). A phase that's irrelevant to the given ICP can be down-weighted; a phase central to it is load-bearing.

### Phase B1 — Footprint & scale
**Pull:** a `site:<domain>` web search and read the total-results count. Also fetch `<domain>/sitemap.xml` and `<domain>/llms.txt` (plain HTTP GET).
**Insight:** rough size of the indexed content estimate, plus two binary signals — does a sitemap exist, does `llms.txt` exist.
**Correlate:** Page volume is a *proxy for content investment*, calibrated by segment (a docs-heavy dev tool or ecommerce catalog runs large; a boutique B2B SaaS runs lean). Use the segment norm and the competitor benchmark (B7) as the yardstick, not a fixed line. As a rough lean-SaaS anchor: 200–500 pages indicates real SEO investment, 500+ indicates heavy investment — adjust per segment. If `site:` count and sitemap URL count disagree wildly, note it and treat them as a range. `llms.txt` present = the team is AEO-aware (a strong positive ICP signal for AI-using teams).

### Phase B2 — Organic outcomes
**Pull:** a domain organic overview for `<domain>`.
**Read:** domain rank (0–100), estimated monthly organic traffic, estimated traffic value (the ad spend that traffic would cost), total # of ranking keywords, organic vs paid split.
**Insight:** whether the content footprint actually *produces* search outcomes. This is the single best "are they really doing SEO" signal — outcomes, not vanity counts.
**Correlate:** High traffic + high traffic value + large keyword count = SEO is working and funded. Large footprint (B1) but low traffic/keywords = volume without results (programmatic/thin content or a neglected site) — flag this divergence explicitly, it changes the verdict.

### Phase B3 — Momentum / trend
**Pull:** a historical rank overview for `<domain>`.
**Read:** trajectory of traffic and keyword count over the available history.
**Insight:** are they investing *now*, or coasting on past work.
**Correlate:** Rising = active, current investment (strongest "live deal" signal). Flat = maintenance mode. Declining = past investment, possibly a recovery/replatform need. Trend direction often matters more than absolute level for qualifying a prospect.

### Phase B4 — Ranking quality
**Pull:** the ranked keywords for `<domain>`, ordered by search volume, top ~100.
**Read:** position distribution (top-3 / top-10 / 11+), branded vs non-branded share, and the intent mix (informational / commercial / navigational).
**Insight:** quality and defensibility of rankings, and whether traffic is earned (non-branded) or just people typing the brand name.
**Correlate:** High non-branded share + many top-10 commercial-intent terms = mature, revenue-relevant SEO. Mostly branded terms = weak organic acquisition despite a presence. Lots of informational top-of-funnel content = a content-marketing-led motion (common in the AI-using SaaS ICP).

### Phase B5 — Authority (off-page)
**Pull:** a backlink summary for `<domain>`.
**Read:** referring domains count, total backlinks, domain authority/rank, anchor profile, spam score.
**Insight:** off-page investment and earned trust — the dimension page-count can't see.
**Correlate:** Many quality referring domains + low spam = serious, sustained SEO investment (link earning is hard and slow). Thin or spammy backlinks alongside high page count = effort concentrated on content, weak on authority — a concrete gap you can name in outreach.

### Phase B6 — Technical health & stack
**Pull:** a Core Web Vitals / Lighthouse-style audit and a detected-technologies lookup for `<domain>`.
**Read:** Core Web Vitals / performance, accessibility, SEO audit scores; detected CMS, analytics, SEO/AEO tooling.
**Insight:** technical maturity and how they operate SEO (tools reveal sophistication and budget).
**Correlate:** Strong CWV + a real SEO stack (headless CMS, schema tooling, an SEO platform) = a literate, resourced operator (matches the "literate buyer" ICP). Poor CWV = a concrete, ICP-relevant pain point to lead with. AEO-oriented tech (schema, structured data, llms.txt tooling) = a forward-looking team. **AI-tooling signals** (e.g. evidence they use AI tools for SEO/marketing) directly test the "AI usage" ICP criterion — note any.

### Phase B7 — Competitive gap (competitors you *discover*, NOT a provider's competitor list)
**Discover (assume none were given):** start from the **problem statement** you derived in A2. Then find competitors two ways and merge the results:
1. **Search the internet with buyer-intent keywords/prompts** — the actual searches or AI prompts someone with that problem, in that **geography**, serving that **target audience**, would type (e.g. "best `<problem/category>` tool for `<audience>` in `<market>`", "alternatives to `<company>`"). See who consistently ranks/appears. This grounds the set in real demand, not just brand adjacency.
2. **Corroborate with an AI answer engine** — query for "top alternatives and competitors to `<company>` for `<derived segment/audience>`" and take the named competitors from the cited sources; get a second opinion from a different AI engine.

Keep only competitors that match the same **segment + audience + geography**; drop ones that merely share a keyword. *Do not* use any SEO provider's "competitors" endpoint — discovery should reflect how the market and LLMs actually frame the space. If the prompt did happen to name competitors, fold them in too.
**Benchmark:** run B1, B2, and B5 (footprint, organic overview, backlink summary) on each competitor.
**Insight:** the target's standing relative to the leaders in their space — the gap.
**Correlate:** Express the target's traffic / keyword count / referring domains as a **ratio** to the segment leader and median ("30% of the leader's traffic, 15% of its referring domains"). Ratios are far more meaningful than absolute numbers and sidestep estimation error. The gap size is also the sizing of the opportunity you'd pitch.

### Phase B8 — AEO / LLM visibility
**Pull:** query AI answer engines on 2–3 high-intent queries the target should win in its category; check whether the target's domain appears in the citations/references.
**Insight:** are they visible where buyers increasingly look (AI answers), beyond classic SERPs.
**Correlate:** Cited in AI answers + has `llms.txt` (B1) = AEO-aware and ahead of the curve (prime fit for an AI-using ICP). Absent from AI answers despite decent classic SEO = a clear, timely gap to lead with.

### Phase B9 — Buyer literacy (light pass)
**Pull:** a *quick* scan of the decision-maker(s) identified in Stage A — do their public profiles/posts suggest they personally understand SEO/AEO? (Full reading is Stage C; here just enough to test the ICP's "literate buyer" criterion.)
**Correlate:** A founder or marketing lead who posts about SEO/AEO/content = a literate buyer and a strong fit signal. No evidence either way = leave neutral, don't penalize.

### Synthesizing the SEO/AEO profile

Combine the phases — never score on one metric alone; look for *agreement and divergence*.

| Dimension            | Primary evidence | Reading                              |
| :------------------- | :--------------- | :----------------------------------- |
| Content footprint    | B1               | scale of investment in content       |
| Organic outcomes     | B2               | is the SEO working                   |
| Momentum             | B3               | investing now vs coasting            |
| Ranking quality      | B4               | earned, defensible, revenue-relevant |
| Authority            | B5               | off-page investment                  |
| Technical & stack    | B6               | operator maturity                    |
| Competitive standing | B7               | gap vs leaders                       |
| AEO visibility       | B8               | future-readiness                     |
| Buyer literacy       | B9 / Stage A     | can they operate a platform          |

**Investment tier (synthesize, don't average):**

* **Heavy & effective** — strong outcomes (B2) + rising trend (B3) + real authority (B5), regardless of raw page count.
* **Heavy but inefficient** — large footprint (B1) but weak outcomes (B2) or thin authority (B5). Effort without return — a coaching/tooling opportunity.
* **Lean & effective** — modest footprint, high traffic-per-page, strong authority. A quality operator who could scale.
* **Light / nascent** — little footprint, low traffic, few links.
* **Dormant** — past traffic now declining (B3) with stale content.

**Divergence checks — the most diagnostic part; call them out explicitly:**

* Big footprint + low traffic → thin or programmatic content.
* High traffic + mostly branded keywords → weak organic acquisition.
* Good content + weak backlinks → authority gap.
* Good classic SEO + absent from AI answers → AEO gap.
* Strong historical peak + current decline → recovery opportunity.

### ICP fit verdict

Map the profile back to the **runtime ICP**. State fit as **strong / partial / weak (= not in ICP)**, with the specific signals that drove it. For a "SEO-literate, AI-using SaaS team" ICP, the ideal signature is: real organic outcomes (B2) + rising or stable trend (B3) + non-branded ranking quality (B4) + decent authority (B5) + AEO awareness (`llms.txt`, AI citations, AEO tooling) + a literate decision-maker (B9). 

* **Strong** or **partial** → proceed to Stage C (Enrich).
* **Weak / not in ICP** → skip Stage C, go straight to Stage D (still record the result and the reason).

***

## Stage C — Enrich (fit only)

**Goal:** gather the raw material to write a personalized, relevant DM. Run **only if the qualification verdict is strong or partial.** This is where you read the decision-maker(s) deeply — not the whole company, just the people a message will go to.

### C1 — Deep-read the decision-maker(s)
For each decision-maker identified in Stage A, read **both LinkedIn and X**:
* **Background / history** — what they've built and done before; prior companies and roles. Reveals what they care about and how to speak to them.
* **Recent posts** — their *latest* posts reveal current interests, priorities, and what's top of mind. This is the freshest, most personalizable signal.
* **Topics & voice** — what they post about (SEO/AEO/content/product/hiring), how they talk, what they react to.

### C2 — Pull the message hooks
Translate the findings into concrete, usable angles for outreach:
* **Personal hooks** — a recent post, a shared interest, a milestone, a take they've voiced.
* **Company hooks** — the specific SEO/AEO gaps from Stage B (e.g. "great content, thin backlinks"; "strong SERP presence but absent from AI answers"; "declining trend = recovery opportunity"), framed as the opening, not a critique.
* **Relevance bridge** — why Berlin specifically maps to their situation, in their language.

### C3 — Note what's missing
If a profile couldn't be found, a key fact is unknown, or a hook is thin, record the gap so the DM-writing step (and future runs) know what's solid vs. inferred.

**Stage C output:** per decision-maker — background summary, recent-interest summary, and a short list of ready-to-use DM hooks (personal + company), each tied to its evidence.

***

## Stage D — CRM write (always)

**Goal:** persist the result of every run — **qualified or not** — so the work isn't lost and a "no" isn't accidentally re-prospected later. Upsert on the resolved domain (avoid duplicates).

**Record schema (tool-agnostic — map these fields onto whatever CRM is wired in):**

*Company*
* Company name, resolved root domain
* Segment / business model, geography/market used
* What they do (one line), who they serve
* Company LinkedIn URL, company X/Twitter URL (or "none found")

*Qualification*
* **ICP-fit verdict:** strong / partial / weak (not in ICP)
* **Investment tier:** heavy & effective / heavy but inefficient / lean & effective / light / dormant
* Key SEO/AEO metrics: page footprint, organic traffic (est.), traffic value (est.), # keywords, domain rank, referring domains, `llms.txt` present (y/n), AI-answer visibility (y/n)
* Competitive gap: target vs leader/median as ratios
* Reason for the verdict (the signals that drove it)
* Date evaluated; market/geo used

*Contacts (one per decision-maker)*
* Name, title, role-in-decision (founder / marketing lead / both)
* LinkedIn URL, X/Twitter URL
* Buyer-literacy read (literate / unclear)

*Enrichment (fit only)*
* Background summary, recent-interest summary
* DM hooks (personal + company), each with its evidence
* Known gaps / unknowns

*Pipeline*
* Stage / status (e.g. "qualified — ready for outreach", "not in ICP — archived")
* Source of the lead, run timestamp

**Disqualified leads:** still write the company, the verdict, and the reason. Mark status so they're excluded from outreach but retained as a record (and not re-researched on the next pass).

***

## Output format (for the run, in addition to the CRM write)

Return:

1. **Snapshot** — target, resolved domain, segment, market, decision-maker(s), and ICP-fit verdict (strong/partial/weak) in 2–3 sentences.
2. **Profile table** — the dimension table from Stage B, each row with the headline number and a one-line read.
3. **Competitive gap** — target vs leader/median as ratios.
4. **Contacts & hooks** — decision-maker(s) with their profile URLs and (if a fit) the ready-to-use DM hooks.
5. **Key gaps & angles** — the divergences found, framed as the openings to lead outreach with.
6. **Evidence appendix** — the exact queries run, data sources used, and key fields pulled, so the run is reproducible and auditable.

Keep estimates labeled as estimates. When a number looks implausible, say so rather than reporting it straight.

***

## Dynamic calibration (do this, don't skip it)

* **Segment sets the baseline.** Page-count, traffic, and keyword norms differ by 10–100× across segments. Anchor expectations to the stated business model, not a universal threshold.
* **Competitors set the yardstick.** Express the target's numbers as ratios to the discovered competitors (B7). Relative standing is robust to estimation error; absolute numbers are not.
* **Geography sets the market.** Query SEO data for the prompt's market. A global SaaS may warrant checking more than one market.
* **Let outcomes overrule vanity.** When footprint (B1) and outcomes (B2) disagree, weight outcomes and authority. Page count is a supporting proxy, not the verdict.
* **The ICP is supplied at runtime.** Re-read it each run and judge against *it*, not against the example signatures in this doc.
