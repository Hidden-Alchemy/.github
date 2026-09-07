# PRD.md — Hidden Alchemy Organization Transformation
### Execution-Grade Master Specification for OpenCode

Version: 1.0
Status: Approved for implementation
Audience: OpenCode (implementation agent), Hidden Alchemy maintainers, organization owner

---

## 1. Executive Summary

Hidden Alchemy is an existing GitHub organization built around a transformation identity: raw ideas are converted into concepts, architecture, systems, automation, and finally working reality. Today the organization has this conceptual DNA but lacks the structural, visual, and procedural infrastructure to act on it: there is no organization-wide profile experience, no contribution pathway, no membership model, no automation, and no repository governance.

This PRD defines the complete transformation of Hidden Alchemy into a functioning open engineering laboratory. It is written for OpenCode, an implementation agent that is capable of executing well-specified instructions but is **not** capable of resolving ambiguity, making architectural judgment calls, or inferring missing requirements. Every decision that would normally be left to engineering judgment has therefore been made explicitly in this document.

The transformation is organized into 11 milestones (M0–M10), each broken into atomic phases, each phase broken into atomic tasks with explicit preconditions, file-level specifications, test procedures, and acceptance criteria. OpenCode must execute milestones strictly in order and must not begin a milestone until the previous one has passed its completion checklist and received explicit sign-off.

This document also defines hard boundaries: what must not be built yet, what must never be automated without human approval, and what security invariants must never be violated (particularly around organization membership invitations and privileged GitHub Actions).

---

## 2. Product Vision

Hidden Alchemy will become the public engineering laboratory where ideas are deliberately, visibly, and rigorously converted into real systems, following the pipeline:

```
IDEA → CONCEPT → ARCHITECTURE → SYSTEM → AUTOMATION → REALITY
```

Anyone can walk in, understand the lab's purpose within seconds, see what is actively being built, and find a concrete way to contribute — from a first small documentation fix to eventually joining the organization as a trusted member. The organization will feel engineered rather than decorated: every repository, label, workflow, and document exists because it serves a specific function in that pipeline.

---

## 3. Existing Context (Preserve, Do Not Replace)

The following identity elements are canon and must be preserved and reinforced, not reinvented:

- **Name**: Hidden Alchemy
- **Core metaphor**: transformation — `IDEA → CONCEPT → ARCHITECTURE → SYSTEM → AUTOMATION → REALITY`
- **Domain alignment**: Frappe, ERPNext, AI, automation, software/product engineering, experimental projects, research, architecture, developer tools, intelligent systems, open source collaboration
- **Stated principles**: Build, Don't Perform · Complexity Should Become Invisible · Automation Should Create Leverage · Design Is Part of Engineering · Experiment Relentlessly · Details Compound
- **Color system**: Ink (dark base), Bone (light contrast), Gold `#BD9C61`, Verdigris `#4C6B5C`
- **Tone**: premium, technical, experimental, precise — never decorative, never gamified, never fantasy-themed despite the "alchemy" name.

Positioning statement (canonical, may be lightly copy-edited but not reconceived):

> Hidden Alchemy is an open engineering laboratory for transforming raw ideas into real systems.

---

## 4. Problem Statement

1. There is no organization-level profile (`.github` repo with a `profile/README.md`), so the org has no public identity surface.
2. There is no defined repository architecture, creating risk of both repository sprawl and, currently, of an empty-looking organization.
3. There is no contribution pathway: no CONTRIBUTING.md, no issue forms, no labels, so first-time contributors have no entry point.
4. There is no membership model: org membership, if granted, is currently an all-or-nothing manual decision with no defined criteria, review process, or security boundary.
5. There is no automation: onboarding, labeling, and repository health checks are all manual or nonexistent.
6. There is no security architecture: no defined token/secret boundaries, no branch protection policy, no rule preventing untrusted input from ever triggering privileged actions.
7. There is no visual design system for READMEs, so any content produced today would look like a generic template rather than a distinctive engineering lab.
8. There is no flagship project that gives outsiders a concrete reason to pay attention.

---

## 5. Strategic Positioning

Hidden Alchemy competes for contributor attention not against other companies but against the default assumption that "another GitHub org" is not worth exploring. The organization must win in the first 15 seconds of a profile visit by being unmistakably intentional: a visible transformation pipeline, a small number of real, clearly-classified projects, and one flagship project that proves the pipeline actually works. Everything else (governance, teams, membership tiers) exists to protect and scale that credibility, not to perform maturity the org does not yet have.

---

## 6. Product Principles (Binding Constraints)

These principles are binding on every milestone. Any task that violates one must be rejected by OpenCode and flagged as an ambiguity (see §53/Section "No Assumption Rule").

1. **Intentionality** — nothing is created without a stated purpose recorded in this PRD.
2. **Premium technical identity** — precise, engineered, minimal; never childish, never a generic template.
3. **Build, don't perform** — no empty repositories, no fake counts, no simulated activity.
4. **Complexity becomes invisible** — sophisticated backend systems, simple front-of-house experience.
5. **Automation creates leverage, never replaces judgment** — automate mechanical work only; every privileged or human-judgment action requires a human.
6. **Design is engineering** — documentation is designed, not dumped; but GitHub rendering and accessibility always outrank visual ambition.
7. **Experiment relentlessly, but classify honestly** — every repository declares its lifecycle status.
8. **Least privilege everywhere** — permissions, tokens, and org membership are minimal by default and escalate only through explicit, human-approved steps.

---

## 7. Goals

- G1: Ship a distinctive, GitHub-rendering-safe organization profile README that communicates identity and the transformation pipeline within one screen.
- G2: Ship a minimal, non-sprawling repository architecture that separates community infrastructure from real project work.
- G3: Ship a complete first-contribution pathway (CONTRIBUTING, issue forms, labels, PR template) usable by a beginner with zero prior context.
- G4: Ship a secure, staged membership model with an explicit human-approval gate before any organization invitation is ever sent.
- G5: Ship baseline automation (welcome, labeling, repo-health checks) with fully documented trust boundaries.
- G6: Ship a security architecture covering tokens, secrets, branch protection, and workflow permissions, tiered by repository maturity.
- G7: Ship a reusable README design system so every future repository is visually and structurally consistent without reinventing structure each time.
- G8: Identify and scaffold (but not necessarily fully build) one flagship project that proves the IDEA→REALITY pipeline.

## 8. Non-Goals (Explicitly Out of Scope for This PRD)

- NG1: Do not create teams for domains (AI, Design, Research, etc.) before there are active projects that need them.
- NG2: Do not build a public web app, dashboard, or external service. Everything ships as GitHub-native artifacts (Markdown, Issue Forms, Actions, Discussions).
- NG3: Do not implement automated organization invitations. Invitations remain a manual, human-triggered action for the entire scope of this PRD (see §15/§29 security rules).
- NG4: Do not build a contributor points/badges gamification system.
- NG5: Do not create more than one flagship project during this PRD's scope.
- NG6: Do not integrate third-party badge services, analytics trackers, or external SaaS dependencies for the profile README.

---

## 9. Target Users / 10. Personas

| Persona | Primary need | Primary surface |
|---|---|---|
| Explorer | Understand what Hidden Alchemy is in <15s | Org profile README |
| Beginner Contributor | A safe, understandable first task | `good first issue` label, CONTRIBUTING.md |
| Developer | Real code to work on, clear architecture | Project repo READMEs, issues |
| Designer | Design/DX work that matters | `design` label, DESIGN section of CONTRIBUTING |
| Research Contributor | A place for analysis/research that isn't "just an issue" | `research` label, Research discussion category |
| Project Initiator | A structured path from idea to repository | Idea submission issue form, `ideas` repo |
| Active Contributor | Visible recognition, path to deeper trust | Recognition system (§32), membership pathway |
| Maintainer | Automation that removes admin toil safely | Workflows (§28), CODEOWNERS |
| Organization Owner | Security, minimal admin overhead, visibility | Security architecture (§30), governance (§32) |

## 11. User Journeys

**Explorer → Contributor (primary journey):**
`Land on org` → `Read profile README hero + pipeline` → `See Active Systems / Experimental Lab sections` → `Click into a project or the ideas repo` → `Find a labeled issue or open an idea` → `Read CONTRIBUTING.md` → `Open first PR or idea issue` → `Receive automated welcome + human review` → `Get merged/acknowledged` → `(optional) Continue contributing` → `(optional, later) Request membership`

**Project Initiator journey:**
`Has an idea` → `Searches ideas repo/discussions for duplicates` → `Opens Idea Submission issue form` → `Automated validation + labeling` → `Maintainer review (RAW IDEA → UNDER REVIEW)` → `Research/validation discussion` → `Decision: promote to repository, keep as discussion, or decline with reason`

**Membership Interest journey:**
`Contributor has track record` → `Opens Membership Interest issue form (or is nominated by a maintainer)` → `Automated validation (duplicate check, required fields)` → `Human review against explicit criteria (§19)` → `Decision recorded on the issue` → `If approved: maintainer manually sends GitHub org invitation` → `Manual onboarding checklist executed`

---

## 12. Ecosystem Architecture — Repository Plan

Legend: **NOW** = create in this PRD's scope · **LATER** = defined but not created yet · **FUTURE** = optional, evaluate when scale justifies it · **DO NOT CREATE** = explicitly rejected

| Repository | Visibility | Status | Purpose |
|---|---|---|---|
| `.github` | Public | **NOW** | Org-wide default community health files, profile README, reusable issue-form/workflow templates |
| `community` | Public | **NOW** | Home for Discussions-adjacent static docs: GOVERNANCE.md, membership process docs, recognition log. Not a code repo. |
| `ideas` | Public | **NOW** | Idea intake and incubation via Issue Forms; lifecycle tracked with labels + a GitHub Project board |
| `experiments` | Public | **LATER** — create only when a first real experiment exists (do not pre-create empty) | Home for short-lived, clearly-labeled experimental code that has not yet earned its own repository |
| `projects` (meta index) | Public | **DO NOT CREATE** | Rejected: redundant with the org profile README's "Active Systems" section, which will list real project repos directly. A meta-index repo with no code is exactly the "empty repository" anti-pattern this PRD prohibits. |
| `<flagship-project-name>` | Public | **LATER**, scaffolded in M9 | The one flagship project proving the pipeline (see §19/M9) |
| `.github-private` (org-internal ops, e.g. membership review notes) | Private | **LATER** | Only created if/when membership review needs a private tracking surface beyond issue forms with restricted visibility. Not required for MVP since GitHub Issue Forms in `community` can be configured with appropriate visibility. |

