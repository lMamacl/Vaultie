---
name: vaultie-maintenance
description: Runs a read-only integrity and freshness audit of Vaultie and returns a prioritized maintenance report. Use for daily/weekly health checks.
---

# Vaultie Maintenance

1. Read Vault operating instructions and inspect actual installed scripts before invoking them.
2. Capture Git status; do not alter existing user changes.
3. Prefer safe, read-only checks for frontmatter, broken wikilinks, index integrity, stale library notes, unverified snippets and missing sources.
4. Classify findings: `P0` data-loss/security; `P1` material integrity issue; `P2` broken navigation/stale claim; `P3` cosmetic or low-risk.
5. For each finding report exact path, evidence, risk, suggested repair, whether mechanical/semantic, and whether user approval is needed.
6. Save only a dated report to `00_Inbox/_agent_bus/reports/`.

This skill is audit-only. Do not auto-correct, archive, delete, overwrite, recompile destructive outputs, commit, push, or change `.agent/` / `.agents/`. If a check cannot run, report that fact.