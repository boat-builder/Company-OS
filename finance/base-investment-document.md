> [!WARNING]
> **SYNC CHECK REQUIRED**: This markdown is the source of truth. When updating this document, verify that any corresponding data in `funding-page/index.html` does not diverge. The HTML is the investor-facing deck and contains a curated subset of this information — ensure consistency where overlap exists.

# Investment Base Document — Agent Berlin

> This is the single source of truth for all fundraising materials. Use this document to feed pitch decks, one-pagers, executive summaries, and data rooms.

---
## 1. Company Overview

- **Company Name:** Agent Berlin (Berlin)
- **Legal Entity:** Agentic World, LLC
- **Entity Type:** Limited Liability Company (LLC)
- **Incorporation State:** Delaware
- **Registered Address:** 1111B S Governors Ave, Ste 29991, Dover, DE 19904
- **Sole Member:** Sherin Chacko Thomas
- **Founded:** May 16, 2025
- **Headquarters:** Dover, DE (registered address)
- **Website:** agentberlin.ai
- **One-Liner:** Berlin is programmable infrastructure for inbound growth — a unified data, workflow, and intelligence layer that lets teams build, run, and scale any SEO operation without engineering overhead.
- **Mission Statement:** To make world-class inbound growth infrastructure accessible to every team — replacing fragmented, manual SEO toolchains with a unified, programmable platform that turns strategy into autonomous execution.
- **Current Phase:** Platform launched late February 2026 (<3 weeks ago). Pre-commercial, in Founding Partner Program with 5 active design partners validating product-market fit before scaling GTM.
- **Key Contact(s):** Sherin Chacko Thomas — +91 890 474 5603

### Product Evolution (May 2025 – Present)

Berlin's current positioning is the result of focused product discovery over ~10 months, each phase informed by direct user feedback:

1. **Conversational SEO data layer (mid-2025):** Built a chat interface for marketers to query and explore their SEO data in natural language. Validated that teams desperately needed unified data access — but learned that *talking to data* wasn't enough. Users wanted the platform to *do the work*, not just answer questions.

2. **Automated SEO assistant for founders (late 2025):** Evolved into an end-to-end automated SEO assistant targeting startup founders. Validated the automation thesis — but learned that founders rarely treat SEO as a primary priority; they either outsource it to an agency or hire a dedicated marketer. This insight clarified that the real buyers are the agencies and marketers who actually own SEO day-to-day, directly shaping the repositioning that followed.

3. **Programmable agentic workflow infrastructure (early 2026 – current):** Repositioned as programmable infrastructure — a unified data, workflow, and intelligence layer where teams build and run their own agentic workflows without engineering overhead. This is where product-market fit signals are strongest, with agencies and enterprise marketing teams engaging as Founding Partners.

---

## 2. The Problem

- **What problem are you solving?**
  SEO teams — especially at agencies and in-house marketing departments — are drowning in manual, fragmented workflows. They cobble together 5–10 different tools (Ahrefs, SEMrush, GSC, GA4, spreadsheets, crawlers) with no unified data layer, no automation capability without developers, and no way to address the emergence of AI search (GEO/AEO). Reporting doesn't scale. Strategy is manual and per-client. And the shift to AI-powered search (ChatGPT, Perplexity, Google AI Overviews) is creating a visibility crisis that existing tools don't address at all.
- The ones who are advanced and trying to automate workflows still use complicated tools like n8n or make which requires technical skills to automate. Even with those, they either have to use MCPs for all the third party services or setup the direct interaction with APIs. While setting APIs with authentication is technically very heavy, handling data with a lot of MCPs is not at all great as it increases the hallucination of models and they end up making a lot of silly mistakes. And because of these, people who do try automation would eventually fall back to their traiditional way of doing things or some automation + a lot of manual work to hand hold these automations together.
- SEO/AEO is evolving at a very high speed and they are faced with new things to do or new reports to make or new things to monitor very frequently which increases the workflow and they endup ignoring these new things or do a bad job and handling it. 

- **Who experiences this problem?**
  - **Primary:** SEO agencies (1–50+ clients) trying to scale delivery without proportional headcount growth
  - **Secondary:** In-house marketing/SEO teams at Series B–C SaaS companies and mid-market businesses struggling to justify SEO budget, attribute SEO to pipeline, and operate without dev support
  - **Emerging:** E-commerce/marketplace SEO teams managing thousands of pages, growth engineers replacing brittle custom scripts

- **How are they currently dealing with it?**
  - Paying $500–$2,000+/month for multiple disconnected point tools (Ahrefs, SEMrush, Screaming Frog, etc.)
  - Manual spreadsheet work to stitch data together across tools
  - Building fragile internal automations (n8n, custom scripts, direct APIs like DataForSEO) that can't be shared with non-technical team members
  - Hiring more people to handle growing workload (expensive, slow)
  - Ignoring AI search entirely or winging it with clients
  - Using something like Claude Code with MCPs and either are ignorant about the hallucination problem or not automating it effectively.

- **How painful is it? (quantify if possible)**
  - Agencies report 15–20 hours per week per client on manual SEO research and strategy
  - Agencies are turning away work or sacrificing quality due to capacity constraints
  - Client churn risk is high when agencies can't articulate an AI search story
  - In-house teams can't prove SEO→pipeline attribution, putting their budget at risk internally
  - Automation failures with hallucinations gone unnoticed and end up causing wrong actions be taken

---

## 3. Market Opportunity

### TAM / SAM / SOM

**Total Addressable Market (TAM): ~$85–93B (2025), growing to $266B+ by 2034 at 13.5% CAGR**

The global SEO software market — encompassing all tools, platforms, and software for keyword research, rank tracking, site audits, backlink analysis, content optimization, competitive intelligence, and technical SEO — is valued at $84.94B (Precedence Research) to $92.74B including services (The Business Research Company). Berlin, as programmable SEO infrastructure, can theoretically address any organization's SEO tooling and workflow spend since it subsumes multiple point solutions into a unified platform. Large enterprises account for ~60% of this market ($44.7B in 2024, Grand View Research), with SMEs as the fastest-growing segment.

Adjacent expansion into marketing automation software ($7.23B in 2025, growing at 12% CAGR) and the broader MarTech ecosystem ($557.94B in 2025, growing at 19.4% CAGR) extends the long-term ceiling significantly.

_Note: Headline figures from research firms bundle software subscriptions with professional services revenue. The pure SEO software market — what companies pay for tools like Semrush, Ahrefs, and BrightEdge — is estimated at $3–5B based on combined revenues of known players._

**Serviceable Addressable Market (SAM): ~$11.5–50B (2025), growing to $58B+ by 2035**

Berlin targets SEO agencies and mid-to-large marketing teams that need comprehensive, multi-capability SEO platforms with workflow automation, team governance, and operational infrastructure. Market Research Future sizes enterprise SEO platforms at $11.35B (2025) growing to $58.29B by 2035. Applying Grand View Research's 60% enterprise share to the broader TAM yields a ~$50B upper estimate. Bottom-up validation from competitor revenues (Semrush $411.6M ARR, Ahrefs ~$149M, BrightEdge ~$120M) confirms $1B+ in current revenue from exactly Berlin's target customer profile — and Berlin's workflow automation layer expands wallet share per customer well beyond what these incumbents capture.

**Serviceable Obtainable Market (SOM): ~$350M–1B over 3–5 years**

Berlin's initial beachhead is SEO agencies (~25,000 globally) and mid-market marketing teams currently stacking 4–6 separate tools. Conservative estimate: ~5,000 agencies and ~2,000 enterprise teams at $24K–$60K/year average contract value yields $170–420M. Moderate estimate: 2% of $50B SAM = ~$1B. Benchmark: Semrush grew from ~$100M to $411M ARR in roughly three years, and Berlin's workflow automation positioning commands higher per-customer revenue than a traditional data tool.

### The AI Search Inflection: AEO/GEO

The most important structural shift in Berlin's market is the emergence of AI-powered search. Answer Engine Optimization (AEO) and Generative Engine Optimization (GEO) are new disciplines focused on ensuring brands are visible within AI-generated answers — ChatGPT, Google AI Overviews, Perplexity, Gemini, Copilot. This market essentially did not exist before 2024 and has already reached ~$1B in 2025.

**The platform shift is real and accelerating:**

