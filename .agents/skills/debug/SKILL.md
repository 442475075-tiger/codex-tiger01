---
name: debug
description: Debug a concrete bug, error, failing test, or unexpected behavior in this repository. Trigger when the user asks to diagnose, fix, investigate, trace, reproduce, or explain a defect. Do not trigger for broad refactors, feature work, or general code review.
---

# Debug workflow

1. Restate the failure in one sentence and identify the narrowest likely subsystem.
2. Inspect only the files, logs, tests, and call paths directly related to that subsystem.
3. Prefer exact error text, stack traces, failing test names, changed files, and nearby symbols as search anchors.
4. Form at most three plausible hypotheses. Rank them by evidence and test the cheapest hypothesis first.
5. Avoid repository-wide scans unless the local evidence is insufficient.
6. Before editing, identify the smallest change that addresses the verified cause.
7. Preserve existing APIs, style, and behavior outside the failing path.
8. Run the narrowest relevant test or reproduction command first. Expand validation only when needed.
9. Stop once the bug is fixed and the relevant validation passes. Do not perform unrelated cleanup or refactors.
10. In the final response, report the root cause, files changed, validation performed, and any remaining uncertainty. Keep it concise.

# Token efficiency

- Reuse already-read context instead of reopening unchanged files.
- Read targeted line ranges when possible.
- Skip generated files, vendored dependencies, caches, build output, lockfiles, and large unrelated assets unless evidence points there.
- Prefer existing tests and scripts over inventing new exploratory tooling.
- When blocked, ask for the smallest missing artifact or detail needed to continue.
