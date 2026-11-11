# Canonical

> **This is the source of truth for everything about AEOxoxo.**
>
> Decks, sales calls, marketing copy, hiring conversations and every other downstream artifact derive from these files — never the other way around. If a fact in a deck contradicts what's here, this directory wins. If an important fact isn't here yet, update the canonical file first, then propagate.

**Naming, in one line:** **AEOxoxo** (`aeoxoxo.ai`) is the product and the public brand. **Swayful** (`swayful.ai`) is the company — an Indian private limited with a US subsidiary, currently being formed. See [`company.md`](company.md).

---

## Files

Six files, one per domain. Each is self-contained and cross-references the others rather than duplicating them.

| File | What's in it |
|------|--------------|
| [`company.md`](company.md) | The two names and what each means, the Swayful structure, the company's address and phone, the formation checklist, standing vendor relationships, and the corporate open decisions |
| [`team.md`](team.md) | The three cofounders, who owns what, departures, and the equity/IP open decisions |
| [`product.md`](product.md) | **High-level only.** What AEOxoxo is, what we sell, the four-step product, the honest position on causes, the seven platform entities, how it's operated, language rules. Links out to the full specs |
| [`engineering.md`](engineering.md) | The nine-system substrate, the `aeo` API layer and its data model, deliberate constraints, and the recorded gaps |
| [`market.md`](market.md) | AI-search inflection data, traffic and conversion shift, the competitor landscape as sourced fact, VC validation, defensibility |
| [`gtm.md`](gtm.md) | Current commercial state and pilot constraints, legacy accounts, the open ICP question and its promotion criteria, sales craft, objection inventory, marketing channels |

---

## The full product definition lives outside canonical

Two documents in [`../product/`](../product/) define the product in detail. They are authoritative and `product.md` links to them rather than restating them:

- **`product/framework.md`** — the classification vocabulary: three axes, every value, the rules for assigning them. Answers *what is this question?*
- **`product/aeo-product-spec.md`** — the v1 spec: measurement, diagnosis, the causes list, pilot constraints, and the evidence base with its source tiers. Answers *what do we do about it?*

The division is strict so neither has to be maintained twice. The framework changes when the taxonomy is wrong; the spec changes when the product is wrong.

Other non-canonical material — transcripts, deck HTML, landing pages, templates, tooling — lives outside `canonical/` and is referenced by path from canonical files. Today that is `product/` and a scatter of loose files at the repo root; those have not been organised and this README does not pretend they have been.

---

## How to maintain this

- **Update canonical first.** Change the fact here, then propagate to decks, pages and templates.
- **One topic, one home.** Substrate belongs in `engineering.md`. Bios belong in `team.md`. Cross-reference; don't duplicate.
- **Keep `product.md` descriptive and high-level.** Detail goes in `product/`. Claims about who it's for and why it wins are positioning and belong in neither until positioning is rebuilt.
- **Mark open decisions explicitly.** Every file ends with an *Open decisions* section listing what is genuinely undecided. An honest gap is more useful than an invented answer — and a file built on a foundation that was itself never settled is worse than no file.
- **Don't restore stale material.** Positioning, pricing and the ICP have no canonical home right now, by decision. Give them one when they exist, not before.
- **Cite the file, not the artifact.** When briefing a cofounder, a contractor or an LLM, point at the path. Decks come and go.

---

## What is unresolved right now

Pulled up from the individual files, because these block work elsewhere:

1. **Swayful is not yet formed**, and the India / US split is undecided. Nothing about the corporate structure is settled until it is. → [`company.md`](company.md)
2. **No equity split and no IP assignment for any cofounder.** Everything built today is assigned to no entity. → [`team.md`](team.md)
3. **No validated ICP.** The spec's pilot profile is a pilot constraint, not an ICP claim. → `gtm.md`
4. **No pricing.** → `gtm.md`
5. **No repos, hosting or deploy path recorded** for any of the nine engineering systems. → `engineering.md`
6. **Market sizing must be re-derived** against the AEO market rather than the SEO one. → `market.md`

---

_Last updated: 2026-09-01 — rebuilt for the AEOxoxo direction. Prior canonical files are in git history._
