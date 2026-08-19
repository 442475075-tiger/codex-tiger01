---
name: review-pr
description: Review a GitHub pull request with minimal context. Focus on changed files, likely regressions, correctness risks, tests, and required adjacent dependencies. Avoid broad repository exploration unless a concrete finding requires it.
---

# Review PR

Use this skill for pull request review tasks where context efficiency matters.

## Workflow

1. Read the PR title, description, changed-file list, and diff first.
2. Classify changed files by risk, such as behavior, data flow, security, API surface, migrations, tests, or configuration.
3. Inspect only the changed files and the smallest set of adjacent definitions needed to verify behavior.
4. Do not scan unrelated directories or historical files unless a specific diff hunk depends on them.
5. Prioritize findings that can cause incorrect behavior, regressions, security problems, data loss, broken compatibility, or missing validation.
6. Avoid style-only comments unless they hide a correctness or maintainability risk.
7. Reuse existing tests and repository conventions when judging expected behavior.
8. When a possible issue is uncertain, verify it with the narrowest targeted lookup before reporting it.
9. Stop expanding context once each meaningful finding has enough evidence.

## Output

Keep the review concise. For each finding, include:

- severity or impact
- file and relevant location
- why it is a problem
- a concrete fix direction

If no meaningful issues are found, say so and mention the main areas checked.

## Token discipline

- Prefer diff-first review.
- Avoid rereading files already inspected unless new evidence requires it.
- Avoid repository-wide searches when a file-level lookup is sufficient.
- Do not summarize unchanged code.
- Do not produce long restatements of the PR description or diff.