- ChatGPT has 700M–1B weekly active users and is the 4th most visited site globally
- Google AI Overviews reach 2B monthly users across 200+ countries, appearing on ~16–25% of U.S. queries
- 50% of consumers intentionally seek out AI-powered search engines (McKinsey, Aug 2025)
- AI-powered search will influence $750B in U.S. consumer spending by 2028 (McKinsey)
- By 2030, AI search is projected to capture 62%+ of total search volume

**GEO/AEO market projections** cluster around 30–50% CAGR, with the market reaching $17B+ by early 2030s (Intel Market Research projects $17.02B by 2034 at 45.5% CAGR; Dimension Market Research projects $17–34B by 2034). This is one of the fastest-growing segments in marketing technology.

**Why this matters for Berlin:** Traditional SEO tools were not built for this world. Existing incumbents (Ahrefs, Semrush) provide data dashboards for Google's blue links. New point solutions (Profound, Peec AI) monitor AI visibility but don't automate the response. Berlin is the operational layer where teams go from data to insight to action to scheduled execution — across both traditional and AI search — from one platform.

### The Traffic and Conversion Shift

AI search is reshaping traffic economics in ways that create both urgency and opportunity:

- Zero-click searches have surged from 56% to 69% in just one year; when AI Overviews appear, organic CTR drops 61%
- In Google AI Mode, zero-click rates reach 93%
- Yet AI-referred traffic is exploding: +620% YoY across content sites, +752% YoY for e-commerce (BrightEdge 2025)
- AI-referred traffic converts at 5–23x higher rates than traditional organic (14.2% vs. 2.8% for AI vs. organic, per SEOmator)
- 35–45% of Fortune 1000 companies already have dedicated AEO programs; 42% of B2B marketers are shifting budget from traditional SEO to AEO

Brands that optimize for AI citations capture disproportionate high-intent traffic. Berlin provides the infrastructure to make that happen systematically.

### Labor-Addressable Market: The Bigger Opportunity

Traditional market sizing measures tool spend. But Berlin's real value proposition isn't "replace your Semrush subscription" — it's "do the work of 1–3 additional SEO specialists without hiring them." This reframes the competitive comparison from tool budgets ($200–$500/month per seat) to labor budgets ($60K–$120K per head per year).

- Direct SEO labor spend: ~$15.5B (207K professionals x $75K average)
- Broader marketing professionals doing SEO work: $30–45B (2–3x the LinkedIn-visible count)
- Agency labor is 50–60%+ of revenue; at ~25,000 agencies globally, the labor addressable market for automation is substantial
- If 5,000 agencies each save one headcount worth of work ($60K+), that alone is $300M+ — a conservative, bottoms-up SOM that doesn't require massive market share

This explains Berlin's pricing power: customers compare the platform to a hire, not a tool, which supports $2–5K/month per team contracts rather than $200/seat subscriptions.

### Key Market Trends

1. **Tool consolidation is accelerating.** Agencies pay for 4–6 separate tools today. Consolidated platforms cut costs 40–60%. The market is ripe for a single operational layer.

2. **AI is making manual SEO unsustainable.** 86% of SEO professionals now use AI in workflows; 67% cite automation of repetitive tasks as the main benefit. The volume and velocity of SEO work now exceeds what manual processes can handle.

3. **Enterprise spend is growing fastest.** Semrush's $50K+/year customers grew 72% YoY. The enterprise segment commands 60% of total market revenue and is where Berlin's workflow value proposition resonates most.

4. **The shift from tools to infrastructure.** The market is moving from "SEO tools" (things you check) to "SEO infrastructure" (systems that run). Berlin sits at this transition — it doesn't just surface data, it executes workflows, schedules operations, and acts on behalf of teams.

5. **Owning the data layer is becoming essential.** Tightening privacy laws (GDPR/CCPA) and third-party cookie deprecation are driving companies to consolidate their data infrastructure. Berlin's proprietary crawlers and its cached keyword database (sourced from leading providers, stored and served from Berlin's own infrastructure) provide a privacy-safe, continuously refreshed data layer that reduces costs over time as the cache compounds.

### VC Validation

The strongest market validation is where top-tier capital is deploying. In the AI search optimization space alone: Profound reached $1B valuation in 18 months (Sequoia, Kleiner Perkins, Lightspeed backed), AirOps at $225M valuation (Greylock-led), Peec AI tripled to $100M+ valuation in 4 months, and Daydream raised $16.6M Series A from First Round Capital. Total venture funding for AI search infrastructure reached $225.8B in 2025. The smart money has validated that AI search optimization is the next major marketing platform shift.

> Full market research with detailed source tables, granular statistics, and complete competitive funding analysis is available in the attached appendix: _Berlin Market Opportunity Research: Comprehensive Report_.

---

## 4. The Solution

