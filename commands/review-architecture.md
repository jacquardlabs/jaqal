---
description: Deep architecture review — evaluate system structure, boundaries, and evolution path
allowed-tools: Read, Glob, Grep, Bash, Task
---

# Architecture review

A deep review of the system's architecture independent of any specific feature. Run quarterly, before a major new feature area, or when something feels "off" about how the system is evolving.

Read CLAUDE.md and PRODUCT.md first.

## Run the review

Spawn @agent-review-architecture. It maps the current structure (dependency graph, actual architecture style, load-bearing modules, data flow for core journeys), evaluates boundaries, complexity distribution, evolution readiness, and the data layer, then classifies findings (REFACTOR NOW / REFACTOR BEFORE [work] / DESIGN DECISION NEEDED / DOCUMENT AND ACCEPT) with a recommended priority order. It saves the report to `docs/jaqal/architecture-reviews/YYYY-MM-DD-architecture-review.md` and compares against the previous review if one exists.

Tell it the project path and today's date. Surface its report when it returns.
