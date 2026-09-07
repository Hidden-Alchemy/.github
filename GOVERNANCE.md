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

> **Organizational membership is not the same as contributing to Hidden
> Alchemy.** Anyone can contribute publicly without ever becoming an org
> member. Membership is a separate, reviewed status granted to people who have
> already demonstrated sustained, trustworthy contribution.

### Levels

| Level | Definition | How you get there |
|---|---|---|
| Public Participant | Interacts via issues/PRs/Discussions; no write access | None |
| Contributor | ≥1 merged PR or ≥1 idea promoted to a real repository | 1 accepted contribution |
| Recognized Contributor | ≥3 accepted contributions spanning ≥1 month | Sustained contribution; credited in the recognition log |
| Community Member | Reviewed org member (base tier), added to `community` team | Recognized Contributor status + Core Team approval |
| Project Member | Active contributor with write access to one specific repo | Maintainer of that repo requests elevation |
| Maintainer | Owns day-to-day health of one or more repositories | Appointed by Core Team |
| Core Team | Cross-repo technical leadership | Appointed by Organization Owner |
| Organization Owner | Ultimate administrative control | Founder(s) only; kept minimal (1–2 people) |

Role titles are deliberately professional, not gimmicky.

### Request & review process

1. **Eligibility is earned first.** A request from someone who is not a
   Recognized Contributor is declined with a written reason pointing at the
   actual bar — re-application after earning it is always welcome.
2. **Submit** the Membership Interest form (in the `community` repo). The form
   is public; no sensitive personal data is requested.
3. **Automation only assists** — labelling (`membership:needs-review`),
   duplicate/ack indicators, and a stale reminder if a request sits unreviewed
   for 21 days (never auto-approved or auto-declined).
4. **Human review** by the Core Team against the criteria above.
5. **Decision recorded** as a comment + label on the issue
   (`membership:approved` / `membership:declined` / `membership:deferred`) and
   the issue is closed.
6. **If approved**, a Core Team member manually sends the GitHub
   organization invitation *outside of any workflow*, adds the person to the
   `community` team, and works the onboarding checklist (§20.1 — invitation
   accepted, team add, welcome, governance/code-of-conduct pointers) as a
   checklist on the closed issue.

This process was exercised end-to-end in a dry run during milestone M7.

### Removal criteria

- Prolonged inactivity alone is **not** grounds for removing Community Member
  status.
- Removal applies for Code of Conduct violations, security policy violations,
  or voluntary departure.
- Reducing a repository's write access (Project Member / Maintainer) does not
  remove org membership — these are separate grants.

### Security boundary (binding)

> No workflow triggered by untrusted, publicly-writable input (an issue opened
> by any GitHub user, a comment, a fork PR) may ever directly perform a
> privileged organization action — including sending an org invitation,
> modifying team membership, changing repository permissions, or changing
> branch protection.

- **Organization invitations are always sent manually by a Core Team member —
  never by automation.** This is a deliberate scope boundary, not a
  limitation to be optimized away.
- No workflow in this organization uses a PAT or org-scoped secret, and no
  workflow carries `admin:org` scope.
- Permitted automation around membership is strictly labelling, comments, and
  reminders — nothing that changes membership state.

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