# The AEO Report — Product Specification (v1)

**Status:** Internal. The base document for the v1 AEO product — the version stakeholders approve and engineering builds from.
**Last updated:** 21 August 2026

***

## Who this is for and how to read it

This document is the common starting point for everyone working on the AEO product — commercial, brand and report design, and engineering. It assumes no SEO knowledge, and every term is defined the first time it appears.

One companion document sits behind it: **[the framework](./framework.html)**, which classifies what people search for and whose vocabulary this document uses exactly. It is a linked page, and anyone who receives this document receives that link too. This document adds what the framework does not contain — the connection between how a question is classified and what we then do about it. That connection is the product.

The division of labour between the two is strict, so that neither has to be maintained twice:

| | The framework | This document |
| :-- | :-- | :-- |
| **Answers** | What is this question? | What do we do about it? |
| **Contains** | The three axes, every value on each, the rules for assigning them, the proofs that they are independent | Measurement, diagnosis, the causes list, pilot constraints, evidence base |
| **Changes when** | We learn the taxonomy is wrong | We learn the product is wrong |

Part 1 below is a bridge, not a summary: it explains why we bucket and what a bucket is *for*, and hands the taxonomy itself to the framework. Read the framework first if you have not seen it; it takes about ten minutes and this document assumes its vocabulary throughout.

The document has four parts plus an appendix:

1. **The map** — why we cut the universe of customer questions into 128 buckets, and what falls out of one.
2. **The diagnosis** — the split between *symptoms* (what is happening to a client) and *causes* (why it might be happening). This is the organising idea for the whole product.
3. **The pilot** — the constraints we have agreed for the first four or five engagements.
4. **What each team does next.**
5. **Appendix — the evidence base.** Every external claim in this document, its source, and how strong that source actually is.

Read parts 1 and 2 in order. They build on each other. The appendix is a reference, not a read.

***

## The idea in one page

A company wants to be recommended when a potential customer asks an AI assistant a question. We tell them whether that is happening, why it is or is not, and what to do about it.

To do that we need three things.

**First, a map.** "Are we visible in AI search?" is not an answerable question — visible to whom, asking what? So we take every question a potential customer might ask in the client's category, and we sort those questions into buckets. There are 128 buckets, produced by classifying each question three ways at once. A bucket is small enough that everything inside it can be fixed by the same kind of work, and there are few enough buckets that a person can look at the whole picture on one screen.

**Second, a measurement.** For each bucket we ask the AI engines the real questions and record what comes back. Does the client get mentioned? Cited? Recommended? Recommended *first*? Who gets recommended instead? We call these results **symptoms** — they are observed facts about the outcome, and they require no guesswork.

**Third, an explanation.** Symptoms tell you where you are losing. They do not tell you why. The *why* lives in a long list of conditions on and off the client's website — whether the AI's crawler can reach the pages at all, whether the content answers the question, whether anyone credible vouches for the brand. We call these **causes**. Unlike symptoms, causes must be hypothesised and tested.

Causes arrive from two directions. One is that list, worked top-down. The other is watching what the brands currently winning a bucket actually change — week by week, on their own site and everywhere else that feeds the answers (§2.6). The second is much harder to reproduce, and it is where our advantage sits.

The product is: map → symptoms → causes → a ranked list of actions. The report is read in that order too. Outcome first, then the analysis that produced it.

***

# Part 1 — The map: 128 buckets

## 1.1 Why bucket anything at all

A mid-sized B2B company's customers might collectively ask hundreds of thousands of distinct questions relevant to what it sells. You cannot act on a list of a hundred thousand questions, and you cannot show one to a client.

You also cannot usefully compress it to a single number. "Your AI visibility is 34" tells nobody what to do on Monday morning.

Bucketing sits between those two failures. It is the smallest number of groups that still satisfies one rule:

> **The bucket rule:** everything inside a bucket should be improvable by roughly the same kind of work.

If that rule holds, then a weak bucket is a work order. If it does not hold, the bucket is just a bin, and knowing you are weak in it tells you nothing.

Above the buckets sits one more layer: the **topic**. A topic is a business goal or product area the client actually cares about — for a psychiatry clinic it might be "ADHD"; for a SaaS company it is usually a product line or a job the product does. Topics come from the client, not from us. Each topic gets its own set of 128 buckets.

```
Client
 └── Topic (e.g. "ADHD treatment", "sales pipeline management")
      └── 128 buckets
           └── Query clusters
                └── Individual questions
```

## 1.2 The three axes

Each question is classified three ways. The three answers together place it in exactly one bucket.

**4 awareness stages × 8 question types × 4 search intents = 128 buckets.**

Each axis reads one thing off the question and decides one thing about the answer that would win it:

| Classification      | What it reads from the query           | What it decides about the answer   |
| :------------------ | :------------------------------------- | :--------------------------------- |
| **Awareness stage** | How much the searcher already knows    | How much the answer has to explain |
| **Question type**   | What they are asking about             | What the answer has to cover       |
| **Search intent**   | What kind of result would satisfy them | What form the answer takes         |

Depth, subject and form — three properties of the same answer, each set by one axis.

> **[The framework](./framework.html) is the document to read for any of this in detail.** Every value on every axis, the dividing lines that get missed, why a third axis is needed at all, the independence proofs, the worked example and the classification rules live there, and are not repeated here. Where the two documents ever disagree, the framework wins on vocabulary and this one wins on what we do with it.

Brand presence — which brands are named in the question itself — is recorded alongside the three axes. It is context, not a fourth axis, and it does not multiply the bucket count.

**A bucket is not quite a position.** The framework counts 128 *positions*: the coordinates the labels can express. A *bucket* is the set of real query clusters that actually lands on one of those coordinates for a given client and topic. There are always 128 positions; there are rarely 128 non-empty buckets, and **an empty bucket is itself a finding** — though not a gap to be filled for its own sake.

**A note on names.** **Northstar** stands in for whichever brand we are working for and **Acme**, **Corvus** and **Halden** for its competitors, in both documents.

