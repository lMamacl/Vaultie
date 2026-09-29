---
trigger: model_decision
description: "Apply when producing documentation, analyses, specifications, research, lore, plans, explanations, technical writing, or other substantive content. Enforces completeness, explicit reasoning structure, traceability, preservation of distinctions, and detection of missing implied content."
---

# Content Quality and Completeness Standard

## Core rule

Do not confuse a shorter answer with a better answer.

The goal is **complete, structured, readable substance**. Compress wording, not reasoning.

Never remove a requested thread merely because it is difficult, secondary, or expensive to explain.

## Requirement coverage

Before writing, identify every explicit request and constraint.

Before finalizing, check that each one is:
- answered directly;
- handled in an explicit section;
- intentionally excluded with a reason; or
- blocked by missing evidence.

No silent omissions.

## Structure for substantive analysis

When appropriate, distinguish:

1. **What is established** — source/project facts.
2. **What follows from those facts** — reasoned interpretation.
3. **What is proposed** — recommendation/design option.
4. **What is unknown or missing** — evidence/questions/gaps.
5. **What conflicts** — contradictory sources, requirements, or assumptions.
6. **What follows next** — concrete implications or actions.

Do not blend these categories into one voice.

## Missingness / implied-content review

After drafting, inspect relationships between sections and ask:

> What can the reader logically infer from the text that the text should have stated explicitly but currently does not?

Examples:
- a stated goal with no success condition;
- a mechanism with no actor/owner;
- a consequence with no causal path;
- an API description with no error behavior;
- a historical claim with no source basis;
- a character motivation with no event that establishes it;
- a rule with no exception or boundary.

Resolve important gaps by adding evidence, explanation, or an explicit unresolved marker.

## Avoid AI-compression failure modes

Do not:
- collapse several different concepts into a generic umbrella sentence;
- replace concrete analysis with buzzwords;
- turn a sequence of causes into a shallow list of outcomes;
- repeat conclusions instead of adding missing reasoning;
- omit counterexamples or limitations that materially affect interpretation;
- silently normalize contradictions;
- invent connective tissue when the source material does not establish it.

## Detail without bloat

When more detail is required, expand by **dimension**, not repetition:
- mechanism;
- context;
- actors;
- constraints;
- chronology;
- dependencies;
- examples;
- edge cases;
- consequences;
- uncertainty.

A long document should become more informative as it becomes longer.
