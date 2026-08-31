# The Pre-Purchase Query Framework

**Status:** v1.0 · internal\
**Purpose:** the shared vocabulary for classifying every question a potential customer asks before they buy.\
**Companion:** [`aeo-product-spec.md`](./aeo-product-spec.md) — what we *do* with the classification. This document defines the labels; that one defines the product built on them.

This is the language layer. Anyone talking about buckets, axes, awareness stages or question types — in a report, a spec, a sales call or a database column — is using the vocabulary defined here, and nowhere else.

## At a glance

```text
Scope filter
    ↓
Awareness stage  ×  Question type  ×  Search intent
    ↓
Supporting attribute: Brand presence
```

Each classification reads one thing off the query and decides one thing about the answer that would win it.

| Classification      | What it reads from the query           | What it decides about the answer   |
| :------------------ | :------------------------------------- | :--------------------------------- |
| **Awareness stage** | How much the searcher already knows    | How much the answer has to explain |
| **Question type**   | What they are asking about             | What the answer has to cover       |
| **Search intent**   | What kind of result would satisfy them | What form the answer takes         |

**Depth, subject and form** — three properties of the same answer, each set by one axis. That is the sentence to remember.

Brand presence adds useful context but is not a core classification.

***

## 1. Scope

### Include

Queries from potential customers who are identifying a problem, exploring solutions, evaluating providers or preparing to act.

### Exclude

* **Unaware audiences.** They produce little identifiable search demand related to the problem.
* **Post-purchase activity.** Onboarding, product usage, customer support and troubleshooting.
* **Irrelevant navigation.** Login, account and documentation queries intended for existing customers.

**The filter runs first, every time.** Before anyone assigns a single label, the query has to survive the scope check. If it fails it does not get a partial label — it leaves the dataset.

Post-purchase is a deliberate exclusion rather than a settled one; the case for reversing it, and what it would cost, is an open question in the product spec.

### The unit of classification

The preferred unit is a **query cluster**: queries that mean the same thing and would be answered by the same page. "seo agency cost", "how much do seo agencies charge" and "seo agency pricing" are one unit of work, not three. Individual keywords are classified only when clustering is not yet available.

***

## 2. The three axes

Each query is classified three ways. The three answers together place it in exactly one position.

> **4 awareness stages × 8 question types × 4 search intents = 128 positions.**

**Position and bucket are related but not identical, and it is worth keeping them apart.** A *position* is a coordinate in the label space — one of the 128 combinations the labels can express. A *bucket* is the set of real query clusters that actually sit at that coordinate for a particular company and topic. There are always 128 positions. There are rarely 128 non-empty buckets. The product spec works in buckets, because it deals in real client data; this document works in positions, because it defines the coordinate system.

**Keeping the three separate is the whole trick.** If you find yourself deriving one axis from another, something has gone wrong — and section 6 exists to show why the derivation never actually holds.

**One caveat on the number.** 128 is the count of positions the labels can *express*, not a claim that every one holds real demand. For any given company and topic a good many will be empty, and some question types barely reach some awareness stages. Not all 128 will ever be worth writing for. The point of the number is that the space is wide and structured rather than a single line running from cold to hot.

**A note on names.** Throughout this document **Northstar** stands in for whichever brand we are working for, and **Acme**, **Corvus** and **Halden** for its competitors. The product spec uses the same placeholders, so examples read the same way in both.

***

## 3. Axis A — Awareness stage (4 values)

How much the searcher already knows, and therefore how much the answer has to explain before it is any use. Adapted from Eugene Schwartz's five stages; we use four and drop "completely unaware", because people at that stage produce little identifiable search demand related to the problem.

| Stage              | The searcher…                                                                     | Example question                                  |
| :----------------- | :-------------------------------------------------------------------------------- | :------------------------------------------------ |
| **Problem-aware**  | recognises a problem or symptom but may not know a category of solution exists    | "why do my sales reps keep losing track of leads" |
| **Solution-aware** | knows a type of solution exists but has not settled on a provider or product      | "what does a CRM actually do"                     |
| **Product-aware**  | knows one or more *specific, named* products or providers and is evaluating them  | "is Corvus any good for small teams"              |
| **Most aware**     | knows Northstar's offering and wants final information or a path to act           | "Northstar free trial length"                     |

