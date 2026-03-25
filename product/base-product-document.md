# Product Base Document — Agent Berlin

> This is the single source of truth for what Berlin is at a structural and functional level. Every pitch deck, landing page, sales conversation, feature announcement, and product update should trace back to this document. It defines what Berlin **is**, not who it's for or why they should care — that translation happens downstream.
>
> If something feels missing, update this document first. Never add capabilities to downstream materials that don't exist here.

---

## Berlin in One Line

> Berlin is programmable infrastructure for inbound growth — a unified data, workflow, and intelligence layer that lets teams build, run, and scale any SEO operation without engineering overhead.

---

## The Six Pillars

The pillars are not independent features. They form a stack — each layer builds on the ones below it.

### Pillar 1: First-Party Data Engine

Berlin generates its own proprietary SEO data. It is not purely a middleware layer connecting other people's data.

**Keyword Intelligence.** Berlin sources keyword research, search volume, difficulty scores, and SERP data from providers (Semrush, DataForSEO) and caches everything in its own database. Users get leading-provider-quality keyword data without needing their own third-party subscriptions — Berlin handles sourcing, caching, and cost optimization. As the cache compounds over time, data costs decrease while coverage increases.

**Site Crawling & Competitor Monitoring.** Berlin operates Snake.blue, a fully proprietary, AI-first web crawler with native MCP support. Automated crawlers keep site and competitor data continuously fresh and queryable — technical SEO data, content structure, internal linking, page-level metrics, and competitive intelligence are always up to date. Snake.blue also serves as standalone infrastructure, extending Berlin's surface area as a platform.

**Ranking Signal Intelligence.** Berlin has built an intelligence layer that tracks 80+ ranking signals across sites and competitors, with automated prioritization that surfaces what matters most. Combined with GSC and GA4 data, this layer turns raw crawl and keyword data into actionable, prioritized insights — not just dashboards to stare at.

This data is the raw material that powers everything else in the platform.

### Pillar 2: Unified Data & Action Layer

A single interface that connects all of a user's data sources and all of their action endpoints.

**Data sources** include Google Search Console, GA4, Bing Webmaster Tools, and others. **Action endpoints** include CMS platforms, social media channels, indexing APIs, and any system where a user publishes, submits, or triggers an outcome. Pre-built connections also exist for Google Search, SERP APIs, Reddit, and a growing list of external data sources.

Users authenticate once per source. After that, every connected source is available across all workflows, all conversations, and all integrations — no repeated OAuth flows, no API key management, no per-tool configuration. Berlin handles authentication and data normalization.

The integration layer is continuously expanding to cover any third-party source a team needs to read from or write to. First-party data from Pillar 1 sits alongside connected third-party data as a unified queryable and actionable surface.

Berlin is building toward becoming a **consolidated platform** — users connect their tools once, and Berlin handles authentication, data normalization, and orchestration across all of them. The goal is that teams no longer need to subscribe to and manage a fragmented stack of point tools; Berlin's subscription covers the infrastructure, the data, and the integrations in one place.

### Pillar 3: Agentic Workflow Engine

A chat-based interface where users describe what they need in natural language, and Berlin generates structured, executable, multi-step workflows — regardless of complexity.

No node graphs. No developer required. No context-window limitations or hallucination problems introduced by raw MCP piping. No writing programs to extract insights from data before feeding them to an LLM. Berlin orchestrates data retrieval, analysis, LLM reasoning, and action-taking into reliable workflows with significantly higher accuracy and precision than typical AI-assisted SEO tools. It handles complexity that would otherwise require engineering involvement.

### Pillar 4: Workflow Ecosystem & Operations

Workflows are not one-and-done executions. They are persistent, operational assets that can be scheduled, shared, templated, and governed.

**Scheduling.** Workflows can run on a schedule without human initiation.

**Report Center.** A centralized collection point for all workflow outputs.

**Review Center.** Human-in-the-loop approval before any action executes.

**Agentic Workflow Marketplace.** A library of pre-built, vetted workflows that automate complex, multi-step SEO operations and can be run with a single click. These are not simple templates — they are fully structured agentic workflows that orchestrate data retrieval, analysis, LLM reasoning, and action-taking across multiple systems. The marketplace lowers the barrier to automation dramatically: teams get immediate value from expert-built workflows without needing to understand the underlying orchestration, while retaining the ability to build custom workflows for anything the marketplace doesn't cover. The library grows with every customer deployment — as teams create proven workflows, the marketplace becomes a self-reinforcing asset.

**Sharing & Governance.** Workflows can be shared across the organization. Teams can standardize delivery by sharing proven workflows across clients and projects.

This is what makes Berlin operational infrastructure rather than a chatbot — it is a system that runs continuously, not only when someone is typing.

### Pillar 5: Interoperability Layer

The same capabilities that power Berlin's native interface are exposed as a tool layer for external LLM applications. Users can work inside Claude Code, Claude Cowork, ChatGPT Codex, Openclaw, or any other AI environment and access their full Berlin data stack and workflow capabilities conversationally.

