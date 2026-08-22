---
tags: [agents, research, literature]
---

# Research Foundations

Back to [[00-Index]]. The original proposal invents fresh-sounding names for ideas that mostly already exist in the literature. Knowing the real names lets you find working implementations instead of prototyping from zero.

## Mapping invented terms to real techniques

| Original proposal's term | Real technique it maps to |
|---|---|
| "Challenger" pass that critiques the plan | Self-Refine / Reflexion / CRITIC — the generate → critique → revise loop |
| `identify_unknowns()` / `rank_by_information_gain()` | Question decomposition (Self-Ask) + active-learning-style uncertainty ranking |
| "Verification Agent" that checks the fix solved the root cause | Execution-grounded verification; process reward models (PRMs) score reasoning steps rather than just the final answer |
| "Problem graph" with dependencies and causal paths | Root-cause / causal graph analysis — standard in SRE and incident response, applied here to an LLM agent |
| "Dependency expansion" (X depends on Y) | Call-graph / dependency-graph analysis — for code, this is a solved problem with existing static-analysis tools; don't have the LLM guess it from text when you can compute it |

## The real lineage (2023–2026)

- **ReAct** (2023) — interleaves reasoning traces with tool actions, so the model reacts to real tool output rather than reasoning in a vacuum. Still the default loop shape in most agent frameworks because of its balance of adaptability and reliability.
- **Self-Refine** — the model generates, then critiques, then revises its own output, no external model needed. Cheapest version of self-improvement; shares blind spots between generator and critic since it's the same model both times.
- **Reflexion** (2023) — adds a persistent verbal self-critique: after a failed attempt, the agent writes down what went wrong and carries that into the next attempt. Reported large jumps in coding-benchmark pass rates versus no reflection.
- **CRITIC** — grounds the critique step in external tools (search, code execution) rather than pure self-talk, addressing Self-Refine's blind-spot problem.
- **Self-RAG** — the model decides *when* to retrieve versus answer from its own knowledge, and critiques its own retrieved evidence — relevant to "should I search before answering."
- **Tree of Thoughts (ToT)** — explores multiple reasoning branches instead of one linear chain, with large accuracy gains on search-like puzzle tasks, at a real cost: an order of magnitude or more tokens versus a single chain-of-thought pass.
- **ReWOO** — plans all tool calls up front rather than interleaving reasoning and action step-by-step, cutting token usage substantially versus ReAct-style loops on predictable workflows.
- **LATS (Language Agent Tree Search)** — combines tree search with reflection and external feedback for agent tasks; the "search + revise" idea generalized.
- **Process Reward Models (PRMs)** — instead of scoring only the final output, a model scores each intermediate reasoning/action step. This is the 2026 frontier replacement for "the agent reports a confidence number about itself": a *separate*, ideally trained, signal scores the trace, rather than the same model grading its own homework with a number it invented.

## Known failure modes (worth designing against, not just aspiring past)

- **Degeneration of thought** — repeated self-critique reinforces an early wrong direction instead of correcting it once the model has "committed" to a framing.
- **Infinite loops** — without a hard stopping rule, "let's investigate further" never terminates.
- **Memory pollution** — an incorrect "lesson" written to persistent memory during one task gets treated as ground truth in later tasks.
- **Multi-agent debate cost** — separating generator/critic/verifier into distinct passes measurably reduces shared blind spots, but reported compute cost is roughly 2–5x a single-agent pass. That cost needs to buy something on tasks that actually matter, or it's waste.
- **More reasoning ≠ better reasoning** — the original proposal itself flags this (its own point 18), and it's the correct instinct: an agent told to "explore every connection" will happily generate 30 searches and 200 pages of low-relevance context. The fix isn't a cleverer formula, it's a hard budget plus a bias toward execution-grounded checks over more self-narration.

## Practical takeaway

If you're implementing this, budget your complexity in this order of proven value: (1) real tool grounding — search, docs, test execution — matters more than any amount of self-reflection; (2) a single critic pass catches a meaningful share of planning errors cheaply; (3) a hard iteration/token budget is not optional; (4) a third independent verifier pass and persistent cross-session memory are real but expensive, and should be added only after you've measured that the cheaper version is insufficient for your workload. See [[02-Architecture]] for how this translates into tiers.
