---
name: test
description: Run the smallest relevant test scope first, expand only when evidence requires it, and avoid expensive broad validation unless the change is cross-cutting.
---

# Test skill

Use this skill when validating a code change, reproducing a failure, or deciding which tests to run.

## Goal
Minimize test runtime, context usage, and unnecessary repository exploration while preserving useful confidence.

## Workflow
1. Identify the files and behavior changed by the current task.
2. Prefer an existing test that directly targets the changed function, module, route, component, or package.
3. Run one narrow test target first when possible, such as a single test file, test class, test name, package, or affected target.
4. If that passes, stop unless the change crosses module boundaries, modifies shared infrastructure, changes public interfaces, or the user explicitly requests broader validation.
5. If that fails, inspect only the failure output and directly implicated code before expanding the test scope.
6. Expand progressively: single test, nearby test group, affected package, broader suite. Skip levels that do not add useful signal.
7. Do not run full repository test suites by default.
8. Do not repeatedly rerun unchanged passing tests unless a subsequent code change could affect them.

## Context efficiency
- Reuse test commands already documented in AGENTS.md, package scripts, Makefiles, CI config, or nearby README files.
- Avoid reading unrelated test directories.
- Prefer targeted command discovery over scanning every package manifest.
- Keep failure summaries concise and retain only the error details needed to choose the next action.

## Result reporting
Report:
- the exact test or check that was run
- whether it passed or failed
- the narrow reason for any scope expansion
- any important validation that remains unrun

Stop when the change has proportionate validation and there is no evidence that broader testing would materially increase confidence.