**Thin MCP Architecture.** Standard MCP (Model Context Protocol) implementations suffer from context overflow — each tool call fills the LLM's context window, increasing hallucination rates and degrading accuracy as complexity grows. Berlin's thin MCP layer solves this by routing data retrieval and action execution through its own unified data layer rather than passing raw data through the LLM context. The LLM orchestrates; Berlin's infrastructure handles the heavy lifting. This reduces MCP-related accuracy issues to near zero, enabling complex multi-source operations that break other AI-assisted tools.

Berlin does not force users into a single UI. The same tasks the workflow builder handles can be run from whichever LLM application a user already works in, without switching tools. This is a deliberate architectural choice: Berlin is infrastructure, not a destination app. It meets users where they already work.

### Pillar 6: Organizational Intelligence

A combined layer of team governance and persistent organizational memory.

**Brand Context.** A shared knowledge layer where teams store brand guidelines, terminology, audience details, preferences, and other reusable context. This context is automatically available to every workflow and every LLM conversation, keeping outputs consistent and on-brand. It gets updated like org-wide memory — without anyone re-explaining it each session.

**Team & Org Management.** Add team members, manage access, scope permissions, and share credits across the organization. Multiple brands or projects can live under a single account.

Security, governance, and institutional knowledge are not afterthoughts — they are structural.

---

## How the Pillars Relate

- **Pillar 1 (First-Party Data)** and **Pillar 2 (Unified Data & Action Layer)** together form the data foundation. Pillar 1 generates proprietary data; Pillar 2 connects and normalizes everything else alongside it.
- **Pillar 3 (Agentic Workflow Engine)** sits on top of the data foundation. It is the intelligence that turns raw data into structured, executable action.
- **Pillar 4 (Workflow Ecosystem)** wraps Pillar 3 in operational infrastructure — scheduling, reporting, review, marketplace, and sharing.
- **Pillar 5 (Interoperability)** extends the entire stack into external environments, making Berlin's capabilities available wherever users work.
- **Pillar 6 (Organizational Intelligence)** wraps around everything — the security, memory, and governance layer that ensures the entire system operates with context, consistency, and appropriate access control.

---

## Feature Reference

A flat reference of all current platform capabilities and their status.

| Feature | Description | Status |
| --- | --- | --- |
| **Keyword Intelligence** | Keyword research, volume, difficulty, and SERP data sourced from providers (Semrush, DataForSEO) and cached in Berlin's own database. Users get leading-provider-quality data without their own third-party subscriptions. | Live |
| **Site Crawling & Competitor Monitoring** | Proprietary crawlers (Snake.blue) keeping site and competitor data fresh and queryable. Technical SEO, content structure, internal linking, and page-level metrics always up to date. Snake.blue is also exposed as standalone infrastructure. | Live |
| **Ranking Signal Intelligence** | 80+ ranking signals tracked across sites and competitors with automated prioritization. Turns raw crawl, keyword, and analytics data into actionable, prioritized insights. | Live |
| **Unified Data Access Layer** | Single API interface connecting all SEO data sources (GSC, GA4, Bing Webmaster Tools, etc.). Connect once, available across all workflows and conversations. | Live |
| **Third-Party Integrations** | Pre-built connections to Google Search, SERP APIs, Reddit, CMS platforms, and expanding list of data sources and action endpoints. Platform handles auth and data normalization. | Live & Expanding |
| **Agentic Workflow Builder** | Chat-based interface for building multi-step SEO workflows without code. Workflows can be run on demand, scheduled, shared across org. Handles complex multi-step operations with higher accuracy than typical AI tools. | Live |
| **Agentic Workflow Marketplace** | Library of pre-built, vetted workflows that automate complex multi-step SEO operations with a single click. Fully structured agentic workflows, not simple templates. | Live |
| **Agentic Coding Environment Integration (Thin MCP)** | Proprietary thin MCP layer exposes Berlin's infrastructure inside agentic coding environments (Claude Code, Claude Cowork, ChatGPT Codex, Openclaw). Routes data through Berlin's unified data layer instead of the LLM's context window, enabling complex multi-source operations without hallucination. | Live |
| **Brand Context** | Shared knowledge layer for brand guidelines, terminology, audience details. Automatically available to workflows and LLM conversations. Updates like org-wide memory. | Live |
| **Team & Org Management** | Add team members, manage access, share credits. Multiple projects (brands) within same org. | Live |
| **Report Center** | Centralized collection of all workflow outputs. | Live |
| **Review Center** | Human-in-the-loop approval before actions execute. | Live |
| **Workflow Scheduling** | Workflows run on a schedule without human initiation. | Live |
| **Workflow Sharing** | Workflows can be shared and standardized across teams, clients, and projects. | Live |

---

## How to Use This Document

This is the canonical reference for what Berlin is at a structural and functional level. When crafting messaging for a specific audience:

1. Start from the pillars and feature reference.
2. Identify which pillars and features matter most to the target audience.
3. Translate the structural description into the language of their pain and ambition.
4. Never add a capability that doesn't exist here. If something feels missing, update this document first.

---

_Agentic World, LLC — Internal Foundation Document_
_Last updated: March 2026_