**The dividing line that gets missed most often** is between solution-aware and product-aware, and it is *named options* — not comparison. Comparing generic approaches is still solution-aware: someone asking "CRM vs a shared inbox", or "SEO agency vs in-house team", is choosing a category, not a supplier. Comparing named suppliers — "Acme vs Corvus" — is product-aware.

**The other common mistake** is reading awareness off the tone of the wording. "Hire an enterprise SEO agency" is unmistakably transactional and sounds decisive, but no provider is named, so it is solution-aware. A question naming *only* a competitor is normally product-aware, not most aware of us.

***

## 4. Axis B — Search intent (4 values)

What kind of result would satisfy the searcher, and therefore what form the winning answer takes. This is the standard classification the SEO industry has used for years, and it carries over unchanged.

| Intent            | Meaning                            |
| :---------------- | :--------------------------------- |
| **Informational** | Learn or understand something      |
| **Commercial**    | Investigate or evaluate options    |
| **Transactional** | Complete an action                 |
| **Navigational**  | Reach a particular website or page |

**Intent is about the result wanted, not the subject.** Pricing makes the point: "average CRM cost" is informational, "CRM pricing for a 50-seat sales team" is commercial, and "request a CRM quote" is transactional. Same subject throughout, three different pages.

**Navigational questions need a second look before they count.** One survives the scope filter only when the destination is part of a purchase decision rather than account access. "Northstar SOC 2 report" is navigational and in scope. "Northstar login" is navigational and out of it.

A default intent may be suggested by the question type, but it should be overridden when the query's meaning or the live search results clearly indicate something else.

***

## 5. Axis C — Question type (8 values)

This axis gets the most space, because it is the least self-evident of the three: it is not obvious what a third cut adds once you already know how much someone knows and what kind of result they want.

**Question type records what the searcher is asking about — the subject a winning answer has to cover.**

It is read off the question itself, not off the person behind it. "How much does a CRM cost on average?" is a pricing question because *the answer has to deal in money*. That is true no matter who asks it or what they do next.

| Question type                                 | What it covers                                            | Examples                                                                          |
| :-------------------------------------------- | :-------------------------------------------------------- | :-------------------------------------------------------------------------------- |
| **Problems and symptoms**                     | Diagnosing a pain, failure or unwanted outcome            | "why is our organic traffic declining" · "why does our payroll keep running late" |
| **Category education and solution discovery** | Understanding what a type of solution is and how it works | "what is an applicant tracking system" · "what does a technical SEO agency do"    |
| **Use cases, outcomes and workflows**         | Applying a solution to a specific goal or process         | "how to track a renewal pipeline in a CRM" · "SEO strategy for a marketplace launch" |
| **Fit, constraints and 'best for'**           | Finding the right option for a particular situation       | "best CRM for a 10-person sales team" · "best SEO agency for B2B SaaS"            |
| **Comparisons and alternatives**              | Weighing approaches, providers or substitutes             | "Acme vs Corvus" · "SEO agency vs in-house team"                                  |
| **Objections, risks and feasibility**         | Reducing uncertainty about risk, effort, timing or implementation | "can a CRM migration lose historic deal data" · "can a site migration damage rankings" |
| **Pricing and procurement**                   | Cost, contracts, commercial terms, buying requirements    | "how much does a CRM cost per seat" · "how much does an enterprise SEO audit cost" |
| **Brand validation and due diligence**        | Reviews, reputation, proof, case studies, is this company real | "Northstar customer reviews" · "Acme SEO agency reviews"                          |

### 5.1 Why two axes are not enough

Hold depth and form still, and the subject still moves. Four questions from someone shopping for a CRM — all **solution-aware**, all **commercial**:

| Question                                           | Question type                     | What the answer has to cover                       |
| :------------------------------------------------- | :-------------------------------- | :------------------------------------------------- |
| "best CRM for a 10-person sales team"              | Fit, constraints and 'best for'   | Which option suits a team that size, and why       |
| "which CRMs allow month-to-month billing"          | Pricing and procurement           | Commercial terms — money, lock-in, minimums        |
| "which CRMs are risky to migrate onto mid-quarter" | Objections, risks and feasibility | What can go wrong in a migration, and for whom     |
| "CRM vs marketing automation platform"             | Comparisons and alternatives      | Where the two categories differ and when each wins |

