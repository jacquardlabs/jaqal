---
description: Run all four periodic reviews in parallel — codebase health, frontend health, architecture, and product health — then compile a master summary with prioritized actions
allowed-tools: Read, Glob, Grep, Bash, Task, Write, Edit
---

# Deep review — full periodic review suite

Run every periodic review against the current codebase on main. This is the "run everything" command for maintenance cycles.

Read CLAUDE.md, PRODUCT.md, and DESIGN.md first.

## Phase 1 — Run all four reviews in parallel

Spawn all four as subagents simultaneously using the Agent tool — do not run them sequentially.

Use these exact `subagent_type` values:

1. **`review-codebase-health`** — Architecture coherence, technical debt inventory, dependency health, test health, API consistency. Saves to `docs/jaqal/health-reviews/YYYY-MM-DD-health-review.md`.

2. **`review-frontend-health`** — Design system consistency, accessibility audit, frontend code quality, responsive spot-check. Saves to `docs/jaqal/frontend-reviews/YYYY-MM-DD-frontend-review.md`.

3. **`review-architecture`** — Map dependencies, evaluate boundaries/complexity/evolution readiness/data layer. Saves to `docs/jaqal/architecture-reviews/YYYY-MM-DD-architecture-review.md`.

4. **`review-product-health`** — PRODUCT.md accuracy, product coherence, onboarding path, proposed PRODUCT.md updates. Saves to `docs/jaqal/product-reviews/YYYY-MM-DD-product-review.md`.

Each agent already knows its full workflow — just tell it the project path and today's date. Run all four with `run_in_background: true`.

## Phase 2 — Compile master summary

After all four reviews complete, read all four reports and synthesize a single master summary.

### Cross-review findings

Identify findings that appear in multiple reviews. These are systemic issues, not isolated ones — they get elevated priority. For example:
- Architecture review flags coupling AND codebase health flags related tech debt = systemic issue
- Product review flags a feature as low-value AND frontend review flags its code as complex = removal candidate
- Frontend review flags design drift AND product review flags persona drift = alignment problem

### Prioritized action plan

Compile a single prioritized list across all four reviews:

**Critical (this week)**
All critical findings from every review, deduplicated and ordered by impact.

**Important (this month)**
All important findings, grouped by theme rather than by which review found them.

**Track (next review cycle)**
Items to monitor. Note which review surfaced each one so you know where to check progress.

### Context doc updates

Based on the reviews, list specific updates needed for each context doc (per the maintenance workflow):
- **PRODUCT.md** — changes proposed by product health review
- **DESIGN.md** — changes proposed by frontend health review
- **CLAUDE.md** — changes proposed by architecture review

Do NOT apply these changes. Present them as proposed diffs for the user to review and approve.

### Metrics dashboard

Pull the metrics snapshots from the codebase health and frontend health reports into a single table for easy trend tracking:

| Metric | Value | Trend vs last review |
|--------|-------|---------------------|
| Lines of code | — | — |
| Test coverage | — | — |
| TODO/FIXME count | — | — |
| Outdated deps | — | — |
| Known vulnerabilities | — | — |
| Component count | — | — |
| Bundle size | — | — |
| Design system deviations | — | — |

If previous review reports exist in the `docs/jaqal/` subdirectories, compare against the most recent one and fill in the trend column. Otherwise mark as "baseline".

Save the master summary to `docs/jaqal/health-reviews/YYYY-MM-DD-deep-review-summary.md`.
