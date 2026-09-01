# Go-to-Market

> Canonical reference for how AEOxoxo sells and markets: what we are selling right now, the pilot constraints, the open ICP question, sales craft, the objection inventory, marketing channels, and the decisions still outstanding.
>
> What the product is → [`product.md`](product.md). Category and competitors → [`market.md`](market.md). Build order and data → [`engineering.md`](engineering.md). Who does what → [`team.md`](team.md). The full product definition — the bucket map, the symptom/cause split, the pilot constraints and the evidence base — is [`product/aeo-product-spec.md`](../product/aeo-product-spec.md), and it is the authority wherever this file summarises it.

---

## Current commercial state

**AEOxoxo** (aeoxoxo.ai) is the product and the public-facing brand. Names and their status are defined once in [`company.md`](company.md) → *Names and what each one means*. Use AEOxoxo in every external context.

What we sell today is one thing: an **AEO measurement and diagnosis product, delivered as an analyst-delivered consultation report**. We measure whether a brand gets recommended when a potential customer asks an AI assistant a question, diagnose why it is or is not happening, and hand over a ranked register of actions. The report is delivered in a client account on our platform, as a live page rather than a PDF attachment — we need the account anyway for Search Console and analytics permissions.

We do not place people inside the client's team. The analyst work happens on our side; the client receives findings, diagnosis and a work order.

The commercial sequence for the report is fixed by the spec: **symptoms earn the meeting, process justifies the price inside it.** See *Commercial guidance from the spec* below.

---

## The pilot

The first engagements are a deliberately constrained pilot. The constraints exist to learn, not to demonstrate maximum capability, and they are tight on purpose. Canonical detail in [`product/aeo-product-spec.md`](../product/aeo-product-spec.md) Part 3.

- **Target 4–5 pilots.** The signal comes from these; anything beyond is a bonus data point.
- **Ideal profile: B2B SaaS, roughly $5–10M ARR.** Take smaller companies if offered, but the learning comes from the target profile. **This is a pilot constraint, not an ICP** — see the next section.
- **One pilot per client.** If they want a second report, they pay, even at a subsidised rate. If they see enough value to ask, they see enough value to pay, and we should ask.
- **Do not rush.** Take the time to do it properly.

Scope caps per pilot: **one topic**; **~100 query clusters** (the unit a person reviews and the client approves — roughly half a day to a day of analyst time); **~500 prompts** (each cluster expands to about five phrasings — this is the number that drives cost); **Google AI Mode only**; **one run per prompt**; competitor coverage across all buckets, cost permitting; field watch **baseline only**. When someone says "we're doing 100" in a meeting, they mean clusters.

Two of these caps have honesty consequences in front of a client. **One run per prompt is below our own ~10-run methodology target, so a single run must not be described as a stable measurement.** The field watch produces nothing until the second run, so **do not sell month one on the competitive activity feed** — take the baseline and claim nothing from it.

### What we need from the client at onboarding

| What | Why | How to get it |
|---|---|---|
| Business goals | They become the topics; everything hangs off them | Questionnaire and onboarding call. We can guess from the website, but confirm. |
| Positioning — what they want to be known for | The benchmark for brand-narrative risk. Without it we cannot say whether the AI's story about them is wrong. | Questionnaire. |
| Existing keyword/prompt list, if any | Removes most of the manual selection work | Ask early — it changes the effort estimate. |
| Search Console and Bing Webmaster access | AI-surface impressions and cited pages; the AI-specific data is not exposed via API | Either add our account, or they export and upload. **Do the export live on the onboarding call** with whoever holds access — it is buried in the interface, and handling it by email turns into a multi-day loop. |

Where a client already has a keyword list — most clients with an SEO agency do — the added value is telling them what is missing, wrong or overweighted in it.

---

## Legacy accounts

Three accounts predate the current product. They are winding down, they are **not evidence for an ICP**, and they must **not** be used to anchor pricing on the report product.

