# Product

> **High-level source of truth for what AEOxoxo is and what we sell.** Descriptive, not persuasive — everything here should be verifiable against the running product.
>
> This file is deliberately short. The full product definition lives in two documents in [`../product/`](../product/) and is not restated here:
>
> - **[`product/framework.md`](../product/framework.md)** — the classification vocabulary. What a question *is*.
> - **[`product/aeo-product-spec.md`](../product/aeo-product-spec.md)** — the v1 product spec. What we *do* about it.
>
> Engineering substrate → [`engineering.md`](engineering.md). Market and competitors → [`market.md`](market.md). Commercial motion → [`gtm.md`](gtm.md).

---

## What AEOxoxo is

A company wants to be recommended when a potential customer asks an AI assistant a question. **We tell them whether that is happening, why it is or is not, and what to do about it.**

That is the whole product in a sentence. Everything below is how.

---

## What we sell today

**An analyst-delivered consultation report.** We run the measurement and the diagnosis, and hand over findings and a ranked action register in a client account on our platform. There are no embedded people at the client, and the client does not operate the tooling themselves.

The report is the deliverable. The platform exists because we need an account for Search Console and analytics permissions anyway, and because a live page beats a PDF attachment.

Pilot constraints — how many, who, and what scope — are in [`gtm.md`](gtm.md) and spec §3.

---

## The product in four steps

The order matters, and the report is read in the same order: outcome first, then the analysis that produced it.

**1. The map.** "Are we visible in AI search?" is not answerable — visible to whom, asking what? So every question a potential customer might ask in the client's category is sorted into buckets. **128 buckets**, produced by classifying each question three ways at once: awareness stage × question type × search intent. Above the buckets sits the **topic** — a business goal the client actually cares about, which they give us. Each topic gets its own 128.

The bucket rule: everything inside a bucket should be improvable by roughly the same kind of work. If that holds, a weak bucket is a work order.

The three axes, every value on them, and why a third axis is needed at all are defined in the framework and **nowhere else**.

**2. Symptoms.** For each bucket we ask the AI engines the real questions and record what comes back. Mentioned? Cited? Recommended? Recommended *first*? Who instead? Six measurements — cross-engine baseline, the answer-participation funnel, retrieval-gap diagnosis, recommendation stance, competitive displacement, and answer accuracy / brand-narrative risk. Symptoms are observed facts and require no guesswork.

**3. Causes.** Symptoms say where you are losing, not why. Twenty conditions in six families — Access, Clarity, Substance, Trust, Off-site, and a conditional family — covering the client's site, their data, and how the rest of the internet talks about them. Causes are hypotheses until tested.

Causes arrive from two directions: that list worked top-down, and the **field watch** — crawling and diffing every competitor and the platforms that feed answers in a category, week over week. The second is much harder to reproduce and is where the advantage sits.

**4. Actions.** A register in which every recommendation states the prompt and engine affected, what the answer says today with evidence, the stage at which it failed, the proposed fix, the leading indicator, effort and owner, **how confident we are in the diagnosis**, and how we will retest.

---

## The honest position

This is a product constraint, not a marketing note, and it governs everything written or said about the product.

**We can measure symptoms with confidence. We cannot yet state which causes drive which symptoms.** Nobody can — the engines do not publish their pipelines. Some causes have documented platform backing; most are widely believed and untested. The causes list is a research programme, not a checklist of known truths.

The rule that follows: **state symptoms as findings, state causes as diagnosis with reasoning attached, and never present a correlational vendor study as a mechanism.** Spec §2.2 and the evidence-tier appendix exist to make this checkable.

---

## What the platform is built from

Seven first-class entities. Everything else composes these.

