#!/usr/bin/env python3
"""
Vaultie Prime Runner — Executable Python Skill for Prime Agent Harness & Student Simulation
Provides a CLI interface to launch background lab runs, student simulations, and refinement loops.
"""

import sys
import os
import json
import subprocess
from pathlib import Path

def run_student_simulation(lesson_id):
    """Launches Prime Agent (or fallback student runner) in blackbox mode on a lab."""
    vault_dir = Path.cwd()
    lab_dir = vault_dir / "labs" / "web-engineering" / lesson_id
    lesson_spec = vault_dir / "90_Meta" / "lessons" / lesson_id / "spec.yaml"

    if not lab_dir.exists():
        return {
            "status": "ERROR",
            "message": f"Lab directory {lab_dir} does not exist yet. Please create lab scaffold first."
        }

    plan = {
        "simulation_id": f"sim-{lesson_id}-{os.urandom(3).hex()}",
        "lesson_id": lesson_id,
        "lab_dir": str(lab_dir),
        "spec_path": str(lesson_spec) if lesson_spec.exists() else None,
        "mode": "blackbox_student",
        "harness": "prime-agent",
        "instructions": [
            f"1. Read lesson spec at {lesson_spec}",
            f"2. Navigate to {lab_dir}",
            "3. Implement code to pass all lab unit/integration tests",
            "4. If tests fail, run /refine to suggest lesson clarifications"
        ]
    }
    return plan

def main():
    if len(sys.argv) < 2:
        print("Vaultie Prime Runner v1.0.0")
        print("Usage: python3 .agent/scripts/prime_runner.py <lesson-id>")
        sys.exit(0)

    lesson_id = sys.argv[1]
    result = run_student_simulation(lesson_id)
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
