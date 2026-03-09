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
- **Mission Statement:** `[FILL IN]`
- **Key Contact(s):** Sherin Chacko Thomas — +91 890 474 5603

### Product Evolution (May 2025 – Present)

Berlin's current positioning is the result of focused product discovery over ~10 months, each phase informed by direct user feedback:

1. **Conversational SEO data layer (mid-2025):** Built a chat interface for marketers to query and explore their SEO data in natural language. Validated that teams desperately needed unified data access — but learned that *talking to data* wasn't enough. Users wanted the platform to *do the work*, not just answer questions.

2. **Automated SEO assistant (late 2025):** Evolved into an end-to-end automated SEO assistant, executing full workflows autonomously. Validated the automation thesis — but discovered that one-size-fits-all automation didn't match how teams actually operate. Agencies and in-house teams need workflows they can build, customize, schedule, and govern.

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

5. **First-party data is becoming essential.** Tightening privacy laws (GDPR/CCPA) and third-party cookie deprecation are driving companies to build their own data repositories. Berlin's proprietary crawlers and keyword databases provide privacy-safe, continuously refreshed data.

### VC Validation

The strongest market validation is where top-tier capital is deploying. In the AI search optimization space alone: Profound reached $1B valuation in 18 months (Sequoia, Kleiner Perkins, Lightspeed backed), AirOps at $225M valuation (Greylock-led), Peec AI tripled to $100M+ valuation in 4 months, and Daydream raised $16.6M Series A from First Round Capital. Total venture funding for AI search infrastructure reached $225.8B in 2025. The smart money has validated that AI search optimization is the next major marketing platform shift.

> Full market research with detailed source tables, granular statistics, and complete competitive funding analysis is available in the attached appendix: _Berlin Market Opportunity Research: Comprehensive Report_.

---

## 4. The Solution [need a lot of modification]

- **What have you built?**
  Berlin is programmable infrastructure for inbound growth. It combines a first-party SEO data engine (keyword intelligence, site crawlers, competitor monitoring), a unified data access and action layer (connecting GSC, GA4, Bing Webmaster Tools, CMS, social media accounts and more), an agentic workflow builder (no-code, chat-based), and an interoperability layer that exposes all of this as tools inside external LLM apps (Claude, ChatGPT). On top of this sits organizational intelligence — brand context memory, team management, and governance.

- **How does it work? (plain language)**
  Users connect their data sources and action parties (like CMS and social media accounts) once. Berlin normalizes everything into a single queryable/actionable layer alongside its own proprietary keyword and crawl data. Users then describe what they need in natural language — Berlin generates structured, multi-step workflows that can be run on demand, scheduled, shared across the org, and governed with human-in-the-loop review. The same capabilities are accessible from Claude, ChatGPT, or any LLM environment via Berlin's tool layer.

- **Core value proposition:**
  - For agencies: More clients, same team size, better deliverables, plus a new AI visibility service line to sell
  - For in-house teams: Unified data layer, no dev dependency, AI visibility metrics for leadership, SEO→pipeline attribution

- **Key differentiators vs. alternatives:**
  - **Not a chatbot — operational infrastructure.** Workflows are persistent, scheduled, shared, and governed. Berlin runs continuously, not just when someone is typing.
  - **First-party data engine.** Built-in keyword database, crawlers, and competitor monitoring — no third-party subscriptions required for core SEO data.
  - **No engineering overhead.** Handles complexity that typically requires developer involvement, with significantly higher accuracy than typical AI-assisted SEO tools.
  - **Interoperability by design.** Berlin is infrastructure, not a destination app. Works inside whatever LLM environment users already live in.
  - **Brand context memory.** Organizational knowledge persists across every interaction, keeping outputs consistent and on-brand without re-explaining.

- **Product screenshots / demo link:** `[FILL IN]`

---

## 5. Features & Product Details

| Feature                                   | Description                                                                                                                                                                                                              | Status           |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| **Keyword Intelligence**                  | Built-in keyword database comparable to leading data providers. Keyword research, volume, difficulty, and SERP data without third-party subscriptions.                                                                   | Live             |
| **Site Crawling & Competitor Monitoring** | Automated crawlers keeping site and competitor data fresh and queryable. Technical SEO, content structure, internal linking, and page-level metrics always up to date.                                                   | Live             |
| **Unified Data Access Layer**             | Single API interface connecting all SEO data sources (GSC, GA4, Bing Webmaster Tools, etc.). Connect once, available across all workflows and conversations.                                                             | Live             |
| **Third-Party Integrations**              | Pre-built connections to Google Search, SERP APIs, Reddit, CMS platforms, and expanding list of data sources and action endpoints. Platform handles auth and data normalization.                                         | Live & Expanding |
| **Agentic Workflow Builder**              | Chat-based interface for building multi-step SEO workflows without code. Workflows can be run on demand, scheduled, shared across org. Handles complex multi-step operations with higher accuracy than typical AI tools. | Live             |
| **LLM App Integration (MCP)**             | Same infrastructure exposed as tool layer for Claude, ChatGPT, and other LLM apps. Users interact with full SEO data stack conversationally from their preferred environment.                                            | Live             |
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
  - Legacy product: ~$800 MRR (~$9.6K ARR) from ~20 active paid users carried over from the pre-pivot product. These users are on a different ICP (individual SEOs, small sites) at legacy pricing (~$49/month avg). This revenue is not representative of the new platform's target market or pricing.
  - New platform: Pre-revenue. Currently in Founding Partner Program phase with unpaid design partners.

