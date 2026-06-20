---
description: Periodic product review — evaluate product coherence, scope drift, and roadmap alignment
allowed-tools: Read, Glob, Grep, Bash, Task
---

# Product health review

A periodic check on the product itself, not the code. Run monthly or when you feel the product is drifting.

Read PRODUCT.md first.

## Run the review

Spawn @agent-review-product-health. It detects whether a live issue tracker is active and adjusts accordingly, checks whether PRODUCT.md is still true (personas, principles, feature inventory, "not building" list, known problems), evaluates product coherence and the onboarding path, then proposes specific PRODUCT.md updates as a diff. It saves the report to `docs/jaqal/product-reviews/YYYY-MM-DD-product-review.md` and compares against the previous review if one exists.

Tell it the project path and today's date. Surface its report when it returns. Do not apply the proposed PRODUCT.md changes — present them for review.
