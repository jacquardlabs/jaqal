---
description: Periodic whole-codebase health review — architecture, debt, patterns, dependencies
allowed-tools: Read, Glob, Grep, Bash, Task
---

# Codebase health review

This is a periodic review of the entire codebase, not scoped to any feature branch. Run this on main/trunk on a regular cadence (weekly or before major milestones).

Read CLAUDE.md and PRODUCT.md first for full project context.

## Run these audits in parallel using subagents:

### 1. Architecture coherence

Spawn a subagent to evaluate:
- Does the current file/folder structure still match the intended architecture in CLAUDE.md?
- Are there modules that have grown beyond their original responsibility?
- Are there circular dependencies or coupling between modules that should be independent?
- Is the layering clean — do controllers call services, services call repositories, or has it gotten tangled?
- Are there patterns that started consistent but have drifted across different parts of the codebase?

### 2. Technical debt inventory

Spawn a subagent to find and catalog:
- All TODO, FIXME, HACK, XXX, and WORKAROUND comments in the codebase. Group by module and severity.
- Functions or files over 200 lines that should probably be split.
- Any copy-pasted logic that appears in more than two places (candidates for extraction).
- Commented-out code that's been sitting for more than one release cycle.
- Dead code: exported functions/components that nothing imports, unused variables, unreachable branches.

### 3. Dependency health

Spawn a subagent to run:
- Check for outdated dependencies (`npm outdated`, `pip list --outdated`, or equivalent).
- Check for known vulnerabilities (`npm audit`, `pip-audit`, `safety check`, or equivalent).
- Flag any dependencies that haven't been updated in 12+ months (potential abandonment risk).
- Flag any dependencies that are pinned to exact versions with no clear reason.
- Check for duplicate dependencies (multiple packages solving the same problem).

### 4. Test health

Spawn a subagent to evaluate:
- Overall test coverage. Run the coverage tool and report the number.
- Identify the 5 most-changed files in recent git history that have NO test coverage (high-risk gaps).
- Check for flaky tests — any tests that have been skipped, marked pending, or have retry logic.
- Check test-to-code ratio by module. Flag modules where the ratio is significantly below the project average.
- Are integration/e2e tests present for the critical user journeys listed in PRODUCT.md?

### 5. API and interface consistency

Spawn a subagent to check:
- Are API endpoints following a consistent naming convention (REST, or whatever the project uses)?
- Are error response formats consistent across all endpoints?
- Are authentication/authorization patterns applied uniformly?
- Do similar features use similar patterns, or has each feature invented its own approach?

## Compile the report

After all subagents return, synthesize into a single health report structured as:

### Summary
One paragraph: overall codebase health, biggest concern, biggest strength.

### Critical (address this week)
Issues that are actively causing problems or are one bad merge away from causing problems.

### Important (address this month)
Issues that will compound if left alone. Technical debt that's accruing interest.

### Track (revisit next review)
Things to monitor. Not urgent but trending in the wrong direction.

### Metrics snapshot
Capture these numbers so you can track trends across reviews:
- Total lines of code
- Test coverage percentage
- Number of TODO/FIXME comments
- Number of outdated dependencies
- Number of known vulnerabilities
- Largest file (lines)
- Deepest dependency chain

Save the report to `docs/health-reviews/YYYY-MM-DD-health-review.md`.