- **Growth rate:** N/A — pre-commercial launch on new platform.

- **Number of customers / users:**
  - 20 legacy paid users (pre-pivot ICP)
  - 5 active pilot partners on the new platform (Founding Partner Program)

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

- **Current GTM phase:** Founding Partner Program
  - Status: Building with users, not for users
  - Selecting a small number of agencies as founding partners
  - Value exchange: 50% off forever + direct product influence in return for weekly calls (8 weeks), workflow walkthroughs, and honest feedback
  - Goal: Validate product-market fit, generate case studies, create champions

- **Current acquisition channels:**
  - Outbound founder-led sales (calls, demos)
  - Social / content (positioning around AI SEO, GEO/AEO thought leadership)
  - `[FILL IN — any other channels: referrals, communities, etc.]`

- **Sales motion:** Founder-led sales → transitioning to sales-led with PLG elements (LLM integration is inherently PLG)

- **Marketing strategy:** `[FILL IN — content marketing, social, community, events, etc.]`

- **Partnerships:** `[FILL IN — any strategic partnerships, integrations, co-marketing]`

- **Expansion / upsell strategy:**
  - Land with one use case (e.g., reporting automation), expand to full workflow stack
  - Per-client/project pricing encourages agencies to add more clients
  - LLM integration creates stickiness as users embed Berlin into daily workflows

- **Geographic focus:** `[FILL IN]`

---

## 10. Competitive Landscape

- **Direct competitors:**
  `[FILL IN — any AI-native SEO platforms, workflow-first SEO tools]`

- **Indirect competitors / incumbents:**
  - **Point tools:** Ahrefs, SEMrush, Moz, Screaming Frog (data but no workflow orchestration, no AI search)
  - **DIY automation:** n8n, custom scripts, DataForSEO API direct (powerful but fragile, not team-accessible)
  - **Generic AI assistants:** ChatGPT/Claude used directly for SEO (no persistent workflows, no data integration, no governance)

- **The "do nothing" alternative:**
  - Continue cobbling together 5–10 tools with spreadsheets and manual work
  - Hire more people to handle growing workload
  - Ignore AI search visibility entirely

- **Competitive positioning (what you do better):**
  - **vs. Ahrefs/SEMrush:** Berlin is a workflow and automation layer, not just a data provider. It combines data from multiple sources (including its own) into executable, scheduled workflows — no developer required.
  - **vs. DIY automations:** Berlin provides team-accessible, governed, shareable workflows with brand context. No brittle scripts to maintain, no technical barrier for non-dev team members.
  - **vs. Generic AI chat:** Berlin has structured, reliable workflows (not one-off chat), persistent data connections, scheduling, reporting, review/approval — operational infrastructure, not a chatbot.

- **Defensibility:**
  - [x] Technology / IP — Agentic workflow engine, first-party data infrastructure, 80+ ranking signal intelligence layer
  - [ ] Network effects — `[FILL IN — potential for workflow template marketplace, community effects]`
  - [x] Data moat — First-party keyword database, crawl data, and continuous competitive monitoring create proprietary data assets
  - [x] Switching costs — Deep integration with data sources, brand context, workflow libraries, and team processes create high switching costs once embedded
  - [x] Speed of execution — Founder combines AI infrastructure engineering + digital marketing agency experience; uniquely positioned to iterate faster than pure-tech or pure-marketing competitors
  - [ ] Brand / trust — `[FILL IN]`

---

## 11. "Why Now?" Narrative

- **What macro trend, technology shift, or regulatory change makes this the right moment?**
  - AI-powered search (ChatGPT, Perplexity, Google AI Overviews) is fundamentally reshaping how users discover information, creating a GEO/AEO visibility crisis. Traditional SEO tools were not built for this world.
  - LLM capabilities (Claude, ChatGPT) have reached the point where complex, multi-step SEO workflows can be reliably orchestrated through natural language — this was not possible even 18 months ago.
  - MCP (Model Context Protocol) and tool-use standards are maturing, making interoperability with external LLM apps viable as infrastructure, not a hack.

- **Why was this impossible or impractical 2–3 years ago?**
  - LLMs were not reliable enough for structured, multi-step workflow execution with the accuracy required for professional SEO operations.
  - There was no standardized protocol (like MCP) for exposing tool capabilities to external AI environments.
  - AI search was nascent — agencies and in-house teams weren't yet panicking about visibility in ChatGPT/Perplexity. The urgency didn't exist.

