# Contributing to Hidden Alchemy

Everything in this organization moves through the same pipeline:

```
IDEA → CONCEPT → ARCHITECTURE → SYSTEM → AUTOMATION → REALITY
```

If you can already picture your contribution somewhere in that pipeline, you
already know where it belongs. This document tells you *how* to hand it in.

**Two things up front:**

1. **Organization membership is separate from contributing.** Anyone can
   contribute publicly to this org without being an organization member. Do
   not put off your first contribution waiting for an invite that isn't
   required.
2. **Be truthful.** Do not open issues for things that have not happened, mark
   work done that is not tested, or pad a proposal with features you do not
   intend to build. This lab runs on honest records.

If you break the Code of Conduct ([CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)),
enforcement follows the ladder defined there.

---

## Find your entry point

| What you want to do | Where to start | Your first action |
|---|---|---|
| **Write code** | Any repo with a `good first issue` label | Comment that you intend to work on it, then open a PR |
| **Design** | Any issue carrying `type:design`, or a Discussion | Open a proposal issue, or comment on an existing design issue |
| **Research** | Research Proposal issue form | Submit the proposal; a maintainer confirms scope before deep work |
| **Documentation** | Issues carrying `type:documentation` | Direct PR against the docs — small fixes need no pre-approval |
| **Testing** | An issue with `help wanted` + `type:bug` | Reproduce and comment; bring a regression test in the PR |
| **Ideas** | Idea Submission form in the `ideas` repo | Fill the form; a maintainer triages it |
| **Architecture** | Project Proposal form, or an Architecture Discussion | A written proposal *before* any code |
| **Community** | A Discussion, or a docs PR in the `community` repo | Open the discussion or the PR |

Sections below cover the two main routes: **contributing work** (code/docs/etc.)
and **proposing ideas** (the idea → project pipeline). If you are not sure which
route fits, open a Discussion in the Help category — this is built for questions
that are not bugs, features, or ideas.

---

## Contributing work to a repo

This org's repos deal in the same four label facets, applied in combination.
Every issue gets **exactly one** `type:` label and, once triaged, exactly one
`status:` label. Priority and difficulty labels are judgment calls made by
humans, never by automation.

| Facet | Labels | Meaning |
|---|---|---|
| **Type** (what it is) | `type:bug` · `type:feature` · `type:documentation` · `type:design` · `type:research` · `type:experiment` · `type:architecture` · `type:idea` | What kind of work the issue represents — every issue carries exactly one |
| **Priority** (how urgent) | `priority:critical` → `priority:high` → `priority:medium` → `priority:low` | Applied by a maintainer based on judgement, never automatically |
| **Difficulty** (how big) | `good first issue` · `help wanted` | `good first issue` = under a day's work, no org tribal knowledge needed, with a testable acceptance criterion |
| **Status** (where it is) | `status:triage` → `status:planned` → `status:in-progress` → `status:review` → `status:blocked` | The lifecycle position; one per issue after triage |

Choose your first issue by looking for `good first issue` — those are scoped
small, self-contained, and carry an acceptance test in the body so you can tell
when you are done.

### The moment you pick up an issue

- Comment on the issue that you are taking it. If two people want the same
  issue, the maintainer decides; do not silently squat.
- Keep the discussion on the issue. No private channels are required for any
  work in this org.
- Small fixes to docs need no pre-approval — open the PR directly. Anything
  architectural goes through the Idea → Project Proposal route first.

---

## Proposing an idea (the pipeline route)

1. **IDEA** — Fill the Idea Submission form in the `ideas` repo. One-line idea,
   problem it solves, why *this* org, rough scope. The labeler adds an
   automated duplicate check; a maintainer then triages it.
2. **CONCEPT** — The idea is examined for actual value and boundary. It may be
   merged, split, returned for more detail, or recorded as a dead end. All three
   outcomes are legitimate and all are recorded.
3. **ARCHITECTURE** — The idea becomes a Project Proposal: it links back to the
   accepted idea, sketches the architecture before any code, and names the
   maintainer commitment. A proposal without an owner stays at ARCHITECTURE.
4. **SYSTEM and beyond** — Once built, the system gets its own repository and
   follows the same label facies as everything else.

An idea is a hypothesis, not a promise. Submitting one commits no one.

---

## Opening a pull request

Open PRs against the default branch. The
[Pull Request template](PULL_REQUEST_TEMPLATE.md) pre-fills the
checklist — you fill in:

1. **Linked issue** — the issue this PR resolves, or an explicit *"no linked
   issue"* with a one-line justification for small/obvious fixes.
2. **Summary of change** — what and why, in a few sentences, not a diff recap.
3. **Testing performed** — what you actually ran, with results.
4. **Documentation impact** — whether this needs a README/CONTRIBUTING update
   (and link that PR if so).
5. **Visual change** — a screenshot is required for any UI/README-visual change.

Merge requires **one maintainer approval**. There is no mandatory org-wide CI;
repos define their own checks as needed.

---

## Recognition, membership, and what happens next

Recognized contributions are tracked and acknowledged ([see *Recognition* in
GOVERNANCE.md](GOVERNANCE.md)). After three accepted contributions spanning at
least a month, you become a **Recognized Contributor** and — if you want to go
further — may submit the Membership Interest form in the `community` repo.

Membership is not a reward for volume and never requested "on demand": it is
evaluated against the criteria in GOVERNANCE.md, reviewed by a human, and the
decision is recorded on the issue.

**Membership is earned through contribution, not requested on demand.**

---

*A reminder that this org is a lab: experiments are allowed to fail, but failure
is always recorded and the record is always readable.*