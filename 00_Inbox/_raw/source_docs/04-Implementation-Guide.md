---
tags: [agents, implementation]
---

# Implementation Guide — Building the Tier 1 MVP

Back to [[00-Index]]. Written so a coding agent (Claude Code, Cursor, etc.) can execute this directly. Read [[02-Architecture]] first for the shape; this file is the "how."

## 1. Repo scaffold

```
/agent
  /state          # one JSON file per task, see schema below
  /prompts        # the system prompts in section 4, as plain text files
  loop.py         # the control loop in section 3
  guardrails.py   # destructive-command checks, section 5
  README.md
```

## 2. State schema (per task — one file, not a graph database)

Keep it a flat JSON file. Confidence is a label, not a number — see [[01-Verdict]] for why.

```json
{
  "goal": "Fix authentication loss after server restart",
  "facts": [
    {"statement": "JWT secret is generated at process startup", "status": "verified", "source": "server/api/login.php:14"}
  ],
  "hypotheses": [
    {"statement": "Restart invalidates existing tokens because the secret regenerates", "status": "inferred", "evidence": "2 restart logs show this pattern"}
  ],
  "unknowns": [
    {"question": "Is the signing secret persisted anywhere, or purely in-memory?", "why_it_matters": "If false, every existing token becomes invalid on restart — changes the whole plan"}
  ],
  "dependencies": ["auth module", "secret management", "session store"],
  "prior_art_checked": true,
  "prior_art_findings": ["Persist signing secret", "External key management", "Key rotation with key IDs"],
  "plan": ["step 1", "step 2"],
  "critique": ["what this plan assumes", "what wasn't tested"],
  "tests_added": ["restart-then-reuse-token test"],
  "iteration": 1,
  "budget": {"max_iterations": 3, "max_tool_calls": 10}
}
```

`status` is always one of `verified` (backed by a test result, a file you actually read, or a search result you actually retrieved), `inferred` (a reasonable guess from evidence), or `assumed` (unverified, flag it loudly). Never let the model write a bare number here.

## 3. The loop (honest version — three roles, hard stop)

```python
def solve(goal, budget):
    state = {"goal": goal, "facts": [], "hypotheses": [], "unknowns": [],
             "dependencies": [], "iteration": 0, "budget": budget}

    for i in range(budget["max_iterations"]):
        state["iteration"] = i

        # INVESTIGATE — only if there's an unresolved unknown that would change the plan
        if state["unknowns"]:
            state = investigate(state)   # one LLM call + at most a couple of tool calls

        # required, not optional: has this been solved before?
        if not state.get("prior_art_checked"):
            state = search_prior_art(state)   # Exa code search / Context7 / GitHub

        # PLAN
        plan = generate_plan(state)

        # CRITIQUE — one pass, not a loop
        critique = challenge_plan(plan, state)
        if critique["requires_more_investigation"] and i < budget["max_iterations"] - 1:
            state["unknowns"].extend(critique["new_unknowns"])
            continue   # go around once more, but the loop still terminates

        # EXECUTE + real verification, not narration
        result = execute(plan)
        test_result = run_real_tests(result)   # actual test suite / build / lint

        if test_result.passed:
            return {"status": "solved", "state": state, "result": result}
        else:
            state["facts"].append({"statement": f"Tests failed: {test_result.summary}",
                                    "status": "verified", "source": "test run"})
            # loop again with real failure evidence, not a hunch

    return {"status": "budget_exhausted", "state": state,
            "message": "Stopped after budget; here is what's known and unknown — human decision needed."}
```

The important discipline versus the original proposal: the loop has a hard iteration cap enforced in code (not "when confidence exceeds a threshold," which the model can't reliably self-assess), prior-art search is a required gate not a maybe, and the terminal signal on success is a real test run, not a model saying it looks solved.

## 4. The three system prompts

**Investigator** — given the current state, produce (a) a short plain-language list of what's known vs. unknown, (b) at most one or two targeted questions ranked by "would this change the plan," (c) tool calls to answer only the highest-ranked question. Explicitly instructed: do not assign numeric confidence; use verified/inferred/assumed.

**Planner** — given the state including any prior-art findings, produce an ordered list of concrete steps, and as its own last step, name the single biggest assumption the plan depends on.

**Critic** — given the plan and state (ideally run with a different system prompt than the Planner, or a different/cheaper model to reduce shared blind spots), answer: what does this depend on that hasn't been verified, is there a simpler existing solution already found in prior art that this plan ignores, what's the one test that should exist before this ships. Output a short list, not a numeric score.

## 5. Guardrails (adopt regardless of framework)

Pattern-match before executing, reject or require human approval:

```python
DESTRUCTIVE_PATTERNS = [
    r"rm\s+-rf",
    r"drop\s+table",
    r"force\s+push",
    r"deploy.*prod",
    r"delete.*database",
]

def check_guardrail(command: str) -> bool:
    """Return True if the command should be blocked pending human approval."""
    return any(re.search(p, command, re.IGNORECASE) for p in DESTRUCTIVE_PATTERNS)
```

This is deliberately simple — a denylist, not a clever classifier — because for destructive actions you want false positives (an unnecessary approval prompt) over false negatives (a missed dangerous command).

## 6. Wire up the tools

Add to your MCP client config (see [[03-Tools-and-APIs]] for the verified endpoints):

```json
{
  "mcpServers": {
    "exa": { "type": "streamable-http", "url": "https://mcp.exa.ai/mcp?tools=web_search_exa,get_code_context_exa" },
    "context7": { "type": "streamable-http", "url": "https://mcp.context7.com/mcp" }
  }
}
```
Start with just these two. Add Tavily or Firecrawl only if you find yourself needing broader crawling than Exa's search/code-search covers (see the comparison in [[03-Tools-and-APIs]]).

## 7. Prove it's actually better before trusting it

The step the original proposal skips entirely: measure this against a plain single-pass agent on a fixed set of real tasks from your own backlog (aim for at least 10–15 for the comparison to mean anything). Track: did it actually catch a real dependency the plain agent missed, did the critique pass catch a real bug before execution, and — honestly — how much extra latency/cost did each iteration add. If the extra machinery isn't winning on your own tasks, cut it back to Tier 1's minimum before adding Tier 2. "More reasoning steps" is a hypothesis to test, not a result to assume.