- **What have you built?**
  Berlin is programmable infrastructure for inbound growth. It combines an integrated SEO data engine (keyword intelligence sourced from providers like Semrush and DataForSEO and cached in Berlin's own database, proprietary site crawlers, competitor monitoring), a unified data access and action layer (connecting GSC, GA4, Bing Webmaster Tools, CMS, social media accounts and more), an agentic workflow builder (no-code, chat-based), and a thin MCP interoperability layer that exposes all of this as tools inside agentic coding environments (Claude Code, Claude Cowork, ChatGPT Codex, Openclaw). On top of this sits organizational intelligence — brand context memory, team management, and governance.

  A critical technical innovation underpins Berlin's interoperability: standard MCP implementations suffer from context overflow — each tool call fills the LLM's context window, increasing hallucination rates and degrading accuracy as complexity grows. Berlin's thin MCP layer solves this by routing data retrieval and action execution through its own unified data layer rather than passing raw data through the LLM context. Inspired by the codemode architecture (2024), but with proprietary implementation and techniques, this approach reduces MCP-related accuracy issues to near zero. The LLM orchestrates; Berlin's infrastructure handles the heavy lifting.

  A core layer of the platform is the **agentic workflow marketplace** — a library of pre-built, vetted workflows that automate complex, multi-step SEO operations and can be run with a single click. These aren't simple templates; they are fully structured agentic workflows that orchestrate data retrieval, analysis, LLM reasoning, and action-taking across multiple systems. The marketplace lowers the barrier to automation dramatically — teams get immediate value from expert-built workflows without needing to understand the underlying orchestration, while still retaining the ability to build custom workflows for anything the marketplace doesn't cover.

  Berlin is also building an expanding integration layer across a wide range of third-party systems — data sources, CMS platforms, social media channels, indexing APIs, and more — with the goal of becoming a **consolidated agentic system**. Users connect their tools once; Berlin handles authentication, data normalization, and orchestration across all of them. The result is that teams no longer need to subscribe to and manage a fragmented stack of point tools — Berlin's subscription covers the infrastructure, the data, and the integrations in one place.

- **How does it work? (plain language)**
  Users connect their data sources and action endpoints (CMS, social media accounts, analytics platforms, etc.) once. Berlin normalizes everything into a single queryable and actionable layer alongside its integrated keyword data (sourced from leading providers, cached in Berlin's own database) and proprietary crawl data. From there, users have two paths: they can browse the workflow marketplace and run pre-built, vetted workflows with a single click — covering the most common and complex SEO operations out of the box — or they can describe what they need in natural language and Berlin generates structured, multi-step custom workflows. All workflows can be run on demand, scheduled, shared across the org, and governed with human-in-the-loop review. The same capabilities are accessible from Claude, ChatGPT, or any LLM environment via Berlin's tool layer.

- **Core value proposition:**
  - For agencies: More clients, same team size, better deliverables, plus a new AI visibility service line to sell. The workflow marketplace gives agencies instant access to proven, complex workflows without building from scratch — reducing ramp-up time for new clients and standardizing delivery quality.
  - For in-house teams: Unified data layer, no dev dependency, AI visibility metrics for leadership, SEO→pipeline attribution. One subscription replaces an entire stack of point tools — teams no longer pay separately for keyword data, crawling, rank tracking, and workflow automation across multiple vendors.

- **Key differentiators vs. alternatives:**
  - **Not a chatbot — operational infrastructure.** Workflows are persistent, scheduled, shared, and governed. Berlin runs continuously, not just when someone is typing.
  - **Agentic workflow marketplace.** A curated library of pre-built, vetted workflows that handle complex multi-step operations with a single click. Users get immediate automation value on day one without building anything. No competitor offers a marketplace of ready-to-run agentic workflows at this level of complexity and reliability.
  - **Consolidated platform — one subscription replaces many.** Berlin is building integrations across a broad set of third-party systems (data providers, CMS platforms, social channels, analytics tools, indexing APIs) and bundling them into a single agentic platform. Users don't need to pay for or manage separate subscriptions for keyword data, site auditing, rank tracking, or content distribution — Berlin's subscription covers the infrastructure, the data, and the integrations.
  - **Integrated data engine.** Keyword intelligence sourced from providers like Semrush and DataForSEO, cached and served through Berlin's own database — users never need their own third-party subscriptions. Crawling infrastructure (Snake.blue) is fully proprietary. Once data is pulled, it's stored in Berlin's own DB and cached, drastically reducing data costs over time for both Berlin and its users.
  - **No engineering overhead.** Handles complexity that typically requires developer involvement, with significantly higher accuracy than typical AI-assisted SEO tools.
  - **Thin MCP architecture — solves the hallucination problem.** Standard MCP implementations pass data through the LLM's context window, causing context overflow and degraded accuracy as operations scale. Berlin's proprietary thin MCP layer (inspired by the 2024 codemode research, with custom implementation) routes data through its unified data layer instead, reducing hallucination to near zero even on complex multi-source workflows. This is why Berlin can reliably automate operations that break other AI-assisted tools.
  - **Interoperability by design.** Berlin is infrastructure, not a destination app. Works inside agentic coding environments — Claude Code, Claude Cowork, ChatGPT Codex, Openclaw — with the accuracy guarantees that standard MCP cannot provide.
  - **Brand context memory.** Organizational knowledge persists across every interaction, keeping outputs consistent and on-brand without re-explaining.

- **Product screenshots / demo link:** Available upon request — live demo walkthrough can be scheduled with founder

---

## 5. Features & Product Details

| Feature                                   | Description                                                                                                                                                                                                              | Status           |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| **Keyword Intelligence**                  | Keyword research, volume, difficulty, and SERP data sourced from providers (Semrush, DataForSEO) and cached in Berlin's own database. Users get access to leading-provider-quality data without needing their own third-party subscriptions — Berlin handles sourcing, caching, and cost optimization. | Live             |
| **Site Crawling & Competitor Monitoring** | Automated crawlers keeping site and competitor data fresh and queryable. Technical SEO, content structure, internal linking, and page-level metrics always up to date.                                                   | Live             |
| **Unified Data Access Layer**             | Single API interface connecting all SEO data sources (GSC, GA4, Bing Webmaster Tools, etc.). Connect once, available across all workflows and conversations.                                                             | Live             |
| **Third-Party Integrations**              | Pre-built connections to Google Search, SERP APIs, Reddit, CMS platforms, and expanding list of data sources and action endpoints. Platform handles auth and data normalization.                                         | Live & Expanding |
| **Agentic Workflow Builder**              | Chat-based interface for building multi-step SEO workflows without code. Workflows can be run on demand, scheduled, shared across org. Handles complex multi-step operations with higher accuracy than typical AI tools. | Live             |
| **Agentic Coding Environment Integration (Thin MCP)** | Proprietary thin MCP layer exposes Berlin's infrastructure inside agentic coding environments (Claude Code, Claude Cowork, ChatGPT Codex, Openclaw). Unlike standard MCP implementations that fill the LLM's context window and degrade accuracy, Berlin's unified data layer handles retrieval and execution outside the context, enabling complex multi-source operations without hallucination. | Live             |
| **Brand Context**                         | Shared knowledge layer for brand guidelines, terminology, audience details. Automatically available to workflows and LLM conversations. Updates like org-wide memory.                                                    | Live             |
| **Team & Org Management**                 | Add team members, manage access, share credits. Multiple projects (brands) within same org.                                                                                                                              | Live             |
| **Report Center**                         | Centralized collection of all workflow outputs.                                                                                                                                                                          | Live             |
| **Review Center**                         | Human-in-the-loop approval before actions execute.                                                                                                                                                                       | Live             |
| **Workflow Templates**                    | Library of expert-built workflow templates users can apply to their own data.                                                                                                                                            | Live             |


---

## 6. Ideal Customer Profile (ICP)

> Detailed ICP files for each segment exist in the `/marketing/ICP/` folder. Summary below.

### Primary ICP: SEO / Marketing Agencies

| Segment                                    | Core Pain                                                           | Value Hook                                                                 | Top Roles                                       | Buying Signal                               |
| ------------------------------------------ | ------------------------------------------------------------------- | -------------------------------------------------------------------------- | ----------------------------------------------- | ------------------------------------------- |
| **ICP 1 — Large Agencies (11–50 clients)** | Reporting doesn't scale; no GEO/AEO story; no dev access            | Build once, run across all clients; sell AI visibility as new service      | Agency Owner, Director of SEO, Head of Ops      | FOMO on AI SEO; client churn risk           |
| **ICP 2 — Small Agencies (1–10 clients)**  | Can't afford full toolstack; manual reporting; need to win pitches  | Force multiplier; punch above weight class; lead gen hooks                 | Agency Founder, Principal Consultant            | Growth-focused; cost consolidation          |
| **ICP 7 — E-Commerce / Marketplaces**      | Thousands of pages; AI shopping invisible; programmatic SEO blocked | Scale infrastructure; AI visibility for shopping queries; competitor intel | Head of SEO, E-Commerce SEO Manager, VP Digital | Revenue attribution; programmatic SEO focus |

### Secondary ICP: In-House Marketing Teams

| Segment | Core Pain | Value Hook | Top Roles | Buying Signal |
|---------|-----------|------------|-----------|---------------|
| **ICP 3 — Series B–C SaaS In-House** | SEO→pipeline attribution broken; AI discovery invisible; no dev support | Unified data layer; LLM integration; AI visibility metrics for leadership | Head of SEO, VP Growth, SEO Manager | Need to justify SEO budget internally |
| **ICP 4 — Growth Eng / Marketing Ops** | Fragmented SEO data; brittle scripts; AI search not instrumented | Programmable infrastructure; replace custom scripts; API-first | Growth Engineer, Head of Marketing Ops | Dev time savings; reduce marketing requests |
| **ICP 5 — SMB/Startup SEOs** | Doing 3 jobs; no dev time; tight budget; AI search stress | One tool replaces many; LLM integration; pre-built workflows | SEO Manager, Growth Marketing Mgr, Founder | Time savings; cost consolidation |
| **ICP 6 — Mid-Market (no dev support)** | Traffic declining; can't explain AI impact; scale breaks manual work | Pre-built workflows; new narrative for leadership; automation at scale | SEO Director, Senior SEO Manager, VP Marketing | Internal credibility; defend SEO to execs |

### Deprioritized (for now)

- Individual founders doing their own SEO
- AI/ML consultants (niche, low volume)
- Marketplace founders (too early stage, budget constraints)

---

## 7. Business Model

- **Revenue model:** Subscription with usage-based credits. Teams subscribe to a tier that includes a base allocation of workflow execution credits; additional credits available on-demand. LLM compute is passed through at cost — users can also bring their own LLM (Claude, ChatGPT, etc.) via Berlin's interoperability layer, removing token cost from Berlin's P&L entirely.

- **Pricing tiers / structure:**

*Current pricing (PMF exploration phase — designed to minimize friction and maximize learning):*

| Tier | Price | What's Included | Purpose |
|------|-------|-----------------|---------|
| **Free / Explorer** | $0 | Connect domain, run pre-built simple workflows, explore the unified data layer | PLG top-of-funnel; let teams experience the platform before committing |
| **Pro** | $100/month | Full workflow execution (including premium), custom workflow creation, multi-client & multi-project support, base credit allocation | Core self-serve tier; designed for PMF validation |
| **Agency / Enterprise** | Custom | Higher credit allocations, unlimited automation, priority support, Forward Deployed Marketers (Berlin's team sets up and optimizes agentic workflows on-site) | High-touch tier for agencies and enterprise teams with complex, multi-client needs |

*Pricing evolution:* Current $100/month pricing is intentionally flat during PMF exploration — every feature is accessible to maximize learning velocity. As product-market fit solidifies, the tier structure will segment: multi-client/multi-project capabilities and premium automation features move to higher tiers, and per-client or per-project add-on pricing drives expansion revenue. The target ACV for agency and enterprise accounts is $24K–$60K/year, consistent with the platform's labor-replacement value proposition (customers compare Berlin to a hire at $60K–$120K/year, not a tool at $200/month per seat).

  *Forward Deployed Marketers:* A planned services layer where Berlin's marketing specialists embed with customers to design, build, and optimize agentic workflows. Dual purpose: accelerates customer time-to-value and generates proprietary workflow templates that feed back into the platform's template library. Pricing TBD — likely bundled into enterprise contracts or offered as a separate onboarding package.

- **Average contract value (ACV):** Current: ~$1,200/year (PMF pricing). Target: $24K–$60K/year for agency/enterprise accounts as pricing matures post-PMF.

- **Gross margin:** ~80% on core platform infrastructure (data engine, integrations, workflow orchestration, crawlers). LLM tokens provided at cost (zero margin) — a strategic decision to maintain pricing parity with native LLM apps and remove adoption friction. Users who bring their own LLM via Berlin's interoperability layer eliminate this cost line entirely. Blended gross margin depends on the mix of BYO-LLM vs. Berlin-provided tokens; as interoperability adoption grows, blended margin trends toward the 80% infrastructure margin.

- **Unit economics:**
  - Customer Acquisition Cost (CAC): Not yet measurable at scale. Current customers acquired through founder-led inbound (LinkedIn content, conferences, network). No outbound sales spend to date.
  - Lifetime Value (LTV): Too early to calculate — insufficient cohort data on the new platform.
  - LTV:CAC Ratio: TBD post-PMF.
  - Payback Period: TBD post-PMF.

---

## 8. Traction & Metrics

> **Current phase:** Pre-commercial launch. Berlin completed a significant product repositioning in late 2025, evolving from a conversational SEO tool to programmable agentic workflow infrastructure targeting agencies and enterprise marketing teams. The company is currently in its Founding Partner Program, validating product-market fit with design partners before scaling go-to-market.

- **MRR / ARR:**
  - Legacy product: No active MRR. Berlin had 5 total paid users historically (via Stripe), all on the pre-pivot product targeting a different ICP (individual SEOs, small sites) at legacy pricing (~$49/month avg). An additional cohort of users paid through a previous Dubai entity but churned when that Stripe account was closed. All historical paid users were on the previous version of the product — none on the current platform.
  - New platform: Pre-revenue. Currently in Founding Partner Program phase with unpaid design partners. Several pilot partners have agreed to convert to paid upon requirements being met, but no revenue has been recognized.

> **Context on timing:** The current platform version launched in late February 2026 — less than three weeks ago. The Founding Partner Program is deliberately structured as an 8-week engagement with clear conversion milestones. Several partners have verbally committed to paid subscriptions upon specific feature requirements being met. The $2M cap appropriately reflects this pre-revenue, pre-conversion stage while providing upside for early believers.

- **Growth rate:** N/A — pre-commercial launch on new platform.

- **Number of customers / users:**
  - 5 total historical paid users (pre-pivot ICP, via Stripe — no longer active)
  - 5 active pilot partners on the new platform (Founding Partner Program, unpaid)

- **Retention / churn:** Insufficient data on the new platform. Legacy product retention data is not representative of the current positioning and ICP.

- **Engagement metrics (early signals):**
  - 5–6 companies actively using the new platform
  - ~20 workflows created across pilot partners
  - Pilots executing workflows across multiple projects and clients
  - Engagement data will become meaningful as Founding Partner Program matures over the next 8 weeks

- **Pipeline:**
  - 5 active pilots in Founding Partner Program:
    - **Fliki.ai** — AI video platform, ~$1M MRR. In-house marketing team piloting Berlin for SEO operations.
    - **Webandcrafts** — Full-service digital agency, 100+ clients. Evaluating Berlin for cross-client workflow automation and scaled delivery.
    - **BlockSurvey** — Privacy-focused survey platform, ~$20K MRR. Piloting Berlin for SEO and content workflows.
    - **Search Indicators** — SEO agency, 20+ clients. Piloting Berlin for multi-client delivery.
    - 1 additional agency partnership in progress (Swedish agency with high-profile enterprise clients)
  - 4 qualified conversations scheduled this week with potential high-value partners
  - Active founder-led outreach ramping

- **Notable customers / logos:** Fliki.ai, Webandcrafts, BlockSurvey, Search Indicators

- **Case studies or testimonials:** In progress. Strong relationships established with Fliki.ai and Webandcrafts for case study development. The Founding Partner Program is specifically designed to produce 2–3 publishable case studies within 8 weeks of engagement.

---

## 9. Go-to-Market Strategy

### Phase & Objective

Berlin is in founder-led, community-driven GTM mode. The immediate objective is to acquire 20 Founding Partners within 50 days — design-partner customers who validate product-market fit, generate case studies, and become the first wave of champions. Every channel below feeds this singular near-term goal.

### Founding Partner Program

The Founding Partner Program is Berlin's primary conversion mechanism during this phase. A small cohort of agencies and in-house SEO teams receive 50% off in perpetuity plus direct product influence, in exchange for 8 weeks of weekly calls, workflow walkthroughs, and candid feedback. Founding Partners receive hands-on workflow buildout support from Berlin's Forward Deployed Marketers — embedded specialists who design and optimize agentic workflows for each partner's specific operations. This accelerates time-to-value and produces battle-tested workflow templates that feed back into the platform's library. The program is designed to produce 2–3 publishable case studies, a library of proven workflow templates, and organic word-of-mouth from practitioners who helped build the platform.

### Content as the Primary GTM Engine

Content is Berlin's trump card. In a market where every SEO tool company publishes content *about* SEO, Berlin's founder brings a fundamentally different angle: an agentic AI infrastructure expert who turned to SEO — not an SEO who picked up AI tooling. This distinction matters. Most "agentic SEO" content in the market comes from the latter perspective and stays at a surface level. Content from an agent-native builder is more tactical, more practical, and more credible to the technical SEO practitioners Berlin targets.

**Founder-led thought leadership (LinkedIn)** is the primary channel. Sherin publishes educational and strategic content that fills a clear gap in the current SEO conversation — practical agentic workflow knowledge that the SEO community can't get elsewhere. This positions Berlin's founder as the go-to voice on agentic workflows for search, drives qualified inbound to the Founding Partner Program, and builds the personal brand that early-stage B2B companies depend on for trust.

### Agentic SEO Education & Community

Berlin is building the definitive education layer for agentic AI in SEO. Rather than competing on features alone, Berlin is investing in making the entire market smarter about agentic workflows — and positioning the platform as the natural home for practitioners who want to act on what they learn.

This takes several forms. Berlin operates r/agent_seo, a growing Reddit community (3.3K members) where pre-built workflow demos are shared as educational content, exposing prospective users to Berlin's capabilities before any sales conversation. The community is being scaled as a self-reinforcing distribution channel where practitioners share workflows, ask questions, and organically discover the platform. Berlin is also publishing "Agentic AI for SEO," a micro-book written from the same agent-expert angle, heavy on practical workflow examples — serving as a lead magnet, a reference asset, and a credibility builder. And Berlin is launching a meetup series for SEO professionals focused on building and running agents for SEO, with heavy live demos. Because Berlin has interoperability with agentic coding environments like Claude Code, Claude Cowork, ChatGPT Codex, and Openclaw, demos run inside environments the audience already knows and trusts, which dramatically increases credibility and approachability.

Every education touchpoint — subreddit post, book chapter, meetup demo — is built around Berlin's pre-built workflows, creating a direct path from learning to platform adoption.

### Micro-Influencer Program

Berlin is building a network of micro-influencers — SEO practitioners and agency operators — who demo Berlin's workflows on their own channels. Influencers receive free platform access and earn affiliate commissions on referrals. The strategy prioritizes authentic workflow demos over polished ads: practitioners showing real results with real workflows, which builds trust and drives qualified inbound.

### Product-Led Growth Engine: Free Workflow Library

Berlin is building a library of ~50 pre-built workflows that automate the most common, mundane SEO tasks agencies and in-house teams perform daily. These workflows will be available for free — usable through a Berlin account or the desktop app — with execution costs minimized to near-zero on Berlin's side. The thesis: if 90% of what agencies do day-to-day can be automated through Berlin's free tier, the platform becomes indispensable before any commercial conversation begins. This is the primary PLG flywheel — users adopt free workflows, experience the platform's value, and convert to paid when they need custom workflows, multi-client management, or advanced capabilities.

Each workflow doubles as a marketing asset: video walkthroughs, social media demos, and influencer content are built around individual workflows, creating a steady stream of highly specific, highly shareable content.

### Proof-of-Concept: Autonomous Affiliate Site

Berlin is building one fully autonomous affiliate marketing website — managed end-to-end by Berlin's agentic workflows — that acquires organic traffic without human intervention. This project has a ~2-month timeline to show initial results and is informed by an advisor with proven examples of this exact playbook. Once results are established, it will be published as a public case study: transparent, verifiable proof that agentic SEO workflows can independently drive traffic. This is the ultimate "show, don't tell" asset — a live, growing website that prospects can inspect and verify.

### Owned Infrastructure: Snake.blue Crawler

Berlin operates Snake.blue, an AI-first web crawler with native MCP support — this is fully proprietary infrastructure built by the team. Snake.blue underpins Berlin's crawl data layer and is also exposed as standalone infrastructure — extending Berlin's surface area as a platform. For keyword intelligence, Berlin sources data from providers like Semrush and DataForSEO, caches it in its own database, and serves it to users — so users never need their own third-party subscriptions. The caching layer means data costs decrease significantly over time as the database grows, creating both a cost advantage and a compounding data asset.

### Sales Motion

Current: founder-led inbound and outbound, converting through the Founding Partner Program. Near-term: as the free workflow library and community channels scale, the motion shifts toward PLG-assisted sales — prospects self-qualify through free workflow usage, and founder-led sales closes high-value accounts. Longer-term: sales-led with PLG underpinning, supported by case studies, community proof, and the autonomous affiliate site as a reference.

### Expansion & Upsell

Land with free workflows or a single use case (e.g., reporting automation), expand to full workflow stack and custom workflow creation. Per-client/per-project pricing encourages agencies to add more clients. Agentic coding environment integration creates deep stickiness as teams embed Berlin into their daily workflows inside Claude Code, Claude Cowork, ChatGPT Codex, or Openclaw.

### Geographic Focus

No geographic restriction in this phase. Berlin's product is cloud-native and language-agnostic for core SEO operations. Initial traction is founder-network-driven (spanning US, India, EU, and Nordics based on current pilot distribution). Meetup locations will follow community density rather than a predetermined geographic playbook.

---

## 10. Competitive Landscape

The AI search optimization space has attracted significant venture capital since 2024, validating the market but also creating a crowded landscape. Berlin's competitive advantage lies in its unique positioning as *programmable infrastructure* — not a dashboard, not a point solution, and not a black-box agent, but the operational layer that teams build on.

### Direct Competitors: AI-Native SEO & GEO Platforms

**Profound** — $1B valuation, $155M raised (Sequoia, Kleiner Perkins, Lightspeed). Tracks brand visibility across 10+ AI engines (ChatGPT, Claude, Perplexity, Google AI Overviews, Gemini, Copilot, DeepSeek, Grok). 700+ enterprise customers including 10% of Fortune 500. Recently launched "Profound Agents" for autonomous campaign execution. *Limitation:* Profound is a monitoring-first platform expanding into automation. It tells enterprises where they're visible in AI search but doesn't provide the unified SEO data layer, custom workflow building, or traditional SEO infrastructure that Berlin offers. Enterprises still need separate tools for keyword research, site auditing, and workflow orchestration.

**AirOps** — $225M valuation, $60M raised (Greylock, Unusual Ventures, Wing). Content engineering platform that analyzes brand performance across on-site and off-site channels, then creates and refreshes brand-consistent content at scale. Clients include Ramp, Webflow, Kayak, Klaviyo, Wiz. Grew from 20 to ~100 employees in 2025. *Limitation:* AirOps is content-first with modular workflow steps ("Power Steps"). It excels at content creation and optimization but doesn't provide the broader SEO data infrastructure (keyword databases, crawlers, GSC/GA4 integration) or the general-purpose workflow orchestration that Berlin offers. Teams still need separate tools for technical SEO, rank tracking, and competitive monitoring.

**Daydream** — $23.4M raised (First Round Capital, Basis Set Ventures). Automates programmatic SEO for AI search by connecting product feeds, databases, and internal docs to generate and manage large volumes of structured content pages. *Limitation:* Narrowly focused on programmatic content generation from structured data. Lacks broader SEO workflow automation, doesn't provide keyword intelligence or crawler infrastructure, and isn't designed for cross-functional SEO operations or agency multi-client management.

**Peec AI** — $100M+ valuation (tripled in 4 months), $21M raised (Singular). Berlin-based European GEO leader using proprietary UI scraping to simulate real user interactions with AI search engines. 1,300+ companies and agencies; $4M+ ARR in 10 months. Clients include Axel Springer, Chanel, n8n, ElevenLabs, TUI. *Limitation:* Dashboard-focused visibility tracking and sentiment analysis. No workflow orchestration, no programmable infrastructure, no first-party SEO data engine.

**Search Atlas / OTTO SEO** — Won Best AI Search Software at Global Search Awards two years running. OTTO is an autonomous AI SEO agent that auto-detects and deploys technical fixes, content optimizations, and link building. Centralizes keyword research, content optimization, technical audits, and rank tracking. *Limitation:* Black-box automation — the system decides and executes rather than letting teams build custom workflows. Not programmable or extensible; doesn't serve as infrastructure that teams build on top of.

**Frase** — Agentic SEO/GEO platform with 80+ specialized AI agent skills spanning research, creation, optimization, and tracking. Offers MCP integration for use inside Claude and other LLM apps. Recently added GEO tracking across multiple AI platforms. *Limitation:* Content-centric — strong on research and writing workflows but lacks the unified data engine (keyword databases, crawlers, competitive monitoring) and the multi-client operational infrastructure that agencies need.

**Relixir** — YC S25, autonomous GEO agent ("Rex") that monitors AI visibility, generates optimized content, and auto-publishes. Claims 17% lead lift and 80 hours/month saved per customer. *Limitation:* Managed autonomous agent, not programmable infrastructure. The system runs its own playbook — teams can't build custom workflows or govern execution at a granular level.

**Search Party** — $3.5M seed (Fuse VC). Founded by the GRIN team (built $1B+ influencer platform). Maps where AI engines source answers and activates workflows to influence those sources. *Limitation:* Early stage (beta). Focused on AI source influence rather than comprehensive SEO operations.

**GenFlux** — $4.2M seed (Symbolic Capital). Multi-engine tracking across 8+ AI platforms with proprietary "Answer Rank Scoring." *Limitation:* Analytics-only — tracks visibility but doesn't automate the response.

**Otterly AI** — Integrated into Semrush App Center. Tracks brand visibility across ChatGPT, Perplexity, and AI Overviews within Semrush's dashboard. *Limitation:* Monitoring add-on, not a standalone platform. No workflow automation or execution capability.

### Indirect Competitors / Incumbents

**Semrush** — $443.6M revenue (2025), 117K+ paying customers. Launched "Semrush One" (Q4 2025) unifying traditional SEO toolkit with AI Visibility Toolkit tracking brand presence across ChatGPT, Perplexity, Gemini, and AI Overviews. Added AI-powered Keyword Strategy Builder, Content Optimizer, and GBP Agent. Customers paying $50K+/year grew 72% YoY. *Critical development:* Acquired by Adobe (announced Nov 2025, expected close H1 2026). *Limitation:* Feature-rich but tools-first, not workflow-first. AI features are bolted onto an existing dashboard architecture. No agentic workflow orchestration, no custom automation building for agencies, API access restricted to $499+/month tier. Adobe acquisition may slow independent innovation and shift focus toward enterprise marketing cloud integration.

**Ahrefs** — ~$149M revenue (2024, 49% YoY growth), bootstrapped. Added "Brand Radar" for tracking mentions across ChatGPT, Perplexity, and AI Overviews (100M+ prompt database). Launched MCP integration for AI-powered report generation and AI Keyword Suggestions. *Limitation:* Best-in-class backlink data but minimal workflow automation. MCP integration is data access, not orchestration. Still a dashboard tool, not programmable infrastructure.

**Conductor** — Forrester Wave Leader (Q3 2025, highest scores in 16/23 criteria). Added 50+ enterprise AI customers in Q3 2025 including BlackRock, Four Seasons, TD Bank. First to launch official ChatGPT App for enterprise AI brand intelligence. Offers scaled AI content generation and end-to-end AEO/SEO measurement. *Limitation:* Most aggressive incumbent but still analytics-first. Content generation is templated at scale, not truly agentic. No programmable workflow layer for teams to build custom operations.

**Botify** — Forrester Wave Strong Performer (Q3 2025, highest scores in AI-integrated SEO and workflow automation). "PageWorkers" autonomously deploy 50+ optimizations per quarter vs. 4 manually. 82% of customers using Botify Assist in workflows. Launched AI Visibility tracking (Oct 2025). *Limitation:* Most agentic of the incumbents but limited to technical SEO. Doesn't address keyword intelligence, content workflows, or broader inbound growth automation.

**BrightEdge** — Trusted by 57% of Fortune 500. Launched "AI Catalyst" (April 2025) for tracking brand presence across generative AI engines. Produces widely-cited AI traffic research. *Limitation:* Measurement and reporting focused. No workflow automation or execution capability.

**seoClarity** — Enterprise platform with "Content Fusion" blending strategy, performance data, and competitive context for AI-assisted content. AI search visibility tracking across ChatGPT, Gemini, Perplexity. *Limitation:* Template-based programmatic SEO, not truly agentic. Content-focused without broader workflow orchestration.

### DIY Automation Alternatives

**n8n / Make / Zapier** — General-purpose workflow automation platforms increasingly used for SEO. n8n offers 70+ AI nodes with LangChain integration and is the most powerful for custom SEO workflows. Make offers 7,000+ integrations at lower cost. *Limitation:* All require engineering skill to configure. None provide proprietary SEO data — teams must bring their own Ahrefs/Semrush/DataForSEO subscriptions and manage API authentication. Workflows are fragile, not team-accessible, and lack SEO-specific governance. The hallucination problem with LLMs handling multiple data sources via MCPs leads to frequent errors that go unnoticed.

**DataForSEO** — Pay-as-you-go SEO API provider trusted by 750+ software companies. Recently added MCP Server for Claude Code integration. Comprehensive keyword, SERP, and backlink data at ~$30–$600/month. *Limitation:* Purely a data provider. No workflow execution, scheduling, orchestration, or team management. Teams must build the entire operational layer themselves.

**Gumloop / Lindy AI** — General AI agent builders with some SEO use cases. Gumloop offers 90+ templates including SEO workflows. Lindy enables multi-agent coordination. *Limitation:* Not SEO-native. Require external data providers, lack proprietary crawlers and keyword databases, and have no domain-specific accuracy guarantees.

**Generic LLM usage** — ChatGPT/Claude used directly for SEO tasks, sometimes with MCPs for data access. *Limitation:* No persistent workflows, no scheduling, no data integration, no governance. Standard MCP implementations fill the LLM's context window with every tool call, causing hallucination rates to spike when handling multiple data sources. Berlin's thin MCP architecture routes data through its own unified layer rather than the LLM context, enabling reliable multi-source operations that generic MCP usage cannot match.

### The "Do Nothing" Alternative

Continue cobbling together 5–10 tools with spreadsheets and manual work. Hire more people to handle growing workload. Ignore AI search visibility entirely. This path is increasingly untenable as AI search captures more query volume and the velocity of SEO work exceeds what manual processes can handle.

### Competitive Positioning Matrix

| Capability | Berlin | Profound | AirOps | Semrush | Ahrefs | n8n/Make | DataForSEO |
|---|---|---|---|---|---|---|---|
| Integrated keyword database (cached, no user subscription needed) | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ |
| Site crawlers & competitor monitoring | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ |
| AI search / GEO visibility | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| Custom workflow building (no-code) | ✅ | ❌ | Partial | ❌ | ❌ | ✅* | ❌ |
| Scheduled, persistent workflows | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| LLM interoperability (thin MCP, no context overflow) | ✅ | ❌ | ❌ | ❌ | Partial | ❌ | Partial |
| Unified GSC/GA4 + proprietary data | ✅ | ❌ | ❌ | Partial | Partial | ❌ | ❌ |
| Brand context / org memory | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Team governance & review | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| No engineering overhead | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |

*n8n requires engineering to configure

### Competitive Positioning Summary

**vs. GEO/AEO platforms (Profound, Peec AI, GenFlux, Otterly):** These platforms tell you where you're visible in AI search. Berlin lets you *do something about it* — build workflows that optimize, monitor, and execute across both traditional and AI search from a single platform with its own data engine.

**vs. Content platforms (AirOps, Daydream, Frase):** These optimize content creation. Berlin orchestrates the entire SEO operation — from keyword research and competitive intelligence through content optimization, technical SEO, and AI visibility — as persistent, scheduled, governed workflows.

**vs. AI-native competitors (Profound, AirOps, Peec AI):** Well-funded AI-native platforms present a different competitive dynamic than incumbents:

1. **Architectural origin still matters.** Profound started monitoring-first, AirOps content-first. Adding "agents" is grafting execution onto existing architecture. Berlin is workflow-infrastructure-first — the fundamental architecture is built for orchestration, not retrofitted.

2. **Different market entry.** Profound and AirOps are pursuing enterprise blitzscaling with massive capital ($155M and $60M raised respectively). Berlin is capital-efficient, targeting agencies first — lower CAC, faster feedback loops, and a customer base that becomes champions as the platform expands upmarket.

3. **Technical moat.** Berlin's thin MCP architecture solves context overflow and hallucination — the fundamental reliability problem that breaks complex multi-source workflows. Neither Profound nor AirOps has demonstrated this capability.

4. **Skill gap in market.** The majority of the SEO world lacks automation knowledge or technical skills. Founder's unique combination of AI engineering + SEO agency background, combined with education-first GTM (community, micro-book, meetups), positions Berlin to capture the underserved segment of practitioners who need guidance — not just tools. Well-funded competitors are building developer-heavy products for sophisticated buyers; Berlin is building accessible infrastructure for the long tail.

5. **Market size validates multiple approaches.** The $85B+ market supports multiple winning strategies. Berlin doesn't need to out-raise Profound — it needs to execute a capital-efficient playbook that reaches profitability with a different customer segment.

**vs. Incumbents (Semrush, Ahrefs, Conductor, Botify):** Incumbents are data companies adding AI features to existing dashboard architectures. Berlin is infrastructure-first — built from day one for agentic workflow orchestration, not retrofitted. Rebuilding as an agentic platform requires fundamental architectural changes that incumbents can't make without disrupting their core products.

**vs. DIY automation (n8n, Make, DataForSEO):** Powerful but fragile, expensive in aggregate, and inaccessible to non-technical team members. Berlin bundles the data layer (keyword data sourced from providers and cached, proprietary crawlers), workflow engine, and governance into a single platform — users don't need their own API subscriptions, no engineering overhead, and no hallucination problems. Berlin's thin MCP architecture routes data through its unified layer rather than filling the LLM context, solving the accuracy degradation that plagues DIY automation with multiple data sources.

**vs. Autonomous agents (Search Atlas/OTTO, Relixir):** Black-box systems where the agent decides and executes. Berlin gives teams control — build custom workflows, govern execution with human-in-the-loop review, and share across the organization. Infrastructure teams build on, not a service that runs for you.

### Defensibility

- **Technology / IP** — Agentic workflow engine, proprietary crawl infrastructure (Snake.blue), integrated keyword data layer with compounding cache, 80+ ranking signal intelligence layer, and thin MCP architecture that solves the hallucination problem inherent in standard tool-use protocols. Purpose-built architecture for workflow orchestration that incumbents cannot retrofit without fundamental rebuilds.
- **Data moat** — Proprietary crawl infrastructure (Snake.blue), cached keyword database (sourced from providers, stored in Berlin's own DB), and continuous competitive monitoring create compounding data assets. As the cache grows, data costs decrease drastically while coverage increases. Every workflow execution enriches the platform's understanding of search patterns.
- **Switching costs** — Deep integration with data sources, brand context, workflow libraries, and team processes create high switching costs once embedded. Agencies building client delivery on Berlin's workflows face significant migration friction.
- **Speed of execution** — Founder combines AI infrastructure engineering + digital marketing agency experience. This rare overlap enables faster iteration than pure-tech competitors (who don't understand SEO operations) or pure-marketing competitors (who can't build the infrastructure).
- **Network effects (emerging)** — Workflow template library grows with every customer deployment. As Founding Partners create proven workflows, the template marketplace becomes a self-reinforcing distribution channel. Community effects from r/agent_seo (3.3K members) and education content create organic awareness loops.
- **Interoperability moat** — Berlin's thin MCP integration embeds the platform inside users' daily agentic coding environments (Claude Code, Claude Cowork, ChatGPT Codex, Openclaw) with accuracy guarantees that standard MCP implementations cannot provide. Competitors face a choice: skip interoperability entirely (limiting to their own UI) or use standard MCP (degrading reliability at scale). Berlin's proprietary architecture solves this tradeoff, making it invisible infrastructure that's harder to rip out.

---

## 11. "Why Now?" Narrative

- **What macro trend, technology shift, or regulatory change makes this the right moment?**
  - AI-powered search (ChatGPT, Perplexity, Google AI Overviews) is fundamentally reshaping how users discover information, creating a GEO/AEO visibility crisis. Traditional SEO tools were not built for this world.
  - LLM capabilities (Claude, ChatGPT) have reached the point where complex, multi-step SEO workflows can be reliably orchestrated through natural language — this was not possible even 18 months ago.
  - MCP (Model Context Protocol) and tool-use standards are maturing, making interoperability with external LLM apps viable as infrastructure, not a hack.

- **Why was this impossible or impractical 2–3 years ago?**
  - LLMs were not reliable enough for structured, multi-step workflow execution with the accuracy required for professional SEO operations.
  - There was no standardized protocol (like MCP) for exposing tool capabilities to external AI environments — and even now, standard MCP implementations suffer from context overflow and hallucination issues that make complex workflows unreliable. Berlin's thin MCP architecture, developed using techniques from the 2024 codemode research, solves this problem.
  - AI search was nascent — agencies and in-house teams weren't yet panicking about visibility in ChatGPT/Perplexity. The urgency didn't exist.

- **What tailwinds are accelerating adoption?**
  - Agencies are losing clients to competitors who can pitch "AI SEO" — FOMO is a real purchasing driver.
  - CTR drops and SERP volatility are making clients demand more data, more explanation, more reassurance — manual work is exploding.
  - The SEO tool market ($7B+) is ripe for platform consolidation. Teams are fatigued from managing 5–10 disconnected subscriptions.
  - AI referral traffic is growing +620% YoY with 5x higher conversion rates (14.2% vs. 2.8% traditional organic), creating urgent demand for GEO/AEO optimization capabilities that legacy tools cannot provide.
  - The GEO services market alone is projected to reach $17–33B by early 2030s (30–50% CAGR from ~$1B today), representing a massive greenfield opportunity.

---

## 12. Team

### Founders

| Name | Role | Background | LinkedIn |
|------|------|------------|----------|
| Sherin Chacko Thomas | Founder & CEO (Sole Member) | Co-built RedisAI (most performant runtime for AI in production at the time). Infrastructure engineer at Lightning.ai (creators of PyTorch Lightning, one of the most popular deep learning libraries). Author of the first published book on PyTorch. Founded and scaled a dev + marketing agency in Dubai to $350K revenue in year two. Combines deep AI infrastructure engineering with firsthand understanding of SEO workflows, agency pain points, and client dynamics. | [LinkedIn](https://linkedin.com/in/hhsecond) |

- **Key hires planned:** First GTM hire (growth marketer / community manager) with this raise. Co-founder discussions with Ticku Mammen Koshy are in final stages, with a decision expected by mid-April 2026. Ticku brings 15+ years of marketing experience, including SEO leadership for major enterprise clients in Dubai, and is currently based in the US. He has served as an advisor to Berlin since its early days and would take on the CMO / Head of Growth role.

- **Why is this team uniquely positioned to win?**
  Founder combines AI infrastructure engineering with hands-on agency experience — a rare combination that is precisely what this product requires. Co-built RedisAI (the most performant AI-in-production runtime at the time), then built AI app infrastructure at Lightning.ai (creators of PyTorch Lightning). Authored the first published book on PyTorch. After Lightning, founded a dev + digital marketing agency in Dubai, scaling to $350K in year two before shutting it down to go all-in on Berlin. This background means the founder has both built production AI systems at scale and personally experienced the exact agency pain points Berlin solves. The potential addition of a marketing co-founder would complement the technical foundation with dedicated GTM leadership.

---

## 13. Financials

### Historical Summary

Berlin has operated lean through its product evolution phase (May 2025 – present), with monthly expenses averaging ~$1,050. The company had 5 total historical paid users (via Stripe) on the pre-pivot product, plus an additional cohort that paid through a previous Dubai entity — all have since churned. There is no active MRR. The new platform is in the Founding Partner Program phase with unpaid design partners; several have agreed to convert to paid upon requirements being met.

### Current State

- **Cash on hand:** ~$10,000
- **Monthly burn rate:** ~$1,050 (product evolution phase)
  - Cloud infrastructure: ~$250
  - LLM API costs: ~$300
  - Logistics & transportation: ~$300
  - Software subscriptions: ~$200
- **Legacy MRR:** $0 (all historical paid users have churned)
- **Runway at current burn:** ~10 months
- **Runway at planned burn (with marketing spend):** ~2 months

### Inflection Point

The company is transitioning from product development to go-to-market. The current burn rate reflects a build-only phase with near-zero marketing spend. As Berlin begins active marketing and sales motions — required to convert design partner learnings into paid customers — monthly expenses will increase significantly. At projected go-to-market spend levels, current cash reserves support approximately 2 months of operations, making this raise critical to capitalizing on the product momentum and design partner traction already established.

### Projections (2–3 year)

- _TODO_

---

## 14. The Ask

### Raise Overview

- **Amount raising:** $100,000
- **Instrument:** SAFE (post-money)
- **Valuation cap:** $2M post-money
- **Discount:** None
- **Pro rata rights:** Yes
- **Minimum check size:** $25,000

### Why Now — The Funding Inflection

Berlin has spent ~10 months building product through three pivots with under $1,100/month in expenses and zero outside capital. The infrastructure is live, the first design partners are in, and the GTM engine is designed. What's missing is fuel: the company is transitioning from build-mode to go-to-market, and current cash reserves (~$10K) support approximately 2 months of operations at planned marketing spend levels. This raise bridges the gap from Founding Partner validation to repeatable, paid customer acquisition.

### Use of Funds

| Category | Allocation % | Monthly Estimate | Purpose |
|----------|:------------:|:----------------:|---------|
| **Go-to-Market & Growth** | 25% | $2,075 | Founder-led direct sales to convert 5 existing Founding Partners and close 4+ qualified conversations already in pipeline; content production and community growth (r/agent_seo); micro-influencer program as secondary pipeline tactic |
| **Engineering & Infrastructure** | 15% | $1,250 | Platform reliability, workflow engine improvements, expanding integration library, scaling crawlers |
| **Cloud & LLM Costs** | 10% | $830 | Infrastructure scaling as pilot partners increase workflow execution volume; LLM API costs |
| **Hiring** | 40% | $3,320 | First GTM hire (growth marketer / community manager) based in India, where $3.3K/month is highly competitive for senior marketing talent with 5+ years experience |
| **Operations & Legal** | 10% | $830 | LLC → C-Corp conversion, SAFE legal costs, accounting, insurance |

### Target Runway

This raise is sized to provide 12 months of runway at planned burn (~$8,300/month), reaching the following milestones before needing additional capital.

### Milestones This Funding Achieves

| Milestone | Target Timeline | Success Metric |
|-----------|:--------------:|----------------|
| Convert Founding Partners to paid | Months 1–2 | 5 paying agency/enterprise customers at $2K+/month ACV |
| Validate repeatable sales motion | Months 3–5 | $10K+ MRR from 5+ new ICP customers beyond Founding Partners |
| Launch free workflow library (PLG engine) | Months 2–3 | 30+ workflows live, 200+ free-tier users driving inbound pipeline |
| Publish autonomous affiliate site case study | Months 2–4 | Verifiable organic traffic growth from fully autonomous site with documented ROI |
| Reach target ARR for next raise | Months 9–12 | $150K–$250K ARR (6–10 customers at $24K–$36K ACV) |
| Produce 2–3 publishable customer case studies | Months 3–5 | Named logos with quantified results |

### What This Round Does NOT Need to Achieve

This is a pre-seed raise designed to get Berlin from validated product to validated GTM. The goal is not profitability — it is repeatable evidence that agencies and enterprise teams will pay $24K–$60K/year for programmable SEO infrastructure, supported by case studies and a functioning PLG engine. That evidence positions Berlin for a seed round at significantly higher valuation.

---

## 15. Cap Table & Legal

### Current Ownership

| Shareholder | Ownership | Type | Notes |
|-------------|:---------:|------|-------|
| Sherin Chacko Thomas | 100% | Sole Member, LLC | Founder & CEO |

The company is 100% founder-owned with no outside investors, no outstanding SAFEs, no convertible notes, and no option pool. The cap table is completely clean.

### Entity Structure

- **Current entity:** Agentic World, LLC — Delaware Limited Liability Company
- **Registered agent:** 1111B S Governors Ave, Ste 29991, Dover, DE 19904
- **Formation date:** May 16, 2025
- **C-Corp conversion planned:** TBD — open to investor guidance. Founder is prepared to convert to Delaware C-Corp if required by lead investor or accelerator terms. SAFE documents can include a conversion covenant.

> _Note: Most institutional investors and accelerators require a Delaware C-Corp. If converting, standard practice is to form a new C-Corp and roll the LLC assets into it prior to or concurrent with closing. SAFE documents can include a conversion covenant._

### Investor History

- **Prior fundraising:** None — fully bootstrapped to date
- **Existing investors:** None
- **Outstanding SAFEs / convertible notes:** None
- **Advisor equity / grants:** None

### Equity & Option Pool

- **Current option pool:** None (to be created as part of this or next round)
- **Planned option pool:** 10% reserved for future hires and advisors, to be established at conversion to C-Corp
- **409A valuation:** N/A (LLC; 409A will be completed upon C-Corp conversion if applicable)

### Intellectual Property

- **IP ownership:** All IP created by the sole founder and assigned to Agentic World, LLC. No third-party contributors or co-developers.
- **IP assignments complete:** Yes — sole founder is sole member of the LLC; all work product is company-owned.
- **Open-source dependencies:** Standard open-source libraries under permissive licenses (MIT, Apache 2.0). No copyleft (GPL) dependencies in production code.
- **Third-party IP or licensing:** DataForSEO API (keyword and SERP data provider, commercial API license). LLM provider APIs (OpenAI, Anthropic) under standard commercial terms. No exclusive or restrictive licensing arrangements.
- **Patents or patent applications:** None

### Legal Matters

- **Pending litigation:** None
- **Regulatory considerations:** Berlin's crawler infrastructure collects publicly available web data. GDPR and CCPA compliance is addressed through: (1) crawling only publicly accessible pages, (2) respecting robots.txt directives, (3) no collection of personal data, and (4) data processing occurs within standard cloud infrastructure with appropriate security controls. Formal compliance documentation to be completed as part of enterprise readiness.
- **Material contracts:** DataForSEO API subscription (keyword and SERP data). Founding Partner Program agreements (non-binding design partner arrangements, no revenue commitments). Standard cloud infrastructure agreements (hosting, LLM APIs).
- **Terms of service / privacy policy:** Drafted and live on site. To be reviewed by legal counsel as part of enterprise readiness and fundraise preparation.

---

## 16. Social Proof & Milestones

- **Press / media coverage:** Thought-leadership content on agentic SEO gaining traction with industry influencers; 16K+ impressions on a single LinkedIn post picked up by SEO and AI community voices.

- **Awards / recognitions:** None yet

- **Accelerator / incubator participation:** None yet — evaluating accelerator programs as part of fundraise strategy

- **Key partnerships or LOIs:** 5 active Founding Partners including Fliki.ai (~$1M MRR SaaS), Webandcrafts (100+ client agency), BlockSurvey, and Search Indicators (20+ client agency). These are unpaid design partnerships validating product-market fit prior to paid conversion.

- **Notable milestones achieved:**
  - Intelligence infrastructure built (80+ ranking signals, automated prioritization, GSC/GA integrations)
  - Agentic workflow engine live and operational
  - Thin MCP interoperability layer live — works inside Claude Code, Claude Cowork, ChatGPT Codex, and Openclaw
  - Integrated keyword database (sourced from leading providers, cached in own DB) and proprietary crawlers operational
  - Founding Partner Program launched — 5 active design partners including Fliki.ai (~$1M MRR), Webandcrafts (100+ client agency), BlockSurvey, and Search Indicators (20+ client agency)

---

## 17. Risks & Mitigations

| Risk                                                         | Likelihood | Impact | Mitigation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------ | ---------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Incumbents add AI/workflow features**                      | Medium     | High   | Berlin's architecture is workflow-first, not bolted on. Incumbents (Ahrefs, SEMrush) are data companies — rebuilding as agentic platforms requires fundamental architectural changes. Speed of execution and founder-market fit are key advantages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **LLM platform risk (OpenAI, Anthropic)**                    | Low-Medium | Medium | Berlin is LLM-agnostic — it's the data and workflow layer, not the model. Interoperability with multiple LLMs is a core design principle.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Agency market adoption speed**                             | Medium     | Medium | Founding Partner Program validates with real users before scaling. Proof-first approach de-risks product direction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **AI search landscape evolving rapidly**                     | High       | Medium | Berlin's flexible workflow architecture can adapt to new search paradigms. Proprietary crawl infrastructure, integrated keyword data layer, and GEO/AEO capabilities position us ahead of the curve.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Data privacy / crawler compliance**                        | Low-Medium | Medium | Crawlers only access publicly available data, respect robots.txt, and collect no personal information. GDPR/CCPA compliance roadmap in progress for enterprise readiness.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Single founder / key-person risk**                         | Medium     | High   | First GTM hire planned with this raise to reduce single-point-of-failure. Co-founder discussions with Ticku Mammen Koshy (15+ years marketing, SEO leadership for enterprise clients, US-based) are in final stages with a decision expected by mid-April 2026. Founder's combined AI engineering + agency background is hard to replicate but the hire plan and imminent co-founder addition build operational depth.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Fundamental shift in how the web works**                   | Medium     | High   | If agents fully reshape how people search and buy online, the current SEO paradigm could become unrecognizable. However, the core assumption holds: regardless of the medium, users will always need to search for and purchase things. Berlin's architecture is workflow-first, not SEO-mechanic-first — workflows are the first-class citizen, not any particular search engine's ranking algorithm. The platform can retarget its workflow engine, data layer, and integrations toward whatever the web becomes (agent-to-agent commerce, conversational discovery, etc.) without a fundamental rebuild.                                                                                                                                                                                                                                                                                                                                                                 |
| **AI-native competitors expand into workflow orchestration** | Medium     | High   | Well-funded AI-native platforms like Profound ($1B valuation, Sequoia/Kleiner Perkins/Lightspeed backed) have already begun expanding beyond monitoring into execution — Profound recently launched "Profound Agents" for autonomous campaign execution. Other GEO-focused startups (Peec AI, Relixir, Search Party) could follow the same trajectory. Mitigation: these platforms are monitoring-first and content-first by architecture — bolting on workflow orchestration is fundamentally different from building it as the core product. Berlin's workflow engine, integrated data layer, interoperability (MCP), and agentic workflow marketplace create structural advantages that monitoring platforms cannot replicate by adding an "agents" feature. The same architectural constraint that limits incumbents applies here: retrofitting execution onto an analytics platform is a different engineering challenge than building execution-first infrastructure. |

---

## 18. Appendix

- **Berlin Market Opportunity Research: Comprehensive Report** — Full market research with detailed TAM/SAM/SOM source tables, AEO/GEO market data, AI traffic and conversion statistics, competitive landscape with funding details, labor-based market analysis, SEO workforce salary data, and investor talking points. _(See: `/market-research/berlin-market-research-final.md`)_
- Links to detailed financial model
- Product demo recording
- Customer testimonials / case studies
- Technical architecture overview
- Data privacy & AI usage disclosures
- Any other supporting materials

---

> [!WARNING]
> **SYNC CHECK REQUIRED**: If you updated this document, verify that `funding-page/index.html` reflects any changes to shared data points. The HTML deck contains only a curated subset of this information — check for divergence, not parity.

---

_Last updated: March 2026_
_Document owner: Sherin Chacko Thomas_

---