All four are **identical on the other two axes**. On a two-axis grid they collapse into one cell. But they are not the same question in any way that matters:

* **They need different pages.** A fit guide, a pricing page, a migration FAQ and a category comparison. No single asset serves all four.

* **They are likely answered from different places.** Our working expectation — to be tested per client, not assumed — is that comparisons get answered largely from review sites and community threads, pricing from the brand's own page or an aggregator, and risk questions from documentation and support forums. If that holds, "where is the answer coming from" has a different answer in each case, and only this axis exposes it.

* **You can be winning one and invisible in the other three.** A two-axis grid averages those four into one figure and hides it.

That last point is the commercial argument. The cell shows a mediocre blended score, and the client never learns that they own pricing questions and are absent from every comparison — which is exactly the finding they would pay for.

### 5.2 The short version

If you only remember one line:

> Awareness stage and search intent tell you **how to talk to someone**. Question type tells you **what to actually talk about**.

***

## 6. The three axes are independent

The instinct is that these are the same measurement wearing three hats — that early-stage people read, late-stage people buy, and it is one clean diagonal from left to right. It is not. That assumption is the single most expensive mistake you can make with this framework, so it is worth seeing it break.

**Hold any two axes still and the third still varies.** That is what makes them three axes rather than three names for the same thing.

### Depth and form fixed — the subject varies

All **solution-aware**, all **informational**. Same knowledge assumed, same kind of result wanted:

| Query                                         | Question type                             | What the answer has to cover                                |
| :-------------------------------------------- | :---------------------------------------- | :----------------------------------------------------------- |
| "what does a technical SEO audit involve?"    | Category education and solution discovery | What the audit involves, step by step, and what it produces |
| "how long does SEO take to show results?"     | Objections, risks and feasibility         | Honest timelines with evidence — a realistic curve          |
| "how much does an SEO agency cost on average?" | Pricing and procurement                   | Real numbers: ranges, what drives them, what is excluded    |

### Depth and subject fixed — the form varies

All **solution-aware**, all **pricing and procurement**. Same knowledge assumed, same subject:

| Intent        | Query                                          | The same query, another category       | What the answer looks like           |
| :------------ | :--------------------------------------------- | :-------------------------------------- | :------------------------------------ |
| Informational | "how much does an SEO agency cost on average?" | "average CRM cost per seat"            | A page of ranges and what moves them |
| Commercial    | "SEO agency pricing for a 50-page B2B site"    | "CRM pricing for a 50-seat sales team" | A page that sizes their situation    |
| Transactional | "request an SEO audit quote"                   | "request a CRM quote"                  | A form and a response time           |

### Form and subject fixed — the depth varies

All **informational**, all **objections, risks and feasibility**. Same kind of result, same subject:

| Awareness stage | Query                                        | The same query, another category            | What the answer has to assume                            |
| :-------------- | :-------------------------------------------- | :-------------------------------------------- | :--------------------------------------------------------- |
| Problem-aware   | "can a traffic drop recover on its own?"     | "can a lead-tracking problem fix itself"    | No category vocabulary; explain what recovery depends on |
| Solution-aware  | "how long does SEO take to show results?"    | "how long does a CRM rollout usually take"  | No provider in mind; explain the shape of the work       |
| Product-aware   | "does an Acme migration need a code freeze?" | "does an Acme migration need a data freeze" | A shortlist exists; answer the detail for that provider  |

**Both of the last two tables show three rows, not four** — no most-aware row in one, no navigational row in the other. That is not an oversight. Not every question type reaches every awareness stage, and navigational questions are rare and mostly out of scope anyway. It is the same point as the caveat in section 2: 128 is what the labels can express, not what any company actually generates.

Past solution-aware, a named provider is usually what marks the shift, so awareness and brand presence tend to move together. They stay separate labels: a brand in the query is *evidence* of awareness rather than a reading of it (see section 7, and rule 3).

