---
tags: [agents, tools, mcp]
---

# Tool & API Landscape — verified August 2026

Back to [[00-Index]]. All of the following were checked against current documentation/registries as of this writing. Pricing, free-tier limits, and exact tool names change often on these products — re-check before committing to one in production. None of this is an endorsement; it's a snapshot.

## Web search / research

**Exa** — semantic (not just keyword) web search purpose-built for agents, plus code search and a research/"deep researcher" mode. Hosted MCP endpoint, works with Claude, Cursor, VS Code, and others.
```json
{
  "mcpServers": {
    "exa": {
      "type": "streamable-http",
      "url": "https://mcp.exa.ai/mcp"
    }
  }
}
```
By default only `web_search_exa` and `get_code_context_exa` (code search) are enabled; other tools (crawling, company research, deep researcher) are opt-in via a `tools=` query parameter. Free tier exists; paid plan needed for volume. No image search as of this check.

**Tavily** — search API designed from the ground up for agents rather than humans; narrower tool surface than Firecrawl by design (`tavily-search`, `tavily-extract`). Formal integrations with major cloud/agent platforms (Bedrock AgentCore, Azure, watsonx, Snowflake, Databricks) and LangChain/LlamaIndex.
```
Hosted endpoint: https://mcp.tavily.com/mcp/
```

**Firecrawl** — scraping-and-crawling-first rather than search-first: search, scrape, deep crawl, and "autonomous research" in one session, so an agent can follow a link from search result → clean markdown → clicked-through page without switching tools. Broadest raw tool surface of the group (~20 tools in some integrations).
```
Hosted endpoint: https://mcp.firecrawl.dev/v2/mcp
```
Keyless/free tier covers search, scrape, and basic parsing; crawl/map/agent features need an API key. Free tier is IP-shared, treat it as a trial rather than a dependable production tier.

**Choosing between them**: Exa for semantic/code research, Tavily for fast search-plus-extract in a RAG pipeline, Firecrawl when the job is really "turn this site into structured data." Several comparison sources from mid-2026 independently converge on this split — it isn't just each vendor's own marketing.

## Documentation grounding

**Context7** (Upstash) — the most directly useful tool for "the agent used a 3-versions-old API by mistake." Exposes two tools: `resolve-library-id` (name → canonical ID) and a docs-fetch tool that returns version-specific documentation and examples pulled from the library's actual source/docs site, with a configurable token budget.
```
Hosted endpoint: https://mcp.context7.com/mcp
NPM (local/stdio): @upstash/context7-mcp
```
MIT-licensed core, free tier without an API key (lower rate limits), free API key available for higher limits. An enterprise/on-prem version exists for teams that can't send proprietary docs to a third party.

## MCP ecosystem, generally

MCP is confirmed as the standard tool-access protocol across essentially every major coding agent (Claude Code, Cursor, VS Code, Windsurf, Codex, and others) as of mid-2026. Be skeptical of precise ecosystem-size numbers you see in vendor blogs (e.g. "10,000+ servers") — treat them as directional, not audited. The practically useful fact is narrower: Exa, Tavily, Context7, and Firecrawl each have official, actively maintained MCP servers you can point a client at today with the URLs above.

## Orchestration (do you need a framework at all?)

The original proposal recommends LangGraph by default. Current comparisons (mid-2026) largely agree on the trade-off rather than the recommendation:

- **LangGraph** — real strength when the *graph topology itself* is the hard part: complex branching, cycles, human-approval checkpoints, auditable execution traces. Cost: a real learning curve, a state-schema/checkpointer system to maintain, and the LangChain dependency tree that comes with it.
- **OpenAI Agents SDK** — opinionated, tracing and guardrails (including tool-call rejection) built in; a solid default if you're already OpenAI-model-centric.
- **CrewAI / AutoGen (AG2)** — role-based multi-agent framing; faster initial setup for "several agents with distinct personas talking to each other," but younger production ecosystem than LangGraph.
- **Temporal** — not an agent framework at all, but a durable workflow engine; worth knowing about if your real requirement is "this needs to survive a crash and resume," which is a different problem than "the agent needs to reason well."
- **Plain code** — for a Tier 1 MVP (see [[02-Architecture]]), a Python loop with state serialized to a JSON file on disk gets you 90% of what LangGraph offers at this scale, with none of the framework lock-in. Adopt a framework once you have a concrete requirement (crash recovery, visual debugging of branches, team-wide standardization) that a plain loop doesn't satisfy — not by default.

## Guardrails

The OpenAI Agents SDK and similar frameworks expose explicit input/output/tool guardrails — e.g. rejecting a tool call that matches a destructive pattern (`rm -rf`, a production-deploy command) before it executes, or requiring a human-approval step for specific tool calls. This is worth adopting regardless of which orchestration layer you pick — see the guardrail pattern in [[04-Implementation-Guide]].
