---
tags: [agents, architecture]
---

# Recommended Architecture — Three Tiers

Back to [[00-Index]]. Build Tier 1. Only move to Tier 2 if Tier 1 provably fails on real tasks you care about. Tier 3 is a research project, not a weekend build — include it here so it's not confused with the MVP.

## Tier 1 — MVP (buildable in days)

```
User goal
   │
   ▼
Investigator pass (one LLM call, tools available)
   - restates the goal
   - lists what it knows vs. doesn't (plain bullet list, not numeric confidence)
   - does ONE round of tool use if a real unknown blocks planning:
       search prior art (Exa / Context7), read relevant files
   │
   ▼
Planner pass
   - proposes a plan as ordered steps
   - explicitly lists: "what could this plan miss?" as its own last step
   │
   ▼
Critic pass (same model, different system prompt — or a cheaper/different model)
   - given the plan, asks: what assumption does this depend on,
     what's the simplest existing solution, what should be tested first
   - can send it back to Planner once, not in a loop
   │
   ▼
Execute + run real tests
   │
   ▼
Verify: did the actual test/build/lint output confirm the fix,
        not "does this look right"
   │
   ▼
If tests fail → one more Investigator→Planner pass with the failure as new evidence,
                then stop and hand back to the human (don't loop silently)
```

State lives in a single JSON/Markdown file per task (see [[04-Implementation-Guide]]), not a full graph database. Hard caps: e.g. 3 iterations, 10 tool calls, then stop and report status honestly rather than continuing to "investigate."

This alone gets you: questioning the plan, one round of prior-art search, one adversarial critique pass, and grounding in real test output — which is most of what the original proposal wanted, at a fraction of the engineering and compute cost.

## Tier 2 — Add real dependency expansion

Add this only once Tier 1 works, and only for the specific failure mode "the fix didn't address the real cause because of an upstream dependency."

- For code: use actual static analysis (call graphs, import graphs — e.g. tooling like `madge`, `pydeps`, or your language's LSP) to compute what actually depends on what. Feed *that* into the Planner as ground truth, instead of asking the LLM to guess dependencies from reading code casually. This is the single highest-leverage upgrade from the original proposal, because it replaces an LLM guess with a computed fact.
- For "is there already a known solution," make the prior-art search step mandatory rather than optional, and require the agent to cite what it found before proposing a novel fix (see [[03-Tools-and-APIs]] for Exa code search / Context7 docs / GitHub search).
- Add a lightweight "problem notes" markdown file that persists *within* a task (not across tasks yet): facts found, dependencies discovered, tests added. This is your placeholder for the "problem graph" — a flat file is enough at this scale; you don't need a graph database until you have evidence a flat file isn't working.

## Tier 3 — Research-grade (don't build this first)

- Persistent cross-session memory / knowledge graph reused across future tasks. Real unsolved problems here: staleness, contradiction resolution, retrieval precision at scale (see [[01-Verdict]]).
- A trained process reward model scoring each reasoning step, replacing self-reported confidence with an actual learned signal (see [[05-Research-Foundations]]).
- True multi-agent debate with independent models per role for high-stakes changes only (e.g. production deploys), where the 2–5x compute cost is justified by the cost of an error.

## What to explicitly not build

- A numeric "confidence" field the LLM fills in for itself, presented as if it were calibrated probability. Use `verified / inferred / assumed` labels instead, tied to an actual source (test result, static analysis, doc citation) for anything marked "verified."
- An uncapped research loop. Every investigation step needs a budget and a stopping rule, checked in code, not left to the model's judgment about when it's "done."
- A rebuild of an existing coding agent's harness from scratch before checking whether your current agent (Claude Code, Cursor, etc.) already covers 80% of this via planning mode, sub-agents, and MCP tools plus a good system prompt.
