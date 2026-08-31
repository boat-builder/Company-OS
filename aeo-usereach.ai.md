# AEO & Organic Growth Process

> A playbook for building an answer-engine optimization (AEO) and organic growth process — from positioning through measurement, A/B testing, and ongoing iteration.

***

## The process at a glance

This playbook lays out a sequence of stages for building an AEO (AI / answer-engine optimization) and organic growth process:

1. **Positioning** — establish a clear, consistent story before doing anything else.
2. **Search demand research** — reverse-engineer the buyer journey into keywords and prompts.
3. **Keyword & prompt research framework** — prioritize the thousands of resulting searches.
4. **Prompt reverse-engineering framework** — work out how to actually rank for a given prompt.
5. **The AI search roadmap** — 5 steps grouped into 3 buckets (foundational, content/on-page, off-page).
6. **Technical SEO** — the 5% that drives 95% of the impact.
7. **Content roadmap** — five principles for prioritizing what to create.
8. **Earning mentions / off-page** — listicles, Reddit, G2, YouTube, PR.
9. **Community & mention outreach** — a targeted, data-driven outreach process.
10. **Measurement** — the metrics that prove value (and the ones to stop chasing).
11. **A/B testing & conversion rate optimization.**
12. **Frequently asked questions.**

A recurring theme throughout: be skeptical of checklists and influencer claims that aren't backed by data. There is no one-size-fits-all; analyze each prompt and keyword, and trust your own data.

***

<br />

## Top takeaways

Five load-bearing claims that anchor the whole approach:

1. **Positioning is infrastructure, not messaging.** LLMs pattern-match on repetition across surfaces. If the homepage, About page, third-party directories, PR, and partner sites all describe the company differently, none of it compounds. Define a stable answer to *"what does this company do, and for whom?"* and codify it everywhere.
2. **Start search-demand research with first-party conversions, not keyword tools.** Top-converting pages in GSC → sales transcripts and support tickets → paid-search winners. Translate the keywords that already convert into the prompts buyers actually use on AI. *"Let the money and the conversions start, then follow from there."*
3. **Reverse-engineer what wins the citation, then match the format.** Run every prompt 3–5× across ChatGPT, Perplexity, Gemini, AI Overviews. Pattern-map the citations. Listicles dominant → earn mentions. Vendor pages dominant + you don't have one → build the page. Reddit dominant → engage. Different prompts demand structurally different content.
4. **3 buckets, not 5 pillars: foundational, content, off-page.** Most teams over-invest in one bucket and skip the other two. Tech SEO is the foundation (don't block AI bots). On-page is new content + content updates. Off-page is earned mentions + community.
5. **Measure recognition, not ranking.** AI is a mention engine, not a referral engine. Track share of voice vs competitors by prompt cohort, brand search volume, direct + branded traffic, and "how did you hear about us" attribution. Stop chasing raw AI referral traffic — it will always look small.

***

## Foundations for a complete AEO strategy

The opening framework frames the whole strategy as **five pillars**, and for each one specifies the artifacts you need to ship and who owns it at what cadence.

| Pillar                         | What it is                                      | Artifacts to ship                                                                                                                              | Owner + cadence                                 |
| ------------------------------ | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **Product Positioning**        | PMM fundamentals. Persona, category, narrative. | Filled Value Prop Canvas · Positioning vs. competitors · Unique PoV on key topics                                                              | Founder + PMM · Quarterly review                |
| **Knowledge Base**             | The context engine every AI + human reads from. | Brand voice + writing guidelines · Positioning + ICP + sales playbook · Win/loss insights + call transcripts · Asset library + style guide     | Marketing + Sales · Living doc (weekly updates) |
| **Target Keywords & Prompts**  | The master list every other pillar reads from.  | Scored keyword list (ICP × intent × opportunity) · Prompt set (Query Fusion Model)                                                             | SEO / Growth Lead · Quarterly updates           |
| **Action Plan**                | Per prompt: build, fix, mention, engage.        | Per-prompt action sheet · Content roadmap (new + revamps + technical SEO) · Community engagement targets · Backlink + mention opportunity list | SEO / Growth Lead · Monthly sprints             |
| **Measure + A/B Test Tactics** | Ship. Measure. Retroactively update.            | GSC + GA dashboards · AI visibility tracker (cohort × model × brand) · Conversion tracking                                                     | SEO + Content teams · Bi-weekly cycles          |

The five pillars map onto the detailed stages below: Product Positioning → Section 1; Knowledge Base → Section 1; Target Keywords & Prompts → Sections 2–4; Action Plan → Sections 5–9; Measure + A/B Test Tactics → Sections 10–11.

**5 pillars vs 3 buckets — a note on framing.** The strategy is presented above as five pillars. The execution side can also be framed as **three buckets** — foundational (tech SEO), content (new + updates), off-page (mentions + community) — covered in Section 5. The two are not in conflict: the five pillars describe *what to ship and who owns it*, the three buckets describe *where the work happens day to day*. Pillars 1–3 feed the inputs; Pillar 4 ("Action Plan") is the work that gets split across the three buckets; Pillar 5 closes the loop.

***

## 1. Positioning

<br />

LLMs pattern-match on **repetition and consensus**. The company needs one clear, consistent answer to *what it does*, *who it is for*, and *why* — repeated across every surface: the website, PR, partner sites, third-party directories, review sites, social media profiles, and more.

If the website says one thing and another surface says something else, it confuses LLMs — they conclude the company is not credible or "all over the place." So clear positioning comes **before anything else**.

### The rule — LLMs pattern-match on repetition

Define a **tight, stable answer** to one question: *"What does this company do, and for whom?"*

If your homepage, PR coverage, social profiles, and partner sites all describe you differently, **none of it compounds**. To put it bluntly: **this is infrastructure, not messaging.**

That tight answer then needs to be **consistent across**:

* Homepage, About page, FAQs, and product pages

* Meta descriptions and structured data

* Press coverage and partner sites

* Third-party directories (Wikipedia, G2, Crunchbase)

* Social profiles and earned media

**The framework: the Value Proposition Messaging Canvas** (created by Anthony Pierri and Robert Kaminski). It gives a simple mental model for deciding how to describe what the company does. Choose a person (the target customer), then describe:

* What they are trying to do.

* How they do it the current way.

* The problem — a limitation of that current way.

* The **product capability** that addresses the problem.

* The **product feature** — a distinct thing from the capability. (Example given: *"now you can work with teammates in the same file at the same time with real-time collaboration."*)

* The benefits.

**The canonical sentence form.** Each row of the canvas should compress into a single readable sentence; if it doesn't flow, the positioning is broken:

> *"Persona is trying to \[use case], by \[current way], but \[problem], because \[limitation]. Now, you can \[capability], with \[feature], so that \[benefit]."*

Applied to Snov.io, based on what is publicly available on its website (the company may have a different internal stance), three rows illustrate the canvas:

1. **Prospecting** — build a verified-email list from a LinkedIn search.
2. **Deliverability** — send 1,000+ cold emails a week without burning the domain.
3. **Stack consolidation** — run the whole motion from sourcing to closed pipeline at SMB pricing.

Row 3 ("stack consolidation") was called out as **the moat** — the row competitors can't easily copy.

**Knowledge base.** Once positioning is clear, codify everything — the value propositions, all three competitors, and how to handle every objection — into a knowledge base. This applies if AI is being used to create content (highly recommended). The knowledge base gives AI the context it needs so content is grounded in truth, avoiding hallucination and "slop."

***

## 2. Search demand research — reverse-engineering the buyer journey

After positioning, research the search demand. Think of this as **reverse-engineering the buyer journey**: figuring out the keywords and prompts buyers use across the *entire* journey — from the moment they experience the problem and search for how to solve it, all the way to evaluating competitors and solutions.

Every search strategy starts with this list of keywords and prompts you want to show up for.

* With Google, this was a "soft" problem — hard to do well, and most companies don't capture the full potential of keyword research.

* With **prompt research it is even harder**: there is no real data on how many people search a specific prompt. AEO monitoring platforms let you track a set of prompts, but the open question is *how do you know they are the right ones?*

### Best proxies for finding real buyer prompts

* **Conversion data first.** Start with the highest-signal data: product category pages and topics that drive the highest-intent users — the ones that resonate with the highest-spending or highest-converting audience.

* **Top pages → Google Search Console → top queries.** Take your top-traffic / top-converting pages and look at their top queries in GSC. Queries don't translate directly into prompts, but they let you formulate prompts that are close to how people search. (Example: an e-commerce store whose top page and keyword is "white dress pants" can build prompts like *"what are the best white dress pants?"* or *"where can I find..."*.)

* **Use prompts that reflect your top keywords.** Everyone phrases prompts slightly differently — one long-tail prompt may be exactly what just one person says. Use somewhat generic prompts that reflect keywords already working for you, because you have *evidence* people search that way. It does not need to be the exact wording.

* **Sales transcripts and customer support tickets.** These tell you in real time what people are asking, and especially what high-value people are blocked on before they can move forward. These are bottom-of-funnel queries.

* **Paid search.** SEO has no keyword-level conversion data — but paid search does. Connect with the paid search team to see their highest-performing pages and keywords, then translate those into prompts with the tracking tool.

### Validated demand in the wild

Beyond first-party data, mine buyer language from places where buyers already write it:

* **Competitor keyword inventory** (what your competitors rank for and you don't).

* **People Also Ask trees** in Google.

* **AI fan-out queries** across ChatGPT, Perplexity, and Gemini — capture the searches the *models themselves* run to answer prompts in your space (these are real, buyer-vocabulary queries even when they aren't yet trackable as "prompts").

* **Review platforms in buyer language:** G2, Capterra, **Trustpilot**.

### Supplemental discovery (lower signal, higher coverage)

These cover emerging vocabulary your structured data won't catch yet:

* Reddit, Quora.

* **Slack community hot threads** (the right channels for your audience).

* Autocomplete (Google, YouTube, Perplexity).

* **Niche newsletters and podcasts** in the category.

Start with the money and conversion data, then follow from there — it lets you tell leadership you are focused on what actually moves the needle.

**Do you need to optimize for SEO and GEO at the same time?** Not really. The keywords and topics already working for you on SEO will be reflected in your prompts.

***

## 3. Keyword & prompt research framework — prioritization

Extensive research produces thousands and thousands of keyword and prompt variations. The common question: *how do you prioritize, and in what order?* A simplified mental model:

### Step 1 — Start with seed keywords

A set of terms known to be relevant, including:

* Google Search Console terms — the keywords people already use to reach your site, especially those driving conversions or traffic to your most valuable pages (double down on these).

* Keywords competitors rank for.

* Plus several other sources.

### Step 2 — Expand each seed by mining real user searches and questions

Sources include: Google "People Also Ask" and related searches (some — not all — phrased as questions, so they resemble real prompts), Perplexity autocomplete, questions in sales call transcripts, questions in reviews, and customer support tickets. This produces 10,000+ searches. This is typically done **programmatically** — doing it manually is possible but extremely time-consuming.

### Step 3 — Prioritize

Three important sub-steps:

1. **Classify for relevance.** For each search, ask: is this a potential buyer in our buyer journey, actively searching to solve a problem we solve?
2. **Assess other aspects.** Search volume; whether it is *possible* for you to rank (SERP features — e.g., Google reviews consuming the whole answer, whether people will actually click); and the source. Many top-of-funnel searches are disappearing: a "how to do something" query that used to be won by a blog post is now consumed by AI overviews, so it often makes no sense to create that content.
3. **Transform keywords into prompts.** The most complex step — there is "game theory" behind it. Key idea: if two searches (keywords *or* prompts) return very similar results, you can **group them**, because Google and AI models understand they share the same search intent. Example: "top X platform" and "best X platform" share intent — one page can serve both. For prompts, there are many long-tail variations; if the searches the models run to answer them are the same across variations, group them and target only one. A long-tail prompt illustration (a deliberately overcooked example): *"I want to find a way to solve email deliverability issues — I've already tried X, Y, and Z, and I want a tool that helps me not have this issue."* If a cluster of such variations triggers the same underlying searches from the same sources, you only need to target one of them. Always double-check this grouping rather than assuming it.

### Worked example — applying this to Snov.io

* There was **no Google Search Console / first-party data** available for Snov. The example worked only with external data from databases (DataForSEO, Ahrefs, keyword planner, and similar — "only a part of the puzzle").

* Hundreds of real user questions were gathered from review and community platforms — G2, Capterra, Reddit — with many more available (there is a cost, since the data must be enriched).

* There was **no access to sales transcripts**, which would have been hugely valuable here.

* The output: a large list of target keywords with grouped secondary keywords, related FAQs (answerable in an FAQ section), and data on which companies appear in each SERP position (and the equivalent for prompts).

* This can be done programmatically — tech-savvy users (e.g., with Claude Code) can describe the reasoning criteria and attempt it themselves; it is a hard process. A purpose-built platform for it enriches the data so Google and each AI model answer each search result, enabling the analysis described next.

***

## 4. Prompt reverse-engineering framework — how to rank for a prompt

### The misconception about "top patterns" research

Providers publish industry reports (the kind of "top 5 patterns most correlated with being cited by AI" research). The catch: they analyze hundreds of thousands of prompts across different verticals, funnel stages, use cases, and prompt formats. **There is no one-size-fits-all.** Never look for a single checklist that applies across all prompts — based on extensive analysis of the data, it does not work.

The methods, page types, and tactics that rank for a prompt differ **even within prompts of the same taxonomy**. Example: ranking for *"best sales email automation platforms"* can require different tactics than *"best Chrome extensions for finding emails."*

The right approach: analyze the data for **each prompt and keyword individually**. Since that is not feasible for everyone, the recommendation is to **sample** — analyze \~5 prompts of the same type, which raises the likelihood (\~80%) that the pattern holds for the rest.

### The framework

The foundations of SEO are the same, but search engines work differently, so some steps are inherently different.

**Step 1 — Analyze the query fan-outs.** When a user enters a prompt (e.g., *"what are the best sales automation platforms"*), the model itself searches the web to answer it. First, figure out what searches the model is running behind the scenes.

**Step 2 — Analyze the SERP and citation patterns for that prompt.** For each search the model runs, see which companies and page types rank. The model fetches roughly 100 pages, then chooses from that **citation pool** which ones to actually use in the answer. Analyze:

* Out of all citations, which ones are actually chosen.

* Out of all citations, which ones influence *the specific part of the answer* you want to rank for.

**Step 3 — Map each pattern to a recommended action.** Examples:

* If \~70 of 100 pages are directories/reviews, it will be hard to influence that answer with owned content — you would instead need to engage those communities or contact the publishers/third-party sites to get mentioned.

* If competitors or companies similar to yours are ranking/being cited, it is likely you can create the same type of page.

* This also reveals the page **format** — a listicle ("what are the best X"), a category page, a feature page, a case study page — and what those pages have in common.

**Citation pattern → action (quick lookup).** A clean way to keep this on a sticky note:

| Dominant citation type                | Action                                               |
| ------------------------------------- | ---------------------------------------------------- |
| Listicles                             | Earn mentions in them (outreach, Reddit, G2 reviews) |
| Vendor pages — and you don't have one | Build the page                                       |
| Reddit threads                        | Engage in the relevant communities                   |
| Third-party reviews / directories     | Programmatic G2/Capterra/Trustpilot push             |

Wrong action = wasted effort.

### Match the content format to the prompt cohort

Same broad topic, different cohort, different page format. A starter mapping (always validate, but this is the default to bet on):

| Prompt cohort                         | Format that tends to win   |
| ------------------------------------- | -------------------------- |
| *"Best X"*                            | Listicle                   |
| *"X vs Y"*                            | Comparison page            |
| *"X alternatives"*                    | G2-style alternatives page |
| *"How does X work"* / *"How to do X"* | Deep guide                 |

The blunt rule: **wrong format = no rank, no citation, regardless of how good the writing is.**

### Worked example — "best email finder Chrome extension for sales reps"

* Across models (Google AI Mode, Google AI Overview, ChatGPT, Perplexity), Snov is mentioned/cited (shown in green) in some responses, not in others.

* **Models are probabilistic** — you do not always get the same answer. But you can do **statistical sampling**: run the same prompt 100 times and consistent answers emerge as probabilities. In the example, out of 56 measured responses, one search was performed 14 times — likely to recur — while others appeared only once. The rule of thumb: **stable = real pattern. Single appearance = noise.** The consistent ones are what matter. (A practical minimum for working analysis is running each prompt **3–5×** across ChatGPT, Perplexity, Gemini, and AI Overviews.)

* Do the same analysis for sources: some are consistently mentioned or cited. Those are the entities and citations associated with that prompt.

* Also analyze **sentiment and positioning**: when you are mentioned, is it positive? Is it aligned with your brand positioning? You want AI to act as your sales rep — even your best account executive fails if they don't say the right unique selling propositions. The same is true of AI, which is why positioning and the positioning frameworks matter so much.

* Look at an actual answer (e.g., how Perplexity answered the prompt on a given day): how it structures the response, what categories it uses, and which sources it uses for which parts. In the example, a specific page influenced the "best budget all-in-one alternative" portion. You want to show up in a **specific contextual placement**, not the whole answer — e.g., Snov wants to appear under "best classic," not "best all-in-one," and in this case it was already in the right place.

### Listicles are not dead

You can never show up in too many listicles. People trust LLMs precisely because a brand is pulled from *multiple* sources, not just its own website claim — others have validated it. You cannot just say it about yourself; those days of SEO are over — you need PR backing.

Contrary to the popular "listicles are dead / Google penalizes listicles" claim, **67% of the pages influencing these prompts are listicles**. Take what you read with a grain of salt — it is often not backed by data.

***

## 5. The AI search roadmap — 5 steps, 3 buckets

The roadmap can be framed as five steps grouped into three buckets.

### Bucket 1 — Foundational

You need a solid foundation before building anything else. The key foundational task: **fix indexability and crawlability** so AI search bots can find you. Many sites previously *required* blocking these bots — check your robots.txt and make sure you are not blocking the very LLMs you want to feature you. (Specifics are covered in Section 6.)

### Bucket 2 — Content / on-page (what you say about yourself)

Two pillars:

* **Net new content.** Define a content roadmap targeting the keywords identified (the prioritized keyword/prompt spreadsheet from Section 3). At Upwork this took several forms: net new blog posts; adding FAQs to top brand pages to answer brand queries; and answering **non-brand queries on product and category pages** — one of the biggest winners — so that content can be shown and referenced in AI search (driving growth in AI overviews and clicks from them).

* **Content updates.** Products are not evergreen. Things evolve constantly (example: a developer page at Upwork, since the world of development changes overnight). Keep updating content so LLMs, Google, and users see you as an expert — this builds both user and bot trust.

### Bucket 3 — Off-page (what other people say about you)

Analogy: if you want people to think your house is the best in the neighborhood, you don't go telling neighbors yourself — you rely on *other* neighbors to recommend it. Same with a product: others must validate it, or it is just vaporware that won't get picked up. Two pillars:

* **Third-party mentions.** Get your brand into third-party listicles (do outreach), and onto review sites like G2 and Capterra. You need a **G2 program**. At Upwork they simply reached out to customers asking for a review — good or bad — saying they valued the feedback; people had a lot of good things to say, and Upwork became the **#1 ranked** on G2 for its target market/query.

* **Community.** Reddit and Quora. A dedicated **Reddit team** is increasingly important — whether scrappy/DIY or a real team owning your community and responding in real time. Be authentic on Reddit; it is heavily populated when people search for "best product," so you need to show up there and address feedback to build trust.

**Cautionary note on reviews:** A LinkedIn post (truth unconfirmed) included screenshots showing Profound approaching its customers, offering **\$250** for a positive review with the placement they wanted on G2. Only companies with "rivers of money" can do that. Reviews matter enormously — and because search is a zero-sum game, competitors doing this make your job 100x harder.

***

## 6. Technical SEO — the 5% that drives 95% of the impact

**Misconception:** that technical SEO is what helps you "win" at search. In reality, technical SEO only ensures the content you produce is **discoverable, indexable, and crawlable** — i.e., that search engines (including AI/generative search) can read it. It only matters if you already have the right content for the searches you are targeting. It is usually *not* the highest-impact area to focus on unless you already have the content — but you still need the right foundations.

A list of the "5% of technical SEO that has 95% of the impact" (based on published research and original analysis across tens of customers — not one-size-fits-all, but a good sample):

1. **Crawlers can find and read your content.** Make sure search-engine crawlers and AI crawlers can reach you — have a sitemap, and don't block them in robots.txt. **Specifically, check your robots.txt does not block:** `GPTBot`, `ClaudeBot`, `PerplexityBot`, `Google-Extended`, and `OAI-SearchBot`. Plenty of sites that historically blocked scrapers are still blocking the very bots they now want to be featured by.

2. **Pages render well.** Crawlers often struggle to read content behind JavaScript rendering, so use **server-side rendering**. Google has spent many years optimizing its crawlers, so this is usually (not always) fine for Google. AI crawlers are newer and have not perfected it. If content is behind JavaScript, there is a high likelihood the crawler cannot read it — and if it cannot read it, it cannot influence the answer.

3. **Page speed.** Not very important unless it is very bad. Content must load before the crawler/bot. The key metric is **Largest Contentful Paint** (how long the most complex component takes to load) — it should be below \~2.5 seconds. (Some things change for mobile; not covered in detail.)

4. **Internal links.** Unlike most technical SEO, this can actively *increase* results. Research from **Graphite** (credited as original research) found that a page with **more than 8 contextual internal links** pulls **300% more traffic** than one without. The links must be relevant within the same context — e.g., an email-finder tool page linking to a blog post about how to find emails.

5. **Schema markup.** Ahrefs released research saying schema markup does not impact citations. That is not entirely true — for many pages you need structured content so search engines understand your brand, especially in terms of **entities**. Several types of schema markup do have an impact; you need the right schema for each page type. **The two consistently most important:** **`FAQPage`** **and** **`HowTo`** on the highest-intent pages.

   **Schema markup cheat sheet — the right schemas per page type:**

   | Page type                      | Example URL                              | Recommended schema                                                                             |
   | ------------------------------ | ---------------------------------------- | ---------------------------------------------------------------------------------------------- |
   | Homepage                       | `/`                                      | `Organization` + `WebSite` + `SearchAction`                                                    |
   | Product feature                | `/email-finder`, `/email-verifier`       | `SoftwareApplication` + `Product` + `AggregateRating` (G2 rating) + `Offer` + `BreadcrumbList` |
   | Solutions / use-case           | `/solutions/lead-generation`             | `Service` + `FAQPage` + `BreadcrumbList`                                                       |
   | Pricing                        | `/pricing`                               | `Product` + `Offer` × N tiers + `PriceSpecification` + `FAQPage`                               |
   | Integration                    | `/integrations`, `/integrations/hubspot` | `SoftwareApplication` + `BreadcrumbList`                                                       |
   | Comparison ("X vs Y")          | `/snov-vs-apollo`                        | `Article` + `ItemList` + `BreadcrumbList`                                                      |
   | Alternative ("X alternatives") | `/apollo-alternatives`                   | `Article` + `ItemList` + `BreadcrumbList`                                                      |
   | Listicle ("best X")            | `/best-cold-email-tools`                 | `ItemList` + `Article` + `BreadcrumbList`                                                      |
   | Review ("X review")            | `/snov-review` (or 3rd party)            | `Review` + `Rating` + `Article`                                                                |
   | How-to / guide                 | `/how-to-find-emails`                    | `HowTo` + `Article` + `Person` (author) + `BreadcrumbList`                                     |
   | Blog post                      | `/blog/cold-email-deliverability`        | `Article` or `BlogPosting` + `Person` + `BreadcrumbList`                                       |
   | Case study                     | `/customers/{logo}`                      | `Article` + `Review` + `Organization` (customer)                                               |
   | Help / docs                    | `/help/setup-spf`                        | `TechArticle` or `HowTo` + `BreadcrumbList`                                                    |

6. **URL hygiene.** Adjacent to schema and crawlability: **hreflang done right** (for international), **no dates in URLs**, **no query-string sprawl**. These don't show up as headline metrics but they suppress citation eligibility when they go wrong.

**TL;DR — test it yourself.** Google's GEO guidelines state you don't need markdown or llms.txt on your site. But one technical team tested switching on markdown via Cloudflare and saw a near-immediate visibility gain. Google chooses its words carefully — *do you need it? maybe not; is it helpful? test it.* Many of these items overlap with regular SEO, but allowing search/AI crawlers and testing markdown matter more for GEO than for traditional SEO. SEOs should stay skeptical of Google's guidelines and others' claims, and trust their own firsthand data.

**Why the incentives are misaligned.** Google and the AI labs do not have an incentive to tell you about exploitable tactics. If everyone knew you could create a listicle ("what are the best X") to influence an LLM, people would stop trusting LLMs — so the platforms will never admit it works. Keep this in mind when reading their guidance.

### Live example — Snov.io product page

* Snov's email-finder extension product page looks good and is interactive. The quick test: right-click → **Inspect** → Chrome DevTools → settings → scroll to bottom → **disable JavaScript** → reload the page. This shows (likely, though not guaranteed) what the crawler sees.

* For Snov, most of the page could not be rendered with JavaScript off — the hero section showed nothing, and the FAQs could not be opened. If the page was trying to rank for a keyword, it no longer does.

* This is where schema helps: with FAQ schema and the FAQ content in place, the FAQs are still accessible even when behind JavaScript.

* Many Snov pages also lack the right schema. A sample of 50 of Snov's 1,000+ pages was tested — many had all five aspects done well, many did not — so there is plenty of room for improvement. Prioritize by highest impact.

* Useful tools: **Screaming Frog**, the **Detailed SEO** extension, and the **Ahrefs** extension. Custom tooling can be built to do this analysis at scale.

***

## 7. Content roadmap — five principles for prioritizing what to create

**Misconception:** that "85% of AI sources come from third-party websites, not yours," implying you must have third-party content to win. **Not true.** Most companies can become the **#1 source for all the prompts they target** using first-party content. If a space is super competitive and competitors also do SEO/AEO well (a zero-sum game), consensus becomes a tiebreaker — more important for some prompts than others. But you do need to create your own content.

### The five principles

1. **Start where you already have authority.** Google has admitted its domain authority/reputation algorithm is **topical** — the domain rating you see in Ahrefs/Semrush is not applied uniformly across all pages or topics. Forbes writing about a software category where it lacks topical authority will not rank just because Forbes' overall authority is high. The same applies to you: if you are known for email finding / email contacts and suddenly try to rank for "AI sales development representative" topics where you have no topical authority, it will be very hard. **Defend the cluster you lead before you attack a new one.** Start where you have already published thought leadership and your ideal pages are ranking; build authority over time in topics where you don't have it. **Compounding traffic from an established topic beats greenfield bets that take 6 months to rank.**

2. **Lead with commercial intent.** Because revenue is typically wanted within ~90 days, start with topics where you have already built authority *and* that have commercial intent — **bottom-of-funnel searches** where the searcher is almost guaranteed to be an ideal customer. **BOFU clusters convert \~10× faster than TOFU.** Skip *"what is X"* until you've covered *"best X"* and *"X vs Y."* **Visibility without intent is vanity.**

3. **Match content type to prompt type.** Different prompts demand structurally different content; the wrong format does not rank no matter how good the writing is. *"Best X"* typically wins with listicles. *"X vs Y"* wins with comparison pages. *"X alternatives"* wins with G2-style alternatives pages. *"How does X work"* / *"How to do X"* wins with deep guides. Always run the prompt reverse-engineering framework (Section 4) to confirm the dominant format before committing — **wrong format = no rank, no citation, regardless of how good the page is.**

4. **Cover the citation gap, not the volume gap.** Build where competitors are cited and you're missing, **not** where search volume looks biggest. A **200-volume prompt you can win is worth more than a 20K-volume prompt where the citations are locked.** A search with only 50 searches/month can be extremely valuable if those 50 people are almost guaranteed to buy — for customers with seven-figure-plus annual contract values, converting just 2 of those 50 can generate over \$1M in revenue. There are also zero-search-volume keyword strategies; just because Ahrefs or Semrush reports "no volume" does not mean a keyword won't drive significant traffic.

5. **Balance the funnel and content-type mix.** A common misconception is wanting to publish a huge amount of one content type (almost programmatic SEO). Publishing only one type is not balanced and can negatively influence how search engines perceive the brand. Publishing only listicles, for instance, won't build enough topical authority and risks being penalized as spam. **Don't ship 20 listicles in a row.** Audiences (and prompt cohorts) need **proof** (case studies) + **how-to** (guides) + **original research** (data) alongside the commercial pages. The mix earns trust *and* feeds different prompt cohorts — balance thought leadership, top-of-funnel research, case studies, product pages, listicles, and competitor reviews.

### Format × funnel priority matrix

Section 4 gives the *rule* (which format wins a given prompt cohort). This matrix is the *prioritization view*: for each format, which funnel stage is the high-ROI bet, which is a useful secondary play, and which to skip entirely. **HIGH ★** = primary bet, **MID** = useful with the right framing, **SKIP** = wasted effort.

The funnel stages: **BOFU** (vendor + comparison + alternatives — buyers evaluating), **MOFU** (how-to + recommendation — buyers solving), **TOFU** (awareness + research — buyers learning).

| Format                         | BOFU (vendor / compare / alt)                                                                | MOFU (how-to / recommend)                                                                                         | TOFU (awareness / research)                                                                    |
| ------------------------------ | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Listicle** *("best X")*      | **HIGH ★** — Best-\[cat] cohort. Owned listicle naming yourself + \~5 competitors.           | **MID** — Recommendation. *"Best practices for cold email sequences"* recommends Snov in flow.                    | **SKIP** — Listicle wasted at TOFU.                                                            |
| **Comparison** *("X vs Y")*    | **HIGH ★** — Vendor comparison. Highest-ROI page Snov can ship. One per top competitor.      | **SKIP** — Comparison content is wasted on MOFU prompts.                                                          | **SKIP** — Comparison wasted at TOFU.                                                          |
| **Alternatives** *("X alt.")*  | **HIGH ★** — *"Snov alternatives"* + *"Apollo alternatives."* Defends + attacks.             | **SKIP** — Too early for vendor switching.                                                                        | **SKIP** — Alternatives wasted at TOFU.                                                        |
| **How-to** *("How to do Y")*   | **MID** — Implementation. *"Set up Snov for cold outbound in 30 min."* Conversion magnet.    | **HIGH ★** — How-to cohort. Snov's strongest MOFU bet. 20+ how-tos: deliverability, list-building, automation.    | **MID** — Research. *"What is sales engagement?"* definition pillar. Wins the category prompt. |
| **Research** *("X benchmark")* | **HIGH ★** — Authority signal. *"State of cold outbound 2026."* Drives mentions + citations. | **HIGH ★** — Authority. *"Cold email benchmarks by industry"* — first-party data.                                 | **HIGH ★** — Category authority. Wins *"what is X"* definition prompts.                        |
| **Case study**                 | **HIGH ★** — Validation. 3 stories: founder-led / agency / SMB SDR persona. Required.        | **MID** — Recommendation via *process* stories (not outcome stories). *"How \[X] built their cold-email engine."* | **SKIP** — Case studies don't convert at TOFU.                                                 |

**Reading the matrix.** Two patterns jump out:

* **Vendor-evaluation formats (listicles, comparisons, alternatives) collapse to BOFU.** Outside BOFU they are mostly SKIPs. If you have limited capacity, every comparison and alternatives page should be a BOFU bet against a specific competitor.

* **Research / benchmarks are HIGH across all three stages.** Original first-party data is the only format that earns citations across the entire funnel. If you can run one benchmark per year, it pays back at every stage. Case studies are nearly the opposite — high BOFU value, mid MOFU value as *process* stories, no TOFU value.

**Bonus levers (off-matrix).** Free tools and community plays (e.g., podcasts) sit outside the format×funnel grid but earn citations and brand recall, especially when paired with the BOFU pages they support.

### Owned content on product & category pages

Owned content — especially on product and category pages, which are harder to get ranked and added to off-platform third-party listicles — has been a game changer at Upwork. AI overviews for their top categories subfolder increased by **200% in the past year** simply by adding this content.

Think of it as a **"keyword universe."** Take your top category topics and cover: the "what is" defining the topic; comparisons of different elements of the topic; "best X" / best-version variations; and all the elements that feed into it (for Upwork, that's skills). Then explain how your brand helps with each. Adding unique content to these pages gets that content pulled and cited directly into AI overviews and LLMs, with a link back to your page. Use People Also Ask, sales/support calls, and top-converting keywords — and make sure those are present on your top pages. This is scrappy and relatively easy to do.

### Supporting examples

* **Webflow.** Webflow added an FAQ section to its product pages based on what customers asked most often on sales calls — they digested all the sales call transcripts, ranked how often each question came up, and used that as a proxy for which FAQs to answer. This increased signups through AI search by a large multiple — **\~8x** has been cited as an explicitly arbitrary, illustrative figure, not a confirmed number. Webflow reportedly drives roughly 10–12% of signups from AI search (exact figure not confirmed).

* **Zapier** has been cited as driving **30% of new signups from AI search**.

* **"How did you hear about us" survey.** Add this survey to your site and make sure LLMs (ChatGPT, AI Mode, AI Overviews) are included as options — a strong way to show your team and leadership that people are finding you this way. (More on this under Measurement.)

### Content formats per prompt type

A *sample* of formats that tend to perform well — always validate, it won't work every time. Doing this analysis at all puts you \~80% better off than doing nothing; targeted analysis with the prompt reverse-engineering framework does much better.

**Listicles** (e.g., "best sales automation platforms"). Listicles usually perform best for this prompt type. You cannot publish only listicles, and many brands don't want to (it can damage the brand). Three things to do:

* **Create a "roundups" folder.** These pages don't show in the blog but are still indexed — so they don't disrupt the experience of normal site visitors. They get few clicks themselves but influence AI recommendations.

* **Reframe as a buying guide.** Instead of "best sales automation platforms" with yourself ranked #1, write a *"guide to choosing the best sales automation platform."* You can honestly describe what each platform is best at and thereby **control the narrative** — e.g., positioning competitors as best for a segment you don't target. Don't do this blindly or in a ridiculous way, or it can be treated as spam.

* **Add real value.** For listicles, use AI to compile competitors' reviews, screenshot them, and include them — you can choose the worst ones. (Example: for a company paying for positive reviews, you could surface the *real*, unpaid negative reviews. That is genuinely useful for a buyer evaluating a tool, since it shows what competitors try to hide.)

**Bottom-of-funnel patterns (high commercial intent).** Patterns to consider for high-intent content:

* **Competitor vs. competitor** — e.g., "Apollo vs. Snov." You control the narrative and capture the searcher. This can be done about competitors too — Snov competitor Salesforge gets the highest citations via pages like "snuff.io review" and "snuff vs. Apollo," essentially arguing they are better. It works like paid ads (when someone searches "Apollo.io," a competitor shows up). Examples: Cognism appearing first for "Apollo.io alternatives"; another brand controlling the "vs. hunter.io" narrative.

* **Category short lists / listicles.**

* **Alternatives** — "alternatives to \[competitor]" / "\[competitor] alternatives."

* **Competitor pricing** — shadier territory; it must be genuinely helpful. Don't do what Salesforge does (blatant selling). Instead, look at what reviews say about pricing, reference real customer reviews, gather relevant information, and give an honest opinion rather than only putting the competitor down. (A strong example: pages framed as *"my honest review after using this tool for three years"* — biased and featuring a competitor, but the honest-review format gives them 10x credibility.)

* **Use case per persona** — e.g., how to find email contacts for small SMBs.

* **"How to do something in a competitor"** — including how to cancel a competitor.

* **Competitor reviews.**

* **Competitor pricing** pages.

### Snov.io content roadmap example

The roadmap for Snov had a **balanced mix**: alternatives pages, use-case pages, satellite blogs, glossary, and more. For each item, SERP results were analyzed using platform data and prioritized by a **relevance score** tied to the searches each piece of content should capture. Also identified: **edit opportunities** — chances to improve existing content so it ranks better for specific keywords/prompts. An accurate relevance score would need Google Search Console / Google Analytics data, which was not available for Snov. The roadmap mixed competitor pricing, competitor reviews, use cases (e.g., reverse email lookup), and more — starting with items that are easier to influence, have the highest buyer-journey impact, and that Snov did not already have.

***

## 8. Earning mentions / off-page

This is the off-page bucket — earning mentions in the sources AI already cites, so that good things are said about you by others (not just by yourself).

### The surprise finding: niche-tool blogs out-cite traditional publishers

For most teams the intuition is "we need TechCrunch / HubSpot / Sales Hacker." The Snov.io analysis showed the opposite. The **top non-owned citation sources** for Snov.io's prompt set were **prospeo.io, lagrowthmachine.com, salesforge.ai, and saleshandy.com** — competitor-adjacent niche tool blogs — *not* the large publishers. Build the outreach list accordingly: the people who can move citations for you are usually the small specialist sites in your category, not the big-name press.

### Listicle placements

Get featured in "best of" category roundups. Two places to focus:

* **Research and pitch editors.** Find the best listicles in your top ~5 keyword types (top product, top category, and general descriptions of your product). If you are not already mentioned, pitch the editor — offer a **"mention swap"** or explain why the article would be better with you included. This tends to have a low response rate.

* **Use more active forums like Reddit.** You can connect directly with moderators, who tend to be more responsive. Reddit is where a lot of "best of" content is pulled from. For the Snov example: searching "best email finder" in Google, the first two sources in the AI Overview were Reddit threads. Reddit functions as a **listicle in real time** — people upvote — arguably the most trustworthy listicle, since it is community-sourced by people with no ulterior motive. Don't spam: have a founder or company employee post openly ("I'm from \[company], these other products are great at X, here's what we're specifically good at, happy to chat"); or, if your product is already recommended, upvote it, add context where something is no longer accurate, and address comments in Reddit listicles.

* **G2** — covered earlier (you need a G2 review program).

### YouTube

YouTube is technically an owned platform but functions off-site, and it has been one of the **biggest winners for Upwork**. Focus specifically on **brand mentions / brand queries** — there are hidden clicks and conversions in brand queries. Process: use Ahrefs or Semrush, enter your brand name, see the top questions and People Also Ask, take the top 5–10, and check how you rank. Often you rank well but the keywords aren't present, the content is outdated, or other content types (like YouTube) are ranking instead. Upwork found others (sometimes competitors, sometimes inaccurate info) ranking for *Upwork's* brand queries with YouTube videos, so they decided to own them. Within five days, the \~3 videos tested were all ranking in the top AI Overview results and in various SERP features in under a week — because they are the experts on their own topic — and bumped competitors out.

### PR and thought leadership

This is often hard to get prioritized internally — it cannot easily be done or automated by AI, and it can be expensive. How to frame it: AI search is *built on* these mentions; if you don't invest now you get left behind, it is difficult to claw back, and you need first-mover advantage. A practical pitch: ask to run \~5 PR articles to prove the value — see if you get citations, get featured in listicles, and get bumped up in AI search for your queries — then use that proof to win budget for more PR and thought leadership.

**Why this compounds.** Because search is zero-sum, doing something hard for competitors to replicate — like producing high-quality YouTube videos — gives a huge advantage. In the data, **YouTube and Reddit are #1 and #2 in citations**, and both are hard to replicate.

**PR misconception.** Some well-known SEO thought leaders claim you just need lots of PR with consensus and consistent placement. That is only half true. PR works best when it is optimized to rank in the places that have the highest impact on your sources, and optimized for the **contextual placement** of the keyword/prompt you want to rank for. It is hard with journalists — you don't control what they write — but optimize for the highest-impact prompts where you can. (Example: a TechCrunch piece optimized for the right contextual placement is likely to show up.)

***

## 9. Community & mention outreach process

After choosing the prompts to rank for, the outreach process:

* For each target prompt, use a tool to find the pages with the **highest number of citations** for that prompt, then get in contact with those pages/companies.

* Custom tooling is often needed because no existing tool executes this end-to-end. It works like a **Clay table**: filter which companies to contact and with which message, then export the messaging to the right people. Find the authors and the marketing teams at each company, use personalized templates (enriched with additional data) — essentially an "outreach intelligence" layer. The output can be imported into outreach platforms (e.g., Snov, Instantly, Apollo) to send specific templates.

* **Template example — mention-for-mention:** *"Hey, I noticed you're ranking here; we're ranking in this prompt that also matters for you — do you want to mention us and we'll mention you?"* This typically works.

* The same approach applies to **community**: find the threads with the highest impact (mostly Reddit and Quora, sometimes Facebook groups and others).

This is done in a **targeted, data-driven way** because the volume of pages is large.

***

## 10. Measurement

People forget about measurement far too often, getting caught up in execution. But proving the value and efficacy of the work is what earns more budget, more visibility within the company (or with clients), and ideally a promotion.

**The reframe to lead with: AI is a mention engine, not a referral engine.** Stop trying to make AI look like a referrer in your analytics — it isn't built that way. Measure *being recommended*, not *being clicked through from*.

Metrics to track:

* **AI share of voice.** Not "we show up in 120 prompts" — that has no context. Instead: *of our top queries (identified from conversions and customer questions), we rank for X% versus competitors.* This tells you whether you need to increase share of voice and gives a benchmark to work against.

* **Citation share by source type.** Break citations down by vendor, third-party, and community sources — this shows which pillar to invest in next.

* **Brand search volume.** Track in Google Trends or Ahrefs. You want a rising line as people encounter your brand more in AI search, leading them to visit your home page and search for you directly by name.

* **Branded / direct ("SEO brand") traffic.** LLMs don't refer directly very well — AI search is more of a zero-click, visibility platform. So track people coming to your home page by typing your brand name, or going direct to your domain. At Upwork, as organic traffic went down (due to all the changes), **direct and branded traffic went up**. Tell that side of the story and set that expectation. These are often higher-value clicks anyway — primed, warmer leads.

* **"How did you hear about us" survey.** Add it to your site and include LLMs as options. A couple of years ago, before Upwork added LLMs as options, the #1 write-in under "other" was ChatGPT / LLMs / Perplexity. Include those options and start tracking.

**Stop chasing:**

* **Raw AI referral traffic.** It will always look low — don't make it your North Star, or leadership won't be impressed.

* **Absolute citation counts.** Track *share*, not raw counts.

* **Position-only metrics.** Useful mainly as a defensive story ("organic traffic is down, but our position is stable or increasing"). You can rank #1 in Google and still not be recommended.

* **Single-prompt wins.** One prompt is noise. Optimize for *cluster* patterns across prompt cohorts.

Aim for **recognition over rankings**.

***

## 11. A/B testing & conversion rate optimization

One of the highest-impact differentiators: run **A/B or A/B/C tests** — try \~3 different approaches and see which performs best.

Because the data is not connected directly to Google Search Console / Google Analytics, for each page track: clicks and impressions from Google Search, your own AI search data, Google Analytics, and conversion data. With one approach used on 10 pages, a second on another 10, and a third on a further 10, you can see which works best — then **retroactively update the 20 underperforming pages** with the winning approach.

**The 14-day loop.** Run this on roughly a two-week cadence per round:

1. **Hypothesize.** Pick one variable to test (page format, intro structure, FAQ placement, CTA, schema).
2. **Ship variants.** Three approaches across 30 pages (10 per variant).
3. **Measure cohort-level citation lift** — not single-page wins. Look at the citation share + conversion data for each cohort.
4. **Double down on the winner.** Retroactively rebuild the losing 20 pages with the winning approach, then start the next round.

**Conversion rate optimization.** From a customer example (Cold IQ), things that tend to work:

* A **fixed call-to-action** on the site, especially on blog pages.

* **Content upgrades** — reports, free tools, lead magnets, or other CTAs relevant to the content/topic. Example: on a page about running LinkedIn outreach, include an email-copy optimizer tool or an intent-signals tool — optimized to gather the email and move the visitor to the next piece of content. These can also be reports or higher-intent content like a case study.

A/B test until you are getting not just traffic and visibility but **conversion data**.

***

## 12. Frequently asked questions

**Do you use prompt-generating tools after researching keywords?** Yes and no. A **Query Fusion model** can be used — a set of formulas to transform keywords into prompts, based on the patterns found in how prompts have query fan-out similarity and how people formulate prompts. This only works if you then do **prompt de-duping**: after generating many variations, see which ones produce the same type of answers, so you can expand wide and then narrow back down to the prompts that matter most. Above all, always try to find **real user questions** — from competitive reviews, sales calls, Reddit, communities, and your own Google Search Console — that is the highest-reliability data available.

**How do you scale AEO in a B2B SaaS company?** For sites as large as Upwork, **programmatic is essential**. The right approach is **human-in-the-loop AI content** — AI content should *not* be used for thought leadership or whole educational articles, but it is very useful for **category and product pages**, which are the best place to scale. Method: use an AI tool (e.g., Claude or another writer), upload your brand voice, positioning, and everything you would give a human writer; then specify the FAQs to write for each page, the subheadings, and the page titles. Upwork uses this in-house to produce FAQ content at scale — thousands of pages — with a **human editor reviewing**, starting from the top-converting pages. Another example: Cold IQ built a programmatic "best AI sales tools" directory — for each page they gather alternatives, pricing, and FAQs (reviews would also be relevant). The result: when someone searches "\[tool] review," they rank — and anyone searching for a go-to-market tool is likely a high-intent customer.

**Is it good practice to manage a website without a CMS — directly with Claude Code, connected to Google Search Console, Google Analytics, and Ahrefs?** "Vibe-coding" your own website is risky: a CMS hides many abstractions and best practices you would otherwise have to handle yourself, and without it you are far more likely to break something every time you make a change — you can't control what the LLM does, even with a checklist of best practices. With a CMS, you build a collection/template once, the best practices are correctly formatted, and there is far less room for error — you mostly just fill in specific fields (meta title, meta description, schemas). The recommendation: use the CMS; it makes life 10x easier. The counterpoint: you gain speed and ease with a non-CMS solution, but you lose the SEO benefit of an out-of-the-box solution. Look at solutions that combine speed with SEO — Lovable recently responded to SEO concerns about lacking SEO best practices and readable content. If speed, ease, and cost are the main concerns, look at headless options that include out-of-the-box SEO benefits rather than doing everything from scratch.

**How do you write great, relevant titles/topics for blog posts, and research what competitors rank for, for inspiration?** For an existing page being updated, look at **Google Search Console first** — in one case, traffic to a pricing page increased by 48% simply by adding keywords it was already ranking for (but not well) that people used but weren't on the site. Then look at competitors — Fiverr's page and a few other competitors, plus Googling the keyword. You can take all that research, put it into an AI tool like Claude, and have it suggest titles (e.g., no more than 60 characters, using all the research) to choose from. In short: look at your own data first if you have it, then competitors and outside keyword research.

**Closing note on Cold IQ.** Cold IQ is now one of the most-cited sources — Reddit is #1 in raw citations, but in *influence over recommendations*, Cold IQ ranks above everything else, competing with and beating much larger, longer-established companies (including a competitor at \~$40M ARR), as a roughly $7M company. This was happening even during a website migration. The takeaway: programmatic SEO with high-quality, valuable content does not get penalized — if done right (and with competition monitored), it works.

***

## Further resources

* The **Value Proposition Messaging Canvas** (Anthony Pierri and Robert Kaminski) — referenced in Section 1.

* A **Looker Studio Google + AI search visibility dashboard** is a useful tracking artifact — it drew \~3.5K–4K comments on LinkedIn when introduced, a sign of how in demand it is.

* A full **slide pack**, the **Value Proposition Messaging Canvas** slides, and the **keyword research** + **content roadmap** spreadsheets pair well with this playbook as working templates.

