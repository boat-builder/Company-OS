# Product

> **The source of truth for what Berlin does.** Descriptive, not persuasive — everything here should be verifiable against the running product. If a capability is missing, add it here first, then propagate to decks, sales material, and marketing copy.
>
> Engineering substrate → [`engineering.md`](engineering.md). Market, category, and competitors → [`market.md`](market.md).

***

## What Berlin Is

Berlin is an AEO engine that a human operator drives in partnership with an agent. The operator brings judgment and intent; Berlin brings the brand's full context, the data, the reusable procedures, and the execution.

The product is deliberately **human-in-the-loop**. An operator working with an agent — not an agent running unattended.

***

## Two Kinds of Execution: Agents and Workflows

Everything Berlin does runs as either an **agent** or a **workflow**. The distinction matters, because it determines what can run on its own.

**Agents are intelligent.** They reason, decide, and handle work that can't be specified in advance — reading a brand's context, judging what matters, writing a report, deciding what actions to create. That intelligence comes from an LLM, which means every agent run costs tokens, and tokens are the binding constraint on how much Berlin can run unattended.

**Workflows are deterministic.** No LLM, no intelligence, no token cost. A workflow pulls a body of data, analyses it programmatically, applies rules, and writes out an intermediate report file. Because it costs nothing per run, **a workflow can be scheduled and left to run on its own.**

The two compose. Workflows do the cheap, repetitive, high-volume analysis on a schedule and leave their output behind. Agents then read those intermediate reports and do the expensive, judgement-heavy part — creating actions, writing and updating reports for stakeholders. This is how Berlin gets continuous coverage of a brand without paying for continuous intelligence.

***

## The Fundamental Pieces

Berlin is built from seven first-class entities. Everything else in the product composes these.

### 1. Brand Profile

When a user adds a domain, Berlin researches the brand from the open internet and from the brand's own website, and assembles a structured profile: name and description, industries, business model, company size, target customer segments, geographies, competitors, and a hierarchical topic tree describing what the brand is about. The user reviews and corrects it.

**This research is not automatic.** It runs when the operator triggers it — it is packaged as a saved skill the operator invokes. Berlin does not act on a brand without someone asking it to.

### 2. Brand Files

The brand profile is a structured input space, and structured spaces never fit everything. Anything without a field of its own — brand tone, keyword priorities, internal playbooks, style guides, product taxonomies — becomes a **brand file** attached to the brand.

The mechanic that makes this work: **file names and a short overview of each file's contents are exposed to the agent at runtime.** The agent sees a catalogue of what's available and pulls the specific file it needs, rather than having everything forced into its context.

Berlin auto-generates a *Brand Context* file from the research pass; every other file is added by the customer or the FDM. The upload surface is a heavily used FDM tool, not an edge case. The file set shapes every downstream decision: which procedures get run, how reports read, what actions get generated.

### 3. Skills

**Skills are saved, reusable procedures for agents.** When an operator works out how to do something well — run a brand research pass, produce a competitor gap analysis, build an audit report — they save it as a skill, and it becomes reusable across every other brand in the system.

This is what makes the operator model scale. The operator doesn't re-derive method per account and doesn't have to get the instructions right each time; they invoke a skill that already encodes the method. Skills accumulate as an asset: every account benefits from work done on any other account.

### 4. Workflows

**Workflows are scheduled, deterministic analysis jobs.** They pull data, analyse it programmatically, and write an intermediate report an agent can later act on. No LLM, so no token cost, so they can run continuously without a human present.

Workflows are **created agentically** — the operator works with the agent to build a workflow and put it on a schedule, rather than writing it by hand. Once scheduled, the workflow runs itself and keeps depositing fresh analysis for the agents to pick up.

### 5. Actions

**Actions are the things to act on.** Berlin's agent generates them; another agent or a human executes them. Each action has a short imperative title, a description tied to a specific finding, and a category: **off-site citation work, content create, content update, technical fix, validation, custom**.

Some actions execute automatically against connected systems — publishing to the CMS, fixing internal linking, updating metadata. The rest route to the Review Center for human approval.

### 6. Reports

**Reports are the stakeholder-facing analysis** — the AEO audit, distinct from the initial brand research that produces the grounding. A report says what is happening in the AEO space for the brand and lets stakeholders track KPIs over time. Reports stay current as new signal arrives and surface in the Report Center.

Note the two senses of *audit* inside Berlin: the **brand research pass** builds the grounding layer, while the **AEO audit** is the ongoing analysis that produces reports and actions. They are different things.