- **What tailwinds are accelerating adoption?**
  - Agencies are losing clients to competitors who can pitch "AI SEO" — FOMO is a real purchasing driver.
  - CTR drops and SERP volatility are making clients demand more data, more explanation, more reassurance — manual work is exploding.
  - The SEO tool market ($7B+) is ripe for platform consolidation. Teams are fatigued from managing 5–10 disconnected subscriptions.
  - `[FILL IN — any additional tailwinds: regulatory, market size growth data, etc.]`

---

## 12. Team

### Founders

| Name | Role | Background | LinkedIn |
|------|------|------------|----------|
| Sherin Chacko Thomas | Founder & CEO (Sole Member) | AI infrastructure engineering + ran a digital marketing agency. Combines deep technical capability with firsthand understanding of SEO workflows, agency pain points, and client dynamics. `[FILL IN — specific previous companies, roles, achievements]` | `[FILL IN]` |

- **Key hires planned:**

- **Why is this team uniquely positioned to win?**
  Founder combines AI infrastructure engineering background with hands-on experience running a digital marketing agency — rare combination of deep technical capability and firsthand understanding of SEO workflows, agency pain points, and client dynamics. `[FILL IN — expand with specific background details, previous companies, achievements]`

---

## 13. Financials

### Historical

| Metric | Month 1 | Month 2 | Month 3 | ... |
|--------|---------|---------|---------|-----|
| Revenue |        |         |         |     |
| Expenses |       |         |         |     |
| Net Burn |       |         |         |     |

### Current State

- **Monthly burn rate:** $___
- **Cash on hand:** $___
- **Runway remaining:** ___ months

### Projections (2–3 year)

- _(Attach or summarize financial model with key assumptions)_

---

## 14. The Ask

- **Amount raising:** $___

- **Instrument:** _(SAFE, priced equity, convertible note)_

- **Valuation / cap:** $___

- **Use of funds:**

| Category | Allocation | Purpose |
|----------|-----------|---------|
| Engineering |         |         |
| Sales & Marketing |  |         |
| Operations |         |         |
| Hiring |             |         |
| Other |              |         |

- **Milestones this funding achieves:**

---

## 15. Cap Table & Legal

- **Current ownership breakdown:**

| Shareholder | Ownership % | Type |
|-------------|-------------|------|
| Sherin Chacko Thomas | `[FILL IN]` | Sole Member, LLC |

- **Entity structure:** Delaware LLC, sole member

- **Existing investors:** `[FILL IN — or "None" if bootstrapped]`

- **Outstanding SAFEs / notes:** `[FILL IN — or "None"]`

- **Option pool:** `[FILL IN]`% (allocated / unallocated)

- **409A valuation:** `[FILL IN — or "N/A for LLC"]`

- **IP assignments:** `[FILL IN — complete? Y/N]`

- **Any pending legal matters:** `[FILL IN — or "None"]`

---

## 16. Social Proof & Milestones

- **Press / media coverage:** `[FILL IN]`

- **Awards / recognitions:** `[FILL IN]`

- **Accelerator / incubator participation:** `[FILL IN]`

- **Key partnerships or LOIs:** `[FILL IN]`

- **Notable milestones achieved:**
  - Intelligence infrastructure built (80+ ranking signals, automated prioritization, GSC/GA integrations)
  - Agentic workflow engine live and operational
  - LLM interoperability layer (MCP) live — works inside Claude, ChatGPT
  - First-party keyword database and crawlers operational
  - Founding Partner Program launched — 5 active design partners including Fliki.ai (~$1M MRR), Webandcrafts (100+ client agency), BlockSurvey, and Search Indicators (20+ client agency)

---

## 17. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **Incumbents add AI/workflow features** | Medium | High | Berlin's architecture is workflow-first, not bolted on. Incumbents (Ahrefs, SEMrush) are data companies — rebuilding as agentic platforms requires fundamental architectural changes. Speed of execution and founder-market fit are key advantages. |
| **LLM platform risk (OpenAI, Anthropic)** | Low-Medium | Medium | Berlin is LLM-agnostic — it's the data and workflow layer, not the model. Interoperability with multiple LLMs is a core design principle. |
| **Agency market adoption speed** | Medium | Medium | Founding Partner Program validates with real users before scaling. Proof-first approach de-risks product direction. |
| **AI search landscape evolving rapidly** | High | Medium | Berlin's flexible workflow architecture can adapt to new search paradigms. First-party data and GEO/AEO capabilities position us ahead of the curve. |
| `[FILL IN — any additional risks: regulatory, technical, market]` | | | |

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

_Last updated: March 2026_
_Document owner: `[FILL IN]`_

---

> **Note:** All `[FILL IN]` markers indicate information that needs to be provided by the founder(s). Sections 3 (Market Opportunity), 7 (Business Model), 8 (Traction & Metrics), 12 (Team details), 13 (Financials), 14 (The Ask), and 15 (Cap Table & Legal) are largely unfilled and require founder input — these contain sensitive data that only the founding team can provide.