### The shift test

When an assignment feels ambiguous, alter the query and see which label shifts:

* Alter what the searcher is assumed to know already → the **awareness stage** shifted.
* Alter what the answer has to be about → the **question type** shifted.
* Alter the kind of result that would satisfy them → the **intent** shifted.

If nothing shifts, the label was never really in doubt.

***

## 7. Supporting attribute — brand presence

Brand presence records which brands appear explicitly in the query.

```text
none
our_brand
competitor_brand
multiple_brands
```

It is context, not a fourth axis, and it does not multiply the position count. It is correlated with awareness but does not determine it: classify the two independently. **A category name is not a brand** and should remain `none`.

***

## 8. A worked example — one buyer, two positions

Switching domain deliberately — the examples so far have been SEO and CRM; this one is recruiting software, to show the labels do not depend on the category. Acme and Corvus are now applicant-tracking vendors.

> **Question:** "why do our job adverts get so few qualified applicants"

* **Awareness:** Problem-aware — they have a symptom, no solution category in mind.
* **Question type:** Problems and symptoms — the answer has to diagnose something.
* **Intent:** Informational — they want to understand, not to buy today.
* **Position:** Problem-aware / Problems and symptoms / Informational.

Now the second question from the same person, two weeks later:

> **Question:** "Acme vs Corvus for a 200-person company"

* **Awareness:** Product-aware — two named providers, so a shortlist exists. Note that the earlier question and this one are both comparisons in spirit, but only this one names options, which is what moves the stage.
* **Question type:** Comparisons and alternatives — with *fit, constraints and 'best for'* as a legitimate secondary, since "for a 200-person company" is a constraint the answer must handle. This is exactly the case the rules allow a second type for.
* **Intent:** Commercial — they are evaluating, not yet acting.
* **Position:** a different one entirely.

Same buyer, same topic, two positions. **This is why we classify questions rather than people.** A single buyer moves through many positions, and asking "which bucket is this customer in" is the wrong question.

***

## 9. The minimum record

```yaml
query_cluster: "best SEO agency for B2B SaaS"
awareness_stage: solution_aware
question_type: fit_and_constraints
search_intent: commercial
brand_presence: none
```

Required fields are `query_cluster`, `awareness_stage`, `question_type` and `search_intent`. Brand presence is a recommended supporting attribute and may be added automatically where reliable.

***

## 10. Classification rules

0. **Apply the scope filter before classifying anything.** A query that fails it leaves the dataset rather than receiving a partial label.
1. Choose one primary awareness stage, question type and search intent.
2. Add a secondary intent or question type only when the query genuinely performs two jobs.
3. Do not derive any axis from any other — and in particular, do not infer awareness from search intent, question type or brand presence.
4. Classify the dominant meaning of the *cluster*, not isolated keyword modifiers. "Cheap CRM" and "affordable CRM software" are the same question.
5. When meaning or intent is ambiguous, inspect what the engines actually return for the query. The results usually settle it.
6. Prefer a consistent, explainable label over false precision.
7. Record unresolved cases so the taxonomy can improve.

***

## 11. Status — what is settled and what is not

**The eight question types are the least settled part.** Eight is not a law of nature. It is our current best cut — built on what the industry already treats as standard, adapted from a review of example questions, and **not yet validated against a real client's data**. If client data keeps producing questions that fit none of the eight, we add a type and the position count changes. That is expected, and worth saying out loud rather than defending the number 128.

**The source-of-answer claim in §5.1 is a working expectation, not a finding.** That comparison questions are answered from review sites, pricing from brand pages and risk questions from documentation is the most important open question in this framework, because it is what turns question type from a content-planning label into a discovery tool. It is testable against real client data, and worth testing early.

**Two exclusions are decisions rather than conclusions.** Post-purchase questions are out of scope; bringing them in would mean a ninth question type. Geography is collected separately, but "near me" style questions carry no location in the text itself, which is unsolved for multi-location brands. Both are tracked as open questions in the product spec.

***

*The framework · v1.0 · The shared vocabulary for classifying search queries from potential customers before purchase. The taxonomy that used to live in Part 1 of the product spec lives here now; the spec links here rather than restating it.*
