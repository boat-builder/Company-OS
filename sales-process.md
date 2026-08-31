# Our Sales Process, Explained From Scratch

*A plain-English walkthrough for someone who has never done sales and has never seen our
system. By the end you'll know exactly what happens to a lead from the moment we first hear
about a company to the moment we win (or drop) the deal — and every single thing we write
down about them along the way.*

***

## 0. First, the 30-second mental model

We sell **Berlin** — an **AI SEO/AEO platform**. In normal words: companies need to show up
when people search Google ("SEO") and now also when people ask AI assistants like ChatGPT
("AEO" = *Answer Engine Optimization*). Traditionally a company hires an SEO agency or builds
an in-house SEO team to do this. Berlin replaces that — it's software that does the work. So we
make money by **taking over the SEO/content budget a company already spends**, not by asking
for new budget.

That one fact drives everything below, because it tells us **who is a good customer**:

* ✅ A company that **uses** SEO to grow itself → potential customer.

* ❌ A company that **builds or sells** SEO/AEO tools to *others* → that's a **competitor**, we
  never pitch them.

Everything we do is about finding companies of the first kind, talking to the right person
there, and walking them toward becoming a paying customer.

### The cast of characters (the words we'll use constantly)

| Word            | What it really means                                                                                       |
| :-------------- | :--------------------------------------------------------------------------------------------------------- |
| **Lead**        | A **company** we might sell to. (Important: a lead is a *company*, not a person.)                          |
| **Contact**     | A **person** at that company we can message (their name, title, LinkedIn, email…).                         |
| **Status**      | A label on the lead saying where it is in our funnel (e.g. *Qualified*, *Engaged*, *Customer*).            |
| **Touch**       | One **attempt to reach out** to a lead (a LinkedIn message, an email, a like…). Logged *after* it happens. |
| **Task**        | A **reminder to do something in the future** ("follow up Friday").                                         |
| **Opportunity** | An actual **deal** we're trying to close, once a lead is genuinely interested.                             |
| **CRM**         | The database where all of this lives. Ours is a product called **Close**.                                  |
| **BDR**         | "Business Development Rep" — the human who actually sends the messages. (Often just *you*.)                |
| **ICP**         | "Ideal Customer Profile" — our written description of our dream customer, used to judge fit.               |

### The tools

Everything is driven by a command-line tool called **`dogfu`** (it talks to our data sources
and to the Close CRM), plus a set of **skills** that tell the AI assistant how to use `dogfu`
correctly. You don't need to memorize commands — but throughout this doc I'll show the real
`dogfu` command behind each step so you can see what's happening under the hood.

The skills, at a glance:

| Skill             | Role                                                                          | Writes to CRM?             |
| :---------------- | :---------------------------------------------------------------------------- | :------------------------- |
| **lead-research** | Phase 1 — research & qualify a new company                                    | ✅                          |
| **lead-touch**    | Phase 2 — run the cold outreach cadence                                       | ✅                          |
| **lead-engage**   | Phase 3 — work the live deal to a close                                       | ✅                          |
| **lead-worklist** | The daily "what do I work on today?" list, across *all* phases                | ❌ read-only                |
| **crm-cleanup**   | Health audit — finds leads/tasks that fell through the cracks                 | ❌ read-only                |
| **first-audit**   | Produces a free SEO/AEO audit report to use as a first-touch asset            | (writes a report, not CRM) |
| **berlin-theme**  | Brand styling for any sales collateral you design (not part of the lead flow) | —                          |

***

## 1. The whole journey in one picture

A company moves through **three phases**, each handled by its own skill. Two more skills run
*across* all phases without changing anything: **lead-worklist** (your daily to-do list) and
**crm-cleanup** (the "janitor" that checks for mistakes).

```
                          ┌───────────────────────────────────────────────┐
                          │   PHASE 1: RESEARCH   (skill: lead-research)    │
   A cold target  ─────▶  │   Discover → Qualify → Enrich → save to CRM     │
 (a name / domain /       │   "Is this company worth talking to at all?"    │
  LinkedIn link)          └───────────────────────────────────────────────┘
                                              │
                   ┌──────────────────────────┼──────────────────────────┐
                   ▼                           ▼                          ▼
              Good fit                    Not a fit               A competitor
           status: Qualified           status: Bad Fit          status: Bad Fit
                   │                    (saved, never            ("do not contact")
                   │                     chased — STOP)               STOP
                   ▼
   ┌───────────────────────────────────────────────┐
   │   PHASE 2: COLD OUTREACH  (skill: lead-touch)   │
   │   Reach out → follow up → follow up → …         │
   │   "Keep nudging until they answer or we quit."  │
   └───────────────────────────────────────────────┘
             │                         │
        They reply              We give up
     status: Engaged          status: Bad Fit /
             │                 Not Interested  (STOP)
             ▼
   ┌───────────────────────────────────────────────┐        ┌──────────────────────┐
   │   PHASE 3: WORK THE DEAL  (skill: lead-engage)  │ ◀──────│  HOT / INBOUND LEAD   │
   │   Discovery → Trial → Proposal → Won / Lost     │        │  (they came to us)    │
   │   "Turn interest into a signed customer."        │        │  jumps straight here  │
   └───────────────────────────────────────────────┘        └──────────────────────┘
             │                         │
        Deal won                  Deal lost
    status: Customer 🎉      status: Not Interested /
                                 Bad Fit / Canceled

   ( Running read-only over ALL of the above:
       • lead-worklist — the unified "what do I work on today?" list (cold + warm + inbound)
       • crm-cleanup   — a health check that finds leads which fell through the cracks
     Neither ever changes anything. )
```

