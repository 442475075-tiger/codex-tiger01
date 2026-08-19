# Codex Instructions

## Scope
- Work only on files relevant to the current task.
- Start with the smallest likely directory or file set.
- Avoid repository-wide scans unless the task requires them.

## Context efficiency
- Read targeted files first.
- Reuse existing project docs and scripts instead of restating them.
- Do not inspect generated output, dependency caches, or build artifacts unless needed.
- Keep explanations concise and avoid repeating unchanged context.

## Changes
- Make the smallest change that fully solves the task.
- Preserve existing style and structure.
- Do not regenerate lockfiles unless dependencies change.
- Do not refactor unrelated code.

## Validation
- Run the narrowest relevant tests or checks first.
- Expand validation only when failures or cross-cutting changes justify it.
- Report what was checked and any remaining uncertainty.

## Git workflow
- Keep commits focused on one task.
- Summarize changed files and validation results in the final response.
