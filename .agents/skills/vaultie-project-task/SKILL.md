---
name: vaultie-project-task
description: Turns a project request into a traceable engineering plan with repository evidence, delegation, acceptance criteria and verification commands.
---

# Project Task Workflow

1. Determine the exact project root; read instructions and Git status.
2. Read related Vaultie concepts/patterns/decisions; use research if important facts may be stale.
3. Decompose into tasks with explicit dependencies, parallelizable steps, touched paths, non-goals, assumptions, risks and rollback notes if relevant.
4. Ask `project-architect` for design when the task crosses modules or changes contracts; ask `project-researcher` for unresolved/current external facts.
5. Present a plan and wait for user approval for high-risk or multi-file implementation.
6. After approval, hand off bounded work to `project-engineer`; afterward use `project-reviewer` and (where risk warrants) `project-security-reviewer`.
7. Close only when each requirement maps to a code change and actual verification evidence.

Do not commit, push, merge, deploy, mutate production data, or silently edit Vaultie canonical knowledge.