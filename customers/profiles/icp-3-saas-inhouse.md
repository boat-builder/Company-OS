# ICP 3 — Series B–C B2B SaaS In-House SEO/Growth Teams [SECONDARY]

> **Living document.** Base thesis below. Append new intel (interviews, social signals, objections, wins) as you learn it.
>
> **Priority tier:** SECONDARY — Strong opportunity with clear pain points. Activated as the primary agency beachhead is established and PLG self-serve scales.

### How this file fits in

| File | What belongs here | What does NOT belong here |
|------|-------------------|---------------------------|
| **This file** (`customers/profiles/icp-3-saas-inhouse.md`) | Everything about the ICP itself — who they are, their pain points, priorities, buying signals, roles, discovery intel, objections, open questions. Tool-agnostic. | Product features, value propositions, pricing anchors, marketing copy, messaging tests. |
| **Product base document** (`product/base-product-document.md`) | What Berlin is at a structural and functional level — pillars, features, architecture. Audience-agnostic. | ICP-specific pain points, marketing angles, positioning language. |
| **Positioning file** (`marketing/positioning-icp3-*.md`) | The derived marketing layer — how Berlin's product maps to this ICP's needs. Messaging, tone, hooks, objection responses, CTAs, pricing framing. | Raw ICP research (that goes here) or raw product specs (that go in the product doc). |

When adding new information, ask: _"Is this about who they are, what we built, or how we sell it to them?"_ — and put it in the matching file.

---

## Quick Stats

| Field | Detail |
|-------|--------|
| **Segment** | Series B–C SaaS In-House |
| **Priority** | SECONDARY |
| **Core Pain** | SEO→pipeline attribution broken; AI discovery invisible; no dev support |
| **Top Roles** | Head of SEO, VP Growth, SEO Manager |
| **Buying Signal** | Need to justify SEO budget internally |
| **Typical Team Size** | Potentially sizable (10+ people across the broader SEO/content org); core SEO-specific team is often 2–4 |
| **Verticals** | Cybersecurity, fintech, healthcare — verticals where content quality and accuracy are non-negotiable |
| **Revenue Dependency** | Majority of company revenue dependent on inbound/organic |
| **Current Toolstack Spend** | Typically 4–6 paid SEO subscriptions + 2–3 LLM subscriptions + automation tool in exploration stage; $1,500–$3,000+/month across subscriptions before labor costs |

---

## Key Pain Points

- **Attribution from SEO to pipeline is broken and getting harder to defend.** Leadership is asking why organic traffic is dropping and whether SEO is still worth the investment. The team doesn't have clean data to answer with confidence.
- **AI-assisted discovery is changing how buyers find them — and they can't see it.** B2B buyers are increasingly using ChatGPT, Perplexity, or Gemini to research categories and shortlist vendors. The team has no visibility into whether their brand is showing up in those conversations.
- **They're small teams with large mandates.** A 2–4 person SEO team at a Series B company is expected to own content, technical SEO, competitor intelligence, and reporting — often with no dedicated developer.
- **Getting engineering support for even basic SEO tasks takes weeks.** Anything that requires a developer (hreflang, schema, internal links at scale, log file analysis) sits in a queue behind product work.
- **Content and messaging consistency is hard across a team building quickly.** Without a centralized source of truth, different writers, freelancers, and tools produce outputs that drift from brand guidelines.
- **Their existing tooling is fragmented.** They're toggling between GSC, GA4, a rank tracker, a crawl tool, and AI tools — with no unified way to query or combine the data.

---

## How They Work

- **They own the full SEO lifecycle:** wireframing, keyword research, content production, technical SEO, and audits. They're methodical — often using entity-based approaches to avoid cannibalization.
- **They're at the very beginning of automation.** Exploring tools like n8n, Claude, Python scripts — but haven't operationalized any of it yet. The gap between experimenting and running reliable automation is where they're stuck.
- **Deep SEO expertise, but need education on AI/automation adoption.** The team knows SEO deeply. What they lack is a clear path to operationalizing AI without sacrificing the content quality and rigor their vertical demands.
- **Content quality is sacred in their verticals.** In regulated or trust-dependent industries, a hallucinated output isn't just wrong — it's a credibility and compliance risk. They want automation that assists research and analysis, not automation that replaces human judgment on content.

---

## What They Need (Tool-Agnostic)

