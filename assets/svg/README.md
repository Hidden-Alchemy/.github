# Shared Visual Assets — usage rules

This directory is the **single shared location** for organization identity
assets per the Hidden Alchemy PRD §16. Assets here are org-identity assets, not
project-specific illustrations; project repositories link to them rather than
copying them.

## Files

| File | Purpose |
|:---|:---|
| `hero-pipeline.svg` | The transformation pipeline: `IDEA → CONCEPT → ARCHITECTURE → SYSTEM → AUTOMATION → REALITY` |
| `contribution-pathway.svg` | The participation pathway: `EXPLORE → DISCUSS → CONTRIBUTE → COLLABORATE → RECOGNITION → TRUST → MEMBERSHIP ELIGIBILITY` |

## Logo set (`assets/logos/`)

The canonical Hidden Alchemy logos live in `assets/logos/`. They are provided
as PNGs in backgrounded and transparent flavors:

| File | Aspect | Use |
|:---|:---|:---|
| `logo-black-transparent.png` | square | Primary identity mark on transparent background (gold/cream glyph) — embeds cleanly in both GitHub color modes |
| `logo-white-transparent.png` | square | Bronze glyph on transparency — higher contrast on light backgrounds |
| `Hidden-Alchemy-header-logo-black-bg.png` | wide banner | Dark banner version (for dark-mode contexts) |
| `Hidden-Alchemy-header-logo-white-bg.png` | wide banner | Light banner version (for light-mode contexts) |
| `Hidden-Alchemy-Logo-200x200-black-bg.png` | square | Org-avatar candidate (dark background) |
| `Hidden-Alchemy-Logo-200x200-white-bg.png` | square | Org-avatar candidate (light background) |

> Filename note: the logo files are pre-existing brand assets and keep their
> original names (mixed case) — an approved exception to the kebab-case rule,
> since renaming user-provided identity assets was judged riskier than
> preserving them. Newly-authored assets must still follow kebab-case.

### Choosing the right logo

- For a single embed that must read in **both** GitHub modes, use
  `logo-black-transparent.png` (gold/cream glyph on transparency).
- For a **dark-only** context use `Hidden-Alchemy-header-logo-black-bg.png` or
  `Hidden-Alchemy-Logo-200x200-black-bg.png`.
- For a **light-only** context use the `-white-bg` equivalents.
- The org avatar and any org-branding image applied through GitHub's UI are
  human-set actions (no public API); use the 200×200 pair as candidates.

## Naming convention

- `kebab-case`, purpose-first: `hero-pipeline.svg`, `contribution-pathway.svg`.
- No version suffixes (`hero-pipeline-v2.svg`). Breaking redesigns replace the
  file in place; git history preserves the previous version.
- If a new org-identity asset is needed, name it by purpose before anything
  else.

## Referencing from repositories

Always reference the raw content URL on the `.github` repo's default branch
(`main`). This is a single point of truth — do not copy asset files into
individual project repos.

```
https://raw.githubusercontent.com/Hidden-Alchemy/.github/main/assets/svg/hero-pipeline.svg
```

Example embed in Markdown:

```md
<img src="https://raw.githubusercontent.com/Hidden-Alchemy/.github/main/assets/svg/hero-pipeline.svg"
     width="100%" alt="IDEA → CONCEPT → ARCHITECTURE → SYSTEM → AUTOMATION → REALITY" />
```

## Authoring rules

- Every SVG requires a `<title>` and, where meaningful, a `<desc>`.
- Every animated SVG's static frame must be the actual first frame of the
  animation, so the illustration is complete even if animation is disabled.
- Because these SVGs are embedded via `<img>`, the page's `currentColor` does
  **not** reach into them. Use explicit colors verified against both GitHub
  backgrounds (`#0d1117` dark, `#ffffff` light): Bone `#F3F0E8` label text over
  a translucent Ink `#0B0B0A` backing reads on both modes, with Gold
  `#BD9C61` and Verdigris `#4C6B5C` as accents only.
- Keep files under 150 KB. No GIFs; motion, if used, is slow and low-amplitude.
- Accessible alternative text (the `alt` attribute) must always be provided at
  the embed site.