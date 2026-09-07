# Hidden Alchemy — Implementation Log

Single source of truth for the M0–M10 transformation of the Hidden Alchemy GitHub organization.
Per PRD §"Implementation Logging": this log lives at the root of the `.github` repository once it
exists. It is **started in M0 as a scratch document** (because `.github` already exists remotely and
must not be overwritten during M0 — see the note in *M1 Task 1.1.1*), and will be **moved into the
`.github` repository as the first real commit of M1** (as "audit and reconcile" per M0's findings).

Format per entry: milestone, phase, date, files changed, tests run/results, failures/fixes, completion status.

---

## M0 — Discovery & Baseline

**Date:** 2026-09-07
**Objective:** Establish ground truth about the current state of the Hidden Alchemy organization before changing anything.
**Method:** GitHub REST API (anonymous, public read access only) against `api.github.com`. No local `gh` CLI, no PAT/token available in the execution environment. Reachability confirmed (HTTP 200 on org + repos endpoints). Rate limit observed: 49/60 remaining at inventory time.

**Output files (scratch):**
- `PRD.md` (existing)
- `IMPLEMENTATION_LOG.md` (this file — created in M0)

---

### Phase 0.1 — Inventory

#### Task 0.1.1 — Enumerate existing repositories

Result from `GET /orgs/Hidden-Alchemy/repos?per_page=100&type=all`:

| # | Repository | Visibility | Fork | Default branch | Created | Last push | Size (KB) | Commit count | LICENSE | README | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `.github` | Public | No | `main` | 2026-08-19 | 2026-08-20 | 12 | 5 | **None** | Yes (root + profile) | Real content; all 5 commits by `Hassan0703` |

Org-level facts (`GET /orgs/Hidden-Alchemy`):
- Login: `Hidden-Alchemy`; Name: "Hidden Alchemy"
- Description: "Hidden Alchemy engineers the potential inside your business — with Frappe, ERPNext, AI, and automation."
- `public_repos: 1` (cross-checked against the API count of 1 — counts match, no repo missed on the public surface)
- Location: Pakistan; created 2026-08-19; updated 2026-08-22
- Org-level projects enabled: `has_organization_projects: True`, `has_repository_projects: True`
- No `blog`, no `email` set

**Existing `.github` contents** (tree of `main`):
- `README.md` (2,286 B) — root, studio-style descriptive README
- `profile/README.md` (14,833 B) — existing org profile README, 13 sections
- `profile/Logo.svg` (2,191 B)
- `profile/assets/logo.svg` (2,191 B) — **byte-identical to `Logo.svg`** (same MD5 `dc6e0f3cd540345051da5e4725ee7ac5`), i.e. a duplicate of the same SVG stored in two locations.

No other files present: no `CONTRIBUTING.md`, no `SECURITY.md`, no `SUPPORT.md`, no `CODE_OF_CONDUCT.md`, no `LICENSE`, no `CODEOWNERS`, no `ISSUE_TEMPLATE/`, no `workflows/`, no `templates/`, no `assets/svg/`, no `assets/og/`.

Commit history (all by `Hassan0703`):
- `4b7d04c8` 2026-08-20 — "Add logo.svg for HIDDEN ALCHEMY branding"
- `cb6443ef` 2026-08-20 — "Add SVG logo for HIDDEN ALCHEMY"
- `40ee3b87` 2026-08-20 — "Revamp README with comprehensive project details"
- `817e08fd` 2026-08-19 — "Create README.md for Hidden Alchemy project"
- `dbda1b08` 2026-08-19 — "Enhance README with company overview and projects"

**Acceptance criteria — Task 0.1.1:**
- [x] Every existing repo listed with the required fields (name, visibility, description, last push, default branch, LICENSE/README presence)
- [x] No repo missed (public surface; cross-checked against org `public_repos: 1`)
- **NOTE (partial-blocker):** Private repositories, if any, are NOT visible to anonymous access. The inventory covers the full *public* surface only. Private repos can only be enumerated with authenticated read access (not available in this environment). See Open Issues #2.

#### Task 0.1.2 — Inventory existing org-level settings

Result from public API:
- **Public member(s):** `Hassan0703` (Hassan Ali) — the only publicly-listed member. GitHub profile: ERPNext & Frappe Framework Developer | Python Engineer; company Infintrix Technologies; user since 2022-08-02.
- **Teams:** `GET /orgs/Hidden-Alchemy/teams` → HTTP 401 "Requires authentication". Teams not enumerable anonymously. Result recorded as **NOT OBSERVED** (expected: none/minimal per §22, but unverified).
- **Owners list:** authenticating `GET /orgs/Hidden-Alchemy/members` returns only public members, not Owner role. Owner assignment NOT directly observable anonymously. Inferred from sole public member + sole committer on all `.github` commits: likely `Hassan0703`, but **flagged unverified** (see Open Issues #1).
- **Existing `.github` contents:** recorded in Task 0.1.1 above (present, real content).

**Acceptance criteria — Task 0.1.2:**
- [x] Owners list → **PARTIAL**: public membership recorded (`Hassan0703`); authoritative Owner role unobservable anonymously → Open Issue #1
- [x] Teams list → recorded as NOT OBSERVED (401); expected minimal/empty but unverified → Open Issue #3
- [x] Existing `.github` repo contents recorded in full (present)

#### Task 0.1.3 — Confirm brand constants

From the existing live SVG assets (`profile/Logo.svg` / `profile/assets/logo.svg`) and `profile/README.md` §05 Design Language:
- Gold `#BD9C61` — **CONFIRMED PRESENT** (matches PRD's Gold)
- The existing live palette (per §05 of profile README) is:
  - Alchemical Gold `#BD9C61` (identity/accents) ✓
  - Gold Light `#D7BF91` (secondary highlight)
  - Obsidian `#0B0B0A` (primary dark background)
  - Graphite `#171715` (supporting neutral)
  - Stone `#2A2925` (supporting neutral)
  - Muted `#77736A` (supporting neutral)
  - Alchemy Ivory `#F3F0E8` (docs/light-mode)
- **Verdigris `#4C6B5C` — NOT FOUND in any existing asset or doc.** The PRD lists Verdigris `#4C6B5C` as a canonical color, but it does not appear in the current live brand. This is a **brand-constant discrepancy** requiring a human decision (adopt Verdigris per PRD, or confirm the observed palette is canonical). → Open Issue #4.

**Acceptance criteria — Task 0.1.3:**
- [x] Confirmed values recorded in the log → Gold `#BD9C61` confirmed; current live palette recorded
- [x] Ambiguity flagged (not guessed): Verdigris `#4C6B5C` absent from live assets → Open Issue #4

---

### Existing intentional work — preservation assessment (Protocol Rule 3)

The following existing files are **intentional work that must NOT be silently overwritten**; they require a logged diff review and, where they conflict with the PRD, a human reconciliation decision before M1/M2 overwrite or replace them:

1. **`profile/README.md`** (existing org profile) — this is real, deliberate prior work. It conflicts with several PRD requirements:
   - §14.2 / NG6: uses third-party services (`capsule-render.vercel.app`, `readme-typing-svg.demolab.com`, `shields.io`, `singlecolorimage.com`) — PRD requires zero external dependencies.
   - §14.1 / §57: uses fantasy iconography (`⚗` alembic everywhere, "The Alchemy", "RAWPOTENTIAL" ASCII) — PRD requires "premium/technical, never fantasy".
   - §14.1 section 4 / §24 / §57: has a **placeholder "Featured Repositories" table with fabricated rows** (`repo-name`, "🟢 Active", "🧪 Experimental") — directly violates the "no fake activity / honest empty-state" rule.
   - §15-design conflict / root README tone: "digital forge" fantasy framing.
   - Not a clean mapping to §14.1's required 8-section order.
   - **Decision required:** full replacement with the M2 Profile README (per §14), or reconciliation. Per PRD Protocol this is a human-flagged item; OpenCode must not auto-delete before M2 with explicit sign-off.
2. **`profile/Logo.svg` + `profile/assets/logo.svg`** — the existing logo wordmark (Godle `#BD9C61` on Obsidian `#0B0B0A`, "WHERE IDEAS BECOME SYSTEMS"). This is brand canon to **preserve and reuse**, not discard. The two copies are byte-identical duplicates (naming: `Logo.svg` vs `logo.svg`) — a consolidation/cleanup candidate under §16 naming (kebab-case, purpose-first), flagged for M2, not auto-removed.
3. **Root `README.md`** — intentional studio README; content partially at odds with PRD tone and references `@Hassan0703`. Consolidation decision for M1 (root README must explain the repo is org-wide config, distinct from profile README, per §13/Task 1.1.1).

### Missing requirements (present in PRD, absent in org)
- No `.github/ISSUE_TEMPLATE/` (M3), no `.github/workflows/` (M4), no `.github/templates/` (M2.5), no `CONTRIBUTING.md` (M3), no `SECURITY.md`/`SUPPORT.md`/`CODE_OF_CONDUCT.md`/`CODEOWNERS` (M1), no `LICENSE` (M1), no `community` or `ideas` repos (M5), no Discussions setup (M5), no flagship repo (M9), no `experiments` repo (correctly absent — LATER per §12).

### Conflicts / reconciliation candidates surfaced (not resolved in M0)
- Existing fantasy-toned identity vs PRD premium-technical tone (profile README + root README).
- Existing third-party badge/SVG dependencies vs PRD zero-external-dependency rule.
- Existing fabricated "Featured Repositories" placeholder rows vs honest-empty-state rule.
- Brand palette: Verdigris absent from live assets (Open Issue #4).
- Root README tone/link references vs PRD governance tone.

### Risks recorded
- **[R1] Overwrite risk:** `.github` already contains intentional work that PRD's baseline assumed was absent (§4 Problem #1 claims "no org-level profile", but one exists). M1/M2 must operate as "audit and reconcile," not "create from scratch," and must not overwrite without explicit sign-off.
- **[R2] Access limitation:** No authenticated GitHub access in this environment → Owners, teams, private repos, and org-team/org-settings mutation cannot be performed or fully enumerated here. Full conflict/settings changes (Teams creation M1, branch protection M8, Discussions M5) require authenticated credentials or a human Owner performing them.
- **[R3] Brand ambiguity:** Verdigris `#4C6B5C` unresolved (Open Issue #4) must be settled before M2 design work.

---

### Open Issues / Ambiguities (require human resolution before the relevant milestone; none block M0 itself)

- **#1** Authoritative Organization **Owners list** not observable anonymously. Confirm that `Hassan0703` is the sole Org Owner (and intended initial `core`/`community` team composition per §22.1, needed for M1 Phase 1.3).
- **#2** **Private repositories** (if any) not enumerable without authentication. Confirm there are no private repos that the PRD's repo plan (§12) must account for.
- **#3** **Teams** not observable anonymously (HTTP 401). Confirm current team state is empty/none before M1 Phase 1.3 creates `core`/`community`.
- **#4** **Brand constant:** Verdigris `#4C6B5C` absent from existing live assets; current live palette uses Obsidian `#0B0B0A`/Ivory `#F3F0E8`/Gold `#BD9C61`/Gold-Light `#D7BF91`/Graphite/Stone/Muted. Decide: adopt PRD Verdigris `#4C6B5C` as a canonical accent, or treat the observed palette as canonical and amend the PRD §3 color set. Required before M2 (visual system).

---

## M0 Completion Checklist

- [x] All Phase 0.1 tasks (0.1.1–0.1.3) executed
- [x] `IMPLEMENTATION_LOG.md` exists with M0 entries (scratch location, pending move into `.github` at M1)
- [x] No ambiguities outstanding FOR M0 itself; ambiguities that affect later milestones (#1–#4) explicitly documented for human resolution above
- [X] **M0 sign-off recorded 2026-09-07** (human sign-off: "all ok now move on"). Open Issues #1–#4 acknowledged as resolution paths for their owning milestones; none block M1's file work. Open Issue #1 (Owners = Hassan0703) additionally confirmed in practice: SSH key authenticates as Hassan0703 with git write access to `.github`.

---

_End of M0 entry. M1 below._

---

## M1 — Organization Foundation

**Date:** 2026-09-07
**Objective:** Create the `.github` repository skeleton and baseline community health/security files.
**Prerequisite:** M0 signed off (recorded above).

Per Task 1.1.1 preconditions, M0 confirmed the `.github` repo **already exists with real content**, so M1 Phase 1.1 operates as **"audit and reconcile," not "create from scratch."** No existing file was overwritten without a diff review (recorded below).

### Phase 1.1 — Repository reconciliation

**Task 1.1.1 — `.github` repo: create → audit-and-reconcile (LICENSE + root README)**

Diff review (existing content vs. replacement) for the two files affected:

1. **`README.md` (root) — REPLACED.** Existing content: studio-style promotional README ("digital forge", shields.io `<img>`, "Core Pillars", Tech Stack JSON, "Active Laboratories & Current Roadmaps", collab blurb referencing `@Hassan0703`). Conflicts with PRD: §13 requires the root README to explain the repo is org-wide configuration (distinct from `profile/README.md`); §14.2/NG6 ban third-party badge/image services (shields.io); §57 bans fantasy-toned language ("forge", "alchemy" as fantasy framing). Git history preserves the old version (commit `40ee3b87` etc.). Replacement: brief org-config README with a contents table. **Preservation decision:** old content intentionally replaced per PRD; logged diff review complete. No data destroyed (recoverable via git history).
2. **`LICENSE` — CREATED (new).** MIT, copyright 2026 Hidden Alchemy (§12.1 default license).

**Files created/modified:** `README.md` (replaced), `LICENSE` (new). Acceptance: repo exists ([x]), LICENSE present ([x]), root README present and distinguishes itself from profile README ([x]).

**Task 1.1.2 — Scaffold directory structure**

Directories created (with `.gitkeep`, per PRD Task 1.1.2 guidance):
`assets/svg/`, `assets/og/`, `ISSUE_TEMPLATE/`, `workflows/`, `templates/`.

`profile/` already contained `README.md`, `Logo.svg`, `assets/logo.svg` — **left untouched** for M2 reconciliation (diff review already logged in M0 entry).

Verification (`find` tree): structure matches §13 with no extra speculative files (Rule 4). Acceptance: [x] structure matches §13, [x] no extra files.

### Phase 1.2 — Baseline community health files

- **Task 1.2.1 — `CODE_OF_CONDUCT.md`** (new): Contributor Covenant 2.1, tone-adapted (lost disembodied "harassment-free community" boilerplate trimmed, enforcement substance intact). Enforcement contact: `@Hidden-Alchemy/core`, current Organization Owner `@Hassan0703`, plus confidential route via SECURITY.md private channel. **No dead email.** Compliance: [x] file present; [x] enforcement contact defined (not a dead link); adapted tone (§6 principle 2), not saccharine.
- **Task 1.2.2 — `SECURITY.md`** (new): private reporting via GitHub Security → Report a vulnerability; no external email/form; honest response-time intention (7-day ack, best-effort, no funded security team). Compliance: [x] present; [x] private reporting explained; [x] no external email required.
- **Task 1.2.3 — `SUPPORT.md`** (new): correctly distinguishes support (Discussions Help) vs. bug (Bug Report form) vs. feature (Feature Request form); honest note that Discussions/`ideas` arrive at M5+. Compliance: [x] present; [x] support/bug/feature clearly separated.
- **Task 1.2.4 — `CODEOWNERS`** (new): patterns `/workflows/**`, `/.github/CODEOWNERS`, `/SECURITY.md` → `@Hidden-Alchemy/core` per §30.7. **Partial compliance:** [x] file present; [x] correct paths covered; [ ] referenced team exists — **DEPENDENCY ON Phase 1.3**, which is currently **BLOCKED** (see Phase 1.3). GitHub will resolve the team once it is created; until then CODEOWNERS review enforcement is inert exactly as documented in the file's header note.

### Phase 1.3 — Baseline teams — **BLOCKED (human action required)**

Attempted via GitHub REST API:
```
POST /orgs/Hidden-Alchemy/teams {"name":"core", ...}
→ 403 "Must have admin rights to Repository."
```
Root cause: no org-admin-scoped credential is available in this environment —
SSH key authenticates as `Hassan0703` (git write only); the stored API token
belongs to `muqeetmughal`, is `repo`-scoped, and that user is **not a member**
of Hidden-Alchemy. Per §22.3, team creation is an Organization Owner action.

This is a genuine credential blocker, not a process ambiguity:
- Task 1.3.1 (`core` team) and Task 1.3.2 (`community` team) cannot be
  executed automatically.
- CODEOWNERS (Task 1.2.4) acceptance is partial until `core` exists.
- PRD Protocol Rule 6/8 forbids skipping a task or proceeding past a failed
  test; Rule 13 (No-Assumption Rule) forbids guessing a workaround. No
  workaround exists (GitHub does not permit org team creation over SSH or with
  a non-owner token).

**Required owner action (any one of):**
1. Create the two teams manually in GitHub UI (Settings → Teams → New team):
   - `core` — "Cross-repository technical leadership (PRD §22.1)"; members: the
     Organization Owner (Hassan0703); privacy: closed/visible.
   - `community` — "All approved org members (PRD §22.1)"; initially empty;
     privacy: closed/visible.
   After creation, M1 acceptance for Phases 1.2/1.3/1.4 can be closed out.
2. Or provide an org-admin-scoped token (e.g., `gh auth` or a fine-grained
   token with Administration:write on the org) so team creation can be
   automated via API with this exact payload.

**RESOLVED 2026-09-07** — after the owner set up `gh auth login` as `Hassan0703`,
teams were created via `gh api`:

- `core` created (`POST /orgs/Hidden-Alchemy/teams`, slug `core`); `Hassan0703`
  added with role `maintainer`. Members now: `Hassan0703`.
- `community` created (slug `community`); Shelley's auto-added creator entry
  (`Hassan0703`, added implicitly at creation) removed via
  `DELETE /teams/community/memberships/Hassan0703`. Members now: `[]` (empty,
  as required by Task 1.3.2 — populated only through the M7 process).
- Verified via `GET /orgs/Hidden-Alchemy/teams` → `community`, `core`.
- CODEOWNERS header comment updated to reflect that `@Hidden-Alchemy/core`
  now exists (Task 1.2.4's "referenced team exists" criterion is satisfied).

### Phase 1.4 — License & governance stub

- **Task 1.4.1 — `GOVERNANCE.md` (new, lightweight, M8-finalizable):** §33 content complete (decision-making simple consensus, single accountable maintainer per repo, conflict resolution, archival decisions, leadership changes incl. WHEN-SCALE-REQUIRES-IT note). Membership section **clearly marked "finalized in milestone M7"** — not a silent gap (no `<!-- TODO -->` HTML comment; deliberate bold marker, so the M4 repo-health-check TODO-scan will not false-flag it). Includes the §19 canonical verbatim membership distinction, §12.1 repository-creation rule carried forward (per Risks mitigation, §61), lifecycle status list (§24), and Future Expansion triggers (§61). Acceptance: [x] present; [x] §33 content complete; [x] membership section explicitly marked M7-finalized.

### M1 Verification & Tests Run

- `find` tree diff vs §13: pass (structure + preserved legacy profile dir only).
- Link/integrity review of new files: internal references (CONTRIBUTING.md, SECURITY.md, GOVERNANCE.md, LICENSE) resolve as of M1 file set; CONTRIBUTING.md itself lands in M3 (referenced from root README — acceptable, matches PRD sequencing; M2 profile links already logged as known limitation to close at M3).
- Team API creation attempt: initially FAILED (403, stale credential) — **RESOLVED** via `gh auth` (owner token): `core` + `community` created 2026-09-07, verified via `GET /orgs/Hidden-Alchemy/teams` (see Phase 1.3 resolution above).
- No workflows exist yet in M1 (expected — workflows ship in M4). repo-health-check cannot run yet (expected per M1 checklist).

### M1 Completion Checklist

- [x] Phase 1.1 tasks 1.1.1–1.1.2 pass acceptance
- [x] Phase 1.2 tasks 1.2.1–1.2.3 pass acceptance
- [x] Phase 1.2 task 1.2.4 — file correct; referenced team `@Hidden-Alchemy/core` now exists (created in Phase 1.3)
- [x] Phase 1.3 tasks 1.3.1–1.3.2 — `core` team created with Hassan0703; `community` team created, empty
- [x] Phase 1.4 task 1.4.1 passes acceptance
- [x] `repo-health-check` not yet runnable (workflows arrive in M4) — expected, not a blocker
- [x] Manual review: directory structure matches §13 exactly (plus preserved legacy profile/ pending M2)
- [x] Implementation log updated
- [X] **M1 sign-off recorded 2026-09-07** (human sign-off: owner set up `gh auth`, teams created; instructed to continue with remaining milestones). M1 is complete.

_End of M1 entry. Next milestone: M2 — Identity & Profile Experience.

---

### Open Issue status update

- **#1 (Owners):** RESOLVED — SSH key + `gh auth` token both act as `Hassan0703`, the org Owner; sole public member; sole `core` team member (role maintainer). Confirmed 2026-09-07.
- **#2 (Private repos):** Awaiting owner confirmation (owner API can enumerate; see M2 note if relevant); not a blocker for M1.
- **#3 (Teams):** RESOLVED — `core` (Hassan0703) and `community` (empty) created 2026-09-07 via `gh api`.
- **#4 (Verdigris color):** Still open for M2 — decision required before visual system work.

---

## M2 — Identity & Profile Experience

**Date:** 2026-09-07
**Objective:** Ship the organization profile README and its visual assets per §14/§16.
**Prerequisite:** M1 signed off (recorded above).

### Brand decision recorded (Open Issue #4 resolved)

Owner directive 2026-09-07: the canonical logo set is `assets/logos/*.png`
(user-provided); the previous SVG logo (`profile/Logo.svg` /
`profile/assets/logo.svg`) is **not** the brand and was removed (`logo.svg was
not aligned with my logos`). Adopted assets:

- `logo-black-transparent.png` (gold/cream glyph, transparent) — primary mark for both-mode embedding.
- `logo-white-transparent.png`, `Hidden-Alchemy-header-logo-*-bg.png`, `Hidden-Alchemy-Logo-200x200-*.png` — mode-specific and avatar-candidate variants.

**Verdigris `#4C6B5C`:** now used as a pipeline accent in the SVG diagrams
(dark mode contrast verified). The pre-existing live palette (Obsidian/Ivory/
Gold) remains the base; Verdigris is adopted as an additional accent per the
PRD, not a replacement of any existing color. No conflicting brand spec was
found, so no ambiguity remains.

### Phase 2.1 — Visual assets

- **Task 2.1.1 — `assets/svg/hero-pipeline.svg`** (created, 4.6 KB): 6 nodes
  (IDEA→…→REALITY), Gold/Verdigris accents, hexagon geometry, Bone labels on
  translucent Ink pills for dual-mode legibility.
  **Design decision (logged):** these SVGs are embedded via `<img>`, so the
  hosting page's `currentColor` does not reach inside them. Static dual-mode
  colors were therefore used instead of `currentColor`, with explicit colors
  verified against both `#0d1117` and `#ffffff` (headless-Chrome pixel
  analysis — PASS both modes: labels, gold, verdigris, and pills all present).
  `<title>`/`<desc>` present; static frame is the first animation frame
  (node-highlight drift, opacity 0.16→0.40, 7s, staggered). Under 150 KB. ✔
- **Task 2.1.2 — `assets/svg/contribution-pathway.svg`** (created, 5.2 KB):
  same structure, 7 stages (EXPLORE→…→MEMBERSHIP ELIGIBILITY). Animation =
  slow directional flow dots only (the two permitted animated elements in
  §35). Dual-mode pixel verified PASS both modes. ✔
- **Task 2.1.3 — `assets/og/org-social-preview.png`** (created, 1280×640,
  RGBA, 134 KB): generated from `logo-black-transparent.png` + brand text +
  pipeline line. **Known limitation:** uploaded-to-org-settings cannot be done
  via API (no public endpoint for org social preview / org avatar) — recorded
  as a **manual owner action** to complete at sign-off.
- **Task 2.1.4 — `assets/svg/README.md`** (created): naming convention
  (kebab-case, purpose-first), raw-URL reference pattern with real example,
  authoring rules (title/desc, static-frame-as-frame-0, dual-mode color
  guidance, <150 KB), and the `assets/logos/` catalog with per-logo usage.
  Logged exception: pre-existing logo filenames keep mixed case (approved
  deviation from kebab-case).

### Phase 2.2 — Profile README

- **Task 2.2.1 — `profile/README.md`** (REPLACED): legacy 13-section profile
  (fantasy iconography, third-party services, fabricated `repo-name` table)
  replaced with the §14-spec 8-section README. Diff review reference: M0 log
  (legacy content captured) — the old file remains recoverable via git
  history (commit `40ee3b87` and the M1 `181f1ae` tree).
  - 8 sections in §14.1 order: Identity Hero (title + positioning + logo +
    hero-pipeline), The Alchemy Process, What We Build, Active Systems
    (honest empty state), Experimental Lab (ideas/experiments explained,
    links land when repos live), How to Participate (pathway + CONTRIBUTING +
    3 entry forms), Organization Principles (table), Join the Lab (verbatim
    membership line + eligibility bar + GOVERNANCE link).
  - Zero external dependencies: only `github.com` and
    `raw.githubusercontent.com` hosts (verified); no shields.io /
    capsule-render / typing-svg / singlecolorimage (verified by grep).
  - No fabricated repos/stats/contributors referenced.
  - **Known limitation (matches M2 checklist):** links to CONTRIBUTING.md and
    the bug/idea/proposal forms are written now but resolve only after M3
    (CONTRIBUTING + forms in `.github`) and M5 (ideas/community repos). Logged,
    not silently ignored.

### M2 Verification & Tests Run

- Tail of SVGs: XML well-formed (ElementTree), sizes 4.6/5.2 KB (≪150 KB).
- Dual-mode legibility: headless-Chrome render on `#0d1117` and `#ffffff`,
  pixel classification for gold/verdigris/text/pills → **all four checks PASS
  for both SVGs in both modes** (see M2 entry test section for numbers).
- Profile README structure: all 8 sections present, in §14.1 order (grep on
  headers).
- Links: only allowed hosts; all referenced `assets/*` files exist locally
  (verified path-by-path); banned third-party services absent.
- Human visual QA (screenshots, both modes, mobile viewport, one-screen hero
  check): **deferred to human sign-off** — not performable by this agent (no
  image display capability), and the PRD's Manual QA Requirements designate it
  as a human review anyway.

### M2 Completion Checklist

- [x] Both SVGs pass their acceptance criteria (size, title/desc, dual-mode
      pixel verification, static-frame completeness)
- [x] Profile README passes §14.3 checklist, item for item (see notes):
      [x] 8 sections present in order; [x] internal link URLs well-formed
      (resolution dependency on M3/M5 logged); [x] hero SVG dual-mode-verified
      (human screenshot pending); [x] no fabricated references; [ ] one-screen
      hero + process (structural estimate OK — human viewport confirmation
      required); [ ] mobile verified (human required); [x] zero external deps
- [x] Known limitations logged (link 404s until M3/M5; social-preview upload is
      a manual owner action; Verdigris decision resolved)
- [ ] Manual QA: screenshot comparison dark vs. light saved to log — **requires
      human**; org social preview upload — **requires owner (UI action)**
- [ ] **Explicit sign-off required before proceeding to M3**

_End of M2 entry._

### Open Issue status update

- #1 Owners — RESOLVED (M1).
- #2 Private repos — still unconfirmed; not a blocker through M2.
- #3 Teams — RESOLVED (M1).
- #4 Verdigris / brand — RESOLVED in this milestone (owner logo directive +
      Verdigris adopted as accent). Closed.

---

## M3 — Contribution Infrastructure

**Date:** 2026-09-07
**Objective:** Make the first contribution possible end-to-end — CONTRIBUTING.md,
org-wide issue forms, the §25 label taxonomy, and the PR template.
**Prerequisite:** M2 signed off (owner directive to continue received as "continue").

### Phase 3.1 — Labels (Task 3.1.1) ✅

Applied the exact §25 taxonomy to `Hidden-Alchemy/.github` (org-wide fallback repo)
via `gh api`. All 24 labels, no extras; one color family per facet:

| Facet | Colors | Labels |
|---|---|---|
| Difficulty | blue tones | `good first issue` `#1F6FEB`, `help wanted` `#0969DA` |
| Type | purple tones | `type:bug` `#8250DF` `type:feature` `#A371F7` `type:documentation` `#BC8CFF` `type:design` `#C297FF` `type:research` `#6E40C9` `type:experiment` `#8957E5` `type:architecture` `#8A63D2` `type:idea` `#D2A8FF` |
| Priority | red→orange→yellow→green | `priority:critical` `#D1242F` `priority:high` `#F97316` `priority:medium` `#FACA15` `priority:low` `#2DA44E` |
| Status | gray→green (+warn end) | `status:triage` `#57606A` `status:planned` `#6E7781` `status:in-progress` `#1A7F37` `status:review` `#4A9E77` `status:blocked` `#9E6A03` |
| Community | gold tones | `membership:approved` `#B07C3C` `membership:declined` `#9A6700` `membership:deferred` `#C08A2E` `membership:needs-review` `#BF8700` `project-proposal` `#8F6F19` |

- Deleted the 8 non-§25 GitHub default labels from `.github` (`bug`,
  `documentation`, `duplicate`, `enhancement`, `invalid`, `question`, `wontfix`,
  `accessibility`). **Cross-section note (logged):** §17's entry-point table
  names bare `documentation`/`design` labels; those are shorthand for the §25
  `type:documentation`/`type:design` labels — §25 is the final taxonomy and its
  "no repo-local label sets" rule wins. No bare labels remain.
- Label plumbing verified live: test issue `#1` created with the bug form's
  auto-labels → confirmed `type:bug` + `status:triage` applied → closed with a
  comment. (Issue #1 is also the org tracker's first issue.)
- Org-wide propagation caveat recorded: GitHub does not retro-apply label sets
  to repos; ideas/`community` repos get the same 24 labels scripted at M5.

### Phase 3.2 — Issue Forms ✅

- **Task 3.2.1 `ISSUE_TEMPLATE/config.yml`** — `blank_issues_enabled: false`;
  one contact link → Discussions Help. ✔
- **Tasks 3.2.2–3.2.7** — all six §26 forms written as native GitHub Issue Form
  YAML and validated (PyYAML parse + field/required mapping + labels
  cross-checked against the live label set):
  - `bug_report.yml` ✓ Summary/Steps/Expected-vs-actual/Repo-version all
    required → `type:bug`,`status:triage`
  - `feature_request.yml` ✓ Problem/Proposed solution/Alternatives →
    `type:feature`,`status:triage`
  - `idea_submission.yml` ✓ One-line idea/Problem/Why Hidden Alchemy/Rough
    scope → `type:idea`,`status:triage`,`project-proposal` (drafted here;
    canonical home `ideas` repo at M5)
  - `project_proposal.yml` ✓ Accepted-idea link/Architecture sketch/Commitment →
    `type:architecture`
  - `research_proposal.yml` ✓ Question/Method/Expected output → `type:research`
  - `membership_interest.yml` ✓ Handle/Contributions-with-links/Areas/GOVERNANCE
    checkbox → `membership:needs-review` (canonical home `community` repo at M5)
- Copy plan for M5 recorded: GitHub requires forms to live in the repo they
  apply to; `.github` org-wide fallback only covers repos with no local
  template. idea/membership forms move to `ideas`/`community` at M5 Phase 5.x.
- Required-field **enforcement** is client-side (UI) — YAML `validations.required`
  flags verified structurally; live UI block-test deferred to Manual QA.

### Phase 3.3 — CONTRIBUTING.md ✅

- Written covering: the pipeline identity (IDEA→…→REALITY); the "membership is
  separate from contributing" rule up front (§19 canonical language); the full
  §17 entry-point table (8 routes, first action each); §25 label taxonomy in
  plain language (one Type per issue, one Status after triage, Priority/Difficulty
  are human-only); the idea→proposal pipeline route (IDEA→CONCEPT→ARCHITECTURE);
  §28 PR expectations; recognition/membership next-steps w/ GOVERNANCE link; the
  lab's honest-failure principle. Links verified (relative paths resolve).
- §26 forms + profile README links to CONTRIBUTING.md now resolve once this
  commit is pushed — **closing M2's logged known limitation** (ideas/community
  form links remain pending M5, already logged).

### Phase 3.4 — PR Template ✅

- `PULL_REQUEST_TEMPLATE.md` at repo root (org-wide fallback for all repos): all
  five §28 items — Linked issue (or explicit no-linked-issue w/ justification),
  Summary of change, Testing performed, Documentation impact, Visual change
  (screenshot required). (PRD's checklist text says "four items" but §28 lists
  five — five implemented, spec is authoritative; noted.)
- Default-PR-body rendering is client-side → deferred to Manual QA
  (open a test PR with no body on a scratch branch).

### M3 Verification & Tests Run

- PyYAML parse of config + all six forms: PASS. Required-field mapping per §26:
  PASS. Form label sets == live label set subset: PASS.
- Live issue flow: created issue #1 with bug-form auto-labels, verified
  `type:bug`/`status:triage` present, closed cleanly. PASS.
- Label set: exactly 24 labels (count + name diff vs §25): PASS, no extras.
- Refs: all relative links in CONTRIBUTING.md exist on disk; post-push URL check
  queued after this commit.
- **Manual QA (human):** full first-time-contributor simulation — open each of
  the six forms as a test and confirm required-field blocking + coherent
  experience; confirm the PR template pre-fills as the default PR body.

### M3 Completion Checklist

- [x] All 24 §25 labels present, no extras, family colors documented
- [x] config.yml + 6 forms complete, structure/required/labels verified
- [x] CONTRIBUTING.md written (entry points, labels, PR expectations,
      membership-separate language, all internal links resolve)
- [x] PULL_REQUEST_TEMPLATE.md with all §28 checklist items
- [x] Profile README's CONTRIBUTING + non-ideas form links now resolve
      (post-push re-verified); ideas/community links tracked to M5
- [x] Live label-plumbing test (#1) passed
- [ ] Manual QA: six-form open-and-block simulation + PR template render
      (human), then explicit sign-off before M4

_End of M3 entry._

### Open Issue status update

- #1 Owners — RESOLVED (M1). #3 Teams — RESOLVED (M1).
- #2 Private repos — still unconfirmed; reviews requested at M4 (workflows run
      only on public default repos).
- #4 Verdigris/brand — RESOLVED (M2).

---

## M4 — Automation Foundation

**Date:** 2026-09-07
**Objective:** Ship the four §29 workflows with security review at creation
time. Prereq: M3 signed off (owner "continue" directive received).
**Deliverables live in `.github/workflows/`:** org-wide *defaults for the
`.github` repo itself*, per §29; GitHub does not auto-propagate workflow files,
so M5 copies them into `ideas`/`community` (that milestone's checklist already
accounts for this).
**Also added:** `.github/dependabot.yml` (§30.6).

### Cross-cutting security self-review (that passed before any commit)

Verified by inspection + grep across all four files (checked §21/§30):
- Explicit top-level `permissions:` blocks, minimal: welcome `issues/PRs write`,
  labeler `issues write`, health `contents read + checks write`, stale
  `issues/PRs write`. No `write-all`, no `administration`, no `organization-*`,
  no `packages`.
- No secrets anywhere except `secrets.GITHUB_TOKEN` (never a PAT).
- No `pull_request_target` as a real key (the string appears only in comments
  documenting the prohibition). No checkout of untrusted fork code.
- Third-party actions pinned to full SHAs: `actions/checkout@11d5960a…` (v4.4.0),
  `actions/first-interaction@1c468894…` (v3.1.0). `dependabot.yml` labelled
  `labels: []` to keep §25's "no extras" taxonomy — Dependabot posts no sticker.

### Task 4.1.1 — welcome-first-interaction.yml ✅

per `§29`: no checkout step, `issues/PRs write` only, SHA-pinned first-interaction,
non-generic templated messages that reference the specific repo's CONTRIBUTING
and First-Time pipeline. Live proof: it fired on the Dependabot PR #3 and left a
"welcome" comment (first interaction, then manually cleaned after verifying).
Full first-human simulation (fresh account) deferred to Manual QA.

### Task 4.2.1 — issue-labeler.yml ✅

Mapping source = the labels an Issue Form emits (GitHub does NOT expose a
reliable form-ID to workflows — documented). Native form `labels:` already apply
§26 sets at submit; the workflow is the safe no-op/idempotent + fallback path:
- known type label present → notice, exit 0 (no double-labeling);
- otherwise → apply `status:triage` only + warning in run log, never an error
  surfaced to the issue author.
**Live test:** opened issue #2 with no labels (simulated blank/API) → workflow
applied exactly `status:triage`, nothing else. PASS.

### Task 4.3.1 — repo-health-check.yml ✅

Checks four conditions (LICENSE present; README present + no
TODO/placeholder/TBD; §24 `Status:` line — syntax `Status: \`<keyword>\``/`Status:
<keyword>`; SECURITY.md present), reports a pass/fail **check-run** (the only
side effect; never auto-blocks merges outside a §31 tier) via `gh api` + step
summary. Fork PRs run with the same minimal read-only block — static perms
`contents:read + checks:write` per §29; interpretation noted: "read-only" means
no repository-content writes and no elevated token on fork code.
**Live test:** the commit that introduced the workflow triggered it on `main` →
`completed/success` with summary "LICENSE ✓ / README ✓ / §24 status line ✓ /
SECURITY.md ✓". PASS.
**Reconciliation made during testing:** README's status line was initially the
markdown-bold `**Status:**` form, which the check could not parse → canonical
form documented (`Status: \`active\``) and README fixed; regex tolerates
backticks. Also fixed a latent CODEOWNERS bug: `/workflows/**` never matched
`/.github/workflows/**` (the real path) → corrected so §30.7 review gates the
actual files. Both noted in the M4 diff.

### Task 4.4.1 — stale-triage.yml ✅

60-day no-activity → single neutral "conversation needs owner/maintainer
decision" comment: never closes, never auto-anything. Membership-interest
(`membership:needs-review`) issues ≥21 days → comment pinging
`@Hidden-Alchemy/core`, per §20.
**Reconciliation (logged):** §25's label taxonomy is final with no extras and
has no `status:stale`; §29 says "status:stale-equivalent label *or comment*".
Chose the comment (preserves taxonomy exactly). If the owner later wants a real
`status:stale` label, that's an amendment to §25 requiring explicit sign-off.
**Schedule trigger shipped DISABLED (commented) per Task 4.4.1's dry-run-first
gate** — enabled by a one-line commit after dry-run sign-off. `workflow_dispatch`
drives it until then (inputs: `dry_run`, `stale_days`, `membership_days`).
**Test harness results** (scratch issues #4/#5, + real Dependabot PR, forced
`0`-day thresholds, then cleaned up):
- dry-run: 0 comments, clean report, conclusion success ✅
- forced real: stale comment on #4, membership @core ping on #5, stale note on
  PR #3 ✅
- idempotency: marker `<!-- stale-triage -->` prevents double-commenting; rerun
  produced zero new comments ✅
- iterative fixes landed during testing (each is a separate commit on `main`,
  all before this log entry): `--repo` required (runner has no checkout);
  `gh api` path needs `repos/` prefix; PR-comment call must use the API helper
  with `payload`. No workflow uses a secret outside GITHUB_TOKEN throughout.

### M4 Completion Checklist

- [x] Four workflows implemented, tested (labeler #2, health on own push, stale
      three-phase harness, welcome on #3), and security-reviewed at creation
- [x] No workflow requests a secret or PAT (inspection: only GITHUB_TOKEN)
- [x] No workflow uses `pull_request_target` (asserted: no real key anywhere)
- [x] Implementation log updated with per-workflow test results
- [x] CODEOWNERS path bug fixed so §30.7 gating covers the actual files
- [x] dependabot.yml live — opened its first supply-chain PR #3 (checkout
      bump), awaiting human review/merge
- [ ] Schedule trigger remains OFF — **owner decision required: enable
      `stale-triage` daily cron after dry-run review?** (default: enable)
- [ ] Manual QA: first-time human contributor simulation via a second account
      (welcome/labeler), and the §33 M5 workflow-copy plan will re-verify
- [ ] **Explicit sign-off required before proceeding to M5**

_End of M4 entry._

### Open Issue status update

- #1 Owners RESOLVED (M1). #3 Teams RESOLVED (M1). #4 Verdigris/brand RESOLVED (M2).
- #2 Private repos: still unconfirmed (owner question); unaffected through M4
  (all automation runs on public repos; owner can reply whenever).

---

## M5 — Community Repositories (community + ideas)

**Committed:** `.github` (this repo) push containing the §34 health-check fix +
config.yml link correction. `community` and `ideas` are separate repos, each
pushed to `main` (Hassan0703 / SSH / GIT_SSH_COMMAND=BatchMode).

### What got built

- **`Hidden-Alchemy/community`** (public, Core-Team-administered):
  - `README.md` — §15 community-type blocks A/C/D/G/J + `Status: active` line;
    hero, this-is/is-not, governance summary links, contribution pointer, MIT
    footer. No install/quickstart (doc repo).
  - `GOVERNANCE.md` — **one-page pointer** to the canonical
    `.github/GOVERNANCE.md` (per §34 "never restate rules"), with one-line
    summaries and an explicit "canonical file wins" inequality clause.
  - `RECOGNITION.md` — §32 chronology log with maintainer instructions and an
    honest empty-state table (no fabricated entries).
  - `ISSUE_TEMPLATE/config.yml` (blank issues off, Help link → community
    discussions) + `membership_interest.yml` (its final home per §26).
  - Full repo-local copies of the four §29 workflows + `.github/dependabot.yml`
    (§30.6) — required because GitHub does **not** auto-propagate workflows or
    labels from the org `.github` repo.
- **`Hidden-Alchemy/ideas`** (public, Core-Team-administered):
  - `README.md` — §15 blocks + `Status: active`; the §23 idea-lifecycle string;
    this-is/is-not (procurement/catalog language); board link; MIT footer.
  - `ISSUE_TEMPLATE/config.yml` + `idea_submission.yml` + `project_proposal.yml`
    (final homes per §26). blank issues off.
  - Same 4 workflow copies + dependabot.yml.
- **Discussion surface:** Discussions enabled on `community`
  (`has_discussions: true`). GitHub's default categories exist (Announcements,
  General, Ideas, Polls, Q&A, Show-and-tell).

### §34 discovery → health-check fix (shipped to all three repos)

The repo-health-check requirement `[ -f SECURITY.md ]` **false-failed** both new
repos despite full org-default inheritance: the community-health API reports
`health_percentage: 100` for `ideas`, resolving SECURITY.md/CoC/CONTRIBUTING/PR
template from the org `.github` repo as §34 intends. Fix: the check now honors
in-repo *or* org-default presence (probe the `.github` repo's SECURITY.md) and
treats the §34-inherited state as passing. Pushed to `.github`, `community`,
`ideas`; live results: all three `repo-health-check … success`.

### Label taxonomy (§25) on the new repos

Applied the 24-label §25 set to both `community` and `ideas`; deleted the
GitHub defaults not in the set. **Automation artifact logged:** Dependabot
auto-creates `dependencies` + `github_actions` ecosystem labels on first run
despite `labels: []` in dependabot.yml — removed from all three repos to hold
the exact 24; note that the next Dependabot run may attempt to recreate the
`dependencies` sticker on its PRs (accepted as documented automation behavior;
a "no issue" conclusion, revert is a one-liner if a human sees it return).

### Live test results on `ideas`

- Issue #2 created with **no labels** → §29 labeler fallback applied
  `status:triage` only, run `completed/success`; welcome-first-interaction
  fired (expected, first issue) and its comment was removed post-close to keep
  the repo pristine. Issue closed.

### Requirement-vs-capability checks (documented owner steps)

1. **GitHub Project (v2) board "Idea Lifecycle"** — REST project creation
   endpoints and the Projects v2 GraphQL `createProjectV2` exist, but the
   org API token lacks `read:project`/`project` scope (verified:
   `INSUFFICIENT_SCOPES`). **Owner/UI step:** create an org-level Projects v2
   board named "Idea Lifecycle" with the §23 stages as the Status field
   options; the `ideas` README documents the expected link.
2. **Discussion categories** — §27 wants {Announcements, Ideas, General,
   Research, Architecture, Help} + merge Show-and-tell into General + add
   Project Collab LATER. Category create/rename/delete is **UI-only**
   (verified: no GraphQL/REST mutation exists). **Owner/UI step:** create
   Research/Architecture/Help; rename Show-and-tell → General is a UI merge;
   delete Polls if it must vanish (defaults are additive, no §25-style label
   constraint applies to categories). Until Help is created, the config.yml
   "Help / Questions" link points at a not-yet-existing `/categories/help`
   (resolves 200 redirect-style today; UX caveat noted).

### Fixed in `.github` (this repo) during M5

- `ISSUE_TEMPLATE/config.yml` Help link now → `community` repo discussions
  (was a 404 to org-level discussions, which are not enabled).
- `repo-health-check.yml` §34 inheritance fix (above).

### M5 checklist

- [x] Community & Ideas repos created (public), Core Team granted admin
- [x] §15 community-template READMEs + `Status: active` in both
- [x] §26 forms moved to their final homes; config.yml blank-issues-off
- [x] §33 workflow copies + dependabot in both repos
- [x] §25 24-label taxonomy applied; count verified = 24 in all three repos
- [x] §34 inheritance honored by repo-health-check; all three health checks
      green after the fix push
- [x] Labeler fallback live-tested on `ideas` (issue #2)
- [x] Discussions enabled on `community` (categories = owner UI step above)
- [x] Implementation log updated (this entry)
- [ ] **GitHub Project board (owner UI step — token scope)**
- [ ] **Discussion category reconcile (owner UI step)**
- [ ] Manual QA: fresh-account simulation carried over from M3/M4
- [ ] **Explicit sign-off required before proceeding to M6**
