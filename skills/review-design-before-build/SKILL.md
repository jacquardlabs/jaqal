---
name: review-design-before-build
description: Use when a design doc or spec for a feature is ready and the user is about to start implementing — they want the design checked before build effort goes in. Triggers on "review this design", "is this design sound", "any problems with this design before I build it". This routes to Studious's design-review gate. Do NOT use for code review, after implementation has already started, or for evaluating whether to build at all (that's the should-we-build gate).
---

# Does this design serve users?

This is the natural-language entry to Studious's design-review gate. A design is on the table and the user wants it vetted before spending build effort — route that to the gate.

Invoke the `/gate-design-review` command. Do not reimplement its logic here — the command owns it. It product-reviews the most recent design doc against PRODUCT.md and walks the design as the primary persona would experience it, returning **PROCEED TO PLAN / REVISE / RETHINK**.

Surface the recommendation; do not begin implementation until the design is sound.
