# Engineering

> Canonical reference for the engineering substrate underneath AEOxoxo — what exists, what it does, and what is not yet recorded anywhere.
>
> **Internal and investor-facing today.** None of this is currently sold or listed as a feature; customers experience it indirectly, as broader coverage and analysis that would not be economical to produce by hand. Whether it stays that way is an open decision at the bottom of this file.
>
> What the product *is* lives in [`product.md`](product.md). This file is the layer beneath it.

---

## The substrate

Nine systems. Each is real and running unless noted. Together they are the reason the measurement and diagnosis described in [`product/aeo-product-spec.md`](../product/aeo-product-spec.md) can be produced at all — particularly the field watch (§2.6), which is Snake.blue plus the versioned page store and has no cheap substitute.

| System | What it is | Status |
|--------|-----------|--------|
| **Agentic runtime** | Custom Go runtime running thousands of agent loops concurrently — past the concurrency ceiling of typical Python orchestration frameworks. Built on prior production AI-runtime work at RedisAI and Lightning.ai. | Live |
| **Snake.blue** | Proprietary AI-first crawler. Stable, batched crawls at any scale, across both brand and competitor sites, without depending on external crawl infrastructure. | Live |
| **Versioned page store** | Pages from Snake.blue stored versioned in our own database — current and historical state of any brand or competitor URL, queryable by agents. Lets a long run reason about *what changed*, not only what is. | Live |
| **Keyword lake** | Millions of keywords with volume, difficulty and ranking data cached in our own database behind a fast query layer agents hit directly, rather than retrieved through an LLM context window. Sourced from Semrush and DataForSEO. | Live |
| **Strategy knowledge base** | Vetted, versioned library of SEO/AEO strategy patterns distilled from controlled experiments, pre-seeded into agents on every run so an agent composes from validated technique rather than reinventing it. | Live — see caveat below |
| **Ranking signal intelligence** | 80+ ranking signals captured with automated prioritization. | Live |
| **Unified data and action layer** | Single-authentication access to Google Search Console, GA4, Bing Webmaster Tools, CMS platforms, social channels, Google Trends, Maps, review platforms and SERP data. | Live, expanding |
| **Semantic page and keyword intelligence** | Brand and competitor pages and keywords auto-indexed as embeddings, searchable by meaning rather than exact match. | Live |
| **Data routing architecture** | Retrieval and action execution routed through the infrastructure rather than through an LLM's context window (inspired by 2024 codemode research), so reliability holds across long multi-source runs that break context-window-based tools mid-flow. | Live |

**Caveat on the strategy knowledge base.** It was described as maintained by an in-house research team. Whether that team exists in any form today is unconfirmed — see *Gaps* below. The asset is real; the maintenance arrangement needs restating.

**Deeper docs outside canonical.**

- How keywords are filed under a brand's topics in bifrost: [`engineering/keywords-topics.html`](../engineering/keywords-topics.html), with the guide to choosing a topic list in [`engineering/selecting-topic-prompt.md`](../engineering/selecting-topic-prompt.md).
- A change-tracking product built on the crawler: [`product/bluesnake-change-tracking-spec.md`](../product/bluesnake-change-tracking-spec.md). The spec calls the crawler *Bluesnake*; this file calls it *Snake.blue*. One name should win.
- The engineering backlog is the Doklin board in [`engineering/todo/`](../engineering/todo/).

---

## The AEOxoxo API layer

The operator-facing surface over the substrate. This is what an analyst or an agent actually touches.

- **One Python package, `aeo`**, shipping an **SDK and a CLI over the same client** — same endpoints, same client, so the choice between them is about what happens to the value, not about capability. The CLI is for when the result *is* the answer; the SDK for when the result feeds another call.
- **An MCP server**, also named `aeo`, which is a bootstrap rather than an API: it mints a single-use OTP that dies three minutes after minting, exchanged via `aeo configure`. It also serves the **playbooks**, which live on the server rather than in the package.
- **Access is staff-admin only.** A rejected exchange is normally an account problem, not a command problem.

### The data model

```
brand → topics → questions → answers / grounding → findings
```

Five resource groups: `brand`, `questions`, `findings`, `grounding`, `answers`. Most work runs topics → questions → answers → findings: read a brand's topics, list the questions under each, ask an engine, write the finding back.

`grounding` returns ranked links; `answers` returns cited prose. **They are not substitutes** — a brand can rank first and be absent from the answer, and that gap is usually the finding itself.

### Deliberate constraints

These are decisions about what an agent may do unattended, not gaps to work around:

- **Question text is never truncated on write.** `question.value` is the literal string typed into the engine. Printing a question and retyping it into the next command runs it through a model that may quietly improve the wording — which breaks the measurement without failing.
- **Absent by design:** question writes, findings delete, the keyword corpus, AI Overview, other search verticals.
- **Nothing retries.** `grounding` and `answers` reach paid third parties billed to the owning org. A connection error means nothing was decided — the call may have run and been billed, so re-running is a choice to pay twice. Do not add a retry wrapper.
- **`answers chatgpt` drives a real browser session.** One to three minutes is normal, four to five happens, the client waits eight on purpose. Killing it early does not stop the billing.
- **Field values are served by the server** (`aeo brand fields`) so they cannot go stale. Never guess a controlled value.
- **Writes require confirmation.** `brand set/add/remove` and `findings save/update` land on live projects other people read. `set` replaces a list whole; `add`/`remove` merge — replacing topics untracks the omitted ones.

An empty answer, a "returned no answer", or a sources list the brand is absent from is **a finding, not an error**.

---

## Gaps

The largest weakness in canonical. None of the following is recorded anywhere, which means the substrate above cannot be handed to a new engineer, audited by an investor, or recovered if a laptop dies.

1. **Repositories.** No repo names, hosts or branch conventions recorded for any of the nine systems or the `aeo` package.
2. **Infrastructure.** No cloud accounts, regions, hosting arrangement, or record of where the Go runtime and Snake.blue actually run.
3. **Deploy path.** No record of how anything ships, or who can ship it.
4. **Verification of "Live".** The status column is inherited and undated. Each row should be confirmed against the running system and stamped.
5. **The research team.** Whether the strategy knowledge base has an owner and a maintenance cadence today.
6. **Data retention and cost.** The keyword lake and versioned page store grow indefinitely; no retention policy or cost trajectory is recorded.

---

## Open decisions

- **Does the substrate stay internal, or become the pitch?** Under an analyst-delivered report, the substrate is arguably what a buyer is paying for, which argues for surfacing it. Against that: it is also the thing a competitor would most want to copy. See the defensibility discussion in [`market.md`](market.md).
- **Self-serve optionality.** The platform underneath is autonomous-capable. Whether that becomes a product direction or stays latent is unresolved.

---

_Last updated: 2026-11-11_
