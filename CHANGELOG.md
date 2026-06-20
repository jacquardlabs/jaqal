# CHANGELOG

<!-- version list -->

## v2.0.0 (2026-06-20)

### Features

- Rename plugin from Jaqal to Studious ([#35](https://github.com/jacquardlabs/studious/pull/35),
  [`2e1809c`](https://github.com/jacquardlabs/studious/commit/2e1809c7f8731082f3a7ae35c86fc5092e9e232c))

### Breaking Changes

- The plugin installs as studious@... and the init command is /studious-init. Existing installs and
  /jaqal-init muscle memory break; reinstall under the new name.


## v1.5.0 (2026-06-20)

### Bug Fixes

- Align product-reviewer verdicts to the gates, specify doc discovery (I5, I6)
  ([#23](https://github.com/jacquardlabs/jaqal/pull/23),
  [`76c71cd`](https://github.com/jacquardlabs/jaqal/commit/76c71cd58cf2aa3cc67c55250daa44ee18f20060))

- Audit cleanup batch (I7, I8, I9, minors) ([#23](https://github.com/jacquardlabs/jaqal/pull/23),
  [`76c71cd`](https://github.com/jacquardlabs/jaqal/commit/76c71cd58cf2aa3cc67c55250daa44ee18f20060))

- Re-wire the PR gate hook as a plugin-level hooks.json (B1)
  ([#23](https://github.com/jacquardlabs/jaqal/pull/23),
  [`76c71cd`](https://github.com/jacquardlabs/jaqal/commit/76c71cd58cf2aa3cc67c55250daa44ee18f20060))

- Reconcile /gate-audit severities, diff base, and a11y call (B2, I1, I2)
  ([#23](https://github.com/jacquardlabs/jaqal/pull/23),
  [`76c71cd`](https://github.com/jacquardlabs/jaqal/commit/76c71cd58cf2aa3cc67c55250daa44ee18f20060))

### Features

- Enforce language idioms and conventions in code-auditor (I3, I4)
  ([#23](https://github.com/jacquardlabs/jaqal/pull/23),
  [`76c71cd`](https://github.com/jacquardlabs/jaqal/commit/76c71cd58cf2aa3cc67c55250daa44ee18f20060))

- Remediate the behavioral audit — hook fix, idiom enforcement, gate-contract repairs
  ([#23](https://github.com/jacquardlabs/jaqal/pull/23),
  [`76c71cd`](https://github.com/jacquardlabs/jaqal/commit/76c71cd58cf2aa3cc67c55250daa44ee18f20060))


## v1.4.0 (2026-06-20)

### Features

- Add a PR-time gate reminder hook ([#22](https://github.com/jacquardlabs/jaqal/pull/22),
  [`36663d4`](https://github.com/jacquardlabs/jaqal/commit/36663d4c34ff6c58b7856b4ee06b953c13ea9055))


## v1.3.0 (2026-06-20)

### Continuous Integration

- Push-notify marketplace on release ([#16](https://github.com/jacquardlabs/jaqal/pull/16),
  [`93a47f2`](https://github.com/jacquardlabs/jaqal/commit/93a47f2fe36493f35e85760b514b71c73cbee991))

### Documentation

- Document the command/agent naming conventions
  ([#17](https://github.com/jacquardlabs/jaqal/pull/17),
  [`a379219`](https://github.com/jacquardlabs/jaqal/commit/a37921938d8e964253f33b6047b3dfc762309da4))

- Fix a11y audit claim, flag backlog GitHub-only, clarify init chaining
  ([#18](https://github.com/jacquardlabs/jaqal/pull/18),
  [`12f0360`](https://github.com/jacquardlabs/jaqal/commit/12f0360f763ab1d019004d7a0de6560582e39e0d))

### Features

- Add natural-language trigger skills for the three product gates
  ([#21](https://github.com/jacquardlabs/jaqal/pull/21),
  [`433e807`](https://github.com/jacquardlabs/jaqal/commit/433e80785330b7e09a5e2418e080212b2667d0d1))

### Refactoring

- Collapse duplicated review commands into thin agent wrappers
  ([#8](https://github.com/jacquardlabs/jaqal/pull/8),
  [`b5ca8c3`](https://github.com/jacquardlabs/jaqal/commit/b5ca8c3efec9624f50f7cf0b0448b0a25549da23))

- Collapse review commands into /deep-review [area] and finalize naming
  ([#17](https://github.com/jacquardlabs/jaqal/pull/17),
  [`a379219`](https://github.com/jacquardlabs/jaqal/commit/a37921938d8e964253f33b6047b3dfc762309da4))

- Collapse review duplication and remove vestigial fix layer
  ([#8](https://github.com/jacquardlabs/jaqal/pull/8),
  [`b5ca8c3`](https://github.com/jacquardlabs/jaqal/commit/b5ca8c3efec9624f50f7cf0b0448b0a25549da23))

- Collapse the 5 review commands into /deep-review [area]
  ([#17](https://github.com/jacquardlabs/jaqal/pull/17),
  [`a379219`](https://github.com/jacquardlabs/jaqal/commit/a37921938d8e964253f33b6047b3dfc762309da4))

- Pin agent models by stakes ([#19](https://github.com/jacquardlabs/jaqal/pull/19),
  [`6c4d630`](https://github.com/jacquardlabs/jaqal/commit/6c4d630db86eaab82247b81c9b5d41f91ab0db2e))

- Remove vestigial fix-orchestration layer ([#8](https://github.com/jacquardlabs/jaqal/pull/8),
  [`b5ca8c3`](https://github.com/jacquardlabs/jaqal/commit/b5ca8c3efec9624f50f7cf0b0448b0a25549da23))

- Rename /audit to /gate-audit and drop Gate N labels
  ([#20](https://github.com/jacquardlabs/jaqal/pull/20),
  [`0f2975b`](https://github.com/jacquardlabs/jaqal/commit/0f2975b457cbb56e297ad115aaf0d30c6ed2f3e9))

- Rename architect-reviewer agent to architecture-auditor
  ([#17](https://github.com/jacquardlabs/jaqal/pull/17),
  [`a379219`](https://github.com/jacquardlabs/jaqal/commit/a37921938d8e964253f33b6047b3dfc762309da4))


## v1.2.0 (2026-06-20)

### Features

- Include /review-readme in /deep-review and flag README drift in /audit
  ([#7](https://github.com/jacquardlabs/jaqal/pull/7),
  [`f0222e3`](https://github.com/jacquardlabs/jaqal/commit/f0222e34d3602b14337cb4c725b6f398fcbfca24))


## v1.1.0 (2026-06-20)

### Documentation

- Rewrite README in Bryan's voice ([#3](https://github.com/jacquardlabs/jaqal/pull/3),
  [`f2222d1`](https://github.com/jacquardlabs/jaqal/commit/f2222d1443bfe0b4cc667aabeb685f5687fded26))

### Features

- Add /review-readme drift review and README creation in /jaqal-init
  ([#6](https://github.com/jacquardlabs/jaqal/pull/6),
  [`653bdb6`](https://github.com/jacquardlabs/jaqal/commit/653bdb68316a8fd37fce5161cb047894469b76b9))


## v1.0.0 (2026-06-20)

- Initial Release
