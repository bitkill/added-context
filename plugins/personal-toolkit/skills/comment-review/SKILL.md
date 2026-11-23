---
name: comment-review
description: Review code comments and flag hidden defects. Remove unnecessary comments when asked.
---

Review the supplied files or diff. Default to `git diff main`.

Keep a comment if it meets any of these criteria.

- It carries a license notice or defines a public API contract.
- It explains a verified external constraint.
- It links to an issue or RFC that explains a constraint.
- It controls formatting or suppresses a confirmed false positive or style-only warning.

Flag redundant comments, banners, and commented-out code. Trace workarounds and check suppressed rules. Flag hidden defects. If a comment explains confusing code, name the symbol and suggest a refactor.

For reviews, cite each recommendation at `file:line`. For requested cleanup, remove only unnecessary comments. Report changed files, removal count, refactor targets, and skips.