| Entity | What it is |
|--------|-----------|
| **Brand profile** | Structured profile researched from the open internet and the brand's own site — industries, business model, segments, geographies, competitors, and a hierarchical topic tree. Operator-triggered, reviewed and corrected by a human. |
| **Brand files** | Everything the structured profile has no field for — tone, keyword priorities, playbooks, style guides, taxonomies. File names and short overviews are exposed to the agent at runtime, so it pulls what it needs instead of carrying everything in context. |
| **Skills** | Saved, reusable procedures for agents. Method gets encoded once and reused across every brand, so an operator invokes rather than re-derives. |
| **Workflows** | Scheduled, deterministic analysis jobs. No LLM, so no token cost, so they run continuously without a human present, depositing intermediate analysis for agents to pick up. Created agentically rather than written by hand. |
| **Actions** | Discrete, well-scoped work items tied to a specific finding. Categories: off-site citation, content create, content update, technical fix, validation, custom. Some execute against connected systems; the rest route to review. |
| **Reports** | The stakeholder-facing analysis. Stays current as new signal lands. |
| **Integrations** | Two kinds. *Per-brand*, connected once by the customer: Search Console, GA, Bing Webmaster Tools, CMS, LinkedIn, Reddit. *Platform-level*, always available: Google Search, ChatGPT search, Perplexity search, exposed directly to the agent — this is how analysis stays grounded in what is live rather than a stale index. The full data-source list is in [`engineering.md`](engineering.md) → *unified data and action layer*. |

**Two kinds of execution.** Agents reason and cost tokens; workflows are deterministic and cost nothing. Workflows do the cheap, high-volume, scheduled analysis and leave output behind; agents read it and do the judgement-heavy part. That composition is how a brand gets continuous coverage without paying for continuous intelligence.

**Two senses of "audit."** The *brand research pass* builds the grounding layer. The *AEO audit* is the ongoing analysis that produces reports and actions. Different things.

Platform surfaces: dashboard, report centre, review centre with configurable oversight, scheduling, and teams/organisations with shared credits and permissions.

---

## How it is operated

The product is exposed as an **SDK and a CLI over one client, plus an MCP server** (see [`engineering.md`](engineering.md) for the API layer and its constraints). The preferred operator surface today is **Claude**, with the tools connected and pre-built skills ready to run.

**This is a cost decision.** The same volume of agent work through the API costs a great deal more than a flat monthly Claude subscription with the tooling connected, and pre-built skills mean an operator cannot get the invocation wrong.

**The tradeoff is honest: full automation is not possible this way.** Workflows run on their own, but agent runs need someone at the keyboard. The CLI + MCP shape is not a workaround bolted on for Claude — it is the same architecture the internal agentic loop uses, which is where this goes once token cost stops binding.

---

## Language rules

- **Say *prompts*, not *keywords*, in front of a client.** The underlying data is keyword data; the client's world is prompts, and "keyword" signals repackaged SEO.
- **On the field watch, describe what the client learns, never how we obtain it.** A competitor with an engineering team could build crawl-and-diff quickly. The defensible part is knowing where to look and what a change means.
- Where a document records uncertainty, that uncertainty is real and should not be smoothed over in client-facing material.

---

## Open decisions

1. **Post-purchase questions** are out of scope. Bringing them in means a ninth question type and 144 buckets rather than 128. Needs deciding rather than drifting.
2. **Geography.** "Near me" questions carry no location in the text. Fine for a single-location client, unsolved for a multi-location brand.
3. **Forward-looking claims.** We cannot yet say "do these four things and you move from position five to two." We will be able to once enough engagements have run.
4. **A single headline number.** Clients want one number to move. Averaging bucket positions destroys the information that makes the buckets useful. Unresolved.
5. **The eight question types are the least settled part of the framework** and are not yet validated against real client data. Expect to add one.
6. **Positioning and pricing have no canonical home, by decision.** Neither exists. Give them a file only when they do — do not let a version of either accumulate inside another file in the meantime. Pricing is tracked as an open decision in [`gtm.md`](gtm.md).

---

_Last updated: 2026-09-01_
