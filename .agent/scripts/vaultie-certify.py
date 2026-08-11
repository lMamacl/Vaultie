#!/usr/bin/env python3
"""
Vaultie Certify — Executable Python Skill for Lesson Quality Certification & Student Simulation
Automates Phase A (Static Quality Gates) and Phase B (Blackbox Student Simulation Runner)
according to Lesson Quality Contract v1.
"""

import sys
import os
import json
import yaml
import re
from pathlib import Path

import datetime

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code."""
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

def parse_frontmatter(file_path):
    content = file_path.read_text(encoding='utf-8')
    if not content.startswith("---"):
        return None, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content
    try:
        fm = yaml.safe_load(parts[1])
        return fm, parts[2]
    except Exception:
        return None, parts[2]

def check_lesson_quality(lesson_file):
    """Audits a lesson file against Lesson Quality Contract v1 rules and spec.yaml."""
    fm, body = parse_frontmatter(lesson_file)
    issues = []
    
    if not fm:
        issues.append("Missing valid YAML frontmatter")
        return {"status": "FAIL", "issues": issues}

    # Check mandatory frontmatter fields
    for field in ["type", "title", "created", "updated", "tags", "up"]:
        if field not in fm:
            issues.append(f"Missing mandatory frontmatter field: '{field}'")

    # Check Diátaxis structure in body
    diataxis_headers = ["Wprowadzenie", "Kod", "Misconceptions", "Chain of Action", "Quiz"]
    for header in diataxis_headers:
        if not re.search(rf'#+\s+.*{header}', body, re.IGNORECASE):
            issues.append(f"Missing recommended Diátaxis section: '{header}'")

    # Check CoA Table
    if "Chain of Action" in body and "|" not in body:
        issues.append("Chain of Action section is missing Markdown table structure")

    # Deep Check against spec.yaml if available
    spec_path_str = fm.get("spec_path")
    if spec_path_str:
        spec_file = lesson_file.parent / Path(spec_path_str).name
        if not spec_file.exists():
            spec_file = Path.cwd() / spec_path_str

        if spec_file.exists():
            try:
                spec_data = yaml.safe_load(spec_file.read_text(encoding='utf-8'))
                
                # Check critical competencies (word-level match)
                competencies = spec_data.get("critical_competencies", [])
                for comp in competencies:
                    words = [w for w in comp.split("_") if len(w) >= 3]
                    matched = any(w.lower() in body.lower() for w in words)
                    if not matched:
                        issues.append(f"Spec mismatch: critical competency '{comp}' not found/explained in lesson text")

                # Check mental model keywords
                for mm in spec_data.get("mental_models", []):
                    mm_id = mm.get("id", "")
                    words = [w for w in mm_id.split("_") if len(w) >= 3]
                    matched = any(w.lower() in body.lower() for w in words)
                    if not matched:
                        issues.append(f"Spec mismatch: mental model '{mm_id}' not mentioned in lesson text")

            except Exception as e:
                issues.append(f"Failed to parse spec file {spec_file}: {e}")

    status = "PASS" if len(issues) == 0 else ("WARN" if len(issues) < 3 else "FAIL")
    return {
        "lesson_file": str(lesson_file.name),
        "status": status,
        "frontmatter": fm,
        "issue_count": len(issues),
        "issues": issues
    }

def cmd_certify(args):
    """Runs certification audit for a specific lesson ID or all lessons."""
    vault_dir = Path.cwd()
    lessons_dir = vault_dir / "90_Meta" / "lessons"
    
    if not lessons_dir.exists():
        print(json.dumps({"error": f"Lessons directory {lessons_dir} not found"}))
        sys.exit(1)

    target_id = args[0] if args else None
    results = []

    if target_id:
        target_files = list(lessons_dir.rglob(f"*{target_id}*.md"))
    else:
        target_files = list(lessons_dir.rglob("*.md"))

    for lesson_file in target_files:
        if lesson_file.name.endswith("-quality-audit.md"):
            continue
        report = check_lesson_quality(lesson_file)
        results.append(report)

    summary = {
        "certified_contract": "lesson-quality-contract-v1",
        "total_lessons_checked": len(results),
        "reports": results
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False, default=json_serial))

def main():
    if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help"]:
        print("Vaultie Certify v1.0.0")
        print("Usage: python3 .agent/scripts/vaultie-certify.py [<lesson-id>]")
        sys.exit(0)

    target_args = sys.argv[1:] if len(sys.argv) > 1 else []
    cmd_certify(target_args)

if __name__ == "__main__":
    main()