**Rule enforced across all repositories:** no repository is created without (a) a named owner/maintainer, (b) a defined purpose recorded in this table or a future PRD amendment, and (c) required baseline files (LICENSE, README following the design system in §15, CODEOWNERS where applicable).

### 12.1 Repository Creation Checklist (must be satisfied before any new repo is created, including by future maintainers)

- [ ] Problem/purpose is written down in one sentence
- [ ] Target users identified
- [ ] Scope boundary stated (what it is NOT)
- [ ] At least one maintainer assigned
- [ ] License decided (default: MIT unless a specific repo requires otherwise — record exception)
- [ ] Initial README drafted using the correct template from §15
- [ ] Lifecycle status assigned (§24)
- [ ] Labels plan confirmed (reuse org-wide taxonomy, §25 — no repo-local label sets without justification)

---

## 13. Organization Profile System — `.github` Repository Architecture

```
.github/
├── profile/
│   └── README.md                 # organization profile (see §14)
├── assets/
│   ├── svg/                      # all custom SVG diagrams/animations
│   │   ├── hero-pipeline.svg
│   │   ├── contribution-pathway.svg
│   │   └── README.md             # asset usage + naming rules
│   └── og/
│       └── org-social-preview.png  # GitHub org social preview image (static fallback)
├── ISSUE_TEMPLATE/
│   ├── config.yml                # disables blank issues, links to Discussions
│   ├── bug_report.yml
│   ├── feature_request.yml
│   ├── idea_submission.yml
│   ├── project_proposal.yml
│   ├── research_proposal.yml
│   └── membership_interest.yml
├── workflows/
│   ├── welcome-first-interaction.yml
│   ├── issue-labeler.yml
│   ├── repo-health-check.yml
│   └── stale-triage.yml
├── PULL_REQUEST_TEMPLATE.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── SUPPORT.md
├── GOVERNANCE.md
└── FUNDING.yml                   # OPTIONAL — only populate if a real funding channel exists; otherwise omit the file entirely rather than ship it empty
```

File-by-file requirement/justification table:

| File | Required now? | Why |
|---|---|---|
| `profile/README.md` | Yes | Primary public interface of the org (§14) |
| `assets/svg/*` | Yes | Supports README visual system without third-party dependency |
| `ISSUE_TEMPLATE/*` | Yes | Structured intake is required for §21 contribution flow and §17 idea system |
| `workflows/welcome-first-interaction.yml` | Yes | Core onboarding automation (§28) |
| `workflows/issue-labeler.yml` | Yes | Reduces triage toil (§28) |
| `workflows/repo-health-check.yml` | Yes | Prevents repository sprawl/anti-patterns (§28, §57) |
| `workflows/stale-triage.yml` | Yes, but non-destructive (label only, never auto-close in v1) | Keeps issue backlog honest without punishing slow but real work |
| `PULL_REQUEST_TEMPLATE.md` | Yes | Baseline contribution quality (§27) |
| `CONTRIBUTING.md` | Yes | Core onboarding document (§21) |
| `CODE_OF_CONDUCT.md` | Yes | Standard community health file (Contributor Covenant, adapted tone) |
| `SECURITY.md` | Yes | Vulnerability reporting path (§30) |
| `SUPPORT.md` | Yes | Where to ask questions vs. file issues |
| `GOVERNANCE.md` | Yes, lightweight | Decision-making model appropriate to current scale (§32) |
| `FUNDING.yml` | No — omit | No funding channel currently exists; do not ship a placeholder |

---

## 14. Organization Profile README — Full Specification

**File:** `.github/profile/README.md`
**Consumers:** Every visitor to `github.com/Hidden-Alchemy`
**Constraint:** Must render correctly in GitHub light mode and dark mode, on desktop and mobile, with zero required external dependencies.

### 14.1 Section order (final, optimized for storytelling → conversion)

1. **Identity Hero** — org name, one-line positioning statement, and the transformation pipeline diagram (`assets/svg/hero-pipeline.svg`)
2. **The Alchemy Process** — short explanation of each pipeline stage (IDEA/CONCEPT/ARCHITECTURE/SYSTEM/AUTOMATION/REALITY), 1–2 sentences each
3. **What We Build** — the domain alignment list (Frappe/ERPNext, AI, automation, dev tools, etc.), framed as "where we currently apply the process," not a generic skills list
4. **Active Systems** — a manually-maintained table of real, non-experimental repositories with status badges (see §24 status system); empty state text if none yet exist ("No active systems yet — see Experimental Lab" rather than a fabricated entry)
5. **Experimental Lab** — link to `experiments` repo (once it exists) and/or open experiment issues; explains what "experiment" means here
6. **How to Participate** — the participation pathway diagram (`assets/svg/contribution-pathway.svg`) plus links to CONTRIBUTING.md and the three entry-point issue forms (bug/idea/proposal)
7. **Organization Principles** — the six stated principles (§6), rendered as a compact visual list, not prose paragraphs
8. **Join the Lab** — membership pathway explanation with explicit statement: *"Membership is earned through contribution, not requested on demand."* Link to Membership Interest form with the eligibility bar stated plainly.

### 14.2 Visual system requirements

- Color usage: Ink/Bone define background/foreground pairing per light/dark mode; Gold `#BD9C61` and Verdigris `#4C6B5C` are accent-only (section dividers, pipeline node highlights, link hover states where GitHub allows), never full-background fills that could break in one color mode.
- Typography: GitHub-rendered Markdown headings only; no attempt to inject custom web fonts (unsupported and fragile). Visual "typography feel" comes from spacing, rule dividers (`---`), and SVG-embedded text for the hero diagram only.
- SVGs must:
  - Use `currentColor` or explicit dual-mode-safe colors (test against both GitHub background colors: `#0d1117` dark / `#ffffff` light)
  - Include a `<title>` element for accessibility
  - Degrade gracefully if animation (SMIL/CSS) is stripped by the renderer — the static frame must still communicate the pipeline
  - Stay under 150KB each
- No third-party badge services (shields.io is acceptable **only** for static, non-tracking badges such as License; no visitor-counter or view-count badges — these are explicitly banned as vanity metrics per §57).
- No GIFs. Motion, if used, must be SVG `<animate>`/CSS-in-SVG, subtle (opacity/position drift, not flashing), and must be visually inert if the client disables animated images — i.e., frame 0 must be a complete, correct illustration on its own.

### 14.3 Acceptance criteria for this file

- [ ] All 8 sections present in the specified order
- [ ] All internal links resolve (CONTRIBUTING.md, issue forms, repo links)
- [ ] Hero SVG renders correctly in GitHub dark mode and light mode (manual screenshot check, both modes)
- [ ] No section references a repository, contributor count, or statistic that does not currently exist
- [ ] Total README length allows the Identity Hero + Alchemy Process to appear without scrolling on a standard 1440×900 desktop viewport at default GitHub zoom
- [ ] Mobile rendering manually verified (no horizontal scroll, SVG scales via `viewBox`)
- [ ] Zero external network dependencies required for correct rendering

---

## 15. README Design System (Reusable Across All Repositories)

Every repository README is composed from these ordered blocks. Not every block is required for every repo type — the table below maps block → repo type.

**Blocks:**
A. Hero (name + one-line purpose + status badge)
B. Identity strip (which pipeline stage this repo currently occupies)
C. Status & lifecycle (explicit state from §24, last-updated note)
D. What this is / is not (scope boundary, 2–4 bullets each)
E. Architecture (only if non-trivial; diagram or short structured description)
F. Installation / Quick Start
G. Contribution (short, links out to org-wide CONTRIBUTING.md — never duplicates it)
H. Roadmap (link to Project board or short bullet list — no fake dates)
I. Maintainers (names/handles, not emails)
J. Footer (license line, link back to org profile)

| Repo type | Required blocks |
|---|---|
| Flagship project | A, B, C, D, E, F, G, H, I, J |
| Experiment | A, B, C, D (esp. hypothesis/objective/status/next-step per §23), I, J |
| Research repository | A, C, D, (findings section replaces F/G), I, J |
| Community repo (`community`, `ideas`) | A, C, D, G, J — no install/quickstart (not applicable) |
| Library/tool | A, B, C, D, E, F, G, H, I, J (full template) |

Templates for each type are stored at `.github/profile/../` — specifically under a new shared location:

```
.github/
└── templates/
    ├── README.flagship.md
    ├── README.experiment.md
    ├── README.research.md
    ├── README.community.md
    └── README.library.md
```

Each template file must contain the block skeleton with `<!-- TODO -->` HTML comments marking required fill-in content, so a maintainer creating a new repo copies the template and cannot accidentally publish an unfilled placeholder (the repo-health-check workflow, §28, scans for lingering `TODO` markers in README files on the default branch and fails a status check if found).

---

## 16. Visual Asset Architecture

- All custom visual assets live in `.github/assets/` (see §13 tree). This is a **single shared location**, not per-repository, because assets are currently org-identity assets (pipeline diagram, pathway diagram), not project-specific illustrations.
- Naming convention: `kebab-case`, purpose-first: `hero-pipeline.svg`, `contribution-pathway.svg`.
- Versioning: assets are versioned by git history in `.github`; no separate asset-versioning scheme is needed at current scale. If an asset needs a breaking redesign, the old file is replaced in place (git history preserves the old version) — do not accumulate `hero-pipeline-v2.svg` files.
- Reference method: other repos link to assets via the raw GitHub content URL of the `.github` repo's default branch (`https://raw.githubusercontent.com/Hidden-Alchemy/.github/main/assets/svg/...`). This is a single point of truth; do not copy asset files into individual project repos.
- Every animated SVG must have its static-frame fallback be the actual first frame of the animation (not a separate "fallback image") to avoid asset drift between the two.
- Accessibility: every SVG requires `<title>` and, where meaningful, `<desc>`. Reduced motion: because GitHub's Markdown renderer does not currently expose `prefers-reduced-motion` to embedded SVG reliably, motion must be inherently subtle (slow, low-amplitude) rather than relying on a media-query opt-out.

---

## 17. Participation System

Pathway (canonical, referenced by the profile README pipeline diagram in §14):