## 1.3 The one thing to carry over from the framework

The commercial argument for the third axis is worth stating here, because it is the argument a client hears.

Take four questions from someone shopping for a CRM: *best CRM for a 10-person sales team*, *which CRMs allow month-to-month billing*, *which CRMs are risky to migrate onto mid-quarter*, *CRM vs marketing automation platform*. All four are solution-aware. All four are commercial. On a two-axis grid they collapse into a single cell and get a single blended score.

They need four different pages, they are likely answered from four different places, and a client can be winning one while invisible in the other three. The blended cell hides exactly that — and it is the finding the client would have paid for. The framework works this through properly, including the caveat that the "answered from different places" expectation is ours to test per client rather than something established.

## 1.4 What we do with a bucket

Once every question in a topic has a bucket, we run the measurement (Part 2) and attach a result to each bucket. The bucket map then becomes the main visual in the report: a three-dimensional grid where each cell shows how the client performs, with competitors overlaid.

Some things that fall out of it immediately:

* **Where you are weak and a competitor is strong.** The highest-value finding, and the one that sets the next campaign.

* **Where nobody is strong.** An opening.

* **Where the engine cites nobody worth citing** — it answers from general knowledge or links only to government and institutional sources. If a client has spent heavily on content in such a bucket, the honest advice is to stop. There is no door to walk through, and AEO is the wrong lever for that question.

* **Progress over time.** "In March you were strong in 5 buckets and weak in 30. Today you are strong in 15." This is the headline KPI for a retained engagement.

***

# Part 2 — The diagnosis: symptoms and causes

## 2.1 The core distinction

Everything we look at falls into one of two kinds, and confusing them is the fastest way to produce a report nobody can act on.

**A symptom is an observed fact about the outcome.** We asked the engine a real question and recorded what came back. Symptoms require no interpretation and no guessing. "For the 12 comparison questions in this topic, your brand appeared in 2 answers and was recommended first in none of them" is a symptom.

**A cause is a condition that might explain a symptom.** Causes live on the client's website, in their data, or in how the rest of the internet talks about them. "Your comparison pages are blocked to one of the crawlers" is a cause. Causes are hypotheses until tested.

The difference in confidence between the two is real and we should not blur it:

| <br />                        | Symptoms                                 | Causes                     |
| :---------------------------- | :--------------------------------------- | :------------------------- |
| How we know                   | Measured directly                        | Inferred, then tested      |
| Confidence                    | High                                     | Varies, often low at first |
| Changes over time             | Yes — engines are volatile, so we repeat | Slowly                     |
| Client can act on it directly | No — it is the scoreboard                | Yes — it is the work       |

## 2.2 The honest position on causes

This matters most for anyone writing copy or talking to prospects.

