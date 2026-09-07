# Hidden Alchemy — `.github`

Status: `active` — org infrastructure, maintained continuously. If this
repository's maintenance stops, its README status key must be updated per §24
_lifecycle statuses_ — never left silently behind.

This repository holds the organization-wide configuration and community health
files for the **Hidden Alchemy** GitHub organization. It is not a product
repository; it is the infrastructure that makes the rest of the organization
work.

> Hidden Alchemy is an open engineering laboratory for transforming raw ideas
> into real systems: `IDEA → CONCEPT → ARCHITECTURE → SYSTEM → AUTOMATION → REALITY`.

## What lives here

| Path | Purpose |
|:---|:---|
| `profile/README.md` | Organization profile shown on `github.com/Hidden-Alchemy` |
| `assets/` | Shared org visual assets (SVG diagrams, social preview) |
| `ISSUE_TEMPLATE/` | Reusable issue forms for bugs, features, ideas, proposals, membership |
| `workflows/` | Org-wide GitHub Actions (onboarding, labeling, health checks) |
| `templates/` | Reusable README templates from the org design system |
| `CONTRIBUTING.md` | How to contribute to Hidden Alchemy projects |
| `CODE_OF_CONDUCT.md` | Community standards and enforcement |
| `SECURITY.md` | Vulnerability reporting via GitHub private advisories |
| `SUPPORT.md` | Where to ask questions vs. file issues |
| `GOVERNANCE.md` | Decision-making, ownership, and membership model |

Many of these files are inherited automatically by other repositories in the
organization via GitHub's default community health file behavior, so changes
here propagate org-wide.

## Using the organization profile

This repository's `profile/README.md` is distinct from this root `README.md`:
the former is the public face of the organization, the latter explains the
purpose of this repository. Both are maintained as part of the org foundation
milestones rather than as an afterthought to any project work.

## License

MIT — see [LICENSE](./LICENSE).