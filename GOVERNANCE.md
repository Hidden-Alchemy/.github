# Governance — Hidden Alchemy

This document defines how the Hidden Alchemy organization makes decisions,
owns repositories, resolves conflict, and — at a high level — how membership
works. It is intentionally lightweight: it matches the current scale of the
organization and is not an artifact of bureaucracy built ahead of need.

> A rule that carries into every downstream decision: **organizational
> membership is a separate, reviewed status. It is not the same as
> contributing to Hidden Alchemy.** Anyone can contribute publicly without
> ever becoming an organization member. Membership is granted to people who
> have already demonstrated sustained, trustworthy contribution.

## Decision-making

- **Org-wide decisions** are made by the Core Team by simple consensus. If
  consensus cannot be reached, the Organization Owner has the final call.
- **Repository-specific decisions** belong to that repository's maintainer(s).
  Disagreements that cannot be resolved at the repository level are escalated
  to the Core Team.

## Project ownership

- Each active repository has **exactly one accountable maintainer**, recorded
  in the repository README's Maintainers block. There may be more than one
  maintainer, but one is always designated as the primary accountable owner.
- The primary maintainer is, by default, a CODEOWNER for that repository.

## Conflict resolution

- Informal discussion first, in the repository where the conflict arises.
- If unresolved, the Core Team makes a final call.
- Conduct issues are handled separately under the enforcement ladder in
  `CODE_OF_CONDUCT.md`; they are not resolved through technical
  disagreement procedures.

## Archival decisions

- A repository's maintainer proposes archival; the Core Team confirms it.
- Archived repositories are set read-only via GitHub's archive feature, and
  their README is updated with the archival note and reason (see the lifecycle
  status list below).

## Leadership changes

- Core Team appointments and removals require Organization Owner sign-off,
  reflecting the organization's current small size.
- This is revisited **when scale requires it** — once the Core Team exceeds
  roughly five people, leadership transition rules will be defined formally.

## Repository creation rule (carried forward, binding)

No repository is created — by any maintainer, now or later — without each of
the following:

- A one-sentence statement of the problem/purpose it exists to solve.
- Its target users identified.
- An explicit scope boundary (what it is **not**).
- At least one assigned maintainer (the accountable owner).
- A decided license (default: MIT; exceptions recorded).
- An initial README drafted from the org design-system template.
- A lifecycle status assigned (see below).
- A labels plan that reuses the org-wide taxonomy.

## Repository lifecycle statuses

`concept` · `research` · `experiment` · `prototype` · `active` · `stable` ·
`maintained` · `archived`

Every repository declares its current lifecycle status in its README. Status
changes are judgment calls made manually by the repository's maintainer and
reviewed only for format by the organizational repo-health check — never
inferred or set by automation.

## Membership

**Status: this section is finalized in milestone M7.** The membership model,
request process, levels, and security boundary are specified in detail by the
organization's implementation PRD (§19–§21) and will be described here in full
once the process has been exercised end-to-end. The binding security principle
that will govern it is already fixed:

> No workflow triggered by untrusted, publicly-writable input may ever
> directly perform a privileged organization action — including sending
> organization invitations, modifying team membership, or changing repository
> permissions. Organization invitations are always sent manually by a Core
> Team member.

Eligibility for membership is earned through contribution and reviewed by the
Core Team; it is never requested on demand.

## Future expansion triggers

These thresholds are recorded now and acted upon only when reached (finalized
as an appendix at milestone M10):

- **Domain teams** (AI, Design, Research) exist when a specific active project
  has ≥2 people actively working in that domain — and are created as
  project-scoped teams, not domain-wide teams.
- **Formal RFC/voting governance** is revisited when the Core Team exceeds
  roughly 5 people.
- **A second flagship project** is considered only after the first flagship
  reaches genuine `stable` or `maintained` status.
- **Mentorship program** is considered when sustained `good first issue`
  volume justifies it.

## Known current-scale limitation

The organization operates with a deliberately minimal owner set (currently
1–2 people). This single-point-of-failure risk is acknowledged and accepted at
current scale; it is revisited under the expansion triggers above.