- A way to connect SEO activity to pipeline revenue — clean attribution they can present to leadership.
- Visibility into AI-assisted discovery channels (ChatGPT, Perplexity, Gemini) where their buyers are increasingly researching.
- Automation that doesn't require engineering support — they can't wait weeks for dev tickets.
- A way to consolidate their fragmented toolstack (GSC, GA4, rank tracker, crawl tool, AI tools) into fewer interfaces.
- Brand and messaging consistency across a fast-scaling team with multiple contributors.

> **Note:** For how our product maps to these needs, see the positioning document for this ICP.

---

## Assumptions About Their Priorities

- **Pipeline attribution is the metric that gets them budget and headcount.** If the platform helps them connect SEO activity to revenue, that's transformational for internal politics.
- **They're already bought in on AI tools and want everything to work inside them.** LLM-native workflows (Claude Code, Claude Cowork, ChatGPT Codex, Openclaw) are not a nice-to-have — it's how they actually work. Any tool that doesn't meet them in those environments will lose.
- **Speed of experimentation is critical.** They need to move fast to keep up with the company's growth stage. Tools that require onboarding time or slow iteration cycles will be abandoned.
- **AI search visibility is an emerging, urgent concern.** They've read the same LinkedIn posts and reports everyone else has. They want to get ahead of it before leadership asks.
- **They prefer depth over surface features.** This is a technically literate ICP. They'll explore the data layer, API, and workflow complexity before judging the product.

---

## Ideal Roles

- **Head of SEO / SEO Lead** — Owns organic performance; needs to justify budget and demonstrate results to leadership. Typically the champion — feels the pain directly — but rarely the final decision-maker.
- **Director of Growth / VP Growth** — Cares about pipeline attribution and cross-channel visibility; usually the decision-maker on tooling.
- **Content Lead / Head of Content** — Needs brand consistency and content performance data; secondary buyer.
- **SEO Manager** — Day-to-day practitioner who will evaluate workflow usability and data access.
- **Marketing Operations Manager** — Cares about data integration and reporting infrastructure; technical evaluator.

**Buying dynamics:** The champion (Head of SEO) needs to be armed with internal justification material to sell upward. There's often a technically capable person on the team (engineering background, writes scripts, uses APIs) who becomes the technical evaluator — their assessment of the architecture can accelerate or block adoption.

---

## Discovery Intel

> _Log insights from conversations, interviews, replies, DMs, etc._

| Date | Source | Insight |
|------|--------|---------|
| Pre-launch | Field conversations | They come in already knowing they need automation — the question isn't "should we?" but "how do we do it reliably?" Different selling motion than convincing skeptics. |
| Pre-launch | Field conversations | LinkedIn content about AI search automation catches this audience. They recognize the gap between what they've tried to build and what purpose-built infrastructure can do. |
| Pre-launch | Field conversations | Competitive pressure is a real driver. They see peers and competitors automating and feel urgency to catch up. |
| Pre-launch | Field conversations | The expanded search surface (more engines, same team) resonates strongly as a pain point. |
| Pre-launch | Field conversations | Manual everything — the full workflow from wireframe to production has no automation in the loop. Even technical SEO (audits, schema checks, internal linking) is manual. |
| Pre-launch | Field conversations | Hallucination on semantically similar data is a known pain. Entity-based SEO approaches (common in specialized verticals) make it worse because AI confuses closely related concepts. |
| Pre-launch | Field conversations | Even "no-code" tools like n8n require API auth, node chaining, and error handling that's too heavy for marketing teams. |
| Pre-launch | Field conversations | Team adoption is a change management challenge, not just a tooling one. The Head of SEO may be bought in, but educating a 10+ person team is hard. |
| Pre-launch | Field conversations | Content quality anxiety — teams in regulated or trust-dependent verticals worry about AI output quality and potential AI penalties. They need to see that automation assists research and analysis, not that it replaces human judgment. |

---

## Objections Heard

> _Track objections and how you've responded._

| Objection | Response / Reframe |
|-----------|--------------------|
| | |

---

## Open Questions

> _Things you still want to validate about this ICP._

- [ ] How are Series B SEO leads currently presenting AI search impact to their VPs / CFO?
- [ ] Is LLM integration a discovery feature or something they've been looking for?
- [ ] What does "pipeline attribution" actually look like in their current stack — what tools are they using?
- [ ] How much are they spending on separate SEO tool subscriptions? Is consolidation a meaningful value driver?
- [ ] Are they already using Claude Code or ChatGPT Codex? Would thin MCP interoperability be an immediate hook?
- [ ] Would pre-built workflows from the marketplace accelerate adoption vs. having to build custom workflows?

---

_Last synced with base investment document: March 2026_
