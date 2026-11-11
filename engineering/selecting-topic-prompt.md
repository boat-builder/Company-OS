# Choosing a brand's topic list

## What a topic is, mechanically

Each topic's name and description are embedded into one vector. Every keyword
in the corpus is embedded and assigned to the nearest topic. Everything below
follows from that.

Two consequences that are easy to miss:

* **Every keyword gets a topic whether or not it fits.** There is no "none of
  these" outcome. A keyword with no correct home is filed under whichever topic
  is marginally closest, at near-zero confidence.
* **Topics separate by the words in their descriptions, not by the ideas behind
  them.** Two topics a person would call clearly distinct will not separate if
  they are described in overlapping vocabulary.

## The three failure modes

**Level mixing.** If one topic is a kind of, or a part of, another, nothing can
separate them — every keyword belonging to the child genuinely belongs to the
parent too. Siblings must sit at the same level of abstraction.

**Coverage gaps.** Subjects the corpus contains but the list omits do not
disappear. They are force-filed into the nearest topic, which both mislabels
them and drags down the confidence of whichever topic absorbs them. This is the
most expensive failure and the easiest to miss, because nothing reports it.

**Cross-cutting axes.** Anything that is a property of a keyword rather than its
subject — publishing channel, audience segment, funnel stage, region, the SKU it
maps to — competes with every subject topic at once. Such an axis belongs as an
attribute, never as a topic.

## Translating business context

Business context describes what a company is and sells. A topic list has to
describe what its audience searches. The gap between those is the main source of
coverage gaps, so read each input for what it is actually good for:

* **Products and features** give you vocabulary and core subjects, but their
  organisation is internal — it reflects how a company builds and prices, which
  has no bearing on how anyone searches. Take the subjects, discard the structure.
* **Customer problems** are the right unit. A query expresses a problem, so
  topics should name problem domains.
* **Ideal customer and positioning** set the register and vocabulary level for
  descriptions, and reveal adjacent subjects the content reaches into.
* **Business model and channel** tell you which axes are cross-cutting and must
  be excluded.

Then deliberately extend past the product surface. A brand's content almost
always spans more ground than its products do, because it answers the questions
its buyers have before they are buyers. A list drawn strictly from a feature
list will systematically under-cover.

## Composing the list

Prefer coverage over precision. A broad topic that holds its content honestly
beats a fine distinction that leaves a neighbouring subject homeless.

Include a general topic for broad and introductory material whenever the corpus
is likely to contain it. This is not a fallback for failure — it is a real
subject with real vocabulary, and naming it stops that content from silently
colonising a specific topic. Without one, some topic becomes the sink.

Balance is a signal, not a target. A topic expected to hold almost nothing is
not earning its place. A topic expected to hold a large share is usually several
topics, or is absorbing what has no home.

Topic count follows from the subjects present. Fewer topics do not help if they
are the wrong ones.

## Writing descriptions

The description is the vector. It is a vocabulary anchor, not a definition.

* Enumerate the concrete things the topic covers, in the words the audience uses
  for them. Specific terms discriminate; abstract characterisation does not.
* Name the subject as the market names it, not as the company brands it.
* Check each description against its siblings and strip shared vocabulary.
  Repeated framing, shared qualifier lists and marketing register add words to
  every topic equally and so distinguish nothing.
* Let length serve the vocabulary, not the prose.

## Checking the result

* For each pair: is either a kind of, or a part of, the other? Collapse if so.
* For each topic: does its description share much wording with a sibling's?
  Rewrite the weaker one.
* What would a keyword have to be about to have no home? If a plausible body of
  content answers that, a topic is missing.
* Would any topic attract content from every other topic's subject? If so it is
  a cross-cutting axis; remove it.

Confidence measurements taken after assignment describe how much better a
keyword's best topic is than its runner-up. They do not measure whether the
assignment is correct, and they improve mechanically as topics are removed.
Never tune a topic list against them.
