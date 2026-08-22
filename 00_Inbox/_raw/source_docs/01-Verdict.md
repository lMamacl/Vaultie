---
tags: [agents, critique]
---

# Verdict — What Actually Works

Back to [[00-Index]].

Claim-by-claim assessment of the original proposal.

## Claims that hold up

| Claim | Verdict | Why |
|---|---|---|
| Agents need an explicit **investigation budget / stopping rule** | ✅ Real, necessary | Reflection research documents "degeneration of thought" — agents that keep critiquing and revising without a stop condition loop, pollute their own memory, and sometimes get *worse* over iterations. A hard cap (max iterations, max searches, token budget) is standard practice, not a nice-to-have. See [[05-Research-Foundations]]. |
| **Dependency / causal expansion** ("fixing X won't help if Y is broken") | ✅ Genuinely good idea | This is root-cause analysis, well established in SRE/incident-response practice, applied to an LLM agent. The mistake is *how* the original proposal fills the graph — see below. |
| **Separate a critic pass from the generator pass** | ✅ Real, but scope it down | This is the Self-Refine → Reflexion → CRITIC lineage. Dual-role reflection (generator + critic as different prompts, ideally different model or temperature) measurably reduces shared blind spots. But the original proposal turns this into 3+ separate "engines" (Planner, Challenger, Verifier) — see the cost note below. |
| **MCP as the plumbing layer** | ✅ Accurate, current | Verified Aug 2026: MCP is the standard way coding agents reach external tools (filesystem, git, web search, docs). This part of the proposal is not hype. |
| **Exa / Tavily / Context7 / Firecrawl exist and work roughly as described** | ✅ Verified, still current | Details, live endpoints, and setup in [[03-Tools-and-APIs]]. |

## Claims that are dressed-up prompting, not engineering

**Numeric confidence scores (0.97, 0.73, 0.62...).** These look like probabilities but there is no calibration process behind them — the model is not computing a real posterior, it's pattern-matching to "what a confident-sounding number looks like here." LLMs are well documented to be poorly calibrated at self-reported numeric confidence, especially outside narrow, trained domains. Treat these as decoration. If you want an actual reliability signal, use something checkable: did a test pass, did N independent sources agree, is this fact sourced from the repo itself vs. an LLM guess. Qualitative buckets (`verified` / `inferred` / `assumed`) are more honest than fake precision.

**The information-gain formula** (`probability_it_changes_plan × consequence × uncertainty / search_cost`). The instinct — rank questions by how much they'd change the plan, not just by "interestingness" — is good and maps to real active-learning ideas. But writing it as a formula with numbers plugged in implies a precision that doesn't exist; the LLM is still just guessing the three numerators. Use it as an ordinal ranking heuristic ("which of these 3 unknowns would most change the plan if answered?") not as literal arithmetic.

**Six separate "engines."** Investigator, Planner, Challenger, Executor, Verifier, plus a Problem Parser — each additional named role is, in practice, the same underlying model called again with a different system prompt (unless you deliberately use different models per role, which is a real and defensible choice — see multi-agent debate below). Every extra pass adds latency, cost, and a new place for context to get lost in translation between roles. Research on multi-agent debate/reflection reports **2–5x the compute** of single-agent generation for the multi-critic version, and it does not uniformly outperform a cheaper single generator + single critic loop. Start with **two roles** (generator, critic) and only add a third (independent verifier) where the cost of a missed error is high — e.g. before executing destructive commands or shipping to production, not for every micro-step.

**Persisting the "problem model" for reuse six months later.** This is the most appealing part of the pitch and the hardest to actually build. Long-term memory / knowledge-graph reuse across sessions runs into real unsolved problems: staleness (the codebase changed, the "fact" didn't), contradiction resolution (two sessions concluded different things), and retrieval precision at scale (the graph gets large and noisy). Don't build this for a first prototype. Log research findings to files for a human to skim; automate reuse only after you've validated the MVP loop on its own.

## The most important correction, and the one the original answer never makes

Across the actual research literature (Reflexion, CRITIC, Self-RAG, process reward models — see [[05-Research-Foundations]]), the single most consistent finding is that **execution-grounded feedback beats verbal self-reflection alone.** An agent that runs the actual test suite, reads the actual compiler error, or gets an actual search result back is getting real signal. An agent that just asks itself "what could go wrong with this plan?" and answers from its own priors is, at best, surfacing things it already implicitly knew, and at worst, hallucinating risks or missing real ones while sounding thorough. The original proposal's Challenger and Verifier stages are useful, but they are worth far less than wiring up real test execution, real static analysis, and real search — and should be judged against that baseline before you trust them.

## A cheaper alternative worth considering first

Before building any of this, note that existing coding agents (Claude Code, Cursor, and similar) already implement pieces of this pattern natively: a planning/todo-list step, the ability to invoke sub-agents for isolated investigation, hooks for guardrails on destructive commands, and now direct MCP tool wiring. You may get a large fraction of the value described here by:
- adding Exa/Context7/Tavily as MCP tools to an agent you already use,
- writing a custom system prompt or skill that tells the agent to explicitly list unknowns and dependencies before planning, and search for prior art before proposing a fix,
- adding a second pass where the same agent (or a sub-agent) critiques its own plan before executing,

rather than building an entirely new orchestration layer from scratch. Build the from-scratch version ([[02-Architecture]]) only if that lighter version turns out to be insufficient for your actual tasks.
