# Jaqal

*Quality loom for Claude Code — from [Jacquard Labs](https://github.com/jacquard-labs)*

A structured workflow for keeping your product, codebase, frontend, and architecture healthy. Provides quality gates for feature development and periodic review agents that track trends over time.

## Install

```bash
claude install github:jacquard-labs/jaqal
```

Then run `/jaqal-init` in your project to set up context documents and review directories.

## What's included

### Quality gates — feature development workflow

```
/gate-should-we-build [idea]     → BUILD / SMALLER / DEFER / DON'T
     ↓
(brainstorm + design doc)
     ↓
/gate-design-review              → PROCEED / REVISE / RETHINK
     ↓
(implement)
     ↓
/audit                           → PASS / FIX AND RE-AUDIT / NEEDS DISCUSSION
     ↓
/gate-acceptance                 → SHIP / FIX AND RE-CHECK / HOLD
     ↓
Merge
```

| Command | Purpose |
|---------|---------|
| `/gate-should-we-build [idea]` | Evaluate whether a feature is worth building |
| `/gate-design-review` | Review a design doc before implementation |
| `/audit` | Run all auditors (security, code, docs, architecture, UX, frontend) |
| `/gate-acceptance` | Product acceptance review before merge |

### Periodic reviews

| Command | Cadence | What it checks |
|---------|---------|----------------|
| `/review-codebase-health` | Weekly / pre-milestone | Tech debt, dependencies, tests, API consistency |
| `/review-frontend-health` | Monthly / post-UI-sprint | Design system consistency, a11y, responsive behavior |
| `/review-architecture` | Quarterly / pre-major-feature | Dependency graph, boundaries, coupling, evolution readiness |
| `/review-product-health` | Monthly | PRODUCT.md accuracy, persona drift, scope creep |
| `/deep-review` | As needed | Runs all four reviews in parallel, compiles master summary |

Reviews save reports to `docs/` subdirectories with dates, so you can track trends across reviews.

### Backlog management

| Command | Purpose |
|---------|---------|
| `/backlog-hygiene` | Find open issues to close — resolved, obsolete, or duplicated |
| `/backlog-priorities` | Ranked shortlist of what to work on next, by work mode |

Both are recommend-only — they never modify issues.

### Context extraction

| Command | Purpose |
|---------|---------|
| `/extract-product-context` | Analyze codebase to populate PRODUCT.md |
| `/extract-design-system` | Analyze codebase to populate DESIGN.md |

### Agents

These agents are available for direct use or are dispatched by the commands above:

| Agent | Role |
|-------|------|
| `review-codebase-health` | Periodic codebase health review |
| `review-frontend-health` | Periodic frontend health review |
| `review-architecture` | Deep architecture review |
| `review-product-health` | Periodic product review |
| `product-reviewer` | Product fit and user experience review |
| `ux-reviewer` | Visual design and interaction quality |
| `frontend-reviewer` | Frontend code quality and performance |
| `security-auditor` | OWASP Top 10, auth, secrets, headers |
| `code-auditor` | Code quality, complexity, consistency |
| `doc-auditor` | Documentation coverage and gaps |
| `architect-reviewer` | Supervises audit-fix-review pipeline |
| `fix-planner` | Consolidates audit findings into prioritized fix plan |
| `pr-writer` | Generates PR descriptions from git changes |
| `backlog-hygiene` | Finds resolvable/obsolete/duplicate issues |
| `backlog-priorities` | Ranks open issues by work mode and product alignment |

## How it works

The workflow is built around three context documents that live in your project root:

- **PRODUCT.md** — Who your users are, what the product does, what you're not building, and what's broken. Every product decision references this.
- **DESIGN.md** — Your actual design system extracted from code: colors, typography, spacing, component patterns. Every UI review references this.
- **CLAUDE.md** — Technical conventions and the review workflow itself. Gets updated by `/jaqal-init`.

The `/jaqal-init` command creates these documents by analyzing your codebase, scaffolds the `docs/` review directories, and adds the workflow to CLAUDE.md.

## After setup

1. **Review PRODUCT.md** — The extraction is evidence-based but sections like product principles and "what we're NOT building" need your judgment.
2. **Review DESIGN.md** — Check the anti-patterns section (left empty for you) and resolve any inconsistencies flagged at the bottom.
3. **Start using gates** — Run `/gate-should-we-build` before your next feature.
4. **Schedule reviews** — Run `/deep-review` monthly to track health trends.

## Maintenance

After each review cycle:

1. Fix **critical** findings before the next feature
2. File **important** findings as tasks for this cycle
3. **Track** minor findings — they compound if ignored
4. Update context docs when reviews surface changes:
   - `/review-product-health` → update PRODUCT.md
   - `/review-frontend-health` → update DESIGN.md
   - `/review-architecture` → update CLAUDE.md

## License

MIT
