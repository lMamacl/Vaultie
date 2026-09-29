---
trigger: model_decision
description: "Apply when creating, modifying, refactoring, debugging, testing, reviewing, or architecting software. Enforces repository-first implementation, correctness, maintainability, regression resistance, and evidence-based verification."
---

# Engineering Quality Standard

## Repository-first analysis

Before editing meaningful code, inspect enough of the repository to establish:

- project structure and relevant modules;
- build/runtime configuration;
- existing implementations solving similar problems;
- public interfaces and call sites affected by the change;
- existing tests and test conventions;
- lint/type-check/build commands and CI checks;
- relevant documentation, generated-code boundaries, and deprecation constraints.

Do not design against an imagined codebase.

## Change design

Choose the smallest coherent design that fully satisfies the requirement.

Prefer:
- existing project abstractions that already encode the needed invariant;
- explicit data flow and ownership;
- narrow interfaces;
- predictable error handling;
- local consistency over introducing a new pattern.

Avoid:
- speculative generalization;
- premature framework changes;
- duplicate utilities;
- hidden global state;
- magic constants without a domain reason;
- comments that merely restate code.

## Correctness review

For every meaningful code change, inspect:

1. normal execution;
2. invalid input;
3. empty/null/missing data;
4. boundary values;
5. failure and recovery paths;
6. partial failure and cleanup;
7. state transitions and repeated calls;
8. concurrency/async ordering when relevant;
9. permissions/security boundaries when relevant;
10. compatibility with existing callers.

Do not stop at the happy path.

## Tests

Tests must validate behavior, not just implementation details.

When applicable, add or update tests for:
- the requested behavior;
- the most likely regression;
- important failure paths;
- boundary conditions;
- integration boundaries affected by the change.

Never weaken a test only to make an implementation pass. If the intended behavior changed, update the test because the requirement changed and state that fact.

## Verification order

After implementation:

1. inspect the actual diff;
2. run the project's format/lint/static checks;
3. run type checking or compilation;
4. run focused tests;
5. run broader tests when the change can affect wider behavior;
6. inspect failures instead of assuming they are unrelated;
7. repeat after fixes.

A test suite passing does not replace reviewing the diff for missing behavior or scope drift.

## Definition of done

A code task is not complete merely because files were modified.

It is complete only when:
- the requested behavior exists;
- relevant existing behavior remains intact unless intentionally changed;
- the implementation follows repository conventions;
- relevant tests/checks pass or their limitations are explicitly reported;
- the final diff contains no accidental changes, debug leftovers, or unrelated refactors;
- the result has passed a separate self-review pass.
