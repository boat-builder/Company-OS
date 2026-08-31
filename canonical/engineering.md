# Engineering

> Canonical reference for the **engineering substrate underneath Berlin** — the internal Tools layer, the moat items, and the architectural reasons Berlin's unit economics work.
>
> **This is internal and investor-facing, not customer-facing.** Nothing in this document is a feature Berlin sells, messages, or lists on a pricing page. Customers experience all of it indirectly: faster outputs, deeper coverage, lower price point, one operator keeping up with their account.
>
> Product capabilities and the user-facing feature reference live in [`product.md`](product.md).

***

## The Tools Layer — Internal Infrastructure

Berlin runs on top of an internal Tools layer. It is **not a product, is not sold, and is not exposed to users** as something to subscribe to or configure. It is the architecture that lets Berlin's agents reach the data sources and action endpoints needed to execute.

The Tools layer provides:

* A **first-party data engine** — the **keyword lake** (millions of keywords cached in Berlin's own database, queryable for AI), the **versioned page store** (pages from Snake.blue stored versioned and queryable to agents — current and historical state), site crawling and competitor monitoring via **Snake.blue** (the proprietary AI-first crawler), and ranking signal intelligence covering 80+ signals with automated prioritization.

* A **strategy knowledge base** — a vetted, versioned library of SEO/AEO strategy patterns maintained by Berlin's in-house research team, distilled from controlled experiments on what is currently working. Pre-seeded into agents on every audit run so every account benefits from every experiment we run.

* A **unified data and action layer** — single-authentication access to Google Search Console, GA4, Bing Webmaster Tools, CMS platforms, social channels, Google Trends, Google Maps, review platforms, search results data, and a continuously growing list of data sources and action endpoints.

* **Semantic page and keyword intelligence** — brand and competitor pages and keywords auto-indexed as embeddings, searchable by meaning rather than exact match.

* A **proprietary data routing architecture** — retrieval and action execution happen through the infrastructure rather than through an LLM's context window, eliminating hallucination from context overflow.

These capabilities are real and load-bearing for what Berlin can do. The user never sees them as a product, and they should not be sold or messaged as features. They are the **engineering substrate that drives Berlin's unit economics** — the reason one FDM can serve more accounts per head than a human-led agency or a Daydream-style Growth Lead can, and the reason Berlin can price at a fraction of agency cost without breaking margin.

***

## The Engineering Moat (Investor / Internal Reference)

For investor and internal context, the substrate decomposes into:

* **Go-based agentic runtime.** Custom-built in Go to run thousands of agent loops concurrently — a concurrency ceiling typical Python orchestration frameworks cannot reach. Built on the founder's prior production AI-runtime work at RedisAI and Lightning.ai. Structural reason one Berlin FDM can serve multiple customers in parallel without queueing or degraded latency.

* **Strategy knowledge base.** A vetted, versioned library of SEO/AEO strategy patterns maintained by Berlin's in-house research team and distilled from controlled experiments on what is currently working across the live search and AI-search landscape. Pre-seeded into agents on every audit run, so the agent doesn't reinvent strategy from scratch — it composes from techniques our research has already validated. This is what compounds: every experiment we run improves every account. (Subsumes what earlier docs called the "curated strategy catalog"; *strategy knowledge base* is now the canonical term.)

* **Proprietary crawl (Snake.blue).** AI-first crawler. Stable, batched crawls at any scale; brand and competitor data fresh and queryable without depending on external infrastructure.

* **Keyword lake — queryable for AI.** Millions of keywords behind a fast query layer that agents hit directly — not a vector-search guess and not raw context dumps. Keyword intelligence sourced from providers like Semrush and DataForSEO and cached in Berlin's own database. Customers never need their own third-party subscriptions; data costs compound down over time as the cache grows. ("Keyword lake" is the canonical term for this substrate piece; "keyword store" is the older framing.)

* **Versioned page store — queryable to agents.** Pages from Snake.blue stored versioned in Berlin's own database, so agents can query both current and historical state of any brand or competitor URL. Behind the same fast query layer as the keyword lake — accessed directly, not retrieved through an LLM's context window. Lets long agentic runs reason about *what changed*, not only what is.

* **Proprietary data routing architecture.** Naive agentic tool-use fills the LLM's context window and degrades reliability as operations scale. Berlin's data routing layer (inspired by 2024 codemode research) routes data through the unified data layer instead — reliability holds across long, multi-source agentic work that breaks other AI-assisted tools mid-flow.

* **80+ ranking-signal coverage.** Automated signal capture and prioritization across the lifecycle, so the FDM doesn't burn cycles assembling them by hand.

Together this substrate is *why* Berlin can offer agency-equivalent scope at a fraction of agency cost without breaking margin — and *why* the platform underneath the FDM is genuinely autonomous-capable, leaving latent self-serve optionality for the future without it being a current focus.

***

## Substrate Reference Table

Listed for internal and investor reference only. Not features Berlin sells, messages, or surfaces in customer pricing pages.

| Capability                                | Description                                                                                                                                                                                                                                                                                                                                     | Status           |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **Agentic Runtime**                       | Custom Go-based runtime running thousands of agent loops concurrently. Built on prior production AI-runtime work at RedisAI and Lightning.ai. The structural reason one FDM can serve multiple customers in parallel.                                                                                                                           | Live             |
| **Strategy Knowledge Base**               | Vetted, versioned library of SEO/AEO strategy patterns maintained by Berlin's in-house research team, distilled from controlled experiments on what is currently working. Pre-seeded into agents on every audit run so every account benefits from every experiment we run. (Subsumes what earlier docs called the "curated strategy catalog.") | Live             |
| **Keyword Lake**                          | Millions of keywords with volume, difficulty, ranking data cached in Berlin's own database. Sits behind a fast query layer agents hit directly — queryable for AI rather than retrieved through an LLM's context window. Sourced from Semrush, DataForSEO, and other providers.                                                                 | Live             |
| **Versioned Page Store**                  | Pages from Snake.blue stored versioned in Berlin's own database — both current and historical state of any brand or competitor URL. Queryable to agents through the same fast query layer as the keyword lake. Lets long agentic runs reason about what changed, not only what is.                                                              | Live             |
| **Site Crawling & Competitor Monitoring** | Proprietary AI-first crawler (Snake.blue) running stable, batched crawls at any scale. Keeps site and competitor data fresh and queryable.                                                                                                                                                                                                      | Live             |
| **Ranking Signal Intelligence**           | 80+ ranking signals tracked with automated prioritization.                                                                                                                                                                                                                                                                                      | Live             |
| **Unified Data & Action Layer**           | Single-authentication access to GSC, GA4, Bing Webmaster Tools, CMS, social, Google Trends, Maps, reviews, and more.                                                                                                                                                                                                                            | Live & Expanding |
| **Semantic Page & Keyword Intelligence**  | Brand and competitor pages/keywords auto-indexed as embeddings, searchable by meaning.                                                                                                                                                                                                                                                          | Live             |
| **Proprietary Data Routing Architecture** | Data routed through Berlin's infrastructure instead of an LLM context window, eliminating hallucination from context overflow.                                                                                                                                                                                                                  | Live             |
