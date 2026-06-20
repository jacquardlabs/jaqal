---
description: Periodic whole-codebase health review — architecture, debt, patterns, dependencies
allowed-tools: Read, Glob, Grep, Bash, Task
---

# Codebase health review

A periodic review of the entire codebase, not scoped to any feature branch. Run on main/trunk on a regular cadence (weekly or before major milestones).

Read CLAUDE.md and PRODUCT.md first for full project context.

## Run the review

Spawn @agent-review-codebase-health. It evaluates architecture coherence, technical debt, dependency health, test health, and API/interface consistency, then compiles a report with critical/important/track findings and a metrics snapshot. It saves the report to `docs/jaqal/health-reviews/YYYY-MM-DD-health-review.md` and compares against the previous review if one exists.

Tell it the project path and today's date. Surface its report when it returns.
