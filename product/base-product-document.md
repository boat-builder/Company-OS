# Product Base Document — Agent Berlin

> This is the single source of truth for what Berlin is at a structural and functional level. Every pitch deck, landing page, sales conversation, feature announcement, and product update should trace back to this document. It defines what Berlin **is**, not who it's for or why they should care — that translation happens downstream.
>
> If something feels missing, update this document first. Never add capabilities to downstream materials that don't exist here.
>
> **Note:** Berlin is one of two products from Agentic World, LLC. The other is USOL (Universal Search Optimization Layer). USOL has its own base document (`base-usol-document.md`). This document covers Berlin only — though the relationship between the two is defined below.

---

## Berlin in One Line

> Berlin is an AI agent for SEO and AEO — it understands search optimization strategy, knows what's working now, and executes the work that would otherwise take up the majority of an SEO or marketing team's time.

Berlin is not a tool you configure or a workflow you build. It is an agent with its own intelligence about search optimization — what strategies work, what signals matter, how to prioritize. It takes on the operational work of SEO/AEO so teams can focus on higher-level strategy and creative work.

Berlin is powered by USOL, the infrastructure layer that provides the data, integrations, and intelligence Berlin operates on.

---

## The Foundation: USOL

Berlin runs on USOL (Universal Search Optimization Layer) — the unified data, integration, and intelligence infrastructure that is also available as a standalone product. USOL provides:

