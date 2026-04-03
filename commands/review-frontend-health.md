---
description: Periodic frontend health review — design consistency, accessibility, performance, and component quality across the entire UI
allowed-tools: Read, Glob, Grep, Bash, Task
---

# Frontend health review

A periodic review of the entire frontend, not scoped to any feature branch. Run this on main after a batch of features ships, or monthly.

Read CLAUDE.md, PRODUCT.md, and DESIGN.md first.

## Run these audits in parallel using subagents:

### 1. Design system consistency

Spawn @agent-ux-reviewer to evaluate:
- Sample 5-8 representative pages/views across the product. For each, check whether typography, spacing, colors, and component usage match DESIGN.md.
- Flag any "one-off" styles — inline styles, magic numbers, or colors that aren't in the palette.
- Are there components that do the same thing but look different in different parts of the app?
- Has the design system drifted from what DESIGN.md describes? If so, which is right — the code or the doc?

### 2. Accessibility audit

Run accessibility checks across all pages. Spawn a subagent to manually check:
- Run through every interactive element: can you reach it with Tab? Can you activate it with Enter/Space?
- Check color contrast on all text against its background.
- Check every form: do inputs have associated labels? Are error messages linked via aria-describedby?
- Check every image: is alt text present and descriptive (not "image1.png")?
- Is there a skip-to-content link?
- Do all pages have a logical heading hierarchy (h1 > h2 > h3, no gaps)?

### 3. Frontend code quality

Spawn @agent-frontend-reviewer to evaluate the full frontend codebase:
- Component architecture health — are components growing too large or too coupled?
- State management patterns — consistent or fragmented?
- Performance patterns — any obvious bottlenecks in common user flows?
- Bundle analysis — run the build and report bundle size, largest chunks.
- Unused code — exports that nothing imports, components that no route renders.

### 4. Responsive spot-check

Spawn a subagent to check the 3 most important pages (the critical user journeys from PRODUCT.md) at three widths:
- 375px (mobile phone)
- 768px (tablet)
- 1440px (desktop)

For each, check:
- Does the layout adapt or just shrink?
- Is text readable without zooming?
- Are touch targets large enough on mobile?
- Does anything overflow horizontally?
- Is the navigation usable at each width?

## Compile the report

After all subagents return, synthesize into a single frontend health report:

### Summary
One paragraph: overall frontend health, biggest UX risk, biggest technical debt item.

### Critical (fix this week)
User-facing bugs, broken accessibility, or performance issues affecting core flows.

### Important (fix this month)
Design inconsistencies, growing technical debt, accessibility gaps on secondary flows.

### Track (revisit next review)
Polish items, minor inconsistencies, potential future problems.

### Metrics snapshot
- Total component count
- Bundle size (total and largest chunk)
- Accessibility issues by severity (if tooling available)
- Pages/views with no test coverage
- Design system deviation count (styles that don't match DESIGN.md)

### DESIGN.md updates
Propose any updates to DESIGN.md based on findings — new patterns that have emerged, decisions that should be codified, anti-patterns to add.

Save the report to `docs/frontend-reviews/YYYY-MM-DD-frontend-review.md`.
