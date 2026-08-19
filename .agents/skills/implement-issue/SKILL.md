---
name: implement-issue
description: Implement a GitHub issue with minimal context usage. Use when the task references an issue number, issue URL, acceptance criteria, or a small scoped feature request.
---

# Implement Issue

## Goal
Complete one issue with the smallest relevant code and validation footprint.

## Workflow
1. Read the issue title, body, labels, and acceptance criteria first.
2. Identify the smallest likely code area from issue wording, paths, symbols, tests, or recent related changes.
3. Inspect only those files plus direct dependencies needed to understand the change.
4. Avoid broad repository exploration unless the issue cannot be localized after targeted search.
5. Summarize the intended change in one short plan before editing.
6. Make the minimum coherent code change that satisfies the issue.
7. Preserve existing APIs, patterns, naming, and formatting unless the issue explicitly requires a change.
8. Do not refactor unrelated code or regenerate unrelated files.

## Search discipline
- Prefer exact filenames, symbols, error text, route names, test names, and imports.
- Follow direct references outward only as needed.
- Stop exploring once the implementation path is clear.
- Do not reread unchanged files unless new evidence requires it.

## Validation
- Run the narrowest relevant tests, type checks, lint checks, or build target.
- Expand validation only when the change crosses package or module boundaries.
- If no relevant test exists, add one only when it is proportionate to the issue.

## Completion
Return a concise summary with:
- issue addressed
- files changed
- validation performed
- any remaining risk or follow-up

Stop after the issue is satisfied. Do not add opportunistic cleanup.
