#!/usr/bin/env python3
"""Small optional Antigravity Stop-hook gate.

This script intentionally checks only objective repository hygiene that can be
reliably automated without making stack-specific assumptions. Semantic quality
and test execution remain enforced by the Rules/Skills layer.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def run(cwd: Path, *args: str) -> tuple[int, str]:
    proc = subprocess.run(
        list(args),
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return proc.returncode, proc.stdout.strip()


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        print(json.dumps({"decision": "continue", "reason": "Quality gate could not parse hook input; inspect manually."}))
        return 0

    if not payload.get("fullyIdle", True):
        print(json.dumps({"decision": "allow"}))
        return 0

    workspace_paths = payload.get("workspacePaths") or []
    if not workspace_paths:
        print(json.dumps({"decision": "allow"}))
        return 0

    root = Path(workspace_paths[0])
    repo_code, repo_output = run(root, "git", "rev-parse", "--is-inside-work-tree")
    if repo_code != 0 or repo_output.strip().lower() != "true":
        print(json.dumps({"decision": "allow"}))
        return 0

    code, output = run(root, "git", "diff", "--check")
    if code != 0:
        reason = (
            "Repository quality gate failed: `git diff --check` found whitespace/conflict-marker problems. "
            "Fix them before stopping.\n" + output[-2000:]
        )
        print(json.dumps({"decision": "continue", "reason": reason}))
        return 0

    print(json.dumps({"decision": "allow"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
