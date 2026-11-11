# Bluesnake — Site Change Tracking

**Product spec · v1 · September 2026**

---

## In one line

Bluesnake crawls a set of websites on a schedule and tells you what changed on them since the last crawl — including your competitors' sites, not just your own.

---

## Why this exists

Websites change constantly and silently. A competitor publishes eleven new pages, rewrites the title tags across a product category, quietly kills a pricing page, or adds FAQ schema to their whole blog. Today a marketing team finds out about this by accident, weeks later, if at all.

The primitive that detects these changes already exists. Screaming Frog has had crawl comparison since v15 — you crawl a site twice, load both crawls, and it shows you which URLs are new, missing, or changed, with a Change Detection view for titles, meta descriptions, H1s, word count, structured data, internal links, and content similarity. Bluesnake already ships crawl comparison locally as well.

**We are not inventing the diff. We are inventing the product around it.**

What exists today is a manual, single-site, desktop workflow aimed at technical SEOs auditing their own site — you have to remember to crawl, remember to crawl again, keep both crawls, open the tool, and read a table of filters. That is a practitioner's utility. It is not something a marketing team subscribes to.

The opportunity is to turn a one-off comparison into **continuous, multi-site competitive monitoring** — always-on, competitor-inclusive, and delivered as a readable change feed instead of a diff table.

---

## What v1 does

**Setup.** The user defines a watchlist: their own domain plus N competitor domains. Each domain gets an initial baseline crawl.

**Schedule.** Every domain is recrawled on an interval — monthly by default, configurable to weekly. Same crawl configuration each time, so the comparison is apples-to-apples.

**Diff.** Each new crawl is compared against that domain's previous crawl. Every URL is classified, and every tracked element on surviving URLs is compared.

**Delivery.** The output is a change report per domain per period, plus a combined cross-competitor view: *here is everything that moved on the sites you care about this month.*

---

## What counts as a change

Page-level, per URL:

| Class | Meaning |
|---|---|
| **New** | URL did not exist in the previous crawl |
| **Removed** | URL existed before, is gone now (404, gone from the crawl, deindexed) |
| **Moved** | URL now redirects, or was redirected to from somewhere else |
| **Modified** | URL exists in both crawls, but something on it changed |

For modified pages, the elements we track and diff:

- **Metadata** — title, meta description, H1
- **Content** — body content changed (similarity-based), word count delta
- **Structured data** — schema types added, removed, or changed
- **Indexability** — canonical, robots meta, status code, hreflang
- **Internal linking** — inlinks gained or lost, crawl depth change

Site-level, rolled up:

- Total page count, by section/directory
- New or removed sections of the site
- Sitemap changes
- Shape of the site's content investment — which directories grew, which shrank

---

## The hard part (and our actual bet)

A raw diff of a large site produces thousands of changes, most of which mean nothing. A footer year update, a rotating testimonial, a cache-busted asset path — these will all show up as "content changed" and drown the signal.

So the core product work in v1 is not detection. It is **significance**: deciding what is worth telling a human about, ranking changes by likely intent, and grouping them into a narrative.

The report a marketer should get is not 4,000 rows. It is:

> *Competitor A published 14 new pages this month, all under /guides/, all targeting comparison intent. They rewrote titles across 62 product pages toward a new naming convention. They removed their free-tier pricing page.*

That summarisation layer is the difference between a crawler feature and a product. It is also the part nobody else has built.

---

## Output surfaces

1. **Change feed** — chronological, filterable, one row per meaningful change, with before/after values
2. **Period summary** — the narrative rollup above, per competitor and across the set
3. **Drill-down** — click any change to see the full before/after for that URL
4. **Export** — CSV/JSON/XLSX, consistent with Bluesnake's existing exports

---

## Scope

**In for v1**

- Scheduled recrawls of a defined domain watchlist
- The change classes and tracked elements listed above
- Significance ranking and period summary
- Change feed UI + export

**Out for v1**

- Social and off-site activity diffs (see below)
- Real-time / daily change alerting
- Ad creative, backlink, or SERP position monitoring
- Screenshot-based visual diffing

---

## Extension: off-site diff (v2)

The same model applies beyond the website. Once we can say "here is what changed on their site this month," the natural next line is "and here is what they did everywhere else" — social activity, new content distribution, announcements.

Website diff is the wedge because it is the highest-signal, lowest-noise, and the only one we can already do end-to-end. Off-site is an extension of the same report, not a separate product.

---

## Who this is for

- **In-house marketing teams** who currently have no systematic way to know what competitors are shipping
- **Agencies** who need to show clients competitive intelligence as a recurring deliverable
- **SEO/content leads** who want to see their own site's drift — unannounced dev changes, pages lost in a release, metadata overwritten by a CMS migration

The competitor angle is the reason someone buys. The own-site angle is the reason they keep it.

---

## Open questions

- Crawl cadence default — monthly is cheap and matches how competitors actually move; weekly is more sellable. Which do we lead with?
- Crawl depth/page cap per competitor domain, and how that maps to pricing
- Do we sell this as a Bluesnake feature, or as a standalone monitoring product with Bluesnake underneath?
- How much history do we retain, and is "12-month trend" a v1 or v2 story?