### 7. Integrations

Integrations are what let Berlin see and act beyond its own database. They come in two kinds.

**Per-brand — connected by the customer.** Google Search Console, Google Analytics, Bing Webmaster Tools, CMS platforms, and social accounts including LinkedIn and Reddit. Single authentication, connected once per brand.

**Platform-level — always available, not brand-specific.** Google Search, ChatGPT search, and Perplexity search, exposed directly to the agent. This is how Berlin inspects live SERPs and AI answers: who currently ranks for a query, what the AI engines actually say about a brand or its competitors, and how that changes.

Integrations are the reason Berlin's analysis is grounded in what is live right now rather than in a stale index.

***

## How Berlin Is Operated

### Claude is the operator interface

Berlin is exposed as a **CLI** and as an **MCP server**. The preferred operator surface today is **Claude**, with Berlin's tools connected into it and pre-built skills ready to run.

**This is a deliberate cost decision.** Running the same volume of agent work through the API would cost a great deal of money. A $200/month Claude subscription with Berlin connected into it does the same work at a flat, predictable cost. Pre-built skills mean the operator can't get the invocation wrong.

**The tradeoff is honest: complete automation is not possible this way.** Agent runs need someone sitting in front of Claude to trigger them. Workflows still run on their own — they cost no tokens — but the intelligent half of the loop waits for a human.

### The same architecture runs internally

The CLI + MCP shape isn't a workaround bolted on for Claude. It is the same architecture Berlin's own agentic loop uses when it runs inside our system. **That internal loop is where we want to be** once token cost stops being the binding constraint — same skills, same workflows, same files, same actions, with no human required at the keyboard.

***

## The Operating Loop — Audit → Report → Act

### Audit

Berlin watches a brand-shaped slice of the SEO/AEO surface, composed from a vetted library of strategy patterns maintained by Berlin's research team. The composition is what makes it personalised: a brand-new website mostly gets content work; an established brand with weak topical authority gets review-presence, citation, and authority tracking; a regulated industry gets a different shape again. Much of this watching runs as scheduled workflows.

### Report

Signal is synthesised into a living per-brand report — findings and prioritised focus areas, kept current as new signal lands. The report is the bridge between *what we're seeing* and *what to do about it*.

### Act

From the report, Berlin generates discrete, well-scoped actions, each grounded in a specific finding. Many auto-execute against connected systems; the rest route through the Review Center.

The three are a cycle, not an onboarding sequence. The brand profile and brand files keep tuning behaviour as the brand evolves. The FDM owns the loop end-to-end for their assigned accounts and can shape any phase.

***

## What Berlin Knows About a Brand

When a brand is connected, two collection processes run continuously behind it.

* **Keyword collection.** Traditional keyword data — volume, difficulty, ranking — pulled from sources like Semrush and cached in Berlin's own database. Customers never need their own third-party subscriptions.

* **Page crawling.** Every page of the brand's site *and its competitors' sites*, crawled on a recurring cadence and stored with full version history.

Both feed a **semantic index** — keywords and pages indexed by meaning, so the agent can ask questions of them rather than run exact-match lookups. What that unlocks:

* **Idea → volume.** Point at an interesting idea and get the cluster of keywords around it, with their volumes.
* **Does this already exist?** Instantly check whether the brand already has a page covering a topic, before commissioning a new one.
* **What changed.** Because crawls recur and are versioned, compare the brand or any competitor against their state at the last crawl.
* **What competitors just published.** See new competitor pages as they appear, and decide whether we should have that page too.

### Beyond the brand's own website

AEO is not won on the brand's own domain alone. Berlin exposes **off-page and third-party surfaces** to the agent — Reddit, LinkedIn, YouTube and others — tracking off-site activity for the brand *and* its competitors, not just on-site work.

***

## The Platform

**Dashboard.** The customer- and stakeholder-facing surface. Progress, reports, and actions surface here. It is not the operator's working surface — that's Claude.

**Report Center.** Centralised collection of every output Berlin produces.

**Review Center and oversight controls.** Before an action affects a live system, Berlin surfaces what it intends to do. Teams configure how much oversight they want — every action, or only certain categories.

**Scheduling.** Workflows and data collection run on schedules without human initiation. Agent runs are operator-triggered under the current model.

**Teams and organisations.** Add team members, manage access, share credits. Multiple projects — one per brand — within the same org. Work can be shared and standardised across teams, clients, and projects, with permissions and governance at the platform level.