- **Reach Psych** (reachpsych.com) — $499/mo.
- **Csuite.so** — $499/mo.
- **miniOrange** (miniorange.com) — in technical/compliance due diligence.

---

## ICP — open

**There is no validated ICP.** Nothing in the current evidence base supports one, and the pilot profile above is a scoping constraint chosen to make the first engagements learnable — it must not be quietly promoted into an ICP because it is the only profile written down.

**Resist writing full personas before the data is in.** A plausible-sounding persona written now would be fiction, and it would then get cited as if it were a finding.

### What we need to discover

- **Buyer.** Who actually buys a diagnostic report — and who holds the budget line it comes out of.
- **Stage / size.** Where the pain is sharpest and willingness-to-pay is clearest.
- **Trigger.** What specifically makes someone decide they need this now rather than later.
- **Sub-vertical.** Which kind of company has the densest, most repeatable version of the pain.
- **Geography.** Where this buyer clusters and converts.

### Promotion criteria — hypothesis → validated ICP

**This gate is an inherited rule of thumb, not settled policy.** It has never been tested against our own deals. Treat it as a heuristic for when to stop calling the ICP a hypothesis, and replace it with something evidence-backed once the pilots have run.

Hold any ICP definition lightly until the evidence log shows a consistent pattern across several qualified conversations — the number carried forward is five, and it is a rule of thumb rather than a threshold we can defend — including:

- a repeatable, specific trigger event;
- a clear willingness-to-pay signal;
- a named role that holds the budget;
- at least one sub-parameter (sub-vertical, stage, geography, buyer title) that narrows the hypothesis further.

Until all four hold together, the ICP stays open and every deal is treated as both a sale and a discovery conversation.

---

## Sales craft

Direction-agnostic mechanics. These survive changes of product and ICP; the specifics they get filled with do not.

### Call structure

**Pre-call prep (5 min).** LinkedIn and company site review. Form a hypothesis about their current state and their trigger before the call, so discovery confirms or breaks it rather than starting cold.

**1. Opening and rapport (3–5 min).** Thank them, confirm time, light rapport. If they open with "tell me about the product" or "what's the price," redirect with permission:

> "Happy to get to that — let me ask a few things first so the answer's relevant to your situation rather than generic. Fair?"

**2. Discovery (12–15 min).** Run the phases below in order.

**3. Positioning and walkthrough (8–10 min).** Lead with outcomes, not features, and anchor everything on what the prospect just told you. Show findings of the kind they would get, tied to the pain they named. Check comprehension every 2–3 minutes — "does this map to how you'd use it?" — and simplify if they are lost.

**4. Close (3–5 min).** See the close taxonomy below.

### What good discovery looks like

- **Phase 1 — Current state (4 min).** The business, their role, what they do about search and AI answers today.
- **Phase 2 — Pain and trigger (4 min).** What hurts, what changed, why now.
- **Phase 3 — Fit (3 min).** Map the current landscape — in-house, freelancer, agency, tools — and what they spend on it.
- **Phase 4 — Decision mapping (2 min).** Who signs, what the process is, what the timeline is.
- **Phase 5 — Success criteria (2 min).** What "working" looks like at 30 and 90 days.

**Red flags — when to disqualify:** zero current spend and no trigger; a proxy buyer with no path to the real decision-maker; unrealistic expectations ("#1 in two weeks"); a prospect who wants execution delivered rather than measurement and diagnosis, and will not hear the difference.

### Why now — the trigger framework

> "What's making you look at this now rather than six months ago or six months from now?"

**Good triggers:** AI search anxiety · a traffic or ranking drop, often AI-overview related · a competitor visibly winning the answers · an exec or board question about AI answers that nobody internally can answer · funding round with growth targets · burnt trust in a current supplier.

The first two are the leading triggers to test: a diagnostic report is the direct answer to "something is happening in AI answers and I don't know what."

**Bad triggers:** "just exploring" · "someone mentioned you" · "curious about AI."

**No trigger, no close.** This is the single most reliable qualification signal we have.

