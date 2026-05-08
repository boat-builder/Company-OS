# Canonical

> **This is the source of truth for everything about Berlin.**
>
> Investor decks, sales calls, marketing copy, hiring conversations, and any other downstream artifact should derive from these files — never the other way around. If you find a fact in a deck or a doc that contradicts what's here, this directory wins. If you find an important fact that *isn't* here yet, update the canonical file first, then propagate.

---

## Files

One `.md` per topical domain. Each file is self-contained and cross-references the others where relevant.

| File | What's in it |
|------|--------------|
| [`company.md`](company.md) | Legal entity, governance, banking, registered agent, agreements on file, annual compliance, C-Corp conversion plan |
| [`product.md`](product.md) | What Berlin is, three-pillar framework, two packaged offerings, capability surfaces, Tools layer, engineering moat, full pricing (Berlin + FDM scope ladder + Berlin for Agencies channel discount band) |
| [`customers.md`](customers.md) | Primary ICP (traditional businesses), 6-cell discovery grid, 6 archetype taxonomy, cell hypotheses, promotion criteria, India market reality |
| [`team.md`](team.md) | Founder bios (Sherin + Rhea), full FDM model, operator ratios, May 2026 partner-agency setup, first FDM hire spec, hiring plan |
| [`sales.md`](sales.md) | Sales positioning, qualification framework, call structure, persona-specific approaches, objection handling, closing motion, pricing discipline, learning log |
| [`marketing.md`](marketing.md) | Content principles, audience definition, content goals, funnel, execution, channels, customer-facing language discipline |
| [`market.md`](market.md) | TAM/SAM/SOM, AEO/GEO inflection, traffic shift, labor-addressable reframing, competitor landscape (4 buckets), why-now narrative, VC validation |
| [`finance.md`](finance.md) | Current state, revenue model, traction, flagship case, projections, cash flow, round structure, use of funds, cap table, risks |

---

## What lives outside canonical

The existing top-level folders (`team/`, `marketing/`, `sales/`, `customers/`, `product/`, `finance/`, `legal/`) keep **non-canonical artifacts** — assets, templates, transcripts, deck HTML, recruitment posters, ephemeral state — referenced by name from canonical files. Examples:

- `team/Forward-Deployed-SEO-JD.md` — public JD (asset; canonical role spec is in `team.md`)
- `team/linkedin_poster.html`, `team/whatsapp_poster.html` — recruitment posters
- `marketing/partners-page/` — partner-channel landing pages
- `sales/transcripts/` — raw call transcripts
- `tools/closex/` — Close CRM CLI (sibling to `tools/calx/` and `tools/stripex/`)
- `sales/llm-instructions.prompt` — LLM prompt for sales-call assist
- `sales/pipeline.md` — ephemeral active-deal tracker
- `finance/funding-page/index.html` — investor-facing HTML deck
- `product/berlin-market-research-final.md` — detailed source-cited market data appendix backing `market.md`

---

## What's deletable

After this canonical/ directory was built, several previously-de-facto-canonical files become **derivative** — their content fully lives here now. See the audit at the bottom of this README before deleting anything. The current investor docs in particular (`finance/base-investment-document.md`, `finance/investor-deck-plan.md`) are now derivative and can be regenerated from canonical/ rather than maintained in parallel.

---

## How to maintain this

- **Update canonical first.** When a fact changes, change the relevant file here. Then propagate to derivative artifacts (decks, landing pages, outreach templates).
- **One topic, one home.** Pricing belongs in `product.md`. Founder bio belongs in `team.md`. Don't duplicate facts across canonical files — cross-reference.
- **Cite the file, not the artifact.** When briefing yourself, the FDM team, contractors, or LLMs, point them at the canonical file by path. Decks come and go; canonical persists.

---

_Created: 2026-05-07_
_Last updated: 2026-05-08 — `closecrm` moved from `sales/` to `tools/closex/`._
