#!/usr/bin/env python3
"""
Epistemic A/B Benchmark Evaluation Harness
Scans all task-* directories in labs/benchmark-suite/, executes test_task.py, and outputs a summary report.
"""

import sys
import os
import json
import subprocess
import time
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def run_task_test(task_dir: Path) -> dict:
    test_file = task_dir / "test_task.py"
    if not test_file.exists():
        return {
            "task": task_dir.name,
            "status": "SKIPPED",
            "passed": False,
            "message": "test_task.py not found"
        }
        
    start_time = time.time()
    try:
        proc = subprocess.run(
            [sys.executable, str(test_file.name)],
            cwd=str(task_dir),
            capture_output=True,
            text=True,
            timeout=30
        )
        elapsed = time.time() - start_time
        passed = (proc.returncode == 0)
        return {
            "task": task_dir.name,
            "status": "PASS" if passed else "FAIL",
            "passed": passed,
            "exit_code": proc.returncode,
            "stdout": proc.stdout.strip()[:500],
            "stderr": proc.stderr.strip()[:500],
            "elapsed_seconds": round(elapsed, 2)
        }
    except subprocess.TimeoutExpired:
        return {
            "task": task_dir.name,
            "status": "TIMEOUT",
            "passed": False,
            "exit_code": -1,
            "stdout": "",
            "stderr": "Execution timed out",
            "elapsed_seconds": 30.0
        }

def main():
    bench_dir = Path(__file__).parent
    task_dirs = sorted([d for d in bench_dir.iterdir() if d.is_dir() and d.name.startswith("task-")])
    
    print("=" * 60)
    print(f"EPISTEMIC BENCHMARK RUNNER — {len(task_dirs)} TASKS DISCOVERED")
    print("=" * 60)
    
    results = []
    passed_count = 0
    
    for task_dir in task_dirs:
        res = run_task_test(task_dir)
        results.append(res)
        if res["passed"]:
            passed_count += 1
            print(f"✅ {res['task']}: PASS ({res['elapsed_seconds']}s)")
        else:
            print(f"❌ {res['task']}: {res['status']} (Code: {res.get('exit_code')})")
            if res.get('stderr'):
                print(f"   Error: {res['stderr'].splitlines()[-1] if res['stderr'].splitlines() else ''}")
                
    total = len(task_dirs)
    pass_rate = round((passed_count / total * 100) if total > 0 else 0, 1)
    
    print("-" * 60)
    print(f"SUMMARY: {passed_count}/{total} PASSED ({pass_rate}% Pass Rate)")
    print("=" * 60)
    
    report_file = bench_dir / "benchmark_report.json"
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump({
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "total_tasks": total,
            "passed_tasks": passed_count,
            "pass_rate_percent": pass_rate,
            "results": results
        }, f, indent=2)
    print(f"Report saved to: {report_file}")

if __name__ == "__main__":
    main()
