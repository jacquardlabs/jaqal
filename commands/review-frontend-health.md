---
description: Periodic frontend health review — design consistency, accessibility, performance, and component quality across the entire UI
allowed-tools: Read, Glob, Grep, Bash, Task
---

# Frontend health review

A periodic review of the entire frontend, not scoped to any feature branch. Run on main after a batch of features ships, or monthly.

Read CLAUDE.md, PRODUCT.md, and DESIGN.md first.

## Run the review

Spawn @agent-review-frontend-health. It evaluates design system consistency against DESIGN.md, accessibility, frontend code quality, and responsive behavior, then compiles a report with critical/important/track findings, a metrics snapshot, and proposed DESIGN.md updates. It saves the report to `docs/jaqal/frontend-reviews/YYYY-MM-DD-frontend-review.md` and compares against the previous review if one exists.

Tell it the project path and today's date. Surface its report when it returns.
