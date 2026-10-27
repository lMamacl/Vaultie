---
name: vaultie-bootstrap-project
description: Registers or prepares a software project under labs using repository evidence, a minimal project charter and Vaultie links without rewriting an existing subrepository.
---

# Bootstrap Project in Labs

1. Confirm the project folder and actual Git root. Inspect `.git`, `.gitmodules`, `git status`, existing README, license, manifests, tests and agent instructions.
2. Do not initialize, convert, move, or replace a Git repository/submodule without explicit approval.
3. Create a project charter proposal containing: goal, target users, non-goals, functional/nonfunctional requirements, current stack, constraints, architecture notes, risks, acceptance criteria and first milestones.
4. Identify relevant Vaultie notes and ADRs. Missing knowledge becomes research tasks or Inbox proposals, never fake citations.
5. If an `AGENTS.md` or `.agents/` already exists, inspect and preserve it. Suggest the smallest compatible additions.
6. Do not implement product features during bootstrap. Present changed files, tests and unresolved decisions.

Project-specific code changes require a separate approved implementation plan.