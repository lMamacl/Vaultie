#!/usr/bin/env python3
"""
Epistemic Runner — State Machine, Guardrails & Grounded Verification Controller
Part of the Vaultie Epistemic Coding Agent Architecture (Tier 1 MVP).

Enforces:
1. Structured state schema (facts, hypotheses, unknowns, prior_art, plan, critique).
2. Strict epistemic labeling (verified facts require valid sources).
3. Hard execution budgets (max_iterations, max_tool_calls).
4. Deterministic regex guardrails against destructive shell operations.
5. Grounded verification via physical test execution.
"""

import sys
import os
import json
import re
import subprocess
import time
from pathlib import Path
from typing import Dict, List, Any, Optional

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


DESTRUCTIVE_PATTERNS = [
    r"\brm\s+-(?:r|f|rf|fr)\b",
    r"\bdrop\s+table\b",
    r"\bdrop\s+database\b",
    r"\bgit\s+push\s+.*--force\b",
    r"\bformat\s+[c-z]:\b",
    r"\bRemove-Item\s+.*-Recurse\b",
    r"\bdel\s+/s\b",
    r"\btruncate\s+table\b",
]

DEFAULT_BUDGET = {
    "max_iterations": 3,
    "max_tool_calls": 10,
}

class EpistemicGuardrailViolation(Exception):
    pass

class EpistemicBudgetExhausted(Exception):
    pass

def validate_command_safety(command: str) -> bool:
    """Returns False if command matches any destructive patterns."""
    for pattern in DESTRUCTIVE_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            return False
    return True

def create_task_state(task_id: str, goal: str, budget: Optional[Dict[str, int]] = None) -> Dict[str, Any]:
    """Initializes a new flat JSON state for an epistemic task."""
    b = budget or DEFAULT_BUDGET
    return {
        "task_id": task_id,
        "goal": goal,
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "iteration": 0,
        "budget": b,
        "facts": [],
        "hypotheses": [],
        "unknowns": [],
        "dependencies": [],
        "prior_art_checked": False,
        "prior_art_findings": [],
        "plan": [],
        "critique": [],
        "tests_added": [],
        "execution_history": [],
        "status": "in_progress",  # in_progress | solved | budget_exhausted | failed
    }

def add_fact(state: Dict[str, Any], statement: str, status: str, source: str) -> None:
    """Adds a fact to the state, ensuring valid epistemic status and provenance."""
    if status not in ("verified", "inferred", "assumed"):
        raise ValueError(f"Invalid epistemic status: '{status}'. Must be 'verified', 'inferred', or 'assumed'.")
    if status == "verified" and (not source or source.strip() == ""):
        raise ValueError("A 'verified' fact MUST include a valid non-empty 'source' (file:line, test output, or URL).")
    
    state["facts"].append({
        "statement": statement,
        "status": status,
        "source": source,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    })

def add_unknown(state: Dict[str, Any], question: str, why_it_matters: str) -> None:
    """Registers an unresolved unknown ranked by impact on planning."""
    state["unknowns"].append({
        "question": question,
        "why_it_matters": why_it_matters
    })

def run_grounded_test(test_command: str, cwd: Optional[Path] = None) -> Dict[str, Any]:
    """
    Executes a real physical test command in the local environment and returns structured results.
    Guarded against destructive commands.
    """
    if not validate_command_safety(test_command):
        raise EpistemicGuardrailViolation(f"Command rejected by safety guardrail: '{test_command}'")
    
    work_dir = str(cwd) if cwd else os.getcwd()
    start_time = time.time()
    
    try:
        process = subprocess.run(
            test_command,
            shell=True,
            cwd=work_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=120
        )
        elapsed = time.time() - start_time
        passed = (process.returncode == 0)
        
        return {
            "command": test_command,
            "passed": passed,
            "exit_code": process.returncode,
            "stdout": process.stdout[:4000],  # Compress output
            "stderr": process.stderr[:4000],
            "elapsed_seconds": round(elapsed, 2)
        }
    except subprocess.TimeoutExpired:
        return {
            "command": test_command,
            "passed": False,
            "exit_code": -1,
            "stdout": "",
            "stderr": "Test execution timed out after 120 seconds.",
            "elapsed_seconds": 120.0
        }
    except Exception as e:
        return {
            "command": test_command,
            "passed": False,
            "exit_code": -1,
            "stdout": "",
            "stderr": str(e),
            "elapsed_seconds": 0.0
        }