```
EXPLORE → DISCUSS → CONTRIBUTE → COLLABORATE → RECOGNITION → TRUST → MEMBERSHIP ELIGIBILITY
```

Entry points by contribution type:

| Type | Entry point | First action |
|---|---|---|
| Code | Any project repo's `good first issue` label | Comment intent to work, then PR |
| Design | `design` label on any repo, or Discussions "Show and Tell" | Open a proposal issue or comment on an existing design-labeled issue |
| Research | Research Proposal issue form | Submit proposal; maintainer confirms scope before deep work begins |
| Documentation | `documentation` label | Direct PR against docs, no pre-approval required for small fixes |
| Testing | `help wanted` + `type:bug` combination | Reproduce and comment; write regression coverage in PR |
| Ideas | Idea Submission issue form in `ideas` repo | Fill form; automated duplicate-check comment; maintainer triage |
| Architecture | Project Proposal issue form or direct Discussion in "Architecture" category | Written proposal before code |
| Community | Discussions "General" or `community` repo docs PRs | Open discussion or doc PR |

Each path shares the same downstream automation (welcome comment, labeling) and the same recognition mechanism (§32) — there is no separate track per contribution type beyond the entry point.

---

## 18. Contributor Onboarding System

Sequence:

```
LAND ON ORG → UNDERSTAND PURPOSE (profile README) → DISCOVER PROJECTS (Active Systems section)
→ FIND CONTRIBUTION (labels) → UNDERSTAND TASK (issue description + CONTRIBUTING.md)
→ CONTRIBUTE (PR or idea submission) → RECEIVE FEEDBACK (review) → RECEIVE RECOGNITION (§32) → CONTINUE
```

- **First-time contributor detection**: GitHub Actions' `github.event.action == 'opened'` combined with the `actions/first-interaction` action (org-pinned to a specific commit SHA, not a floating tag — see §30 supply-chain rule) detects first issue/PR from a given author across the org's repos where the workflow is installed.
- **Welcome workflow**: posts one templated, non-generic comment (references the specific label/type of issue/PR, links CONTRIBUTING.md and CODE_OF_CONDUCT.md). Never posts more than once per person per repository.
- **Good-first-issue strategy**: a maintainer must explicitly apply `good first issue` only to tasks that are (a) scoped to <1 day of work, (b) do not require org-specific tribal knowledge beyond what's in CONTRIBUTING.md, (c) have a clearly testable acceptance criterion written in the issue body. The repo-health-check workflow flags (does not block) any `good first issue` open for >30 days without activity, for maintainer review, not auto-removal.
- **Mentorship**: not automated in this PRD's scope (NG-adjacent) — a maintainer may volunteer directly in the issue thread. No formal mentorship program is built yet (documented as FUTURE in §59).
- **Duplicate/spam prevention**: issue forms require structured fields (not free text only) to raise the effort bar; the labeler workflow flags issues with near-duplicate titles for human review (does not auto-close).

---

## 19. Membership System

Explicit distinction (must appear verbatim in `GOVERNANCE.md` and in the profile README "Join the Lab" section):

> GitHub organization membership is not the same as contributing to Hidden Alchemy. Anyone can contribute publicly without ever becoming an organization member. Membership is a separate, reviewed status granted to people who have already demonstrated sustained, trustworthy contribution.

### 19.1 Levels

| Level | Definition | Permissions | Entry criteria | Promotion path |
|---|---|---|---|---|
| Public Participant | Anyone interacting via issues/PRs/Discussions | None (no repo write access) | None | Becomes Contributor on first merged PR or accepted idea |
| Contributor | Has ≥1 merged PR or ≥1 idea promoted to a real repository | Triage-suggest via labels (comment only, no write access) | 1 accepted contribution | Recognized Contributor after 3 accepted contributions across ≥1 month |
| Recognized Contributor | Sustained contribution (≥3 accepted contributions, spanning ≥1 month) | Same as Contributor + credited in recognition log (§32) | 3 accepted contributions / 1 month span | Eligible to submit Membership Interest form |
| Community Member (org member, base tier) | Approved via Membership Interest review | GitHub org member (no elevated repo permissions by default); added to `community` team | Recognized Contributor status + maintainer approval | Project Member if actively working a specific repo |
| Project Member | Active, ongoing contributor to a specific repository | Write access to that specific repository only | Maintainer of that repo requests elevation for a Community Member | Maintainer, by repo owner decision |
| Maintainer | Owns day-to-day health of one or more repositories | Admin on owned repositories; cannot modify org-wide settings | Appointed by Core Team based on sustained ownership-level contribution | Core Team, by existing Core Team consensus |
| Core Team | Cross-repository technical leadership | Org "Member" role with elevated team memberships across maintained repos; no billing/org-deletion rights | Appointed by Organization Owner | N/A |
| Organization Owner | Ultimate administrative control (billing, org deletion, security settings) | GitHub "Owner" role | Founder(s) only in current scope | Not applicable — must remain minimal (target: 1–2 people max) |

Names are deliberately professional (not "Alchemist," "Adept," etc.) per §57's prohibition on gimmicky branding overriding professionalism — the transformation *metaphor* lives in the pipeline diagram and prose, not in role titles.

### 19.2 Removal criteria (must be documented, not just growth)

- Prolonged inactivity is **not** by itself removal justification for Community Member status (avoid punishing people for having a life).
- Removal applies for: Code of Conduct violations (per CODE_OF_CONDUCT.md enforcement ladder), security policy violations, or explicit voluntary departure.
- Repository-level write access (Project Member/Maintainer) can be reduced by the relevant repo's maintainer/Core Team without removing org membership, since these are separate grants.

---

## 20. Membership Request System

Workflow:

```
USER EXPRESSES INTEREST (Membership Interest issue form, in `community` repo)
→ AUTOMATED VALIDATION (required fields present, GitHub account age/public-activity sanity check surfaced for reviewer — not auto-rejected)
→ DUPLICATE CHECK (labeler workflow flags if an open/recent request exists from same author)
→ AUTOMATED ACKNOWLEDGEMENT COMMENT (sets expectation: "reviewed within X, decision recorded on this issue")
→ HUMAN REVIEW (Core Team, against §19.1 criteria)
→ DECISION recorded as a comment + label (`membership:approved` / `membership:declined` / `membership:deferred`) — issue is then closed
→ IF APPROVED: a Core Team member manually sends the GitHub org invitation outside of any workflow
→ TEAM ASSIGNMENT (manual, by the same Core Team member, added to `community` team at minimum)
→ ONBOARDING (manual checklist, §20.1)
```

- **Where requests happen**: Issue Form (not Discussions, not an external form) — because it needs structured required fields, is versionable, and keeps a durable audit trail tied to a GitHub identity. Discussions is not chosen because it lacks required-field structure; an external form is rejected to avoid an unnecessary third-party dependency and data-handling surface.
- **Privacy**: the form must not request sensitive personal data (no phone numbers, no home addresses, no government ID). Only GitHub handle, summary of contributions, and areas of interest are requested.
- **Public visibility**: requests are public by default (consistent with "public participation, reviewed membership"); the form must state this plainly before submission so applicants aren't surprised.
- **Expiration**: if a request sits with no maintainer decision for 21 days, the stale-triage workflow labels it `membership:needs-review` and pings the Core Team team handle — it is never auto-declined or auto-approved.

### 20.1 Manual onboarding checklist (performed by the inviting Core Team member, tracked as a checklist in the closed membership-interest issue)

- [ ] GitHub invitation sent
- [ ] Invitation accepted (verified before continuing)
- [ ] Added to `community` team
- [ ] Welcomed in the appropriate Discussions category
- [ ] Pointed to GOVERNANCE.md and CODE_OF_CONDUCT.md enforcement expectations for members specifically

---

## 21. Membership Automation & Critical Security Rule

**CRITICAL SECURITY RULE (binding, non-negotiable):**

> No workflow triggered by an untrusted, publicly-writable event (an issue opened by any GitHub user, a comment, a fork PR) may ever directly perform a privileged organization action — including sending an org invitation, modifying team membership, modifying repository permissions, or modifying branch protection.

Enforced pattern:

```
UNTRUSTED EVENT (issue_comment, issues, pull_request from a fork)
→ VALIDATION (format/field checks only — read-only operations)
→ HUMAN APPROVAL (a Core Team member takes a manual, out-of-band action: closing with a label, and separately, manually inviting via GitHub UI/CLI with their own credentials)
→ [NO WORKFLOW STEP CROSSES THIS LINE AUTOMATICALLY]
```

Permitted automation around membership: labeling, duplicate-detection comments, acknowledgement comments, stale-reminders. **Not permitted, in this PRD's scope, under any workflow:** any step that calls the GitHub API to create an org invitation, add a team member, or change a repository collaborator list. This is intentional and must not be "optimized away" by OpenCode even if technically feasible — it is a deliberate scope boundary, not an oversight.

Token/secret rules for all workflows in this system:

- Workflows triggered by `issues`, `issue_comment`, or `pull_request_target` must use the default `GITHUB_TOKEN` with explicitly minimized `permissions:` block (e.g., `issues: write, pull-requests: write` only — never `admin:org` scope, ever, in any workflow file in this PRD's scope).
- No workflow in this PRD's scope requires a Personal Access Token (PAT) or an org-scoped secret. If a future capability seems to require one, that is out of scope and must be flagged as an ambiguity, not implemented.
- `pull_request_target` is not used anywhere in this PRD's scope, because none of the defined workflows need write access combined with checkout of untrusted fork code. If a future workflow seems to need it, treat as high-risk and stop for human review (§30.4).

---

## 22. GitHub Teams and Permissions

### 22.1 Teams created NOW

| Team | Members | Repository access |
|---|---|---|
| `core` | Core Team (§19.1) | Admin on all active repos except where a Maintainer team is more specific |
| `community` | All approved org members | Read on all public repos (default already via public visibility — team exists for @mention/notification grouping and Discussions moderation permissions, not for elevated repo access) |

### 22.2 Teams explicitly NOT created yet

`ai`, `design`, `research`, or any other domain team — these are **DO NOT CREATE YET**. They are created only when a specific active project both (a) exists and (b) has ≥2 people actively working in that domain, at which point a Core Team member creates a project-scoped team (e.g., `<flagship-project>-maintainers`), not a domain-wide team.

### 22.3 Permission rules

- Only Organization Owners can create/delete teams and modify org-wide settings.
- Only Core Team (or Owners) can add members to `core`.
- Any Core Team member can add an approved applicant to `community` (this is the one place manual membership actions happen, deliberately outside of automation per §21).
- Repository-level write access beyond `community`'s read default is granted per-repository by that repository's Maintainer or Core Team, never org-wide.
- Least privilege default for every new repository: Owner/Admin = Core Team + repo's designated Maintainer(s) only; Write = explicitly named Project Members; everyone else = Read (public repos are inherently readable).

---

## 23. Project Proposal System

Refined lifecycle (improves on the prompt's draft by merging "Validation" into "Research" to avoid a redundant stage, and by giving every stage an explicit exit condition):

```
RAW IDEA → UNDER REVIEW → RESEARCH (incl. feasibility/validation) → ARCHITECTURE → PROTOTYPE → ACTIVE PROJECT → STABLE → MAINTAINED → ARCHIVED
```

| Stage | Entry condition | Exit condition | Where tracked |
|---|---|---|---|
| Raw Idea | Idea Submission form submitted | Maintainer acknowledges within 7 days | `ideas` repo issue |
| Under Review | Acknowledged | Maintainer decides: proceed to Research, or Decline (with written reason), or Defer | `ideas` repo issue + label |
| Research | Proceed decision made | Feasibility + scope written up in the issue as a comment; a go/no-go decision recorded | `ideas` repo issue |
| Architecture | Go decision made | A short architecture note exists (can be a comment or linked doc) describing shape of the eventual system | `ideas` repo issue |
| Prototype | Architecture note accepted | A minimal working prototype exists, in `experiments` repo or a scratch branch | `experiments` repo (created at this point if it doesn't exist yet) |
| Active Project | Prototype validates the core idea and has a committed maintainer | New dedicated repository created per checklist in §12.1; idea issue closed with link to new repo | New repo |
| Stable | Repo has a tagged release and documented usage | — | Repo README status badge |
| Maintained | Ongoing, lower-velocity upkeep | — | Repo README status badge |
| Archived | No longer actively developed | Repository archived via GitHub's native archive feature (read-only), README updated with archival note and reason | Repo README + GitHub archived flag |

**Explicit rule:** not every Raw Idea becomes a repository. Decline is a normal, expected, first-class outcome and must always include a written reason for respect and learning purposes.

---

## 24. Repository Lifecycle / Status System

Statuses (final): `concept` · `research` · `experiment` · `prototype` · `active` · `stable` · `maintained` · `archived`

- Displayed via a single-line badge at the top of every README (block A/B in §15), formatted as plain bold text plus a small colored dot SVG (not a third-party shields.io dynamic badge, to avoid an external dependency for something this simple): e.g. `**Status:** 🟢 Active`.
- Update mechanism: manual, by the repo's maintainer, as part of any PR that changes the repo's maturity — this is a judgment call and is never automated.
- The repo-health-check workflow verifies only that *a* status line exists in the expected format — it never sets or infers the status value itself.

---

## 25. Issue Management System — Label Taxonomy (Final)

Organized into 4 non-overlapping facets, applied in combination. Reused identically across every repository (no repo-local label sets).

**Contribution difficulty:** `good first issue` · `help wanted`

**Type:** `type:bug` · `type:feature` · `type:documentation` · `type:design` · `type:research` · `type:experiment` · `type:architecture` · `type:idea`

**Priority:** `priority:critical` · `priority:high` · `priority:medium` · `priority:low`

**Status:** `status:triage` · `status:planned` · `status:in-progress` · `status:blocked` · `status:review`

**Community (cross-cutting, used mainly in `community`/`ideas` repos):** `membership:approved` · `membership:declined` · `membership:deferred` · `membership:needs-review` · `project-proposal`

Rules: every issue gets exactly one Type label (auto-suggested by the labeler workflow based on which issue form was used) and, once triaged, exactly one Status label. Priority and difficulty labels are optional and human-applied only (never inferred automatically, since priority is a judgment call).

---

## 26. Issue Forms (Final Set)

| Form | File | Key required fields | Auto-label | Notes |
|---|---|---|---|---|
| Bug Report | `bug_report.yml` | Summary, Steps to reproduce, Expected vs actual, Repo/version | `type:bug`, `status:triage` | |
| Feature Request | `feature_request.yml` | Problem, Proposed solution, Alternatives considered | `type:feature`, `status:triage` | |
| Idea Submission | `idea_submission.yml` (lives in `ideas` repo) | One-line idea, Problem it solves, Why Hidden Alchemy, Rough scope | `type:idea`, `status:triage`, `project-proposal` | Feeds §23 lifecycle |
| Project Proposal | `project_proposal.yml` | Links back to an accepted idea, Architecture sketch, Maintainer commitment | `type:architecture` | Used at the Architecture stage of §23, not for brand-new raw ideas |
| Research Proposal | `research_proposal.yml` | Research question, Method, Expected output | `type:research` | |
| Membership Interest | `membership_interest.yml` (lives in `community` repo) | GitHub handle, Summary of contributions with links, Areas of interest, Confirmation they've read GOVERNANCE.md | `membership:needs-review` | Governed by §20/§21 |

`ISSUE_TEMPLATE/config.yml` sets `blank_issues_enabled: false` and adds a contact link pointing to Discussions "Help" category for open-ended questions that aren't bugs/features/ideas.

Security note: none of these forms' automation is permitted to take any action beyond labeling/commenting (§21).

---

## 27. Discussion System

Categories (final, trimmed from the draft's list by merging "Show and Tell" into "General" since a lab this size doesn't yet need the split, and by keeping "Project Collaboration" only once a project exists to collaborate on — it is created at that point, not pre-created):

| Category | Purpose | Created |
|---|---|---|
| Announcements | Maintainer-only posts (releases, milestones reached) | NOW |
| Ideas | Open-ended brainstorming that hasn't yet been formalized into an Idea Submission issue | NOW |
| General | Everything else conversational, including show-and-tell | NOW |
| Research | Longer-form research discussion tied to `type:research` issues | NOW |
| Architecture | Design discussion preceding formal Project Proposals | NOW |
| Help | Questions that aren't bugs | NOW |
| Project Collaboration | Space for a specific active project's contributors | LATER, created when M9's flagship project ships |

Relationship to Issues: Discussions are for open-ended conversation; once something becomes actionable it graduates to an Issue Form (Idea Submission, Project Proposal, etc.). Moderation: Core Team members can lock/unpin; enforcement follows CODE_OF_CONDUCT.md's ladder.

---

## 28. Pull Request System

`PULL_REQUEST_TEMPLATE.md` requires:

- Linked issue (or explicit "no linked issue" with justification for small fixes)
- Summary of change
- Testing performed checklist
- Documentation impact checklist (does this PR require a README/CONTRIBUTING update?)
- Visual change checklist (screenshot required if UI/README-visual change)

Process is intentionally lightweight for current project maturity: one maintainer approval required for merge on any repo; no mandatory CI beyond what that specific repo defines for itself (repo-specific CI is out of this PRD's org-wide scope — see M9 for the flagship project's own testing requirements).

---

## 29. Automation Architecture — Workflow Specifications

All workflows live in `.github/workflows/` (org-wide defaults) unless a specific repo needs its own CI, which is defined separately in that repo (out of scope here except for the flagship project, M9).

### Workflow: `welcome-first-interaction.yml`
- **Purpose:** Post a single non-generic welcome comment on a user's first issue or PR in the org.
- **Trigger:** `issues: [opened]`, `pull_request_target: [opened]` — *(see note below on why `pull_request_target` risk is mitigated here)*
- **Trust level:** Untrusted (any public user)
- **Permissions:** `issues: write`, `pull-requests: write` only
- **Secrets:** None
- **Inputs:** Event payload only (author login, issue/PR number, labels present)
- **Steps:** (1) checkout is NOT performed — this workflow never checks out repository code, only reads event metadata and posts a comment, which eliminates the primary risk `pull_request_target` normally carries; (2) `actions/first-interaction@<pinned-sha>` checks contribution history via API; (3) if first interaction, post templated comment referencing CONTRIBUTING.md
- **Outputs:** One issue/PR comment
- **Failure behavior:** Log and exit non-zero; no retries (idempotency risk); does not block the issue/PR itself
- **Human override:** Maintainer can delete/edit the comment manually; no override mechanism needed pre-post
- **Tests:** Dry-run against a test issue in a scratch repo; verify comment posts exactly once; verify it does not repost on a second issue by the same now-returning user

### Workflow: `issue-labeler.yml`
- **Purpose:** Apply the correct `type:*` and `status:triage` label based on which Issue Form was used
- **Trigger:** `issues: [opened]`
- **Trust level:** Untrusted
- **Permissions:** `issues: write` only
- **Secrets:** None
- **Inputs:** Issue form's hidden form-ID field (Issue Forms tag their output; the workflow maps form ID → label set per §26 table)
- **Outputs:** Labels applied
- **Failure behavior:** If form ID doesn't match a known mapping, apply `status:triage` only and log a warning — never fail loudly on the user-facing issue
- **Human override:** Maintainers can always relabel manually
- **Tests:** One test issue per form type; verify correct label set

### Workflow: `repo-health-check.yml`
- **Purpose:** Scan default branch on push/PR for: missing LICENSE, missing/placeholder-TODO README, missing status line (§24), missing SECURITY.md reference
- **Trigger:** `push: [main]`, `pull_request` (same-repo only, not forks, to avoid needing elevated permissions on untrusted code)
- **Trust level:** Trusted for `push`; for `pull_request` from forks this check runs read-only (`contents: read` only) and simply reports pass/fail as a status check — it never writes anything
- **Permissions:** `contents: read`, `checks: write`
- **Secrets:** None
- **Outputs:** A GitHub status check (pass/fail) with a summary of missing items
- **Failure behavior:** Fails the check, does not block merge automatically unless branch protection (§30) is configured to require it for that repo's maturity tier
- **Tests:** Run against a fixture repo missing each required file one at a time; verify each is individually detected

### Workflow: `stale-triage.yml`
- **Purpose:** Label (never close) issues/PRs with no activity for 60 days, and membership-interest issues per §20's 21-day rule
- **Trigger:** `schedule` (daily) — this is the one workflow that is NOT triggered by untrusted public input, so it is treated as trusted/internal
- **Permissions:** `issues: write`, `pull-requests: write`
- **Secrets:** None
- **Outputs:** `status:stale`-equivalent label/comment (never auto-close in this PRD's scope — auto-close is deliberately excluded to avoid punishing legitimate slow-moving work)
- **Tests:** Dry-run mode first (label a scratch issue with an artificially old timestamp via test fixture)

**Cross-cutting rule for every workflow above:** every third-party Action referenced is pinned to a full commit SHA, not a floating version tag (supply-chain protection, §30).

---

## 30. Security Architecture

### 30.1 Organization ownership
- Organization Owner role limited to 1–2 people maximum for the duration of this PRD's scope. Any additional Owner grant is treated as an ambiguity requiring explicit sign-off, not something OpenCode ever performs autonomously.

### 30.2 GitHub Actions permissions
- Every workflow file must declare an explicit `permissions:` block at the top level with the minimum scopes needed (never rely on the default broad token permissions).
- No workflow in this PRD's scope uses `permissions: write-all` or requests `administration`, `organization-*`, or `packages` scopes.

### 30.3 Token & secret storage
- No org-level or repo-level secrets are required by any workflow defined in this PRD. If a future workflow appears to need a secret, that is explicitly out of scope until a separate security review amends this PRD.

### 30.4 Fork PR / `pull_request_target` policy
- `pull_request_target` is avoided everywhere in this PRD's scope (see §29's welcome workflow note). If any future workflow seems to require combining elevated permissions with untrusted code checkout, OpenCode must stop and flag it as an ambiguity rather than implement it — this is exactly the class of risk (secret exfiltration, injection) this PRD exists to prevent.

### 30.5 Action pinning (supply chain)
- All third-party GitHub Actions referenced anywhere in this org are pinned to a specific commit SHA (e.g., `actions/checkout@<sha>` not `@v4`). A comment beside each pin notes the human-readable version for maintainability. Dependabot (see below) is configured to open PRs bumping these pins, which still require human review/merge.

### 30.6 Dependabot
- Enabled at `.github/dependabot.yml` for `github-actions` ecosystem across the org's repos (via reusable config where GitHub allows), keeping pinned Action SHAs current via reviewed PRs — this is safe because Dependabot PRs from GitHub itself only *propose* a change; a human still merges it.

### 30.7 CODEOWNERS
- `.github/CODEOWNERS` at minimum assigns Core Team as owners of `.github/workflows/**`, `.github/CODEOWNERS` itself, and `SECURITY.md` — meaning any change to privileged automation or the security policy always requires Core Team review, even if branch protection for a given repo is otherwise lightweight.

### 30.8 SECURITY.md
- Defines a private vulnerability-reporting channel (GitHub's built-in "Report a vulnerability" private advisory feature — no email address or external form needed) and a stated (non-committal, since there's no dedicated security budget yet) response-time intention.

---

## 31. Branch Protection by Repository Maturity Tier

| Tier | Applies to | Rules |
|---|---|---|
| Experimental | `experiments` repo contents, prototype-stage repos | No required reviews; `repo-health-check` runs but does not block merge |
| Active Project | Any repo at `active` status (§24) | 1 required approving review; `repo-health-check` required to pass; direct pushes to `main` disabled |
| Flagship Project | The flagship repo (M9) | 1 required approving review + required status checks (health check + any project-specific CI) passing; direct pushes to `main` disabled; force-push disabled |
| Critical Infrastructure | `.github` repo itself | 1 required approving review from CODEOWNERS specifically (not just any maintainer) for changes under `workflows/` or `CODEOWNERS`; direct pushes disabled |

A repo's tier is set manually by its maintainer as part of that repo's setup/status changes — never inferred automatically.

---

## 32. Contributor Recognition System

Non-gamified, honest mechanisms only:

- **Recognition log**: `community/RECOGNITION.md` — a plain, chronological list of first-time contributors and notable sustained contributions, updated manually by a maintainer when merging a first-time PR or accepting an idea. Not a leaderboard; no points.
- **Release notes**: any repo that ships a tagged release credits contributors to that release by GitHub handle in the release notes (native GitHub "Generate release notes" feature, which already does this correctly — no custom automation needed).
- **Project acknowledgements**: each project README's "Maintainers" block (§15, block I) may also list "Contributors" for people with sustained, non-maintainer contribution, added manually.
- Explicitly excluded: badges/points/levels displayed on profile, automated "milestone" comment spam, leaderboards.

---

## 33. Community Governance

`GOVERNANCE.md` (lightweight, matching current scale) covers:

- **Decision-making**: Core Team makes org-wide decisions by simple consensus; repo-specific decisions belong to that repo's maintainer(s); disagreements escalate to Core Team.
- **Project ownership**: each active repository has exactly one accountable maintainer (may be more than one person, but one is always designated primary) recorded in that repo's README "Maintainers" block and in CODEOWNERS if applicable.
- **Conflict resolution**: informal discussion first; Core Team makes a final call if unresolved; CODE_OF_CONDUCT.md enforcement ladder applies for conduct issues specifically (separate from ordinary technical disagreement).
- **Archival decisions**: a repo's maintainer proposes archival; Core Team confirms; archived per §24.
- **Leadership changes**: Core Team appointment/removal requires Organization Owner sign-off given the org's current small size; this is explicitly marked as something to revisit ("WHEN SCALE REQUIRES IT") once Core Team exceeds ~5 people.

Explicitly deferred to **LATER**/**WHEN SCALE REQUIRES IT**: formal RFC process, voting procedures, elected leadership terms, sub-committees. Building these now would be bureaucracy without a community large enough to need it (§6 principle 8, §57 anti-pattern "Permission Explosion"/complexity-before-need).

---

## 34. Organization Documentation Architecture

Source-of-truth rules (prevents duplication):

| Content | Lives in | Never duplicated in |
|---|---|---|
| How to contribute (general) | `.github/CONTRIBUTING.md` | Individual repo READMEs (they link to it instead) |
| Code of Conduct | `.github/CODE_OF_CONDUCT.md` | Anywhere else |
| Governance model | `.github/GOVERNANCE.md` | `community` repo may summarize with a link, never restate rules |
| Membership criteria | `.github/GOVERNANCE.md` (§19 content) | Profile README links to it rather than restating full criteria |
| Repo-specific setup/usage | That repo's own README | Not referenced elsewhere |
| Security reporting | `.github/SECURITY.md` | Every repo inherits this automatically via GitHub's org-default-file behavior — no per-repo copy needed |

---

## 35. Visual Identity — README Motion & Component Guidance

Motion system: at most two animated elements exist in the entire org profile (the hero pipeline diagram's node-highlight drift, and optionally a slow directional flow indicator on the contribution-pathway diagram). No other repository README uses animation — project READMEs are static, consistent with "complexity should become invisible" and avoiding a maintenance burden across many repos.

Visual language: engineered-alchemy, not fantasy — pipeline nodes rendered as clean geometric shapes (hexagon/circle) connected by directional lines, using Gold/Verdigris as signal-color accents against Ink/Bone, not literal alchemical symbols, no potion/wizard iconography.

---

## 36. Community Experience Design / 37. First-Time Experience

(Journeys already specified in §11; this section defines the success metric per stage for measurement purposes only — see §38 for the metrics themselves.)

| Stage | User question answered | Interface | Success signal |
|---|---|---|---|
| First visit | "What is this?" | Profile README hero | Time-to-scroll-past-hero (qualitative, not instrumented — no tracking scripts per NG6) |
| Understanding | "What do they actually build?" | Alchemy Process + What We Build sections | — |
| Exploration | "Is anything real here?" | Active Systems table | Non-empty table (tracked manually as a milestone gate, not a live metric) |
| Participation | "Can I actually do something?" | How to Participate + labels | Count of `good first issue` currently open (manual spot-check) |
| Contribution | "Did it work?" | PR/issue flow + welcome automation | First-interaction comment delivered correctly |
| Recognition | "Did anyone notice?" | RECOGNITION.md, release notes | Entry added within 1 week of merge |

---

## 38. Metrics (Honest Only)

| Metric | Purpose | Collection | Review cadence |
|---|---|---|---|
| New first-time contributors / month | Health of top-of-funnel | Manual count via GitHub Insights + welcome-workflow logs | Monthly, Core Team |
| Merged PRs / month | Real output | GitHub Insights | Monthly |
| Idea → Active Project conversion rate | Is the pipeline actually working | Manual tally against `ideas` repo issue closures | Quarterly |
| Issue response time (time to first maintainer reply) | Contributor experience | GitHub Insights | Monthly |
| Membership requests reviewed within 21 days | Process integrity (§20) | Manual audit of `community` repo issues | Monthly |
| Active repositories at `active`+ status | Prevents fake-org appearance | Manual count vs. §12 table | Quarterly |

Explicitly excluded as vanity metrics: star count, follower count, view/traffic counters (per §57).

---

## 39/40. Roadmap & Milestones — Overview

Refined milestone order (dependency-corrected from the prompt's draft — Security Hardening is folded into each milestone incrementally rather than bolted on at M8, since e.g. workflow permissions must be correct the moment a workflow is created, not retrofitted; Membership is sequenced after Automation Foundation since it depends on issue forms + labeler already existing):

- **M0 — Discovery & Baseline**
- **M1 — Organization Foundation** (`.github` repo skeleton, community health files, license/CODEOWNERS)
- **M2 — Identity & Profile Experience** (profile README, visual assets)
- **M3 — Contribution Infrastructure** (issue forms, labels, PR template, CONTRIBUTING.md)
- **M4 — Automation Foundation** (welcome/labeler/health-check/stale workflows, all security-reviewed at creation time)
- **M5 — Community Repos** (`community`, `ideas` repos live)
- **M6 — Idea & Project Incubation Live** (idea lifecycle operating end-to-end)
- **M7 — Membership System** (membership form + manual review process live, per strict §21 security boundary)
- **M8 — Governance & Branch Protection Hardening** (GOVERNANCE.md finalized, branch protection tiers applied)
- **M9 — Flagship Project Integration**
- **M10 — Organization Health & Scale Review**

Each milestone below is expanded into phases and atomic tasks. M0–M4 are specified to full task-level depth as the exemplar format; M5–M10 are specified at phase level with the same task format required but with representative (not exhaustively enumerated) tasks — OpenCode must apply the identical task template (§45 format) when generating the remaining tasks within each listed phase, and must stop and request clarification (per the No-Assumption Rule) rather than invent scope beyond what each phase's objective states.

---

## M0 — Discovery & Baseline

**Objective:** Establish ground truth about the current state of the Hidden Alchemy organization before changing anything.
**Why this exists:** OpenCode must never overwrite existing intentional work (Rule 3, §51) — this is impossible without first knowing what exists.
**Prerequisites:** Read access to the Hidden Alchemy GitHub organization.

### Phase 0.1 — Inventory

**TASK 0.1.1 — Enumerate existing repositories**
- Objective: Produce a complete list of current repos, their visibility, last-commit date, and whether they contain real content or are empty.
- Preconditions: none
- Files to create: `IMPLEMENTATION_LOG.md` (org root of `.github` once it exists, or a scratch tracking location if `.github` doesn't exist yet) — begin the log here.
- Exact requirements: use the GitHub API/UI to list all repos under the org; record name, visibility, description, last push date, default branch, whether it has a LICENSE/README already.
- Test procedure: cross-check the count against the org's public repo count shown on the org page.
- Acceptance criteria: [ ] every existing repo is listed with the above fields; [ ] no repo is missed.

**TASK 0.1.2 — Inventory existing org-level settings**
- Objective: Record current organization role assignments (Owners, Members), existing teams, existing org-wide default files if any `.github` repo already exists.
- Files to create: entry in `IMPLEMENTATION_LOG.md`
- Test procedure: manual review against GitHub org People/Teams pages.
- Acceptance criteria: [ ] Owners list recorded; [ ] Teams list recorded (expect empty/minimal); [ ] existing `.github` repo contents recorded if present, otherwise explicitly noted as absent.

**TASK 0.1.3 — Confirm brand constants**
- Objective: Confirm the Gold `#BD9C61` / Verdigris `#4C6B5C` hex values and any existing logo/wordmark assets are still current (do not silently invent new brand values).
- Test procedure: check for any existing brand assets in the org or linked external brand doc.
- Acceptance criteria: [ ] confirmed values recorded in the log, or [ ] flagged as an ambiguity if conflicting values are found (per the No-Assumption Rule — do not guess which is correct).

### Phase 0.1 completion checklist
- [ ] All tasks above complete
- [ ] `IMPLEMENTATION_LOG.md` exists with M0 entries
- [ ] No ambiguities outstanding, or all ambiguities explicitly documented for human resolution before M1 begins
- [ ] **Explicit sign-off required before proceeding to M1**

---

## M1 — Organization Foundation

**Objective:** Create the `.github` repository skeleton and baseline community health/security files.
**Prerequisites:** M0 signed off.

### Phase 1.1 — Repository creation

**TASK 1.1.1 — Create `.github` repository**
- Objective: Create the public `.github` repository per §12/§13.
- Preconditions: Confirmed via M0 that it does not already exist with conflicting content; if it exists, this task becomes "audit and reconcile" instead of "create," and OpenCode must not overwrite existing files without a diff review noted in the log.
- Files to create: repository itself, `LICENSE` (MIT, per §12.1 default), root `README.md` (brief, explaining this repo is org-wide configuration — distinct from `profile/README.md`).
- Test procedure: repository is visible at `github.com/Hidden-Alchemy/.github`.
- Acceptance criteria: [ ] repo exists; [ ] LICENSE present; [ ] root README present and distinguishes itself from the profile README.

**TASK 1.1.2 — Scaffold directory structure**
- Objective: Create the full directory tree from §13.
- Files to create: `profile/`, `assets/svg/`, `assets/og/`, `ISSUE_TEMPLATE/`, `workflows/`, `templates/` (empty placeholder directories won't persist in git — create with a `.gitkeep` or the first real file for each, whichever lands first per the milestone sequence below).
- Test procedure: `git ls-tree` shows expected structure.
- Acceptance criteria: [ ] structure matches §13 exactly, no extra speculative files (Rule 4, §51).

### Phase 1.2 — Baseline community health files

**TASK 1.2.1 — CODE_OF_CONDUCT.md**
- Objective: Adapt Contributor Covenant 2.1 with Hidden Alchemy's tone (precise, not saccharine) while keeping all enforcement substance intact.
- Test procedure: verify GitHub recognizes it as the org-wide Code of Conduct (shown in repo "Insights > Community Standards" for repos inheriting it).
- Acceptance criteria: [ ] file present; [ ] enforcement contact method defined (points to SECURITY.md-style private reporting or a maintainer contact — must not be a dead email).

**TASK 1.2.2 — SECURITY.md**
- Objective: Define vulnerability reporting via GitHub private security advisories per §30.8.
- Acceptance criteria: [ ] file present; [ ] private reporting path explained; [ ] no external email/form required.

**TASK 1.2.3 — SUPPORT.md**
- Objective: Direct questions to Discussions "Help" category vs. bug reports to Issue Forms.
- Acceptance criteria: [ ] file present; [ ] correctly distinguishes support vs. bug vs. feature.

**TASK 1.2.4 — CODEOWNERS**
- Objective: Implement §30.7's ownership rules.
- Files to create: `.github/CODEOWNERS`
- Exact requirements: assign Core Team (placeholder team handle `@Hidden-Alchemy/core` — created in Phase 1.3) as owner of `workflows/**`, `CODEOWNERS` itself, `SECURITY.md`.
- Acceptance criteria: [ ] file present; [ ] correct paths covered; [ ] referenced team exists (dependency on Phase 1.3 — sequence CODEOWNERS finalization after team creation, or create the team first).

### Phase 1.3 — Baseline teams

**TASK 1.3.1 — Create `core` team**
- Objective: Create the `core` team per §22.1, with the current Organization Owner(s) as initial members (no new people added without a human decision — OpenCode does not invent membership).
- Test procedure: team visible under org Teams.
- Acceptance criteria: [ ] team exists; [ ] initial membership matches M0's recorded Owners list exactly, or is flagged as an ambiguity if unclear who should be on it.

**TASK 1.3.2 — Create `community` team**
- Objective: Create the `community` team per §22.1, initially empty (populated only through the M7 membership process).
- Acceptance criteria: [ ] team exists; [ ] empty at creation, which is expected and correct, not a defect.

### Phase 1.4 — License & governance stub

**TASK 1.4.1 — GOVERNANCE.md (lightweight stub for M1; full content finalized in M8)**
- Objective: Create the file with the decision-making/ownership/conflict-resolution content from §33 already correct at this stage (this content doesn't depend on later milestones), leaving a placeholder section for membership criteria to be finalized once M7 confirms the process is live end-to-end.
- Acceptance criteria: [ ] file present; [ ] §33 content complete; [ ] membership section clearly marked as "finalized in M7," not silently incomplete.

### M1 completion checklist
- [ ] All Phase 1.1–1.4 tasks pass acceptance criteria
- [ ] `repo-health-check` cannot yet run (workflows come in M4) — this is expected, not a blocker
- [ ] Manual review: directory structure matches §13 exactly
- [ ] Implementation log updated
- [ ] **Explicit sign-off required before proceeding to M2**

---

## M2 — Identity & Profile Experience

**Objective:** Ship the organization profile README and its visual assets per §14/§16.
**Prerequisites:** M1 signed off (need `.github/profile/` and `.github/assets/` to exist).

### Phase 2.1 — Visual assets

**TASK 2.1.1 — Build `hero-pipeline.svg`**
- Objective: Create the transformation-pipeline diagram per §14.1 section 1 and §16's technical constraints.
- Exact requirements: 6 nodes (IDEA/CONCEPT/ARCHITECTURE/SYSTEM/AUTOMATION/REALITY) connected left-to-right (or top-to-bottom for mobile-safe `viewBox` scaling), Gold/Verdigris accent colors, dual-mode-safe background handling (transparent background, `currentColor`-aware text where possible, or two explicit color values verified against both `#0d1117` and `#ffffff`), `<title>`/`<desc>` present, under 150KB, subtle optional `<animate>` node-highlight drift.
- Test procedure: render in a local browser against both dark and light backgrounds side-by-side; embed in a scratch Markdown file and preview via GitHub's README preview to confirm actual GitHub rendering (not just raw SVG viewing).
- Acceptance criteria: [ ] readable in both modes; [ ] under size limit; [ ] accessible title/desc present; [ ] static frame alone (animation disabled) still fully communicates the pipeline.

**TASK 2.1.2 — Build `contribution-pathway.svg`**
- Objective: Diagram for §17's pathway (`EXPLORE → DISCUSS → CONTRIBUTE → COLLABORATE → RECOGNITION → TRUST → MEMBERSHIP ELIGIBILITY`).
- Requirements/tests/acceptance: identical structure to Task 2.1.1.

**TASK 2.1.3 — Org social preview image**
- Objective: Static PNG fallback (`assets/og/org-social-preview.png`) used for link-unfurl previews (GitHub org settings, not embedded in the README itself).
- Acceptance criteria: [ ] correct dimensions per GitHub's social preview spec (1280×640); [ ] uploaded to org settings, not just committed to the repo.

**TASK 2.1.4 — `assets/svg/README.md` usage doc**
- Objective: Document naming convention and reference-URL pattern from §16 so future assets follow the same rules.
- Acceptance criteria: [ ] file present; [ ] naming rule stated; [ ] raw-URL reference pattern documented with a real example.

### Phase 2.2 — Profile README assembly

**TASK 2.2.1 — Draft the 8 sections per §14.1**
- Objective: Write `profile/README.md` content section by section, in the specified order, with the Active Systems table starting in its correct **empty state** (no fabricated entries — see §14 rule).
- Files to modify: `.github/profile/README.md`
- Exact requirements: embed `hero-pipeline.svg` and `contribution-pathway.svg` via the raw-URL pattern from §16; include working links to (stub, not-yet-existing-until-M3) CONTRIBUTING.md and issue forms — these links are written now but will only resolve correctly once M3 lands; note this dependency in the task rather than treating it as done.
- Test procedure: GitHub Markdown preview, both color modes, desktop and mobile viewport widths.
- Acceptance criteria: matches §14.3's full checklist exactly.

### M2 completion checklist
- [ ] Both SVGs pass their acceptance criteria
- [ ] Profile README passes §14.3 checklist
- [ ] Known limitation logged: some links will 404 until M3 completes (acceptable, documented, not silently ignored)
- [ ] Manual QA: screenshot comparison, dark vs. light mode, saved to implementation log
- [ ] **Explicit sign-off required before proceeding to M3**

---

## M3 — Contribution Infrastructure

**Objective:** Make first contribution possible end-to-end: CONTRIBUTING.md, issue forms, labels, PR template.
**Prerequisites:** M2 signed off.

### Phase 3.1 — Labels

**TASK 3.1.1 — Create org-wide label set**
- Objective: Implement the exact taxonomy from §25 as the default label set applied to every repo (via GitHub's org default label management, or scripted application to each existing repo since GitHub doesn't universally propagate label-set changes automatically to already-existing repos).
- Exact requirements: every label from §25 created with a consistent color scheme (one color family per facet: difficulty=blue tones, type=purple tones, priority=red/orange/yellow/green scale, status=gray-to-green scale, community=gold-accent).
- Test procedure: verify label list on `.github` repo and on `ideas`/`community` repos once they exist (cross-reference in M5).
- Acceptance criteria: [ ] all labels from §25 present with no extras; [ ] color scheme is consistent and documented in the implementation log for reuse.

### Phase 3.2 — Issue Forms

**TASK 3.2.1 — `config.yml`**
- Objective: Disable blank issues, add contact link to Discussions Help.
- Acceptance criteria: [ ] `blank_issues_enabled: false`; [ ] contact link present and correct.

**TASK 3.2.2 through 3.2.7 — One task per form** (`bug_report.yml`, `feature_request.yml`, `idea_submission.yml`, `project_proposal.yml`, `research_proposal.yml`, `membership_interest.yml`)
- Objective (per form): implement exactly the required fields listed in §26's table, as native GitHub Issue Form YAML (`type: input/textarea/dropdown/checkboxes` as appropriate), each requiring the listed fields as `required: true`.
- Note on placement: `idea_submission.yml` and `membership_interest.yml` are drafted here but their canonical home is the `ideas` and `community` repos respectively (created in M5) — draft and validate the YAML now in `.github` as the template source, then copy at M5 Phase 5.x into the correct repo's own `ISSUE_TEMPLATE/` folder, since GitHub Issue Forms must live in the repo they apply to (the org-wide `.github` fallback applies only to repos that don't define their own).
- Test procedure: submit a test issue through each form in a scratch/test context; verify required-field enforcement blocks submission when empty.
- Acceptance criteria per form: [ ] all required fields from §26 present and enforced; [ ] auto-label mapping documented for Phase 4's labeler workflow to consume.

### Phase 3.3 — CONTRIBUTING.md

**TASK 3.3.1 — Write CONTRIBUTING.md**
- Objective: Cover §17's entry points by type, link to CODE_OF_CONDUCT.md, explain the label taxonomy in plain language, explain PR expectations (links to PR template), explicitly state "organization membership is separate from contributing" (per §19's canonical language) with a link to GOVERNANCE.md for detail.
- Acceptance criteria: [ ] a reader with zero context can identify their entry point within the document in under 2 minutes (manual QA read-through); [ ] all internal links resolve.

### Phase 3.4 — PR Template

**TASK 3.4.1 — `PULL_REQUEST_TEMPLATE.md`**
- Objective: Implement exactly the checklist from §28.
- Acceptance criteria: [ ] all four checklist items present; [ ] renders correctly as the default PR body when opening a test PR.

### M3 completion checklist
- [ ] All labels, forms, CONTRIBUTING.md, PR template complete and tested
- [ ] Profile README's links to CONTRIBUTING.md and forms now resolve correctly (close out M2's known limitation)
- [ ] Manual QA: full first-time-contributor simulation performed (open each issue form as a test, confirm experience is coherent)
- [ ] **Explicit sign-off required before proceeding to M4**

---

## M4 — Automation Foundation

**Objective:** Ship the four workflows from §29 with security review built in at creation time (not retrofitted).
**Prerequisites:** M3 signed off (workflows depend on labels/forms existing).

### Phase 4.1 — Welcome automation

**TASK 4.1.1 — Implement `welcome-first-interaction.yml`**
- Objective: Exactly per §29's specification.
- Security constraints: permissions block limited to `issues: write, pull-requests: write`; no checkout step; third-party action pinned to commit SHA.
- Test procedure: per §29's test description, using a scratch repo/test account to simulate a first-time issue/PR.
- Acceptance criteria: [ ] comment posts exactly once per first-time author; [ ] permissions block verified minimal; [ ] action pin verified as a SHA, not a tag.

### Phase 4.2 — Labeler automation

**TASK 4.2.1 — Implement `issue-labeler.yml`**
- Objective/security/test: per §29.
- Acceptance criteria: [ ] correct label applied per form type from Phase 3.2's mapping; [ ] unknown form IDs fall back safely to `status:triage` only, without error surfaced to the issue author.

### Phase 4.3 — Repo health check

**TASK 4.3.1 — Implement `repo-health-check.yml`**
- Objective/security/test: per §29, including the fork-PR read-only constraint.
- Acceptance criteria: [ ] correctly detects each of the four missing-file conditions individually in a fixture test; [ ] fork PR run uses `contents: read` only, verified in the permissions block.

### Phase 4.4 — Stale triage

**TASK 4.4.1 — Implement `stale-triage.yml`**
- Objective/security/test: per §29, dry-run first.
- Acceptance criteria: [ ] labels (never closes) stale issues/PRs after 60 days; [ ] membership-interest issues flagged at 21 days per §20; [ ] dry-run results reviewed manually before enabling schedule trigger for real.

### M4 completion checklist
- [ ] All four workflows implemented, tested, and security-reviewed against §21/§30's rules
- [ ] No workflow requests a secret or PAT (verified by inspection)
- [ ] No workflow uses `pull_request_target` (verified by inspection)
- [ ] Implementation log updated with test results for each workflow
- [ ] **Explicit sign-off required before proceeding to M5**

---

## M5 — Community Repositories (`community`, `ideas`)

**Objective:** Bring the `community` and `ideas` repositories live per §12, hosting the membership-interest and idea-submission forms in their correct final location (per Phase 3.2's note), plus `RECOGNITION.md` and `GOVERNANCE.md`'s public-facing copy.

**Phase 5.1 — Create `community` repo**: apply §12.1 checklist; add `GOVERNANCE.md` (linked from, not duplicated out of, `.github/GOVERNANCE.md` — see §34 rule, so this is a thin repo-specific README pointing to the canonical file, plus `RECOGNITION.md` per §32, plus the `membership_interest.yml` form copied from Phase 3.2's draft).

**Phase 5.2 — Create `ideas` repo**: apply §12.1 checklist; add the `idea_submission.yml` and `project_proposal.yml` forms copied from Phase 3.2's drafts; add a README (community-type template from §15) explaining the lifecycle from §23; set up a GitHub Project board with columns matching the §23 stages for visual tracking.

**Phase 5.3 — Discussions setup**: enable Discussions on the org's primary community-facing repo (`community` or the org itself, per current GitHub org-Discussions capability at implementation time — verify which is technically correct rather than assuming); create the 6 "NOW" categories from §27.

Each phase follows the same task/test/acceptance-criteria format as M1–M4 (§45). Completion checklist: [ ] both repos live and pass repo-health-check; [ ] both forms functional and correctly labeled by the M4 labeler workflow (cross-repo — verify the org-wide workflow applies, or install repo-local copies if GitHub requires it); [ ] Discussions categories live; **explicit sign-off required before M6.**

---

## M6 — Idea & Project Incubation Live

**Objective:** Validate the full §23 lifecycle operates end-to-end with a real or realistic test idea, and update the profile README's Active Systems / Experimental Lab sections to link to the now-live `ideas` repo.

**Phase 6.1 — End-to-end lifecycle test**: submit a real (not fabricated-for-show, per §6 principle 3) idea through the form; walk it manually through Raw Idea → Under Review → Research stages to confirm labels, project board movement, and maintainer workflow all function; document any friction found.

**Phase 6.2 — Profile README update**: update §14.1 section 5 (Experimental Lab) to link the live `ideas` repo; leave Active Systems empty/honest until a real project graduates (per §14's empty-state rule) — do not fill it prematurely.

Completion checklist: [ ] at least one idea has moved through at least two lifecycle stages for real; [ ] profile README updated and re-passes §14.3 acceptance criteria; **sign-off required before M7.**

---

## M7 — Membership System Live

**Objective:** Activate the Membership Interest form and human-review process end-to-end, strictly honoring the §21 security boundary (no automated invitation, ever).

**Phase 7.1 — Activate the form**: confirm `membership_interest.yml` (already placed in `community` in M5) is correctly labeled by automation; confirm the acknowledgement comment behavior works.

**Phase 7.2 — Dry-run the review process**: Core Team performs a full manual review cycle on a test submission, including the manual out-of-band invitation step (§20.1 checklist), to confirm the process is usable — this validates the *process*, not automation, since the critical step is deliberately manual.

**Phase 7.3 — Finalize GOVERNANCE.md's membership section**: replace the M1 placeholder (Task 1.4.1) with the confirmed, tested criteria and process description, referencing §19/§20/§21 content faithfully.

Completion checklist: [ ] form live and tested; [ ] at least one full dry-run review cycle completed and logged; [ ] GOVERNANCE.md membership section finalized (no placeholders remain — verified by the repo-health-check's TODO-scan, §15); **sign-off required before M8.**

---

## M8 — Governance & Branch Protection Hardening

**Objective:** Apply §31's branch-protection tiers to every existing repository and finalize GOVERNANCE.md in full.

**Phase 8.1 — Tier assignment**: for each existing repo (per current §24 status), assign and apply the correct branch protection tier from §31.

**Phase 8.2 — CODEOWNERS verification**: re-verify `.github/CODEOWNERS` correctly gates `workflows/**` and `CODEOWNERS` itself now that `core` team membership may have evolved since M1.

**Phase 8.3 — Full security self-audit**: walk every workflow file against §30's checklist (permissions minimal, no secrets, no floating tags, no `pull_request_target`) as a final verification pass, documented in the implementation log.

Completion checklist: [ ] every repo has branch protection matching its tier; [ ] CODEOWNERS current; [ ] security audit log complete with zero unresolved findings; **sign-off required before M9.**

---

## M9 — Flagship Project Integration

**Objective:** Select and scaffold the one flagship project (§19 of the original brief / §12 table) that demonstrates the IDEA→REALITY pipeline for real.

**Phase 9.1 — Flagship selection**: apply explicit criteria — community value, contributor accessibility (can a newcomer meaningfully help within their first PR), technical feasibility with current maintainer capacity, alignment with the domain list in §14.1 section 3. Candidate alignment noted in the original brief: an AI-assisted idea-to-system tool would be thematically perfect (it literally implements the org's own pipeline) — but this must be confirmed as strategically justified by Core Team, not assumed by OpenCode, since committing a flagship project is a judgment call, not a mechanical task. **This is flagged explicitly as a decision point requiring human confirmation before Phase 9.2 begins.**

**Phase 9.2 — Repository creation**: apply the full §12.1 checklist and §15 flagship README template; set status `concept` or `prototype` (§24) honestly based on actual state — do not mark `active` prematurely.

**Phase 9.3 — Profile README Active Systems update**: once the flagship project reaches genuine `active` status, update §14.1 section 4 to list it for real, closing out the honest-empty-state placeholder from M2/M6.

**Phase 9.4 — Discussions "Project Collaboration" category**: create this category (§27, marked LATER) now that a real project exists to collaborate on.

Completion checklist: [ ] flagship project selection explicitly confirmed by Core Team (not OpenCode-assumed); [ ] repo created per checklist; [ ] README passes flagship template requirements; [ ] profile README updated only when status is genuinely earned; **sign-off required before M10.**

---

## M10 — Organization Health & Scale Review

**Objective:** Confirm the full system holds together as a coherent whole and define what triggers future expansion.

**Phase 10.1 — Full acceptance sweep**: re-run every acceptance-criteria checklist from M1–M9 in one pass to confirm nothing has drifted.

**Phase 10.2 — Metrics baseline**: record initial values for every §38 metric as the baseline for future review — this is the first data point, not a judgment of success/failure yet.

**Phase 10.3 — Future-expansion triggers documented**: record explicit, concrete thresholds (not vague aspirations) that would justify revisiting NG1's domain-team restriction, §33's lightweight-governance restriction, and §12's single-flagship restriction — e.g., "create a domain team when ≥2 people are sustained-active on a specific non-flagship project," "revisit formal RFC process when Core Team exceeds 5 people." These thresholds are recorded in `GOVERNANCE.md` as a "Future Expansion" appendix, not acted upon now.

Completion checklist: [ ] full sweep passes with zero regressions; [ ] metrics baseline recorded; [ ] expansion triggers documented; [ ] final Definition of Done (§F below) verified in full; **this is the terminal sign-off for the PRD's scope.**

---

## Testing Strategy (Cross-Milestone)

- **Documentation testing**: link-checking (every internal Markdown link resolves) performed manually at the end of every milestone that touches documentation, using GitHub's own rendering as the source of truth.
- **README testing**: dark/light mode + mobile width, manual screenshot comparison, at M2, M5, M9, and M10.
- **Workflow testing**: dry-run/fixture-repo testing before enabling any schedule- or event-triggered workflow for real, per each M4 task's test procedure.
- **Security testing**: permissions-block inspection, secret-usage inspection, and action-pin inspection performed at workflow creation (M4) and re-verified at M8's full audit.
- **Community flow testing**: full persona simulation (new visitor, beginner contributor, project proposer, membership requester, maintainer) performed at M6 (idea flow) and M7 (membership flow) specifically, and again as part of M10's full sweep.

## Manual QA Requirements (Cannot Be Automated)

- README visual/animation quality — human screenshot review, both color modes
- Mobile rendering — human review on an actual narrow viewport
- Onboarding clarity — a human reading CONTRIBUTING.md fresh, timing how long it takes to find "what do I do first"
- Permission safety — human review of every `permissions:` block before a workflow is enabled for real
- Membership review-and-invitation process — inherently human by design (§21)

## Failure & Recovery Strategy

- **README asset failure** (broken raw-URL link, malformed SVG): restore from git history, re-verify the raw-URL path, re-render, re-test before continuing.
- **Workflow failure**: inspect Actions logs, identify root cause, fix, re-run the specific test from that workflow's task spec, do not proceed to dependent tasks until it passes.
- **Privileged-boundary concern** (any moment a workflow seems to need a secret, PAT, or `pull_request_target`): immediately halt that task, log it as a blocked ambiguity in `IMPLEMENTATION_LOG.md`, and do not implement a workaround — this requires explicit human security review, not agent judgment.

## Implementation Logging

`IMPLEMENTATION_LOG.md` lives at the root of the `.github` repository (started in M0 before `.github` exists as a scratch doc, then moved in as the first real commit of M1). Each entry records: milestone, phase, date, files changed, tests run and results, failures and fixes, and completion status. No redundant per-repo logs are created — this is the single source of truth.

---

## Anti-Patterns — Explicitly Prohibited (Binding)

- **Fake Organization Syndrome**: never create repos/teams ahead of real need (enforced throughout §12, §22.2).
- **Template README Syndrome**: never ship a README that is just Logo/Badges/About/Installation/Contributing/License with no identity (enforced by §14/§15's specific section requirements and the repo-health-check's TODO scan).
- **Automation Theater**: every workflow in §29 exists to remove specific, named toil — none exist "to look advanced."
- **Permission Explosion**: enforced by §22.3/§30's least-privilege rules throughout.
- **Repository Sprawl**: enforced by §12.1's creation checklist and the explicit DO NOT CREATE entries in §12.
- **Generic Community Language**: CONTRIBUTING.md and profile README language must reference Hidden Alchemy's actual pipeline/identity, never generic "welcome to our amazing community" phrasing (manual QA check at M2/M3).
- **Visual Gimmicks**: enforced by §14.2/§35's motion and asset constraints.

---

## OpenCode Implementation Protocol (Binding Rules)

1. Read the entire current milestone's specification before editing anything.
2. Inspect existing repository/file structure before creating files — never assume a clean slate (see M0).
3. Never overwrite existing intentional work without a logged diff review.
4. Do not create speculative files not named in this PRD.
5. Do not skip any test procedure listed in a task.
6. Do not continue to the next task after a failed test in the current task.
7. Fix the failure before continuing; if the fix requires a decision this PRD doesn't cover, stop and log it as an ambiguity instead of guessing.
8. Do not begin the next phase until the current phase's completion checklist is fully satisfied.
9. Do not begin the next milestone until explicit sign-off is recorded for the current one.
10. Do not make architectural changes outside the current phase's stated scope.
11. Do not introduce any new dependency (Action, library, service) not already named in this PRD without explicit approval.
12. Never expose a secret in a workflow log, commit, or comment.
13. Never implement privileged automation triggered by untrusted public input — see §21's binding rule.
14. Verify GitHub-specific behavior (Issue Forms syntax, Actions permissions syntax, org Discussions availability) against current GitHub documentation at implementation time rather than assuming remembered syntax is current.
15. Maintain `IMPLEMENTATION_LOG.md` continuously, not retroactively.
16. Produce a Phase Completion Report (format below) at the end of every phase, and a Milestone sign-off record at the end of every milestone.

### No-Assumption Rule

When ambiguity exists: (1) inspect existing documentation/architecture for a prior decision; (2) if none exists, stop; (3) document the ambiguity precisely in `IMPLEMENTATION_LOG.md`; (4) request clarification rather than guessing — especially for anything touching security, permissions, organization ownership, destructive operations, privileged tokens, repository deletion, contributor removal, or membership invitations, where autonomous guessing is never acceptable.

### Phase Completion Report Format

```
PHASE:
STATUS: [COMPLETE | BLOCKED]
OBJECTIVE:
FILES CREATED:
FILES MODIFIED:
AUTOMATION CREATED:
TESTS RUN:
TEST RESULTS:
MANUAL VERIFICATION:
KNOWN LIMITATIONS:
SECURITY REVIEW:
ACCEPTANCE CRITERIA: [checklist with pass/fail per item]
NEXT STEP:
BLOCKERS:
```
If `STATUS: BLOCKED`, implementation halts on that phase until the blocker is resolved by a human decision.

---

## Risks

| Risk | Mitigation |
|---|---|
| README visual ambition breaks GitHub rendering in one color mode | Mandatory dual-mode manual QA at every README-touching milestone (§14.3, M2/M5/M9/M10) |
| Automation scope creep into privileged territory | Hard binding rule in §21, reinforced in OpenCode Protocol rule 13 |
| Repository sprawl reintroduced later by well-meaning maintainers | §12.1 checklist is process, not just a one-time PRD instruction — GOVERNANCE.md must carry it forward |
| Empty Active Systems section undermines credibility indefinitely | M9's flagship project exists specifically to resolve this; §14's honest-empty-state is an interim, not permanent, acceptable state |
| Core Team single point of failure (1–2 Owners) | Documented as a known current-scale limitation in GOVERNANCE.md, revisited per M10's expansion triggers |
| Third-party Action supply-chain compromise | SHA-pinning + Dependabot review process (§30.5/§30.6) |

## Future Expansion (Explicitly Deferred, Not Built Now)

- Domain teams (AI/Design/Research) — trigger defined in M10.3
- Formal RFC/voting governance — trigger defined in M10.3
- Second flagship project — only after the first reaches genuine `stable`/`maintained` status
- Mentorship program — only after sustained `good first issue` volume justifies it
- `experiments` repo — created at the first real experiment, not before (§12)

## Final Definition of Done

The initiative is complete only when all of the following are true simultaneously, not merely when files exist:

- [ ] Organization profile README communicates identity and the pipeline within one screen, passes §14.3 in both color modes
- [ ] Repository architecture matches §12 exactly, with zero sprawl and zero unjustified files
- [ ] A complete, tested first-contribution pathway exists (CONTRIBUTING, forms, labels, PR template)
- [ ] Idea lifecycle (§23) has processed at least one real idea through at least two stages
- [ ] Membership pathway (§19–§21) is live, security-bounded, and has completed at least one full dry-run review cycle
- [ ] All automation is tested, minimally-permissioned, and contains zero privileged actions triggered by untrusted input
- [ ] Branch protection tiers (§31) applied across all repositories per their actual maturity
- [ ] GOVERNANCE.md is complete with no placeholder sections
- [ ] README design system (§15) is in place and reusable, with templates for every repo type
- [ ] At least one repository carries an honest, non-empty `active` or better lifecycle status (from the flagship project, M9)
- [ ] Security architecture (§30) fully audited with zero unresolved findings
- [ ] Manual QA sign-off recorded for every item in this checklist
- [ ] A scalable-but-not-overengineered foundation exists, with expansion triggers documented rather than pre-built