**We can measure symptoms with confidence. We cannot yet state which causes drive which symptoms.** Nobody can — the engines do not publish their pipelines, and the public evidence is a mix of vendor correlational studies and a small amount of peer-reviewed work. Some causes have strong published backing (a page must be indexed and snippet-eligible before it can be cited in Google's AI surfaces — that one is documented by Google). Others are widely believed and untested.

So the causes list is a research programme, not a checklist of known truths. The plan is to implement the cheap, unambiguous ones first, apply them across the pilot clients, and watch what moves. That is a real advantage — we get to learn from a portfolio — but it must not be described as settled knowledge.

**Practical rule for external material:** state symptoms as findings. State causes as diagnosis, with our reasoning attached. Never present a correlational vendor study as a mechanism.

## 2.3 Layer 0 — the map (prerequisite)

Before either symptoms or causes, we need the question universe itself: the set of questions a client's buyers actually ask, clustered into topics and sorted into the 128 buckets.

Where the questions come from:

* Traditional keyword sources — Semrush, Ahrefs, DataForSEO, and the client's own Search Console.

* Translation into prompts — the same buying question phrased the way someone talks to an AI assistant rather than types into a search box.

**The framework's scope filter runs before any of this**, and it is where the post-purchase exclusion is enforced — see the open questions at the end of this document for what reversing it would cost.

Once clustered, each cluster is weighted by commercial importance, audience relevance, journey stage and a defensible demand proxy. Weighting is what decides which clusters get the measurement budget.

Two caveats worth knowing:

**The data sources disagree with each other.** Search Console gives position but not volume. Semrush gives volume and its own difficulty score, which is not comparable to Ahrefs' difficulty score. We currently take the questions themselves and treat volume only as a rough signal of whether something is worth attention. We do not present these numbers as precise.

**Prompt translation is not reliable and we should not claim it is.** Asking an AI "what prompt would someone use for this keyword" produces plausible output, not ground truth. Neither we nor a client can verify it. Our differentiation here is not the translation step — it is the clustering into topics and the sorting into buckets, which is genuinely hard to reproduce.

**Language rule:** internally we say keywords. **In front of a client we always say prompts.** The underlying data is keyword data, but the client's world is prompts, and the word "keyword" signals that we are selling repackaged SEO.

## 2.4 Layer 1 — Symptoms

These are the six things we measure. This is the output the client is buying.

### S1 — Cross-engine visibility baseline

For every important prompt, on every engine that matters, record: whether an AI answer fires at all; whether the brand is mentioned; whether the brand's site is cited; who gets recommended first; whether the brand is shortlisted but not preferred; share of recommendations against competitors; how prominently the mention appears.

**Repetition is not optional.** Profound's 80,000-prompt study measured monthly drift of roughly 40–60% in *which domains get cited* across the major platforms, and a 2026 review of 45 studies in this field recommends repeated measurements, paraphrases and controls. A single screenshot is not defensible evidence. Our own working target is around ten runs per prompt; that number is a judgement call, not a published standard. We are reducing it for the pilot on cost grounds (see Part 3) and should be aware that we are trading rigour for price.

### S2 — The answer-participation funnel

Do not collapse everything into one visibility score. A brand can lose at any of several distinct stages:

```
Eligible → Retrieved → Cited → Used in the answer → Named
        → Shortlisted → Recommended → Preferred → Visited or searched
```

Being cited is not the same as shaping the answer, and being mentioned is not the same as being recommended. The gap between "cited" and "named" is large enough to have its own term — a **ghost citation**, where your page is used as a source but your brand never appears in the answer the customer reads. Semrush found the majority of citations in its study produced no explicit brand mention. Reporting the funnel per topic is far more useful than a score: "for four of your five problem areas you are eligible, retrieved, used, named and recommended; for the fifth, everything holds except the recommendation."

Some stages have to be inferred — the engines do not expose their full pipeline — and we should label inferred stages as inferred.

### S3 — Retrieval-gap diagnosis

For each important absence, identify the stage at which it failed: the AI surface never activated; the site was unreachable or ineligible; no page addressed the sub-question; a page existed but was not retrieved; it was cited but did not influence the answer; it influenced the answer but the brand was not named; the brand was named but not recommended; a third party vouched for a competitor instead.

**This is the hinge of the whole product.** It is the step that turns a symptom into a pointer at a category of cause. Everything in Layer 2 is only reachable through this diagnosis.

### S4 — Recommendation stance

For commercial purposes, being recommended matters more than being cited. Every appearance gets classified: recommended; included neutrally; mentioned in passing; cautioned against; explicitly excluded; or — the worst outcome — **used as a source for recommending somebody else**.

Without this you can produce a cheerful report showing the client's article cited fifteen times, while every one of those answers recommends a competitor.

### S5 — Competitive displacement

The same analysis run on competitors: who owns each problem or segment, where the client is missing from a shortlist, which attributes get a competitor picked, which external sources vouch for them, who replaces the client when the client is absent, and which prompts nobody owns.

**We run this across** ***all*** **buckets, not only the weak ones** — cost permitting, see Part 3. Knowing where you lead, and tracking whether you keep the lead, is itself a deliverable, and it is what makes the three-month progress report possible.

### S6 — AI answer accuracy and brand-narrative risk

What the engines actually believe about the company: its category and positioning, who it is and is not for, capabilities and limits, pricing, integrations, markets served, security and compliance, ownership and history, policies, perceived strengths and weaknesses, and how it compares to named competitors.

Each material inaccuracy is logged with the exact claim, its severity, which prompts and engines reproduce it, and the source that appears to be feeding it.

This is where the client's own positioning — what they told us they want to be known for — meets what the machine actually says. It turns vague brand sentiment into a concrete misinformation and commercial-risk register, and it is disproportionately valuable for regulated, medical, financial, legal, enterprise and reputation-sensitive businesses.

## 2.5 Layer 2 — Causes

Twenty items, grouped into six families. Grouping matters more than the individual items: when a symptom points somewhere, it usually points at a *family*.

### Family A — Access: can the engine reach the content at all?

The most basic failure mode, and the one with the strongest published evidence.

| #  | Item                                                   | In plain terms                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| :- | :----------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C1 | Answer-engine crawler access                           | Do the specific bots — Google's, Bing's, OpenAI's search bot, Perplexity's — actually get a successful response? Security, CDN and bot-management layers can block or rate-limit them without anyone intending it. Note that a bot for *search inclusion* and a bot for *model training* are different things; blocking one is not blocking the other.                                                                                                       |
| C2 | Search eligibility, indexation and snippet eligibility | Is the page indexed, and is it allowed to show a snippet? Google states plainly that a page must be both before it can appear as a supporting link in AI Overviews or AI Mode. **This is the single strongest documented requirement in the whole list** — a stated rule, not an inference. **Not this:** a site-wide "percentage indexed" score. An excluded URL only becomes a finding once it is tied to a priority prompt and page.                                                                                                                                                                  |
| C3 | Crawlability, rendering and machine-visible content    | Does the important content exist in the page's raw HTML, or does it only appear after JavaScript runs? Google can render JavaScript, though it acknowledges limitations and notes that other crawlers may ignore it — so a site that renders everything in the browser risks being partly invisible to some engines. Google's own recommendation is server-side or static rendering rather than treating dynamic rendering as a permanent solution. **Premium output:** side-by-side evidence for the priority page set — user view, raw HTML, rendered DOM, bot response.          |
| C4 | Sitemaps and feed coverage                             | Basic discovery plumbing — the list of pages handed to the engines, whether it is accurate, whether change dates are honest. Sitemaps help discovery; they guarantee neither indexation nor citation.                                                                                                                                                                                                                                                        |
| C5 | Page experience                                        | The parts that affect access, consumption or conversion: severe slowness, content buried under consent walls or interstitials, broken mobile rendering, insecure delivery, inaccessible navigation, and AI-referred landing pages that fail to continue the journey. Cheap to check. Google includes page experience in its AI guidance but also says relevance can outweigh a subpar experience. Clients rarely act on it, because it costs developer time. **Not this:** a generic Lighthouse dump of low-impact fixes unconnected to priority pages or conversions. |

### Family B — Clarity: can the engine tell what the page is for?

| #  | Item                                                      | In plain terms                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| :- | :-------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C6 | Canonicalisation and duplicate consolidation              | Are there several competing versions of the same page? If so the engines have to choose which to trust. Bing explicitly links duplicate content to blurred intent and to outdated URLs surfacing in AI answers. The goal is one clearly preferred current page per purpose, not merely passing a tag check.                                                                                                                                                                                                                                                                                                                                                |
| C7 | Internal information architecture                         | How pages link to each other. Are important pages reachable? Do the links express a coherent structure? Google says links are used to discover pages and understand relevance, and its AI guidance recommends making content findable through internal links. Whether this drives *topical authority* specifically is industry belief, not documented. Higher implementation effort than the rest of this family — many variables to tune — so it lands later in the build order. **Not this:** a raw crawl-depth export. Depth and links only matter here as they relate to prompt coverage and cited-page performance.                                                                                                                                                                          |
| C8 | Descriptive titles, headings and unambiguous page purpose | Whether the page's title and headings honestly describe it. Google uses titles and prominent headings to build the title link, and its guidance asks for titles and headings that summarise content accurately. Reading that as an aid to *retrieval clarity* is our interpretation, not Google's wording. Our further hypothesis, currently unevidenced, is that it matters at a specific moment: when the assistant chooses which of many candidate pages to actually open, the title, heading, description and URL are much of what it has to go on. Worth testing first where a client ranks well in traditional search but is absent from AI answers. **Not this:** a site-wide list of title lengths. Pixel-length scoring is not a finding; titles that create ambiguity or duplication are. |
| C9 | Freshness and index propagation                           | Only where the fact is genuinely time-sensitive — prices, stock, policies, statistics, "best of" content, opening hours. Cosmetic date changes get no credit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

### Family C — Substance: is there a reason to pick this page?

| #   | Item                                      | In plain terms                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :-- | :---------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| C10 | Retrieval relevance for fan-out questions | AI assistants break one question into several sub-questions before searching — Google confirms this fan-out. Does the page cover the sub-questions too: definitions, constraints, trade-offs, alternatives? The useful output is a four-way split per page — ranks and is cited; ranks but is not cited; does not rank yet is cited via fan-out; neither. **Lower priority:** hard to measure, because the sub-questions are not observable on Google's AI Mode. Bing now publishes sampled grounding queries, and we have observed ChatGPT exposing its fan-out queries to anyone inspecting the network traffic — the latter is our own observation, not documented behaviour, and could disappear without notice. **Not this:** keyword density, exact-match quotas, or a separate thin page per prompt variation. The unit is the buyer problem and its fan-out concepts.                                                                                                                                                                                                |
| C11 | Passage-level citation readiness          | The idea is that assistants pull short passages rather than whole articles, so an individual passage should be self-contained and quotable. **Lower priority, needs research — and the published evidence cuts against the naive version.** Google says explicitly that tiny content chunks and special "AI writing styles" are unnecessary, and a NeurIPS 2025 benchmark found many popular conversational-SEO rewrites ineffective or harmful. Before committing to this we need to establish both that it matters and how to assess it. **Not this, whatever we conclude:** a word-count exercise or "add more FAQs".                                                                                                                                                                                                                                                                                                                                                                          |
| C12 | Originality and information gain          | Does the page add material value beyond the pages already ranking and being cited — original research, reporting, analysis or first-hand experience? Google says unique, non-commodity content is likely to influence long-term presence in generative search more than its other suggestions, which makes this the best-supported item in the family. Our own working view, which goes beyond anything Google says, is that the bar is lower than "novel to the world": a named expert asserting something already known can still be a signal. **On request, priced separately.** Expensive to run, and a numeric "information gain score" can read as invented. Its real use is as a fallback explanation — when a client has published heavily and nothing performs, "your content adds nothing new" is often the true answer, and an existing tool's mass-produced-content signal can substantiate it cheaply. **Not this:** generic word-count comparisons, or advice to make every page longer. |

### Family D — Trust: is there reason to believe it?

| #   | Item                          | In plain terms                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :-- | :---------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C13 | Trust evidence and authorship | Who wrote it, are they qualified, how was the research done, are claims sourced, is the company identifiable and contactable. A doctor writing about a condition is not equivalent to an anonymous blogger. Strongest as a *comparative* finding: "every competitor's articles carry a named expert author; yours do not." Do not present this as a single score — it is a bundle of signals, not a measurable ranking factor. Worth extending the same lens to third-party pages that discuss the brand. **Premium output:** missing trust evidence located at the claim and page level — never an invented "E-E-A-T score".                                                                                                                                                                                                                                                                              |
| C14 | Backlink quality              | **This item is about references, not authority scores.** Domain authority and page authority are proxies for SEO effort and tell a client nothing they can act on, so we do not report them. What we report is the part that matters: are there relevant, credible references to the client's important pages, do they point at the right version, and are competitors better endorsed? What is documented: Google confirms link analysis and PageRank remain part of core ranking. What is only *correlational*: Semrush found higher-authority domains had stronger AI visibility across 1,000 domains, while Ahrefs found weak relationships for raw backlink volume but much stronger correlations for broad branded web mentions across 75,000 brands. Neither establishes cause. |
| C15 | Search-quality and spam risk  | Things that can get content demoted or discredited: mass-produced pages, site reputation abuse, fake reviews and authors, scraped content, manipulative links, hacked content, misleading structured data, and hidden instructions or prompt injection aimed at agents. **Low priority** — largely covered as sub-parts of other items — but the prompt-injection element is new and worth watching separately.                                                                                                                                                                                                                                                                                                                                                                        |

### Family E — Off-site: what the rest of the internet says

Probably the highest-leverage family, and the one competitors are least likely to cover.

| #   | Item                                                 | In plain terms                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :-- | :--------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C16 | Brand, entity, product and location data consistency | Is the same story told everywhere — website, docs, review sites, directories, business profiles, product feeds, partner pages? Conflicting names, categories, prices or locations give the engines a reason to distrust all of it. Two sub-parts travel with this item: **structured data**, checked only for whether the machine-readable labels match what is actually on the page (Google says no special schema is required for AI search and warns against overfocusing on it — so no "add FAQ schema everywhere"); and **product, local and vertical feed integrity** — Merchant Center, Shopify or OpenAI catalogs, business profiles, hours and addresses — which becomes a *primary* item for commerce and local businesses rather than a secondary one. **Note how this differs from symptom S6:** S6 starts from what the AI said and works backwards; C16 starts from what is out there and checks it independently. S6 cannot see problems in places the AI never looked. **Not this:** invented "AEO schema", or any claim that valid markup guarantees citation. |
| C17 | Third-party source influence map                     | Which external sources are actually shaping answers in this category — trade press, review sites, Reddit and communities, YouTube, Wikipedia, marketplaces, analysts. For each: which prompts it influences, whether it mentions the client, whether it is accurate, and whether competitors are better represented there. This is the item most likely to change what a client does with their budget. A 2026 study of 167,551 grounded citations across 128 brands put 85.7% on third-party sites; Profound's 27-million-citation analysis points the same way. Both are **observational rather than universal constants** — the direction is consistent, the number is not a law. This item also produces the target list for the field watch (§2.6).                                                                                                                                                                                                                               |
| C18 | Citation fidelity                                    | Whether a cited page actually supports the claim the AI attached to it. Research has documented real citation-correctness failures in generative search, so the problem is genuine. **Under research** — unproven method, not committed for v1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

### Family F — Conditional: only for some businesses

| #   | Item                                | In plain terms                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :-- | :---------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C19 | Multimodal readiness                | Images and video, where the category depends on them — fashion, food, travel, home, automotive, anything instructional. Skip it otherwise.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| C20 | Multilingual and regional integrity | Only for clients serving multiple languages or markets, and only where they serve local-language speakers rather than English speakers abroad. Separate real URLs per language, correct regional signals, and — importantly — testing prompts in the customer's actual language rather than translated English. Profound's 3.25-billion-citation study found query language materially changes which sources get cited. Separately, our own observation — not something the published research shows — is that competition in some non-English markets is far weaker than the equivalent English one, which would make this an opportunity item as well as a hygiene one — worth verifying per market before we say it to a client. If a client already uses an SEO agency, much of the hygiene is probably in hand. |

## 2.6 The field watch — the second source of hypotheses

Layer 2 works top-down: a list of conditions, inspected on a client. There is a second way to arrive at a hypothesis, and it is the capability worth protecting.

We can crawl an entire website on a weekly cadence and diff it — every new page, every changed line, every altered date. It runs on the client's own site and, more importantly, on every competitor's. Tools that do this for your *own* site exist, and few clients run them; we know of nothing that does it for everyone else in a category.

Extended off-site it becomes something larger. C17 establishes which platforms actually shape answers in this category; the watch then covers those platforms — the competitors' own accounts, the influencers and threads that carry the category, the review sites and communities the engines keep citing. Coverage off-site is good rather than complete: we find what each platform's own search surfaces plus what gets cross-posted, which is most of what matters and not all of it. On-site coverage is effectively complete.

Two things come out of it.

**A client-facing feed.** *Your competitor published five pages on this product line last month and started campaigning here — they are moving into your space.* Brands ask for this internally and do not have it, from us or from anyone else. It is the easiest thing we have to sell.

**Hypotheses for Layer 2.** We know who is winning a bucket, we know which platforms feed the answers in it, and we know what those winners changed. That is not a causal chain, but it aims the next test far better than working down a checklist does.

Two cautions:

1. **The connection is indirect and must be described as such.** Winning brand, influential platform, observed change — three facts and no proven link between them. Presenting it as causation would be dishonest, and clients with any analytical instinct will catch it.

2. **Describe the capability, not the method.** A competitor with an engineering team could build crawl-and-diff quickly. The defensible part is knowing where to look and what a change means. Public material should say what the client learns, never how we obtain it.

**Cadence.** The value is longitudinal — the first run is only a baseline and shows nothing. Take that baseline during the pilot and price the pilot without it; the first real output belongs in the second month's report. Do not sell month one on this.

## 2.7 Layer 3 — Actions

The output of the whole process is a register in which every recommended action states:

* the prompt, audience and engine affected

* what the answer says today, with evidence

* the stage at which it failed

* the proposed fix

* the leading indicator we expect to move

* business importance

* effort, dependencies and likely owner

* **how confident we are in the diagnosis**

* how and when we will retest

That confidence field is not decoration. Given the honest position in §2.2, it is what separates our report from a list of assertions.

**Measurement inputs.** Where the client gives us access, we connect Search Console (whose Generative AI Performance report separates AI Mode and AI Overview impressions), Bing Webmaster Tools (which exposes citation-level data and sampled grounding queries), and referral traffic from the assistants — OpenAI tags ChatGPT referrals with a trackable parameter. Our finding is that the AI-specific portions of this are **not yet exposed through the APIs**, so getting them requires either an account grant or a manual export by the client — see Part 3.

**Attribution honesty.** Branded search and direct traffic movement should be labelled as correlation, not attribution. We do not have a clean causal chain and should not imply one.

## 2.8 A note on terminology

Two vocabularies are in circulation and they describe the same split from different angles.

* **Symptoms and causes** — the diagnostic angle. What is happening to you, and why.

* **Outcomes and process** (also said as "output and input") — the commercial angle. What the client receives, versus the work we perform to produce it.

They are not quite the same cut. Running a crawler is *process* but it is not a *cause*; the finding it produces — "160 of your pages cannot be read by answer engines" — is an *outcome*, and the blocked pages are a *cause*.

Rough guide: **causes and symptoms are both outcomes** from the client's point of view, because both are things we hand them. The process is everything we do to get there — the crawling, the prompt runs, the clustering, the analysis.

This matters because the two vocabularies serve different audiences. Outcomes are what earn a first meeting. Process is what justifies the price once the meeting happens. Both are true; neither leads in the wrong room.

## 2.9 The report shape that follows

1. **Executive summary first.** What is working, what is not.
2. **Then section by section, in order of importance.** Each section: here is the outcome → here is the analysis behind it → here is the likely reason → here is the fix.
3. **The analysis is not an appendix.** It is the reason to believe the finding, and burying it makes the report look like generated filler.
4. **Plus the interactive bucket map**, for clients who want to explore rather than read. Click a bucket, see the client's position and the competitors' in it.
5. **From the second report onward, the competitive activity feed** — what the brands winning each topic changed since the last report (§2.6).
6. **Delivered in a client account on our platform.** We need one anyway for Search Console and analytics permissions, so the questionnaire and the report both live there. It also gives us somewhere to put everything we build later.

***

# Part 3 — How the pilot runs

Constraints for the first four or five engagements. These are deliberately tight: the pilot exists to learn, not to demonstrate maximum capability.

## 3.1 Who and how many

* **Target 4–5 pilots.** The signal comes from these; anything beyond is a bonus data point.

* **Ideal profile:** B2B SaaS, roughly \$5–10M ARR. Take smaller companies if offered, but the learning comes from the target profile.

* **One pilot per client.** If they want a second report, they pay — even at a subsidised rate. If they see enough value to ask, they see enough value to pay, and we should ask.

* **Do not rush.** Take the time to do it properly.

## 3.2 Scope caps

| Constraint          | Pilot setting           | Why                                                                                                                                                                |
| :------------------ | :---------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Topics              | **1**                   | A client may have ten business goals. We pick one. This alone cuts the work by an order of magnitude.                                                              |
| Query clusters      | **\~100**               | The manual selection cap. Roughly half a day to one day of analyst time.                                                                                           |
| Prompts             | **\~500**               | Each cluster expands to about five prompt phrasings. This is the number that drives cost, and it is the one to quote internally.                                   |
| Engines             | **Google AI Mode only** | Google carries far more search volume than ChatGPT, and the gap is not close. ChatGPT is deferred on cost grounds, not importance.                                 |
| Runs per prompt     | **1**                   | Our target methodology is \~10 to average out variability. We are knowingly trading rigour for cost, and should not describe a single run as a stable measurement. |
| Competitor coverage | **All buckets**         | See S5. Cost permitting.                                                                                                                                           |
| Field watch         | **Baseline only**       | See §2.6. The diff produces nothing until the second run, so the pilot captures the snapshot and claims nothing from it.                                           |

Keep the two units apart. The cap applies to **query clusters** — the unit a person reviews and the client approves, roughly 100. Each expands to about five prompt phrasings, giving the ~500 **prompts** the engines are actually billed on. When someone says "we're doing 100" in a meeting, they mean clusters.

## 3.3 Selecting the clusters

This is the manual step and the main consumer of our time. The unit here is the query cluster, not the individual prompt — see the note in §3.2.

**If the client already has a keyword list** — most clients with an SEO agency do — the work is small. We take their list, and the extra value we add is telling them what is missing, wrong or overweighted. Example: Northstar hands us 250 keywords for its CRM, of which exactly one covers email-inbox integration — while that sub-topic has real demand and they already ship the feature. That gap is the finding.

**If the client has no list**, we start from their stated business goals, turn those into high-level topics, gather a keyword universe, cluster it under the topics, and narrow down.

The important and slightly counterintuitive point: **narrowing a universe of 100,000 down to 100 clusters costs the same as narrowing it to 2,000.** The cost is in reading the universe, not in the size of what comes out. So capping the output does not cap the effort — capping the *topic* does.

Traditional agencies narrow using search volume as a filter, which is increasingly a poor proxy. We can rank with a language model against the client's actual business goals instead, which is better, but where to draw the line is a judgement call made per client by looking at the data.

**Effort-versus-impact rule:** do not spend three days hunting the one extra cluster that marginally beats the rest. Clients with a list already know their questions; clients without one cannot evaluate ours. Take the model's ranking, sanity-check it, move on.

## 3.4 What we need from the client

| What                                         | Why                                                                                                   | How to get it                                                                                                                                                                                                     |
| :------------------------------------------- | :---------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Business goals                               | They become the topics. Everything else hangs off them.                                               | Questionnaire and onboarding call. We can guess from the website, but we should confirm.                                                                                                                          |
| Positioning — what they want to be known for | The benchmark for S6, brand-narrative risk. Without it we cannot say whether the AI's story is wrong. | Questionnaire.                                                                                                                                                                                                    |
| Existing keyword/prompt list, if any         | Removes most of the manual selection work.                                                            | Ask early — it changes the effort estimate.                                                                                                                                                                       |
| Search Console and Bing Webmaster access     | AI-surface impressions and cited pages. The AI-specific data is not yet exposed via API.              | Either add our account, or they export and upload. **Do it live on the onboarding call** with whoever holds access — the export is buried in the interface, and handling it by email turns into a multi-day loop. |

***

# Part 4 — What each team does with this

**Commercial.** Symptoms are what earn the meeting; process is what justifies the price inside it. Lead with outcomes: what the AI says about you, where you are recommended and where a competitor is, which of your pages the engines can and cannot read, and what your competitors changed last month. Save the pipeline description for the second conversation. Say *prompts*, not *keywords*. On the field watch (§2.6), say what the client learns and never how we obtain it.

**Brand and report design.** The report shape is in §2.9: outcome first, analysis attached rather than appended. The bucket map is the signature visual and the strongest single artefact we have — it needs to work as a three-dimensional grid that can be filtered by topic and clicked into, with competitors overlaid. There is an open idea to render the bucket markers as the brand's own mark rather than plain boxes. The competitive activity feed needs its own treatment: it is a timeline, not a grid, and it is the part of the report a client will read first. The report should be a live page in the client's account, not a PDF attachment.

**Engineering and data.** Build order is roughly: Layer 0 and Layer 1 first — these must exist for any client. Then Family A causes, which are cheap, unambiguous and part of every credible audit. Then the field watch (§2.6) together with Family E, which is where the differentiation sits and which share the same off-site source list. Families B and D next. Family C last: C10 is hard to measure, C11 needs research before we commit to it at all, and C12 is on-request and priced separately. Setting those three aside, the remaining items in Families A–D cost close to nothing per additional client once built, which is why they are in scope despite uncertain individual impact.

***

## Open questions

1. **Post-purchase.** Onboarding, usage, support and troubleshooting questions are currently out of scope. Bringing them in means a ninth question type and 144 buckets rather than 128. Either decision is workable; it needs making rather than drifting.
2. **Geography.** We collect questions by geography, but "near me" style questions carry no location in the text itself. For a client operating in one place this is fine; for a multi-location brand it is unsolved.
3. **Forward-looking claims.** "Do these four things and you move from position five to position two" — we cannot say that yet. An experienced agency can, from pattern recognition across many engagements. We will be able to once we have run enough.
4. **A single headline number**, equivalent to what domain authority became in SEO. Clients like one number to move. We do not have one, and averaging bucket positions loses the information that makes the buckets useful in the first place.

***

# Appendix — The evidence base

Every external claim this document makes, with its source and how strong that source actually is.

This appendix exists because of §2.2. If we are going to say out loud that some of our causes are documented and others are guesses, we have to be able to show which is which — to a co-founder, to an engineer deciding what to build first, and to a prospect who pushes back on a number in the report. **Nothing below should be described to a client as more certain than the tier it sits in.**

The tiers, strongest first:

| Tier                         | What it means                                                                                    |
| :--------------------------- | :----------------------------------------------------------------------------------------------- |
| **Documented**               | The platform states it in its own guidance. As close to fact as this field gets.                 |
| **Peer-reviewed / benchmark** | Published academic work or a controlled benchmark. Strong, but usually narrow in scope.          |
| **Observational**            | Large-scale measurement, often by a vendor. Shows a real pattern; establishes no mechanism.      |
| **Correlational**            | A relationship found in data, with no isolation of cause. The weakest tier we cite at all.       |
| **Our observation**          | Something we have seen or concluded ourselves, with no external source. Never cite as evidence.  |

## A1 — Documented

Platform guidance. Safe to state as fact.

| Claim                                                                                                                    | Where          | Source                                                                                                                                                                                                       |
| :----------------------------------------------------------------------------------------------------------------------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A page must be indexed **and** snippet-eligible before it can appear as a supporting link in AI Overviews or AI Mode      | C2             | [Google — AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)                                                                                                     |
| Generative search features are rooted in core Search ranking and quality systems                                          | §2.2, C15      | [Google — AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)                                                                                                |
| Search-inclusion bots and training bots are distinct; blocking one is not blocking the other (OAI-SearchBot vs GPTBot)    | C1             | [OpenAI publisher guidance](https://help.openai.com/en/articles/12627856) · [Perplexity crawler docs](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)                                          |
| Google renders JavaScript but acknowledges limits; recommends server-side or static rendering over dynamic rendering      | C3             | [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) · [Dynamic rendering](https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering) |
| Sitemaps aid discovery but guarantee neither indexation nor citation; `lastmod` counts only when it reflects a real change | C4, C9         | [Sitemaps overview](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview) · [`lastmod` guidance](https://developers.google.com/search/blog/2023/06/sitemaps-lastmod-ping)            |
| IndexNow can bring current information into search and AI experiences faster                                             | C9             | [IndexNow FAQ](https://www.indexnow.org/faq) · [Bing — sitemaps in AI-powered search](https://blogs.bing.com/webmaster/July-2025/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search)             |
| Page experience is in Google's AI guidance, but relevance can outweigh a subpar experience                                | C5             | [Page experience](https://developers.google.com/search/docs/appearance/page-experience) · [AI features](https://developers.google.com/search/docs/appearance/ai-features)                                     |
| Duplicate content blurs intent and can surface outdated URLs in AI answers                                               | C6             | [Bing — duplicate content and AI search](https://blogs.bing.com/webmaster/December-2025/Does-Duplicate-Content-Hurt-SEO-and-AI-Search-Visibility) · [Google ranking systems](https://developers.google.com/search/docs/appearance/ranking-systems-guide) |
| Links are used to discover pages and understand relevance; AI guidance recommends internal links for findability         | C7             | [Link best practices](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) · [AI features](https://developers.google.com/search/docs/appearance/ai-features)                          |
| Titles and prominent headings build the title link; guidance asks for titles and headings that summarise accurately      | C8             | [Title links](https://developers.google.com/search/docs/appearance/title-link) · [Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)                           |
| AI Mode and AI Overviews generate multiple related searches — query fan-out                                              | C10            | [Google — AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)                                                                                                |
| Bing exposes sampled grounding queries and citation-level data                                                           | C10, §2.7      | [Bing AI Performance](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)                                                                        |
| Tiny content chunks and special "AI writing styles" are unnecessary                                                      | C11            | [Google — AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)                                                                                                |
| Unique, non-commodity content likely influences long-term generative-search presence more than Google's other suggestions | C12            | [AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) · [Helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)    |
| E-E-A-T is not a single ranking factor                                                                                   | C13            | [Google — helpful content and E-E-A-T](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)                                                                                        |
| Link analysis and PageRank remain part of core ranking                                                                   | C14            | [Ranking systems guide](https://developers.google.com/search/docs/appearance/ranking-systems-guide)                                                                                                           |
| Google warns against scaled pages and inauthentic mentions; generative features depend on core quality and spam systems  | C15            | [AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) · [Spam policy update](https://developers.google.com/search/blog/2024/03/core-update-spam-policies)     |
| No special schema is required for generative AI search; Google warns against overfocusing on it                          | C16            | [Structured data intro](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) · [AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) |
| Current Merchant Center and Business Profile data recommended for AI features; ChatGPT uses merchant metadata and feeds  | C16            | [AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) · [OpenAI shopping docs](https://help.openai.com/en/articles/11128490-shopping-with-chatgpt-search)     |
| Existing image and video SEO practices also optimise for generative AI features                                          | C19            | [AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) · [Image SEO](https://developers.google.com/search/docs/appearance/google-images)                       |
| Explicit locale URLs and `hreflang` are recommended; crawlers may not discover dynamically served regional variants      | C20            | [Managing multi-regional sites](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites)                                                                               |
| Search Console's Generative AI Performance report separates AI Mode and AI Overview impressions                          | §2.7, §3.4     | [Search Console documentation](https://support.google.com/webmasters/answer/16984139)                                                                                                                         |
| OpenAI tags ChatGPT referrals with a trackable parameter (`utm_source=chatgpt.com`)                                      | §2.7           | [OpenAI publisher FAQ](https://help.openai.com/en/articles/12627856)                                                                                                                                          |

## A2 — Peer-reviewed and benchmark

| Claim                                                                                                                       | Where     | Source                                                                                                                                                                                                        |
| :-------------------------------------------------------------------------------------------------------------------------- | :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Retrieval ranking is more influential than conversational-SEO content transformations; many popular rewrites are ineffective or harmful | C11       | [C-SEO Bench, NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/27aa3aeff0f8460a7b43d30fa6c5c032-Abstract-Datasets_and_Benchmarks_Track.html)                                            |
| Generative search engines show documented citation-correctness and completeness failures                                    | C18       | [Evaluating Verifiability in Generative Search Engines](https://arxiv.org/abs/2304.09848)                                                                                                                      |
| Repeated measurements, paraphrases, controls and human validation are recommended for this kind of measurement              | S1        | [Critical review of 45 GEO/AEO studies, 2026](https://arxiv.org/abs/2607.14035)                                                                                                                                |
| Citation *selection* is distinct from citation *absorption* — how much a source shapes the answer's facts and language      | S2        | [Citation selection vs absorption](https://arxiv.org/abs/2604.25707)                                                                                                                                           |
| Awareness staging adapted from Eugene Schwartz's five stages; we use four and drop "completely unaware"                     | Framework §3 | [Levels of awareness](https://adlibrary.com/glossary/levels-of-awareness)                                                                                                                                      |

## A3 — Observational

Large-scale measurement. The direction is consistent; the numbers are not constants and should never be quoted to a client as fixed.

| Claim                                                                                                        | Where     | Scale                        | Source                                                                                                                       |
| :------------------------------------------------------------------------------------------------------------ | :-------- | :--------------------------- | :--------------------------------------------------------------------------------------------------------------------------- |
| Monthly drift of ~40–60% in which domains get cited, across major platforms                                  | S1, §3.2  | 80,000 prompts               | [Profound — AI search volatility](https://www.tryprofound.com/blog/ai-search-volatility)                                     |
| The majority of citations produce no explicit brand mention (62% in study) — the *ghost citation*            | S2        | Semrush study                | [Semrush — ghost citations](https://www.semrush.com/blog/the-ghost-citations-study/)                                          |
| 85.7% of URL-grounded citations point to third-party sites                                                    | C17       | 167,551 citations, 128 brands | [Cross-market brand-source study](https://arxiv.org/abs/2606.25787)                                                          |
| Even brand-specific answers draw materially from media, social and institutional sources                      | C17       | 27M citations                | [Profound — citation categories](https://www.tryprofound.com/blog/enhanced-citation-categories)                              |
| Only 41.6% agreement on the top-recommended brand across three models                                         | S5        | Cross-model study            | [Category-ownership study](https://arxiv.org/abs/2606.23057)                                                                 |
| Genuine recommendations are followed by materially more branded search and site visits than neutral name-drops | S4        | Opt-in conversations + clickstream | [Prompt-to-purchase study](https://arxiv.org/abs/2606.10907) — **not a randomised trial**                                |
| Query language materially changes which sources get cited                                                     | C20       | 3.25B citations, 7 models, 14 countries | [Profound — query language and citations](https://www.tryprofound.com/blog/how-query-language-reshapes-ai-citations) |
| Only ~12% URL overlap between AI citations and the top ten results for the original prompt                    | §2.2      | Ahrefs study                 | [Ahrefs — AI search overlap](https://ahrefs.com/blog/ai-search-overlap/)                                                     |

## A4 — Correlational

**These establish no mechanism.** §2.2's rule applies with full force: never present one of these as a cause.

| Claim                                                                                              | Where | Scale         | Source                                                                                         |
| :-------------------------------------------------------------------------------------------------- | :---- | :------------ | :--------------------------------------------------------------------------------------------- |
| Higher-authority domains showed stronger AI visibility                                             | C14   | 1,000 domains | [Semrush — backlinks and AI search](https://www.semrush.com/blog/backlinks-ai-search-study/)   |
| Weak relationship for raw backlink volume; much stronger for broad branded web mentions and anchors | C14   | 75,000 brands | [Ahrefs — AI brand visibility correlations](https://ahrefs.com/blog/ai-brand-visibility-correlations/) |
| YouTube mentions had the strongest correlation among the brand-visibility factors tested            | C19   | 75,000 brands | [Ahrefs — AI brand visibility correlations](https://ahrefs.com/blog/ai-brand-visibility-correlations/) |

## A5 — Our own observations

No external source. These are ours, they may be wrong, and they must never be presented to a client as evidence. They are listed here precisely so nobody mistakes them for the tiers above.

| Observation                                                                                                                  | Where     | Status                                                                        |
| :---------------------------------------------------------------------------------------------------------------------------- | :-------- | :---------------------------------------------------------------------------- |
| ChatGPT exposes its fan-out queries to anyone inspecting network traffic                                                      | C10       | Undocumented behaviour. Could disappear without notice.                       |
| Competition in some non-English markets is materially weaker than the equivalent English one                                  | C20       | Verify per market before saying it to a client.                               |
| The bar for information gain is lower than "novel to the world" — a named expert asserting something known can still signal   | C12       | Our working view. Goes beyond anything Google states.                         |
| ~10 runs per prompt as the methodology target                                                                                 | S1, §3.2  | A judgement call, not a published standard. Pilot runs 1 (see §3.2).          |
| Comparisons answered largely from review sites and communities, pricing from brand pages, risk questions from docs and forums | §1.3, Framework §5.1 | Working expectation. To be tested per client, not assumed.                    |
| Titles, headings, descriptions and URLs matter most at the moment the assistant chooses which candidate page to open          | C8        | Hypothesis, currently unevidenced. Test where a client ranks but is absent.   |
| The eight question types are the right cut                                                                                    | Framework §5, §11 | Not yet validated against a real client's data. Expect to add a type.         |

***

*Where this document records uncertainty, the uncertainty is real and should not be smoothed over in client-facing material.*