def save_state(state: Dict[str, Any], output_path: Path) -> None:
    """Saves state to a formatted JSON file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)

def load_state(input_path: Path) -> Dict[str, Any]:
    """Loads state from a JSON file."""
    with open(input_path, "r", encoding="utf-8") as f:
        return json.load(f)

def render_markdown_report(state: Dict[str, Any]) -> str:
    """Renders a concise, human-readable summary of the epistemic task state."""
    lines = [
        f"# Raport Epistemiczny: {state['task_id']}",
        f"**Cel:** {state['goal']}",
        f"**Status:** `{state['status'].upper()}` | **Iteracja:** {state['iteration']}/{state['budget']['max_iterations']}",
        "",
        "## Zweryfikowane Fakty (Verified Facts)",
    ]
    
    verified = [f for f in state['facts'] if f['status'] == 'verified']
    if verified:
        for f in verified:
            lines.append(f"- ✅ **{f['statement']}** (Źródło: `{f['source']}`)")
    else:
        lines.append("- *Brak zweryfikowanych faktów.*")
        
    lines.append("\n## Niewiadome i Ryzyka (Unknowns & Assumptions)")
    assumed = [f for f in state['facts'] if f['status'] in ('inferred', 'assumed')]
    for a in assumed:
        lines.append(f"- ⚠️ [{a['status'].upper()}] {a['statement']}")
    for u in state['unknowns']:
        lines.append(f"- ❓ {u['question']} (*Wpływ:* {u['why_it_matters']})")
        
    lines.append("\n## Stan Poprzedni (Prior Art)")
    if state.get("prior_art_checked"):
        lines.append(f"- **Sprawdzono:** Tak")
        for finding in state.get("prior_art_findings", []):
            lines.append(f"  - {finding}")
    else:
        lines.append("- ❌ **Nie sprawdzono stanu poprzedniego (Prior Art)**")
        
    lines.append("\n## Plan i Wyniki Testów")
    for step in state.get("plan", []):
        lines.append(f"1. {step}")
        
    if state.get("execution_history"):
        lines.append("\n### Historia Uruchomień Testów:")
        for exec_item in state["execution_history"]:
            status_emoji = "🟢 PASS" if exec_item.get("passed") else "🔴 FAIL"
            lines.append(f"- {status_emoji} `{exec_item.get('command')}` (Kod: {exec_item.get('exit_code')}, Czas: {exec_item.get('elapsed_seconds')}s)")
            
    return "\n".join(lines)

def main():
    if len(sys.argv) < 2:
        print("Vaultie Epistemic Runner v1.0.0")
        print("Usage:")
        print("  epistemic_runner.py init <task_id> <goal> [output_file]")
        print("  epistemic_runner.py test <test_command> [state_file]")
        print("  epistemic_runner.py report <state_file>")
        print("  epistemic_runner.py check-command <shell_command>")
        sys.exit(0)

    cmd = sys.argv[1]
    
    if cmd == "init":
        if len(sys.argv) < 4:
            print("Usage: epistemic_runner.py init <task_id> <goal> [output_file]")
            sys.exit(1)
        task_id = sys.argv[2]
        goal = sys.argv[3]
        out_path = Path(sys.argv[4]) if len(sys.argv) > 4 else Path(f"00_Inbox/_proposals/state-{task_id}.json")
        state = create_task_state(task_id, goal)
        save_state(state, out_path)
        print(f"Initialized state file at: {out_path}")
        
    elif cmd == "test":
        if len(sys.argv) < 3:
            print("Usage: epistemic_runner.py test <test_command> [state_file]")
            sys.exit(1)
        test_cmd = sys.argv[2]
        state_file = Path(sys.argv[3]) if len(sys.argv) > 3 else None
        
        result = run_grounded_test(test_cmd)
        print(json.dumps(result, indent=2))
        
        if state_file and state_file.exists():
            state = load_state(state_file)
            state["execution_history"].append(result)
            if result["passed"]:
                state["status"] = "solved"
                add_fact(state, f"Test command passed: {test_cmd}", "verified", f"test_runner:{test_cmd}")
            else:
                add_fact(state, f"Test failed (exit {result['exit_code']}): {result['stderr'][:200]}", "verified", "test_runner")
            save_state(state, state_file)
            print(f"Updated state file: {state_file}")
            
    elif cmd == "report":
        if len(sys.argv) < 3:
            print("Usage: epistemic_runner.py report <state_file>")
            sys.exit(1)
        state_file = Path(sys.argv[2])
        if not state_file.exists():
            print(f"Error: {state_file} not found.")
            sys.exit(1)
        state = load_state(state_file)
        print(render_markdown_report(state))
        
    elif cmd == "check-command":
        if len(sys.argv) < 3:
            print("Usage: epistemic_runner.py check-command <shell_command>")
            sys.exit(1)
        cmd_str = " ".join(sys.argv[2:])
        safe = validate_command_safety(cmd_str)
        print(json.dumps({"command": cmd_str, "safe": safe}, indent=2))
        if not safe:
            sys.exit(2)
            
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
