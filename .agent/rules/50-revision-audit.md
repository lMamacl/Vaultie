---
trigger: model_decision
description: "Apply after substantial code, content, architecture, research, or documentation work. Performs a separate adversarial revision pass for correctness, omissions, unsupported claims, contradictions, scope drift, and quality regressions before final delivery."
---

# Adversarial Revision Gate

Do not use the creation pass as the review pass.

After producing a substantial result, mentally switch from **author mode** to **reviewer mode**.

## Reviewer questions

### A. Correctness
- Is every important statement or behavior supported?
- Are any details invented because they seemed likely?
- Does the result solve the requested problem rather than a nearby problem?
- Are there contradictions with the existing repository/material?

### B. Completeness
- Did every requirement appear in the result?
- Which requirement is currently least covered?
- What important information is implied but not explicitly addressed?
- Are edge cases, failure modes, or limitations missing?

### C. Consistency
- Are terms used consistently?
- Are names, interfaces, assumptions, and conventions coherent across sections/files?
- Does the implementation still match the approved plan?

### D. Specificity
- Could any paragraph be removed and lose no information?
- Did a generic phrase replace a concrete explanation?
- Is a reader expected to infer a critical missing step?

### E. Verification
- What evidence proves the most important claims?
- Which checks were actually executed?
- Which things remain unverified?

### F. Risk
- What is the most likely regression or misunderstanding?
- What is the least obvious failure path?
- What would a skeptical reviewer challenge first?

## Required response to findings

If the review finds a defect, omission, contradiction, unsupported claim, or scope problem:

1. fix it;
2. re-run the affected verification;
3. review the revised result again.

Do not merely mention defects that you can reasonably fix yourself.

## Stop condition

The work is ready for delivery only when no known material defect remains, or when a blocker is explicitly recorded as unresolved.
