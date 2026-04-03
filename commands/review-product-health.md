---
description: Periodic product review — evaluate product coherence, scope drift, and roadmap alignment
allowed-tools: Read, Glob, Grep, Task
---

# Product health review

A periodic check on the product itself, not the code. Run this monthly or when you feel the product is drifting.

Read PRODUCT.md first. This review evaluates whether PRODUCT.md is still accurate and whether the product is evolving coherently.

## Part 1 — Is PRODUCT.md still true?

1. **Persona check.** Read the personas in PRODUCT.md, then scan the recent feature history (git log, recent commits). Are we still building for the stated personas, or have we drifted toward building for ourselves / edge cases / hypothetical users?

2. **Principles check.** Read the product principles. For each one, find one recent feature decision that honored it and one that bent it. Are the principles still the right principles, or has the product evolved past them?

3. **Feature map accuracy.** Compare the feature map in PRODUCT.md against what actually exists in the codebase. Are there shipped features missing from the map? Are there features listed that were removed or never completed?

4. **"Not building" check.** Has anything from the "what we're NOT building" list crept in? Check recent features for scope that arguably crosses those boundaries.

5. **Known problems freshness.** Are the known problems still the real problems? Have any been fixed but not removed from the list? Are there new problems that should be added?

## Part 2 — Product coherence

1. **Does this feel like one product?** Mentally walk through the product as a new user. Open it cold. Navigate through the core features. Does it feel like a unified product or a collection of features that happen to live together?

2. **Feature interaction.** Do recently added features interact well with existing ones? Or are they isolated silos? Are there natural connections between features that we haven't built yet?

3. **Complexity audit.** For each feature, ask: if we removed this, would users notice? Would they care? Flag any features that add complexity without proportional value.

4. **Onboarding path.** Can a brand new user get to the core value proposition within 60 seconds? Walk through the first-time experience. Flag every point of friction, confusion, or unnecessary decision.

## Part 3 — Update PRODUCT.md

Based on this review, propose specific updates to PRODUCT.md:

- Personas that need updating (changed needs, new context)
- Principles that need revision or addition
- Features to add or remove from the map
- Items to add or remove from "not building"
- Known problems to add, remove, or reprioritize

Present the changes as a diff against the current PRODUCT.md. Don't apply them — present them for review.

Save the report to `docs/product-reviews/YYYY-MM-DD-product-review.md`.
