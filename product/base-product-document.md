# Product Base Document — Agent Berlin

> This is the single source of truth for what Berlin is at a structural and functional level. Every pitch deck, landing page, sales conversation, feature announcement, and product update should trace back to this document. It defines what Berlin **is**, not who it's for or why they should care — that translation happens downstream.
>
> If something feels missing, update this document first. Never add capabilities to downstream materials that don't exist here.
>
> **Note:** Berlin is one of two products from Agentic World, LLC. The other is USOL (Universal Search Optimization Layer). USOL has its own base document (`base-usol-document.md`). This document covers Berlin only — though the relationship between the two is defined below.

---

## Berlin in One Line

> Berlin is the AI agent platform for SEO and AEO — a chat-based system where teams build, run, schedule, and govern agentic workflows that automate search optimization operations without engineering overhead.

Berlin is the **agent**. It is where automation happens — where natural language becomes structured, executable, multi-step workflows. Berlin sits on top of USOL, the infrastructure layer that provides the data, integrations, and intelligence Berlin's agents operate on.

---

## The Foundation: USOL

Berlin runs on USOL (Universal Search Optimization Layer) — the unified data, integration, and intelligence infrastructure that is also available as a standalone product. USOL provides:

- **First-party data engine** — keyword intelligence (sourced from Semrush, DataForSEO, cached in Berlin's database), site crawling and competitor monitoring via Snake.blue (proprietary AI-first crawler), and ranking signal intelligence (80+ signals with automated prioritization).
- **Unified data and action layer** — single-authentication access to GSC, GA4, Bing Webmaster Tools, CMS platforms, social channels, Google Trends, Google Maps, review platforms, SERP APIs, and a continuously growing list of data sources and action endpoints.
- **Semantic page and keyword intelligence** — brand and competitor pages and keywords auto-indexed as embeddings, searchable by meaning rather than exact match.
- **Thin MCP architecture** — data retrieval and action execution routed through USOL's infrastructure rather than the LLM context window, eliminating hallucination from context overflow.
- **Organizational intelligence** — brand context, team & org management, permissions, and governance. Shared across both products.

For the full specification of USOL's capabilities, integrations, and architecture, see `base-usol-document.md`.

Berlin inherits all of USOL's data and integrations automatically. Every workflow, every agent, and every scheduled operation in Berlin draws from this foundation. Users who subscribe to Berlin get USOL's full infrastructure as part of the platform — they never need to manage the data layer separately.

---

## Berlin's Pillars

Berlin's unique value sits above the USOL foundation. These pillars define what Berlin adds: the agentic automation layer that turns USOL's data and integrations into executable, governed workflows.

### Pillar 1: Agentic Workflow Engine

A chat-based interface where users describe what they need in natural language, and Berlin generates structured, executable, multi-step workflows — regardless of complexity.

No node graphs. No developer required. No context-window limitations or hallucination problems introduced by raw MCP piping. No writing programs to extract insights from data before feeding them to an LLM. Berlin orchestrates data retrieval, analysis, LLM reasoning, and action-taking into reliable workflows with significantly higher accuracy and precision than typical AI-assisted SEO tools. It handles complexity that would otherwise require engineering involvement.

Berlin's workflow engine is the key differentiator from USOL alone. USOL gives AI agents access to the data and tools — Berlin's engine structures that access into reliable, repeatable, multi-step automations that non-technical users can build conversationally.

### Pillar 2: Workflow Ecosystem & Operations

Workflows are not one-and-done executions. They are persistent, operational assets that can be scheduled, shared, templated, and governed.

**Scheduling.** Workflows can run on a schedule without human initiation.

**Report Center.** A centralized collection point for all workflow outputs.

**Review Center.** Human-in-the-loop approval before any action executes.

**Agentic Workflow Marketplace.** A library of pre-built, vetted workflows that automate complex, multi-step SEO operations and can be run with a single click. These are not simple templates — they are fully structured agentic workflows that orchestrate data retrieval, analysis, LLM reasoning, and action-taking across multiple systems. The marketplace lowers the barrier to automation dramatically: teams get immediate value from expert-built workflows without needing to understand the underlying orchestration, while retaining the ability to build custom workflows for anything the marketplace doesn't cover. The library grows with every customer deployment — as teams create proven workflows, the marketplace becomes a self-reinforcing asset.

**Sharing & Governance.** Workflows can be shared across the organization. Teams can standardize delivery by sharing proven workflows across clients and projects.

This is what makes Berlin operational infrastructure rather than a chatbot — it is a system that runs continuously, not only when someone is typing.

### Shared: Organizational Intelligence

Brand Context, Team & Org Management, and governance are **platform-level infrastructure shared between Berlin and USOL** — not Berlin-specific. They are defined in `base-usol-document.md` and apply across both products. Berlin workflows inherit brand context, permissions, and team structure automatically through this shared layer.

---

## How the Pillars Relate

- **USOL (Foundation)** provides the data engine, integrations, semantic intelligence, thin MCP architecture, and organizational intelligence (brand context, team management, governance). It is the infrastructure layer that both Berlin and standalone USOL users draw from.
- **Pillar 1 (Agentic Workflow Engine)** sits on top of USOL. It is the intelligence that turns raw data and integrations into structured, executable, multi-step automations.
- **Pillar 2 (Workflow Ecosystem)** wraps Pillar 1 in operational infrastructure — scheduling, reporting, review, marketplace, and sharing.

---

## Berlin and USOL: The Relationship

Agent Berlin ships two products. They share infrastructure but serve different users and use cases.

**USOL** is the infrastructure layer — the universal connector that gives any AI coding agent (Claude Cowork, Claude Code, Codex, etc.) access to the full SEO/AEO toolchain. USOL is for teams who already work inside AI coding environments and want to bring SEO data and actions into those environments without building custom integrations. USOL is a lower-abstraction product — it provides the tools, the user's AI agent provides the automation.

**Berlin** is the agent platform — the higher-abstraction product where non-technical users build, run, schedule, and govern SEO/AEO workflows through a chat-based interface. Berlin uses USOL under the hood but adds the agentic workflow engine, the workflow marketplace, scheduling, reporting, and review. Berlin is for teams who want the automation done for them, not teams who want to wire it up themselves.

**Organizational intelligence** (brand context, team management, governance) is shared platform infrastructure — available in both products. It lives in the USOL layer and is inherited by Berlin.

**How to think about it:**
- USOL = the layer. Gives AI agents the ability to do SEO/AEO work.
- Berlin = the agent. Does the SEO/AEO work for you.
- A Berlin subscription includes USOL. A USOL subscription does not include Berlin's agentic capabilities.

**In practice:** An agency might use Berlin for their core delivery workflows (automated audits, scheduled reports, marketplace workflows) and also use USOL inside Claude Cowork for ad hoc analysis and custom one-off tasks. The same data, integrations, and brand context are available in both contexts.

---

## Feature Reference

A flat reference of Berlin-specific capabilities and their status. For USOL's feature reference (data engine, integrations, thin MCP, semantic intelligence), see `base-usol-document.md`.

### Berlin-Only Features (Require Berlin Subscription)

| Feature | Description | Status |
| --- | --- | --- |
| **Agentic Workflow Builder** | Chat-based interface for building multi-step SEO workflows without code. Workflows can be run on demand, scheduled, shared across org. Handles complex multi-step operations with higher accuracy than typical AI tools. | Live |
| **Agentic Workflow Marketplace** | Library of pre-built, vetted workflows that automate complex multi-step SEO operations with a single click. Fully structured agentic workflows, not simple templates. | Live |
| **Report Center** | Centralized collection of all workflow outputs. | Live |
| **Review Center** | Human-in-the-loop approval before actions execute. | Live |
| **Workflow Scheduling** | Workflows run on a schedule without human initiation. | Live |
| **Workflow Sharing** | Workflows can be shared and standardized across teams, clients, and projects. | Live |

### USOL Foundation Features (Included in Berlin, Also Available Standalone)

| Feature | Description | Status |
| --- | --- | --- |
| **Keyword Intelligence** | Keyword research, volume, difficulty, and SERP data sourced from providers (Semrush, DataForSEO) and cached in Berlin's own database. | Live |
| **Site Crawling & Competitor Monitoring** | Proprietary crawlers (Snake.blue) keeping site and competitor data fresh and queryable. | Live |
| **Ranking Signal Intelligence** | 80+ ranking signals tracked with automated prioritization. | Live |
| **Unified Data & Action Layer** | Single-authentication access to GSC, GA4, Bing Webmaster Tools, CMS, social, Google Trends, Maps, reviews, and more. | Live & Expanding |
| **Semantic Page & Keyword Intelligence** | Brand and competitor pages/keywords auto-indexed as embeddings, searchable by meaning. | Live |
| **Thin MCP Architecture** | Data routed through USOL's infrastructure instead of LLM context window, eliminating hallucination from context overflow. | Live |
| **Brand Context** | Shared knowledge layer for brand guidelines, terminology, audience details. Automatically available to workflows and AI agent sessions. Updates like org-wide memory. | Live |
| **Team & Org Management** | Add team members, manage access, share credits. Multiple projects (brands) within same org. | Live |

---

## How to Use This Document

This is the canonical reference for what Berlin is at a structural and functional level. When crafting messaging for a specific audience:

1. Start from Berlin's pillars and feature reference for agentic/automation messaging.
2. Reference `base-usol-document.md` for infrastructure, data, and integration messaging.
3. Identify which capabilities matter most to the target audience — and whether they're Berlin capabilities (agentic workflows, marketplace, scheduling) or USOL capabilities (data, integrations, thin MCP).
4. Translate the structural description into the language of their pain and ambition.
5. Never add a capability that doesn't exist here or in the USOL document. If something feels missing, update the appropriate source document first.

---

_Agentic World, LLC — Internal Foundation Document_
_Last updated: April 2026_
