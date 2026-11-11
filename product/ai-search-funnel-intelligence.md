# AI Search Funnel Intelligence

**Status:** product idea, September 2026. Not part of the v1 spec ([`aeo-product-spec.md`](aeo-product-spec.md)) and not decided. The current rule on attribution is in [`../canonical/gtm.md`](../canonical/gtm.md): branded search and direct traffic are correlation, not attribution.

---

AI search is becoming an important way for customers to discover brands—but measuring its real impact is difficult.

Website analytics can identify some traffic coming directly from platforms such as ChatGPT, Perplexity, or Google’s AI experiences. But much of the journey remains invisible. Someone might discover a company through an AI answer, return later through Google, visit the website directly, or mention the original source only during a sales conversation.

Our platform would connect the signals spread across that journey:

* Website analytics and identifiable AI referrals
* CRM data covering leads, pipeline, customers, and revenue
* “How did you hear about us?” responses
* Notes from sales and customer-success conversations
* Other relevant attribution and customer-research data

Bringing these sources together would give marketers a more complete view of how AI search is influencing the funnel—from discovery and website visits through to leads, opportunities, and revenue.

The important point is that this will never be perfect attribution. Some AI activity cannot be tracked, self-reported answers are incomplete, and customer journeys rarely follow a clean, linear path. We should be open about that.

The value is in producing a consistent, directionally reliable signal.

For example, the platform might show that measurable AI traffic increased from 1% last month to 5% this month. Those numbers may significantly underestimate AI’s true contribution. But if the measurement method remains consistent and the underlying data is meaningful, the change strongly suggests that AI-driven discovery has grown substantially.

This allows us to answer the questions marketers actually care about:

* Is AI search becoming a more important acquisition channel?
* Is that visibility translating into leads and pipeline?
* Which content and topics are driving the strongest outcomes?
* Is our investment in SEO and AEO producing measurable progress?

We are not selling perfect attribution or pretending we can observe every interaction with AI. We are offering **AI Search Funnel Intelligence**: the best available view of how AI discovery is influencing customer behaviour and commercial outcomes.

The promise is simple: connect scattered first-party signals, measure them consistently, and help marketers understand whether AI search’s contribution to the business is growing. It replaces guesswork with evidence—imperfect, but credible and useful enough to guide decisions.

---

## Notes from comparing competitor features

Our read of what Profound, AthenaHQ and Demand-Genius offer, against what we have or could build.

**Profound**

* Noble integration: easy. We could also build this eventually.
* Synthetic prompts, asking AI and analysing the answers: already built.
* Agent analytics benchmark (analysing log files): can be built if needed.
* Their data: too big. We can’t compete on it with the current GTM.
* Page quality check: they compare against a huge set of existing pages. We could have another mechanism that produces a page score; we still have to figure out whether it’s good.

**AthenaHQ**

* Commerce attribution seems nice. We can build it, but it’s never accurate, it could be far from reality, and it’s really messy. We could try Athena to see how they do it, but in practice there is no real way to do attribution in SEO/AEO. How directionally correct the data is, we can only find out by trying. The B2B journey version of it is implementable.

**Demand-Genius**

* We need to find where their 84% figure comes from, but I think we are good on these. We may need to add other sources, such as sales transcripts.
