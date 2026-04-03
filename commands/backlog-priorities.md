---
description: Curate a ranked shortlist from open GitHub issues based on your current intent — tech debt, maintenance, polish, or new initiative
allowed-tools: Read, Glob, Grep, Bash, Task
---

# Backlog priorities

Help decide what to work on next by curating a ranked shortlist from open issues.

Read PRODUCT.md and CLAUDE.md first for product context.

## Run the analysis

Spawn @agent-backlog-priorities to:

1. Fetch all open issues via `gh issue list`.
2. Read the most recent deep review summary and individual review reports.
3. Ask the user to pick a work mode:
   - **Tech debt** — code quality, refactoring, dependency upgrades, test coverage gaps
   - **Maintenance** — bug fixes, security patches, performance, accessibility
   - **Polish existing feature** — finish, adjust, or improve something already shipped
   - **New initiative** — start something from the roadmap, known problems, or backlog
4. Filter and rank issues by:
   - Severity from review reports (Critical/Important findings rank higher)
   - Product alignment (addresses PRODUCT.md known problems or principles)
   - Unblocking potential (enables other issues or features)
   - Context freshness (code areas with recent commits are cheaper to tackle)
5. Present top 3-5 with rationale.

## Output

The report presents:
- **Recommended (top pick)** — with 2-3 sentence rationale referencing PRODUCT.md or review findings
- **Also strong candidates** — 2-3 alternatives with one-line rationale each
- **Honorable mentions** — additional options worth considering

This command is recommend-only. It never starts work, creates branches, or modifies issues.
