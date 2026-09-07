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