- **First-party data engine** — keyword intelligence (comprehensive keyword data cached in Berlin's database), site crawling and competitor monitoring via Snake.blue (proprietary AI-first crawler), and ranking signal intelligence (80+ signals with automated prioritization).
- **Unified data and action layer** — single-authentication access to GSC, GA4, Bing Webmaster Tools, CMS platforms, social channels, Google Trends, Google Maps, review platforms, search results data, and a continuously growing list of data sources and action endpoints.
- **Semantic page and keyword intelligence** — brand and competitor pages and keywords auto-indexed as embeddings, searchable by meaning rather than exact match.
- **Thin MCP architecture** — data retrieval and action execution routed through USOL's infrastructure rather than the LLM context window, eliminating hallucination from context overflow.
- **Organizational intelligence** — brand context, team & org management, permissions, and governance. Shared across both products.

For the full specification of USOL's capabilities, integrations, and architecture, see `base-usol-document.md`.

Berlin inherits all of USOL's data and integrations automatically. Users who subscribe to Berlin get USOL's full infrastructure as part of the platform — they never need to manage the data layer separately.

---

## What Berlin Is

### An AI Agent with SEO/AEO Intelligence

Berlin is not a generic AI assistant pointed at SEO tools. It has domain-specific intelligence about search optimization:

- **Strategy awareness.** Berlin understands what SEO/AEO strategies are working now — not just textbook knowledge, but current, practical knowledge about what moves the needle.
- **Prioritization.** Given a brand's data, Berlin can identify what matters most and in what order. It doesn't just surface information — it makes recommendations about where to focus.
- **Execution capability.** Berlin doesn't just advise — it does the work. Content optimization, technical fixes, reporting, monitoring, competitive analysis — the operational tasks that consume most of an SEO team's time.

### Effort Reduction, Not Just Assistance

The goal is to take approximately 70% of the operational effort off an SEO or marketing person's plate. This is not about answering questions or generating suggestions — it's about Berlin actually doing the work that would otherwise require hours of manual effort.

This includes:
- Running audits and producing actionable reports
- Monitoring rankings, competitors, and opportunities
- Identifying and prioritizing optimization opportunities
- Executing content and technical improvements
- Tracking performance and surfacing what's changed

### Human Oversight

Berlin operates with human oversight. Before taking actions that affect live systems (publishing content, making changes), Berlin surfaces what it intends to do for review. Teams can configure how much oversight they want — from reviewing every action to reviewing only certain categories of work.

---

## Operational Infrastructure

Berlin includes infrastructure for managing ongoing SEO/AEO operations:

**Scheduling.** Work can run on a schedule without human initiation — monitoring, reporting, recurring audits.

**Report Center.** A centralized collection point for all outputs Berlin produces.

**Review Center.** Human-in-the-loop approval before actions execute.

**Sharing & Governance.** Work can be shared across the organization. Teams can standardize delivery across clients and projects.

This infrastructure makes Berlin operational — it runs continuously, not only when someone is actively using it.

---

## Berlin and USOL: The Relationship

Agentic World ships two products. They share infrastructure but serve different use cases.

**USOL** is the infrastructure layer — the universal connector that gives any AI coding agent (Claude Code, Codex, etc.) access to the full SEO/AEO toolchain. USOL is for teams who already work inside AI coding environments and want to bring SEO data and actions into those environments without building custom integrations. USOL provides the tools and data; the user's AI agent provides the automation.

**Berlin** is the agent — the higher-abstraction product where an AI agent with SEO/AEO expertise does the work for you. Berlin uses USOL under the hood but adds domain intelligence, operational infrastructure, and the ability to take action autonomously (with oversight). Berlin is for teams who want the work done, not teams who want to wire up their own automation.

**Organizational intelligence** (brand context, team management, governance) is shared platform infrastructure — available in both products. It lives in the USOL layer and is inherited by Berlin.

**How to think about it:**
- USOL = the layer. Gives AI agents the ability to do SEO/AEO work.
- Berlin = the agent. Does the SEO/AEO work for you.
- A Berlin subscription includes USOL. A USOL subscription does not include Berlin's agent capabilities.

**In practice:** An agency might use Berlin for their core SEO operations (audits, monitoring, optimization, reporting) and also use USOL inside Claude Code for ad hoc analysis and custom one-off tasks. The same data, integrations, and brand context are available in both contexts.

---

## Feature Reference

A flat reference of Berlin-specific capabilities and their status. For USOL's feature reference (data engine, integrations, thin MCP, semantic intelligence), see `base-usol-document.md`.

### Berlin-Only Features (Require Berlin Subscription)

| Feature | Description | Status |
| --- | --- | --- |
| **AI Agent for SEO/AEO** | An agent with domain intelligence about search optimization — understands strategy, prioritizes work, executes operations. | Live |
| **Report Center** | Centralized collection of all outputs Berlin produces. | Live |
| **Review Center** | Human-in-the-loop approval before actions execute. | Live |
| **Scheduling** | Work runs on a schedule without human initiation. | Live |
| **Sharing** | Work can be shared and standardized across teams, clients, and projects. | Live |

### USOL Foundation Features (Included in Berlin, Also Available Standalone)

| Feature | Description | Status |
| --- | --- | --- |
| **Keyword Intelligence** | Comprehensive keyword research, volume, difficulty, and ranking data cached in Berlin's own database. | Live |
| **Site Crawling & Competitor Monitoring** | Proprietary crawlers (Snake.blue) keeping site and competitor data fresh and queryable. | Live |
| **Ranking Signal Intelligence** | 80+ ranking signals tracked with automated prioritization. | Live |
| **Unified Data & Action Layer** | Single-authentication access to GSC, GA4, Bing Webmaster Tools, CMS, social, Google Trends, Maps, reviews, and more. | Live & Expanding |
| **Semantic Page & Keyword Intelligence** | Brand and competitor pages/keywords auto-indexed as embeddings, searchable by meaning. | Live |
| **Thin MCP Architecture** | Data routed through USOL's infrastructure instead of LLM context window, eliminating hallucination from context overflow. | Live |
| **Brand Context** | Shared knowledge layer for brand guidelines, terminology, audience details. Automatically available to Berlin and AI agent sessions. Updates like org-wide memory. | Live |
| **Team & Org Management** | Add team members, manage access, share credits. Multiple projects (brands) within same org. | Live |

---

## How to Use This Document

This is the canonical reference for what Berlin is at a structural and functional level. When crafting messaging for a specific audience:

1. Start from Berlin's core value proposition (AI agent with SEO/AEO intelligence that does the work).
2. Reference `base-usol-document.md` for infrastructure, data, and integration details.
3. Identify which capabilities matter most to the target audience — and whether they're Berlin capabilities (the agent, operational infrastructure) or USOL capabilities (data, integrations, thin MCP).
4. Translate the structural description into the language of their pain and ambition.
5. Never add a capability that doesn't exist here or in the USOL document. If something feels missing, update the appropriate source document first.

---

_Agentic World, LLC — Internal Foundation Document_
_Last updated: April 2026_
