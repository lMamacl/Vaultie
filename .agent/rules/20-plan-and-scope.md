---
trigger: model_decision
description: "Apply to non-trivial implementation, refactoring, architecture, migration, debugging, or feature work. Enforces explicit planning, plan-to-code traceability, scope control, and re-planning when new evidence invalidates the original approach."
---

# Plan Integrity and Scope Control

## When planning is mandatory

Prefer `/plan` before implementation when a task is:
- multi-file;
- architectural;
- behaviorally non-trivial;
- ambiguous;
- high-risk;
- likely to require several dependent steps;
- likely to introduce migrations, interface changes, or broad regressions.

Small, local, low-risk edits may be executed directly.

## Plan quality requirements

A useful implementation plan must contain:

1. **Problem** — what is wrong or what behavior is required.
2. **Goals** — observable outcomes that must exist when done.
3. **Non-goals** — nearby work that is intentionally excluded.
4. **Constraints** — architecture, compatibility, dependencies, tooling, performance, security, or user constraints.
5. **Repository evidence** — relevant files/components actually inspected.
6. **Design** — chosen approach and why it fits existing code.
7. **Change set** — concrete files/modules/interfaces expected to change.
8. **Execution order** — dependencies between steps.
9. **Acceptance criteria** — conditions proving each important step works.
10. **Verification** — exact checks/tests that will be used.
11. **Risks** — likely regressions and mitigations.
12. **Unknowns** — facts that still require verification.

A plan must not contain invented paths, APIs, configuration, or behavior.

## Plan as execution contract

Once a plan has been reviewed/approved:

- execute it in order unless a dependency requires reordering;
- keep each change attributable to one or more plan steps;
- do not silently expand scope;
- do not replace the chosen design merely because an alternative appears more elegant;
- do not mark a step complete without its acceptance/verification condition being satisfied.

## Deviation protocol

When implementation reveals that the approved plan is wrong or incomplete:

1. identify the exact discrepancy;
2. explain what repository evidence caused it;
3. determine what downstream steps are affected;
4. revise the plan before making changes that depend on the revision;
5. continue only from the corrected plan.

Never conceal plan drift inside code edits.

## Progress integrity

At meaningful checkpoints, compare:

`planned requirement -> implementation -> verification evidence`

Any item without a corresponding implementation or verification result remains open.
