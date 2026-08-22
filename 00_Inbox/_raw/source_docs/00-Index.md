---
tags: [moc, agents, research]
---

# Epistemic Coding Agent — Research Vault

Source question: can we build a coding agent that doesn't just fetch information on command, but actively questions its own plan, expands into connected subsystems ("fixing X won't help if Y is broken"), searches for prior art, and only then executes — with real guardrails and test scenarios?

A GPT-authored answer to that question proposed a fairly elaborate 6-engine architecture (Investigator → Planner → Challenger → Executor → Verifier, plus a "problem graph" and numeric confidence scores). It's a genuinely good starting intuition, but parts of it are more science-fiction than engineering. This vault is a critical rebuild: what's real, what's dressed-up prompting, and what an agent could actually implement this week vs. what's a research project.

## Read in this order

1. [[01-Verdict]] — point-by-point debunk of the original proposal. Start here.
2. [[05-Research-Foundations]] — the actual academic lineage this idea belongs to (Reflexion, CRITIC, Tree of Thoughts, etc.), so you're not reinventing 2023 research under new names.
3. [[02-Architecture]] — a scoped-down architecture in three tiers: MVP, V2, research-grade.
4. [[03-Tools-and-APIs]] — verified (Aug 2026) state of Exa, Tavily, Context7, Firecrawl, MCP, and orchestration frameworks, with working config snippets.
5. [[04-Implementation-Guide]] — concrete steps, state schema, prompts, and guardrails for an agent to actually build the MVP.

## One-paragraph verdict

The core instinct — an agent should question its plan and expand into causally-connected problems before executing — is correct and has real research behind it. The proposed *implementation* over-trusts LLM self-reported numbers (confidence scores, information-gain formulas), over-multiplies distinct "engines" that are really just the same model with different system prompts (expensive, not obviously better), and skips the one thing the research consistently says matters most: grounding verification in things that can actually be checked (test execution, static analysis, real search results) rather than in more LLM narration about itself. Build the small, cheap version first and measure whether the extra machinery actually beats a plain agent on your own tasks — don't assume it does.