> **"Cold" vs "hot" in one line:** a **cold** lead is one *we* found and who has never heard of
> us — it starts at Phase 1 and has to be chased. A **hot / inbound** lead is one that *came to
> us* — it skips Phases 1–2 and jumps straight into Phase 3 (see §6).

***

## 2. The two "tracks" you must never confuse

This is the single most important idea in our system, so we'll get it out of the way early.
Every lead is described by **two independent things at once**:

1. **Status** — the *funnel label*. A **human judgment** of where the relationship stands.
   Examples: *Potential, Qualified, Engaged, Customer, Bad Fit*. A human sets this.
2. **Outreach / deal state** — the *sequence position*. **Machine-tracked** bookkeeping of
   "where are we in the back-and-forth" (which follow-up is next, when it's due, etc.).

They move **independently**. Recording that you sent a follow-up advances the *outreach state*
but does **not** change the *status*. Changing the status doesn't touch the outreach state. The
only moments they deliberately move together are "they replied" and "we gave up."

Why two tracks? Because "what do I think of this lead?" (status) and "what's the next physical
action and when?" (state) are genuinely different questions, and keeping them separate is what
stops leads from getting lost.

### The funnel statuses (the lifecycle labels)

These are account-specific labels in Close. A lead has exactly **one** at a time:

| Status             | Meaning                                                                               |
| :----------------- | :------------------------------------------------------------------------------------ |
| **Potential**      | We've recorded the company but haven't decided / worked it yet ("maybe").             |
| **Qualified**      | Researched and judged a **good fit** — ready to be contacted.                         |
| **Engaged**        | The lead **replied / is in a live conversation**. Cold chasing stops here.            |
| **Customer**       | They **signed**. 🎉 (Set only when a deal is *Won*.)                                  |
| **Bad Fit**        | Not a fit (or a competitor). Kept on file so we don't waste time re-researching them. |
| **Not Interested** | They (or we) ended it — a real "no."                                                  |
| **Canceled**       | A former customer who churned.                                                        |
| **DNC**            | "Do Not Contact."                                                                     |

> ⚠️ We **never hardcode** the internal IDs for these — labels can differ per account, so the
> tools always look them up live with `dogfu crm status list`.

***

## 3. Phase 1 — Research: "Is this company worth talking to?"

**Skill:** `lead-research`. **Goal:** take a sparse hint about a company and turn it into a
fully-researched record in the CRM, with a verdict on whether they're a fit.

You start with almost nothing — maybe just a company name, a website, a person's name, or a
LinkedIn/X link. The research runs in **four stages**. The first two always happen; the third
only happens if the company looks promising (because it costs money); the fourth always
happens.

> **Cost discipline is a real theme here.** Many of the data lookups hit paid services. So we
> always pull the *cheap, telling* signals first, and only spend on the expensive ones once a
> company already looks worth it.

### Stage A — Discover ("Who are they, and who do we talk to?")

We figure out the basics:

* **A1 — Resolve the company** to one official website / root domain. Everything later keys off
  this domain. *(`dogfu google search --query "<name> official site"`)*

* **A2 — Read their own website** (homepage, About, product, pricing, blog) to understand
  **what they do, who they sell to, what region/language, and their core problem.** This is
  done with a normal web-fetch, and it's the foundation for every later judgment.

* **A3 — Map their social footprint** — the company's LinkedIn and X/Twitter pages.
  *(`dogfu linkedin companies`,* *`dogfu x profiles`)*

* **A4 — Find the decision-maker** — the person who owns marketing/SEO. Usually a founder or a
  head of growth/marketing.

* **A5 — Find that person's personal LinkedIn and X profiles** and save the links.

**What we capture and keep no matter what:** the company's LinkedIn + X links, and **every
person we find with their LinkedIn + X links.** These are the handles we'll message later, so we
keep them even if the company turns out to be a bad fit.

### Stage B — Qualify ("Are they a fit, and how good is their SEO already?")

This is the heart of research: we judge the company against our **ICP** (Ideal Customer
Profile — our written description of a dream customer; see §7) and build a profile of how
they're doing on SEO/AEO today.

**B0 — Competitor gate (runs first; cheapest "no").** Before spending any money: do they *use*
SEO to grow, or do they *build/sell* SEO tools to others? If they sell SEO/AEO capability —
including broader "AI agent" platforms that produce SEO outcomes — they're a **competitor**:
stop immediately, mark them excluded, and skip to saving the record. (We're careful **not to
over-exclude**: a normal SaaS doing its own SEO is exactly who we want.)

If they pass the gate, we profile them, **cheapest signals first**, stopping early if it's
obviously not a fit:

| Phase                             | Question it answers                             | Roughly how                                                                                     |
| :-------------------------------- | :---------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| **B1 — Footprint & scale**        | How much content do they have?                  | count of indexed pages; check for `sitemap.xml` and `llms.txt`                                  |
| **B2 — Organic outcomes**         | Is their SEO actually *working*?                | est. monthly traffic, traffic value, # of ranking keywords (`dogfu seo domain-overview`)        |
| **B3 — Momentum**                 | Are they investing now, or coasting?            | traffic/keyword trend over time (`dogfu seo historical-rank-overview`)                          |
| **B4 — Ranking quality**          | Are they ranking for valuable, non-brand terms? | top keywords, positions, branded vs not (`dogfu seo ranked-keywords`)                           |
| **B5 — Technical health & stack** | Is the site healthy and well-tooled?            | Core Web Vitals + detected tech (`dogfu seo lighthouse`, `dogfu seo technologies`)              |
| **B6 — Competitive gap**          | How do they compare to rivals?                  | benchmark vs competitors we *discover* (`dogfu seo bulk-traffic-estimation`)                    |
| **B7 — AEO visibility**           | Do AI assistants cite them?                     | do they appear in ChatGPT / Google AI answers? (`dogfu chatgpt search`, `dogfu google ai-mode`) |
| **B8 — Buyer literacy**           | Does the decision-maker "get" SEO/AEO?          | quick scan of their public posts                                                                |

> **Key principle: we judge** ***relatively***\*\*, not by fixed numbers.\*\* "Big" or "small" only makes
> sense compared to that company's segment and competitors. So we always express things as
> ratios ("30% of the market leader's traffic") rather than raw numbers, because the underlying
> data is just *modeled estimates*.

**The verdict.** We combine all of that into one of four outcomes:

* **Strong fit** → looks like our bullseye customer.

* **Partial fit** → close, with a caveat (slightly wrong size, adjacent industry, etc.).

* **Weak fit** → not in our ICP.

* **Excluded (competitor)** → from the B0 gate; overrides everything.

### Stage C — Enrich ("Get the contact details — but only if they're a fit")

This stage **only runs for strong/partial fits**, because it spends credits. Here we pull:

* **Firmographics from Apollo** — estimated **revenue, employee count, marketing-team size,
  funding** — the size/money facts that SEO data can't tell us.
  *(`dogfu apollo org enrich --domain <d> --with-people`)*

* **A verified work email** for the 1–2 people we'll actually contact.
  *(`dogfu apollo people email`)*

* **A deep read** of the decision-maker(s) — their background and recent posts on LinkedIn/X —
  so we can write a personal message.

* **"DM hooks"** — specific, personalized openers: a recent post to comment on, a shared
  interest, the exact SEO gap we'd lead with.

### Stage D — Save to CRM ("Write everything down — fit or not")

**This always happens, even for bad fits and competitors.** The research cost real money and
effort, so none of it is thrown away. A "no" is recorded so we never accidentally re-research
the same company. Crucially, each piece of data goes **in its proper place** (not dumped in one
blob), so the CRM stays scannable:

| What we found                                                                                             | Where it's stored                                                                                         |
| :-------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| Company name, website, a 1–2 line headline summary, and the **status**                                    | the lead's native fields                                                                                  |
| **Industry, # employees, revenue, business model, # SEO pages**                                           | the five "curated" lead fields (see §8)                                                                   |
| Each **person** + their **LinkedIn/X links** + email/phone                                                | a **contact** on the lead (links go in the native URL field, so you can message them straight from Close) |
| Everything else — full profile, all the metrics, the verdict + reason, company social links, the DM hooks | a **note** on the lead                                                                                    |

**Status is set from the verdict:** strong/partial fit → **Qualified**; weak fit or competitor
→ **Bad Fit**; unsure/not-yet-worked → **Potential**.

> **End of Phase 1:** a *Qualified* lead is now ready to be contacted. A *Bad Fit* lead is
> parked forever. The research is fully saved either way.
>
> *(Under the hood: the moment a lead is set to* ***Qualified**, the system automatically
> creates its first "reach-out" reminder task, due today — so it shows up in your work queue
> and Close's own task list immediately. You don't create that first reminder by hand.)*

***

## 4. Phase 2 — Cold outreach: "Chase them until they answer or we quit"

**Skill:** `lead-touch`. This runs the **cold cadence** — the rhythm of reaching out and
following up. The crucial thing to understand: **a human (the BDR) sends every message by hand.**
The system's job is only to (a) tell you who to contact today and (b) record what you did.

### Touches: the "attempts," counted in order

A **touch** is *one attempt to reach the lead*, recorded **after** you send it. The number is
just the attempt order:

* **Reach-out** = the **first** attempt (internally "touch 0"). It can be light — a LinkedIn
  connection request, a like, or a comment — it doesn't have to be a full message.

* **Follow-up 1, 2, 3, … N** = each later attempt. **There is no limit** — a great lead can be
  nudged as many times as you want. Nothing auto-stops the chase.

**Channel** (LinkedIn / email / X / call / …) is just an **optional label** you attach to each
touch, so you can later see *how* you reached out and *which channels you haven't tried yet*.
You can also attach an optional **detail** — the actual message you sent.

### The machine-tracked outreach fields

You never set these by hand; recording a touch computes them automatically:

| Field            | Meaning                                                                                          |
| :--------------- | :----------------------------------------------------------------------------------------------- |
| `touch_stage`    | How many touches are done (0 after the reach-out, 1 after follow-up 1, …). `null` = none yet.    |
| `last_touched`   | The date of the most recent touch.                                                               |
| `next_touch_due` | When the next follow-up is due. **Empty = the lead has left the sequence** (replied or stopped). |
| `touch_channel`  | The set of channels you've tried so far.                                                         |

**The follow-up rhythm** (the "wait curve") is built in — after the reach-out wait \~3 days, then
4, then 6, then 7, then 7 days from there on. You can override any gap with `--wait-days`.

### The work queue: "Who do I act on today?"

This is the BDR's daily question, and one command answers it:

```bash
dogfu crm touch due
```

It returns **one list**, most-overdue first, with each lead tagged by its next action:

1. **Reach-outs** — Qualified leads with no touch yet ("new people to say hello to").
2. **Follow-ups** — leads whose next follow-up is due today or earlier ("people to chase"),
   showing which follow-up is next and which channels you've already tried.

(You can narrow it with `--kind reach-out` or `--kind follow-up`.) Note this is only the
**cold** queue. For the *cross-phase* to-do list — cold **plus** live deals **plus** inbound
conversations, all in one ranked list — use the **lead-worklist** skill (see §10).

### Recording what you did, and moving leads along

| What happened                     | Command                                                                | Effect                                                                                |
| :-------------------------------- | :--------------------------------------------------------------------- | :------------------------------------------------------------------------------------ |
| You sent the next touch           | `dogfu crm touch record <lead_id> [-c <channel>] [--detail "<msg>"]`   | logs the touch, stamps the date, schedules the next follow-up                         |
| They **replied / are interested** | `dogfu crm touch reply <lead_id>`                                      | **ends the chase** and moves the lead to **Engaged** — this is the handoff to Phase 3 |
| You're **giving up**              | `dogfu crm touch stop <lead_id> [--status <Bad Fit / Not Interested>]` | ends the chase; you choose the closing status                                         |

Three rules worth internalizing:

* **A reply is the only happy exit.** `reply` ends the sequence *and* sets the lead to Engaged
  automatically. That's the doorway into Phase 3.

* **Nothing ends a chase by itself.** Because there's no auto-stop, **`stop`** **is a deliberate
  action** — it's how you say "I'm done with this one." Otherwise a lead sits "due" forever.
  (Shortcut: recording a touch with `--final` logs one last nudge *and* ends the sequence in a
  single step — a combined "send and stop.")

* **We never assume a reply.** Close can't see your LinkedIn/X inbox, so the system only marks a
  reply when *you* tell it one happened.

### Touch vs Task — a subtle but important distinction

* A **touch** is the **past** ("I reached out") — a logged event / receipt.

* A **task** is the **future** ("do X by Friday") — a reminder.

There are two kinds of task:

* **Cadence task** — the *one* auto-managed "next action" reminder for a lead in the sequence.
  It's tagged `[dogfu:cadence]`, and **only the tool** creates or closes it. The very first one
  — the *reach-out* reminder — is opened automatically when the lead becomes **Qualified**; from
  then on, recording each touch closes the current one and opens the next. You must **never**
  hand-edit it — letting the tool be the single owner is what keeps everything in sync.

* **Ad-hoc task** — any other reminder you want ("send the deck Friday"). You're free to create
  these; they don't affect the outreach machinery.

> **End of Phase 2:** the lead either **replied → Engaged** (on to Phase 3) or was **stopped →
> Bad Fit / Not Interested** (done).

***

## 5. Phase 3 — Engage: "Turn interest into a signed customer"

**Skill:** `lead-engage`. This is the **warm phase** — the real deal-making after a lead engages.
The lead sits at **Engaged** for this entire phase and only flips to **Customer** if it's won.

### The core new idea: the Opportunity (the deal)

In cold outreach, the unit was a *touch*. Here, the unit is an **opportunity** — *the actual
deal you're forecasting*. It lives on the lead and carries:

* a **pipeline stage** (Discovery → Trial → Proposal → Won/Lost),

* a **value** — the recurring revenue (MRR), e.g. "\$1,500 / month",

* a **deal type** — Berlin's two engagement shapes: **Co-Pilot** or **Fully-Run**,

* a **confidence** — how likely it is to close (0–100%).

A lead usually has one open opportunity, but can have more than one (e.g. a Co-Pilot *and* a
Fully-Run deal running at once) — each tracked separately.

### The "gate": don't open a deal just because someone replied

This trips up newcomers, so it's a hard rule:

> **A reply is a conversation, not a deal.** A reply might be "who are you?" or "maybe later."

So you **don't** open an opportunity when a lead becomes Engaged. You open one **only after a
call confirms a real deal** — meaning there's a genuine *need*, a plausible *buyer*, and a
realistic *path*. That qualifying call is "the gate."

* **Before the gate** (Engaged, no opportunity yet): the only job is to *land the qualifying
  call*. You track that with a normal ad-hoc task ("book intro call").

* **At the gate** (the call confirms a deal): you **open the opportunity** at the *Discovery*
  stage, with the value and deal type you scoped.

### The pipeline (the deal's stages)

| Stage            | What it means                                                                                  | A typical next step                               |
| :--------------- | :--------------------------------------------------------------------------------------------- | :------------------------------------------------ |
| **Discovery**    | Deal just opened; scoping the need and agreeing a trial                                        | "set up the trial", "send scope"                  |
| **Trial**        | They're running a trial/POC of Berlin                                                          | "check in mid-trial", "review results on \<date>" |
| **Proposal**     | Trial worked; pricing/terms are out, awaiting a yes                                            | "follow up on proposal"                           |
| **Won** *(end)*  | Signed → set lead status to **Customer** 🎉                                                    | onboarding (not covered here)                     |
| **Lost** *(end)* | Dead → set lead status to **Not Interested / Bad Fit** (or **Canceled** if a customer churned) | —                                                 |

### The unit of work here: the "next step"

Cold leads ran on a *computed rhythm*. Live deals can't — the next move is a *human decision*
("send the proposal Friday", "wait for their board meeting Tuesday"). So each open opportunity
carries **exactly one open "next-step" task**, tagged `[dogfu:deal:<opportunity_id>]`. Same
single-owner rule as the cadence task: **only the tool manages it** (via `opportunity next`),
you never hand-edit it.

> **A live deal with no next step is a dropped ball** — the system surfaces these loudly.

### The deal work queue

```bash
dogfu crm opportunity due
```

returns the deals needing attention, most-urgent first:

1. **Due next-steps** — act now.
2. **Dropped balls** — open deals with *no* next step (surfaced loudest — set one!).
3. **Stalled deals** — no movement in 14+ days (quietly dying — nudge or re-qualify).

### Moving a deal along

| What happened              | Command                                                                                                                  |
| :------------------------- | :----------------------------------------------------------------------------------------------------------------------- |
| Call confirmed a real deal | `dogfu crm opportunity create <lead_id> --value <mrr> --period monthly --deal-type co-pilot\|fully-run --note "<scope>"` |
| They started a trial       | `dogfu crm opportunity update <opp_id> --stage trial`                                                                    |
| You sent the proposal      | `dogfu crm opportunity update <opp_id> --stage proposal`                                                                 |
| **Signed!**                | `dogfu crm opportunity win <opp_id>` then set the lead to **Customer**                                                   |
| Dead                       | `dogfu crm opportunity lose <opp_id> --reason "<why>"` then set the terminal status                                      |

> **One thing that's easy to get wrong:** `win`/`lose` only change the *deal's* status. The
> *lead's* status move (→ Customer, or → Not Interested) is a separate, deliberate step — they
> always go together so you never leave a "zombie" Engaged lead after a deal ends.

Also note: events (a call, demo, trial kickoff) are written as **notes** (the audit trail). The
deal *moving* is done with the opportunity verbs. Don't confuse "what happened" (a note) with
"the deal changed stage" (a verb).

***

## 6. The two paths: a COLD lead vs a HOT (inbound) lead

You asked specifically about cold vs hot. Here's the difference laid out:

### Cold lead (outbound — *we* found them)

They've never heard of us, so they go through the **full journey**:

```
Research (Phase 1) ─▶ Qualified ─▶ Cold cadence (Phase 2) ─▶ reply ─▶ Engaged
   ─▶ qualifying call ─▶ Opportunity (Phase 3) ─▶ Won/Lost
```

Most of our prospecting is this. It's slower and needs the chasing rhythm.

### Hot / inbound lead (*they* came to us)

Someone reached out to us (replied to a campaign, filled a form, DM'd us). They've shown intent,
so they **skip cold prospecting entirely** and are created **straight into Engaged** ("inbound
intake"):

```
Create lead as Engaged ─▶ add contact + intro-call notes
   ─▶ if the first call confirms a deal: open Opportunity ─▶ Phase 3 as usual
```

```bash
dogfu crm lead create -n "<company>" -u <url> -d "INBOUND (<channel>, <date>): <one-liner>" -s <Engaged id>
```

There's **no cold cadence and no touches** for an inbound lead — touches are a cold-only
concept. If the inbound company was never researched, we *may* run a quick `lead-research` pass
afterward to fill in the facts, but we **never make them wait** for it — the conversation comes
first.

> So in our vocabulary: **"cold" = we chase it through the cadence; "warm/hot" = it's a live
> conversation in the engage phase.** A cold lead *becomes* warm the moment it replies.

***

## 7. The ICP — how we decide "fit"

The **ICP (Ideal Customer Profile)** is our written description of a dream customer. Research
(Stage B) judges every company against it. We keep our ICPs as files; today there are two:

### ICP 1 — Founder-Led, SEO-Active B2B SaaS Scaleups *(the default — our bullseye)*

* **Segment:** B2B / B2B2C **SaaS or marketplace**.

* **Size:** a fast-growing scaleup, roughly **$20k–$150k MRR** (a *soft* guide, not a hard cut).

* **Has an in-house marketing/SEO person** (1–3 people, or a hands-on founder) who can run a
  platform — this is essential; we don't want to do everything for them.

* **Already doing real SEO** (so adopting Berlin is *reallocating* spend, not new spend).

* **Buyer:** a **founder or founder-delegated growth/marketing lead** who can say yes fast.

* **Bonus:** the buyer personally understands SEO/AEO.

* **Disqualifiers:** no marketing team; not doing SEO yet; wants a done-for-you agency;
  enterprise procurement/committee buying.

### ICP 2 — AEO-Led Mid-Market B2B *(an exploratory, higher-end experiment)*

Bigger companies ($10M–$50M ARR) approached via the **AEO** angle (AI-answer visibility), used
only when explicitly chosen. Flagged as experimental.

**How strictly we apply it:** size and industry are treated as **soft signals**, not hard
gates. A behaviorally perfect lead that's a bit too big/small, or in an adjacent industry, is
scored **partial** and surfaced for a human to decide — never silently dropped. The only true
hard "no" is the **competitor** exclusion.

***

## 8. The complete list of everything we record about a lead

This is your reference cheat-sheet — every field, where it lives, who fills it.

### On the LEAD (the company)

| Field                | What it is                                                        | Who/what sets it           |
| :------------------- | :---------------------------------------------------------------- | :------------------------- |
| `name`               | Company name                                                      | research                   |
| `url`                | Website / root domain (also the duplicate-check key)              | research                   |
| `description`        | A *brief* 1–2 line headline (segment + verdict + lead-with angle) | research                   |
| `status`             | Funnel label (Potential / Qualified / Engaged / …)                | human judgment             |
| **`industry`**       | Sector, mapped to Close's allowed choices (e.g. "Software")       | research *(curated field)* |
| **`employees`**      | Headcount (a number)                                              | research *(curated field)* |
| **`revenue`**        | Annual revenue in USD (modeled estimate, fits only)               | research *(curated field)* |
| **`business_model`** | e.g. SaaS, Marketplace, Services                                  | research *(curated field)* |
| **`seo_pages`**      | Indexed-page count                                                | research *(curated field)* |
| `touch_stage`        | # of completed touches (null = none)                              | **machine** (cold cadence) |
| `last_touched`       | Date of last touch                                                | **machine**                |
| `next_touch_due`     | When the next follow-up is due (empty = out of sequence)          | **machine**                |
| `touch_channel`      | Set of channels tried                                             | **machine**                |

> Those five **bold "curated" fields** are the *only* custom company fields the tool will set —
> by design. Anything else goes in the description or a note. (A Close admin creates these five
> fields once in the Close UI; `dogfu` only reads/writes them.)

### On a CONTACT (a person at the company)

| Field    | What it is                                                              |
| :------- | :---------------------------------------------------------------------- |
| `name`   | Person's name                                                           |
| `title`  | Their job title                                                         |
| `urls`   | Their LinkedIn / X links (repeatable) — *this is what you message from* |
| `emails` | Verified work email (from Apollo, for fits)                             |
| `phones` | Phone, if found                                                         |

### Other records attached to a lead

| Record                                | What it holds                                                                                                               |
| :------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------- |
| **Note**                              | The deep stuff: full research write-up, metrics, verdict + reason, company social links, DM hooks, and logs of calls/demos. |
| **Touch** (history entry)             | One outreach attempt: its number, date, channel, and the message detail.                                                    |
| **Cadence task** `[dogfu:cadence]`    | The single auto-managed "next cold action" reminder. Tool-owned.                                                            |
| **Deal task** `[dogfu:deal:<opp_id>]` | The single auto-managed "next step" for an open deal. Tool-owned.                                                           |
| **Ad-hoc task**                       | Any other reminder you create. Yours to manage.                                                                             |

### On an OPPORTUNITY (a deal — Phase 3 only)

| Field                                     | What it is                                |
| :---------------------------------------- | :---------------------------------------- |
| `stage`                                   | Discovery / Trial / Proposal / Won / Lost |
| `value` + `period`                        | Deal size, e.g. $1,500 **/ month**        |
| `deal_type`                               | Co-Pilot or Fully-Run                     |
| `confidence`                              | 0–100% likelihood of closing              |
| `next_step`                               | The one open `[dogfu:deal]` task          |
| `note`                                    | Scope / context                           |
| `date_won` / `date_lost` / `date_updated` | Auto-stamped milestones                   |

### Where data comes from

LinkedIn, X/Twitter, Google (incl. AI mode), ChatGPT, an SEO data backend (traffic/keywords/
tech), and Apollo (firmographics + verified emails) — all through `dogfu`. The CRM itself is
**Close**, reached through a secure proxy (so `dogfu` never even sees the Close password).

***

## 9. The branches, summarized

Every decision point in the journey, and where each branch goes:

| Decision point                    | Branch                    | Result                                             |
| :-------------------------------- | :------------------------ | :------------------------------------------------- |
| **B0 competitor gate** (research) | Sells SEO/AEO to others   | **Bad Fit** — "do not contact", saved, STOP        |
| <br />                            | Uses SEO for itself       | continue qualifying                                |
| **ICP verdict** (research)        | Strong / Partial fit      | **Qualified** → enrich → cold outreach             |
| <br />                            | Weak fit                  | **Bad Fit** — saved, never chased, STOP            |
| <br />                            | Unsure / not worked yet   | **Potential** — parked                             |
| **Cold cadence** (outreach)       | They reply                | **Engaged** → Phase 3                              |
| <br />                            | We give up (`stop`)       | **Bad Fit / Not Interested** — STOP                |
| <br />                            | No answer yet             | keep following up (no limit)                       |
| **The gate** (engage)             | Call confirms a real deal | open **Opportunity** (Discovery)                   |
| <br />                            | Just a chat, no deal yet  | stay Engaged, keep an ad-hoc task to land the call |
| **Deal pipeline** (engage)        | Trial → Proposal → signed | **Won** → lead becomes **Customer** 🎉             |
| <br />                            | Deal dies                 | **Lost** → **Not Interested / Bad Fit**            |
| <br />                            | Customer later churns     | **Canceled**                                       |
| **Inbound shortcut**              | They came to us           | created straight at **Engaged**, skip Phases 1–2   |

***

## 10. The two cross-cutting read-only skills

Three skills *do* the work and write to the CRM (research, touch, engage). Two more just *read*
it — one to tell you what to do, one to tell you what's broken. Neither ever changes anything.

### 10a. lead-worklist — your daily driver ("what do I work on today?")

**Skill:** `lead-worklist`. The three phase skills each have their own in-phase queue
(`touch due` for cold, `opportunity due` for deals). **lead-worklist is the skill that merges
them into a single ranked to-do list** so "what's on my plate" has one home. It pulls from three
sources and unifies them, most-urgent first:

| Row type                                                      | Where it comes from                            | Phase |
| :------------------------------------------------------------ | :--------------------------------------------- | :---- |
| **Reach-out** — Qualified, not yet contacted                  | `crm touch due` (never-touched rows)           | cold  |
| **Follow-up N** — next cadence touch due                      | `crm touch due`                                | cold  |
| **Engaging (pre-gate)** — replied/inbound, no deal opened yet | `crm lead list -s <Engaged>` + its ad-hoc task | warm  |
| **Live deal** — opportunity due / dropped / stalled           | `crm opportunity due`                          | warm  |

It's **read-only**: every row ends with a pointer to the skill that records the action
(lead-touch to log a touch, lead-engage to move a deal). You can ask for everything, or a slice
("just my reach-outs", "follow-ups due", "deals that need action"). It also **tiers the
context**: for the whole list it shows just enough to act (contact + LinkedIn/X handle, next
action, channels tried, days overdue); it only pulls the deep research/notes when you actually
sit down to work *one* lead. This is the "who do I message today?" entry point for the BDR.

### 10b. crm-cleanup — the janitor ("what's broken?")

**Skill:** `crm-cleanup`. Also **read-only**. Because leads can fall through cracks, this scans
the whole CRM and reports **anomalies**, each with the exact command to fix it. Examples:

* A lead being chased that already replied or is marked Bad Fit.

* A "next action" reminder that's missing, duplicated, or left open after the lead exited.

* A Qualified lead with **no contacts** (nobody to message) or **no website**.

* Duplicate leads (same company twice).

* Follow-ups badly overdue, or a lead nudged 5+ times with no reply.

* A live deal with no next step ("dropped ball").

Much of this it reads from the CLI's own `dogfu crm touch reconcile` audit; the bulk of the
tagged-task repairs are applied with `dogfu crm touch reconcile --apply` (the single-writer
rule — you never hand-edit those reminders). Run crm-cleanup whenever you want an "is our CRM
healthy?" report; it tells you *what's wrong and how to fix it*, and the fixing is done by the
other skills.

> **Bonus skill — first-audit.** Not part of the lead's CRM journey, but part of the sales
> toolkit: `first-audit` generates a free, branded SEO/AEO audit report for a prospect's domain
> from public data. It's a **first-touch asset** — something to send or reference when you reach
> out — rather than a step that changes a lead's status. (And `berlin-theme` just supplies the
> brand look for any collateral you design.)

***

## 11. TL;DR — the one-paragraph version

We find companies that *do their own SEO* (not ones that *sell* SEO — those are competitors). We
**research** each one, judge it against our **ICP**, and save everything to our CRM with a fit
verdict (`lead-research`). Good fits become **Qualified** and we **chase** them with a sequence
of hand-sent **touches** — reach-out, then unlimited follow-ups — until they **reply** (→
**Engaged**) or we **stop** (`lead-touch`). Once **Engaged**, and *only after a call confirms a
real deal*, we open an **Opportunity** and move it **Discovery → Trial → Proposal → Won/Lost**,
flipping the lead to **Customer** if we win (`lead-engage`). Leads that come *to us* skip the cold
part and start at **Engaged**. Throughout, a lead is described by two independent things — its
**status** (human funnel label) and its machine-tracked **outreach/deal state**. Two read-only
skills sit across the whole thing: **`lead-worklist`** gives the BDR one unified "what do I work
on today?" list (cold + warm + inbound), and **`crm-cleanup`** watches for anything that fell
through the cracks.

<br />

<br />

<br />

<br />

<br />

<br />

<https://www.linkedin.com/in/edwin-delgado4change/>

<https://www.linkedin.com/in/olga-melnikova-a64558213/>

<https://www.linkedin.com/in/tessgeri/>

<https://www.linkedin.com/in/amulya-vadrevu-60330381/>

<https://www.linkedin.com/in/nitya-sridhar-550131187/>

<https://www.linkedin.com/in/ericahughberg/>

<https://www.linkedin.com/in/derek-morgen-731a1211b/>
<https://www.linkedin.com/in/alanna-boudreau/>

<https://www.linkedin.com/in/sashalovehiggins/>

<https://www.linkedin.com/in/yu-shan-sandy-liu/>

<https://www.linkedin.com/in/clinton-ford-4329712/>

<https://www.linkedin.com/in/jerry-henry/>

<https://www.linkedin.com/in/charleslacalle/>

<https://www.linkedin.com/in/cody-bernard/>

<https://www.linkedin.com/in/smb06/>

<https://www.linkedin.com/in/alanna-boudreau/>

<https://www.linkedin.com/in/sashalovehiggins/>

<https://www.linkedin.com/in/yu-shan-sandy-liu/>

<https://www.linkedin.com/in/clinton-ford-4329712/>

<https://www.linkedin.com/in/jerry-henry/>

<https://www.linkedin.com/in/charleslacalle/>

<https://www.linkedin.com/in/cody-bernard/>

<https://www.linkedin.com/in/smb06/>
