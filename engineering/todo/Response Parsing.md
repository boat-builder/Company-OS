---
rank: aA
---
We have heard that AI mode is not directly linking the target but hiding it behind a google url so they control who does the visit and also block proxy etc.

<br />

Also there can be edge cases and response structure changes which makes our analysis wrong. We need very extensive test cases and evals around this analysis

<br />

<br />

**What it does not match, and won't:**

* **A name variant of any kind.** No name matching in code at all — not "Attio", not a misspelling, not a possessive.

* **`Source.Label`** **or** **`Title`.** Never matched on, deliberately. `record.go` records that a single answer has labelled sites `"https://attio.com"`, `"Attio"`, and `"automationjinn.com"` — Label is evidence of how a brand was *named to a reader*, and matching on it is a bug.

* **The brand's name inside someone else's URL.** `g2.com/products/attio/reviews` counts as G2, not Attio — correct, it's G2's page about them. But it does mean "the brand was discussed inside a cited source" isn't measured by anything today.