### Budget sanity

> "What are you spending on SEO today, across tools, freelancers, and agency or in-house?"

Ask it plainly and early. It is the cleanest phrasing we have found; it surfaces the budget line the report would come out of, and it is diagnostic even when the answer is zero.

### Decision authority

> "If this looks like a fit, who needs to be involved to say yes?"

Anyone who is not the budget holder is a proxy. Do not accept a proxy buyer, and never let one carry the pitch into the decision-maker's office without you — insert yourself into that next conversation.

### Closes

**Standard close (preferred).** Name a specific start date, name the prerequisites they must supply before kickoff (see *What we need from the client*), name what they will see and when, and offer a binary choice of dates.

**Proof-of-value close (for the skeptical but qualified).** One narrow, scoped piece of real analysis on their actual property, delivered against a booked follow-up.

**Scope-creep guard, non-negotiable:** always book the follow-up *before* doing the work; one topic, one artefact, no expansion once agreed; and keep it rare — it spends analyst time nobody is paying for. A proof-of-value that grows into a free pilot is a lost deal that has not admitted it yet.

**What makes a close strong:** a specific start date, not "soon" · clear prerequisites · binary scheduling ("Tuesday or Wednesday?") · agreed success metrics so there is no ambiguity at the review.

**Weak closes to avoid:** "I'll send you an email" · "let me know when you're ready" · "sounds good, talk soon" · letting the prospect defer to an internal meeting you are not in.

### Price pushback

Pricing itself is undecided (see *Open decisions*). The ladder below is the discipline, not a number:

1. **Don't discount casually.** A discount given to end an uncomfortable moment tells the prospect the number was invented.
2. **Frame the number against the value of the decision it informs**, never against what it costs us to produce.
3. **Connect to a specific outcome they named** in discovery, not a generic one.
4. **Confirm fit before negotiating.** If they are not a fit, price is a symptom and not the issue.

**Never say:**

- "We're still figuring out pricing."
- "We're early-stage so…"
- "It's expensive for us to run."
- Anything else that implies uncertainty about the number.

The internal honesty about how much is undecided is real and stays internal; it does not belong in the price conversation.

A planned price increase is a legitimate urgency lever *only if it is genuinely planned*, and only paired with a CTA. There is nothing to plan against until pricing is set.

### Critical mistakes

**Discovery.** Don't skip qualification. Don't skip budget. Don't skip the trigger. Don't accept a proxy buyer.

**Walkthrough.** Don't over-explain the architecture — the prospect cares about outcomes, not the pipeline. Don't lead with features. Don't volunteer incompleteness; if asked directly about a gap, be honest, but don't raise it unprompted. Don't peer-talk technology with technical prospects — with a technical buyer it is easy and fatal to slide into a technology discussion; stay on business outcomes. Don't lecture: keep any explanation to one or two sentences, then pivot to the outcome. Don't talk about our internal journey — prospects do not care about our experiments or our history.

**Pricing.** Don't hedge: state the number, connect it to value, stop. Don't justify price with our costs.

**Closing.** Don't close vaguely. Don't let a prospect defer to an internal meeting without you. Don't end a call without booking the next action on it. Don't give vague timelines — never "compound effects"; say what happens by when.

---

## Objections

This is an **inventory of the questions prospects actually raise**, kept because prospect contact is the only evidence of its kind we have. **The answers must be rebuilt against the current product** — the report, its constraints, and the honesty rules below. Do not carry forward answers written for an execution product.

**These are anticipated, not observed.** No objection here is attributed to a named prospect or a dated call. Treat the list as a preparation checklist, not as field data, and log the real ones as they arrive with the prospect and date attached.

Positioning:

- "How is this different from hiring an SEO agency?"
- "Why wouldn't I just hire someone in-house?"
- "What about the tools I already pay for?"
- "Isn't this just a wrapper on an LLM?"
- "How do I know the output quality is any good?"
- "We have an agency contract until [date]."

Commercial:

- Pricing pushback of every kind.
- "Can I just try it and cancel?"
- "Do you have a free trial?"
- "How do you know the analysis is representative?" — answer inside the pilot's one-run-per-prompt honesty constraint stated under *The pilot*. Do not overstate it.
- "We prefer human-only work."

Some of these presuppose an execution vendor and may not survive contact with a diagnostic product at all. That is itself worth learning: which objections disappear is a signal about how the product is being understood.

---

## Commercial guidance from the spec

Rules from [`product/aeo-product-spec.md`](../product/aeo-product-spec.md), binding on anything client-facing.

- **Symptoms earn the meeting; process justifies the price inside it.** Lead with outcomes — what the AI says about them, where they are recommended and where a competitor is, which of their pages the engines can and cannot read, what their competitors changed last month. **Save the pipeline description for the second conversation.**
- **Label attribution honestly.** Branded search and direct-traffic movement are correlation, not attribution.
- Client-facing wording — *prompts* not *keywords*, capability never method, symptoms as findings and causes as diagnosis — is owned by [`product.md`](product.md) → *Language rules*. It is not restated here; follow it there.

---

## Marketing channels

Inherited assets, with their real status.

- **r/agent_seo (Reddit)** — our own subreddit, ~4,400 members. Being moved or renamed under the AEOxoxo brand; the transfer is not done and is an open decision.
- **"Agentic AI for SEO" micro-book** — lead magnet, reference asset, credibility builder. Also awaiting a decision on whether it transfers under the new brand and product.
- **Meetup series** for SEO professionals — in-person, with heavy live demos.
- **LinkedIn** — the inherited primary founder-led channel. The distribution model is unresolved now that there are three cofounders rather than one: whether the funnel becomes three parallel voices, one designated voice, or a brand account is unanswered. See *Open decisions*.
- **Outbound** — LinkedIn primary, email secondary, X tertiary. An inherited priority order, untested; no evidence has been gathered for the ranking.

### Adjacent programmes

- **Micro-influencer programme.** Practitioners demo the product on their own channels in exchange for free access plus affiliate commission on referrals. Mechanics are sound — authentic output demos beat polished ads, because practitioners trust practitioners — but the programme needs an outcome check before it gets more investment.
- **Autonomous affiliate site (proof of concept).** One affiliate site run end-to-end by our own system, with roughly a two-month horizon to initial results, then published as a public case study — verifiable proof rather than a claim. **Needs an outcome check:** the timeline has run, and whether it produced anything is an open question.

### Language discipline

**In external content and prospect-facing copy, do not use internal jargon — speak in the audience's own role and industry terms.** Internal shorthand for segments and models never appears externally. Client-facing wording rules live in [`product.md`](product.md) → *Language rules*.

**A translation table does not exist yet.** Build one against the current product's actual terms and the spec's language rules — *prompts* not *keywords*; capability, never method.

One translation is genuinely unresolved: **is "AEO" public-facing vocabulary?** The brand is literally AEOxoxo, and the plain-language alternative for non-technical audiences is "AI search" or "answer engines." Both cannot hold. See *Open decisions*.

---

## Open decisions

1. **ICP.** No validated ICP exists. The pilot profile is a constraint, not an answer. Gated by the promotion criteria above.
2. **Pricing.** Undecided. No number is carried forward, and the legacy accounts do not anchor it.
3. **Is "AEO" client-facing vocabulary?** The brand argues yes; plain-language discipline argues for "AI search" or "answer engines" with non-technical audiences. Decide it once, then build the translation table around the decision.
4. **Do the subreddit and the micro-book transfer** to AEOxoxo, and in what form?
5. **Who owns sales** among Sherin Thomas, Omar Marks and Nitin Venugopal — including whose voice carries the LinkedIn funnel. See [`team.md`](team.md).
6. **The affiliate-site PoC outcome.** Did it produce a publishable result? If not, it either gets a deadline or gets stopped.

---

_Last updated: 2026-09-01_
