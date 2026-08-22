#!/usr/bin/env python3
"""
Vaultie Certify — Phase A static quality gates for masterclass lessons.

Implements structural, pedagogical, lab, and artifact checks from
90_Meta/lesson-quality-contract-v1.md (Phase A subset).

Phase B (Student-sim / Judge / teach-back) is NOT implemented — see
90_Meta/lessons/certifier-audit-2026-08-11.md

Usage:
  python .agent/scripts/vaultie-certify.py [lesson-id] [--strict]
"""

from __future__ import annotations

import datetime
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print(json.dumps({"error": "PyYAML required: pip install pyyaml"}))
    sys.exit(1)


VAULT_ROOT = Path.cwd()
LESSONS_DIR = VAULT_ROOT / "90_Meta" / "lessons"
ROADMAP = VAULT_ROOT / "90_Meta" / "web-engineering-roadmap.md"
CANVASES_DIR = VAULT_ROOT / "90_Meta" / "canvases"

DIATAXIS_HEADERS = [
    "Wprowadzenie",
    ("Kod", ["Lab", "Laboratorium", "worked example"]),
    "Misconceptions",
    "Chain of Action",
    "Quiz",
]

SPEC_REQUIRED_KEYS = [
    "id",
    "title",
    "learning_objectives",
    "critical_competencies",
    "mental_models",
    "misconceptions",
    "assessment_ladder",
    "sources",
]

QUIZ_SPOILER_PATTERNS = [
    r"\*Odpowiedź\s*:",
    r"-\s*\*Odpowiedź\s*:",
    r"^\s*\*\*Odpowiedź\s*:",
    r"Rubryka zaliczenia.*\n.*\*\*Odpowiedź",
]

LAB_ARTIFACT_CHECKS = {
    "pnpm-workspace": ["pnpm-workspace.yaml"],
    "lockfile": ["pnpm-lock.yaml", "package-lock.json", "yarn.lock"],
    "husky": [".husky/pre-commit", ".husky/commit-msg"],
    "ci": [".github/workflows/ci.yml", ".github/workflows/ci.yaml"],
    "gitignore": [".gitignore"],
    "editorconfig": [".editorconfig"],
    "apps/web": ["apps/web/package.json"],
    "packages/shared": ["packages/shared/package.json"],
}


def json_serial(obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")


def parse_frontmatter(file_path: Path):
    content = file_path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return None, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content
    try:
        fm = yaml.safe_load(parts[1]) or {}
        return fm, parts[2]
    except Exception:
        return None, parts[2]


def find_h2_titles(body: str) -> list[str]:
    return re.findall(r"^##\s+(.+)$", body, re.MULTILINE)


def extract_wikilinks(body: str) -> list[str]:
    return re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", body)


def resolve_canvas_path(link: str) -> Path | None:
    name = link.strip()
    if name.endswith(".canvas"):
        candidate = CANVASES_DIR / name
        if candidate.exists():
            return candidate
    candidate = CANVASES_DIR / f"{name}.canvas"
    if candidate.exists():
        return candidate
    return None


def check_lab_artifacts(lab_path: Path, spec_data: dict | None) -> list[str]:
    issues = []
    if not lab_path.exists():
        return [f"Lab directory missing: {lab_path.relative_to(VAULT_ROOT)}"]

    readme = lab_path / "README.md"
    if not readme.exists():
        issues.append(f"Lab missing README.md: {lab_path.relative_to(VAULT_ROOT)}")

    # Generic monorepo lab checks when spec mentions pnpm/workspace
    lab_spec = (spec_data or {}).get("lab", {})
    dod = lab_spec.get("dod") or []
    dod_text = " ".join(str(x) for x in dod).lower()

    if "pnpm" in dod_text or "workspace" in dod_text or "monorepo" in dod_text:
        for label, candidates in LAB_ARTIFACT_CHECKS.items():
            if not any((lab_path / c).exists() for c in candidates):
                issues.append(
                    f"Lab artifact missing ({label}): expected one of "
                    f"{candidates} in {lab_path.relative_to(VAULT_ROOT)}"
                )

    return issues


def check_spec_completeness(spec_data: dict | None, spec_file: Path) -> list[str]:
    issues = []
    if spec_data is None:
        return [f"Cannot parse spec: {spec_file}"]

    for key in SPEC_REQUIRED_KEYS:
        if key not in spec_data or spec_data[key] in (None, [], {}):
            issues.append(f"Spec incomplete: missing or empty '{key}'")

    sources = spec_data.get("sources", {})
    normative = sources.get("normative") if isinstance(sources, dict) else None
    if not normative:
        issues.append("Spec incomplete: sources.normative empty")

    return issues


def check_roadmap_link(lesson_id: str, lesson_stem: str) -> list[str]:
    issues = []
    if not ROADMAP.exists():
        return ["Roadmap file missing: 90_Meta/web-engineering-roadmap.md"]

    text = ROADMAP.read_text(encoding="utf-8")
    section = re.search(rf"##\s+{re.escape(lesson_id)}\s+—", text)
    if not section:
        issues.append(f"Roadmap missing section header for lesson {lesson_id}")
        return issues

    # Look at ~40 lines after section header for wikilink to lesson
    start = section.start()
    chunk = text[start : start + 2500]
    if lesson_stem not in chunk and f"[[{lesson_id}/" not in chunk:
        issues.append(
            f"Roadmap section {lesson_id} missing wikilink to full lesson "
            f"(expected [[{lesson_id}/…]] or stem '{lesson_stem}')"
        )
    if ".canvas" not in chunk and "Kanwa" in chunk:
        issues.append(f"Roadmap section {lesson_id} mentions Kanwa but no canvas wikilink")

    return issues


def check_quality_report(lesson_dir: Path, fm: dict) -> list[str]:
    issues = []
    report_path = lesson_dir / "quality-report.yaml"
    status = fm.get("certification_status", "draft")

    if status == "certified" and not report_path.exists():
        issues.append(
            "certification_status=certified but quality-report.yaml missing"
        )
        return issues

    if not report_path.exists():
        if status not in ("draft", "static-fail", "teachback-fail"):
            issues.append("quality-report.yaml missing for non-draft lesson")
        return issues

    try:
        report = yaml.safe_load(report_path.read_text(encoding="utf-8")) or {}
    except Exception as e:
        return [f"quality-report.yaml parse error: {e}"]

    report_status = report.get("status") or report.get("verdict")
    if status == "certified" and report_status not in ("certified", "needs-human"):
        issues.append(
            f"Frontmatter certified but quality-report status={report_status!r}"
        )

    return issues


def check_lesson_quality(lesson_file: Path, strict: bool = False) -> dict:
    issues: list[str] = []
    fm, body = parse_frontmatter(lesson_file)

    if not fm:
        return {
            "lesson_file": str(lesson_file.relative_to(VAULT_ROOT)),
            "lesson_id": None,
            "status": "FAIL",
            "issue_count": 1,
            "issues": ["Missing valid YAML frontmatter"],
            "phase_b": "not_implemented",
        }

    lesson_id = fm.get("lesson_id") or "?"
    lesson_dir = lesson_file.parent

    # Frontmatter MUST fields (contract 5.2)
    for field in ["type", "title", "created", "updated", "tags", "up", "lesson_id", "diataxis", "certification_status", "spec_path"]:
        if field not in fm:
            issues.append(f"Missing mandatory frontmatter field: '{field}'")

    # Diátaxis section headers (legacy heuristic + contract 4.2)
    for header in DIATAXIS_HEADERS:
        if isinstance(header, tuple):
            label, aliases = header
            patterns = [label] + aliases
        else:
            patterns = [header]
        if not any(
            re.search(rf"#+\s+.*{re.escape(p)}", body, re.IGNORECASE)
            for p in patterns
        ):
            issues.append(
                f"Missing recommended section containing: "
                f"'{patterns[0]}'"
                + (f" (aliases: {patterns[1:]})" if len(patterns) > 1 else "")
            )

    # Duplicate H2
    h2s = find_h2_titles(body)
    seen = set()
    for h in h2s:
        norm = re.sub(r"\s+", " ", h.strip().lower())
        if norm in seen:
            issues.append(f"Duplicate H2 heading: '{h}'")
        seen.add(norm)

    # Chain of Action table
    if re.search(r"Chain of Action", body, re.IGNORECASE):
        coa_match = re.search(
            r"(?is)(##\s+.*Chain of Action.*?)(\n##\s+|\Z)",
            body,
        )
        coa_block = coa_match.group(1) if coa_match else body
        if "|" not in coa_block or "---" not in coa_block:
            issues.append("Chain of Action section missing Markdown table")

    # Transfer section
    if not re.search(r"#+\s+.*Transfer", body, re.IGNORECASE):
        issues.append("Missing Transfer section (contract 4.2 #8)")

    # Blackbox quiz — no inline answers
    quiz_match = re.search(
        r"(?is)(##\s+.*Blackbox.*?)(\n##\s+|\Z)",
        body,
    )
    quiz_block = quiz_match.group(1) if quiz_match else ""
    if not quiz_block:
        issues.append("Missing Blackbox Quiz section")
    else:
        for pat in QUIZ_SPOILER_PATTERNS:
            if re.search(pat, quiz_block, re.IGNORECASE | re.MULTILINE):
                issues.append(
                    "Blackbox quiz contains inline answer/spoiler "
                    f"(pattern: {pat})"
                )
        if "Rubryka" not in quiz_block and "rubryka" not in quiz_block.lower():
            issues.append("Blackbox quiz missing rubryka zaliczenia")

    # Canvas link
    canvas_links = [l for l in extract_wikilinks(body) if "canvas" in l.lower()]
    if not canvas_links:
        issues.append("Lesson body missing wikilink to .canvas")
    else:
        for link in canvas_links:
            if resolve_canvas_path(link) is None:
                issues.append(f"Canvas wikilink not found on disk: [[{link}]]")

    # Spec deep check
    spec_data = None
    spec_path_str = fm.get("spec_path")
    spec_file = None
    if spec_path_str:
        spec_file = VAULT_ROOT / spec_path_str
        if not spec_file.exists():
            spec_file = lesson_dir / Path(spec_path_str).name
        if not spec_file.exists():
            issues.append(f"spec_path not found: {spec_path_str}")
        else:
            try:
                spec_data = yaml.safe_load(spec_file.read_text(encoding="utf-8"))
                issues.extend(check_spec_completeness(spec_data, spec_file))

                for comp in spec_data.get("critical_competencies", []):
                    words = [w for w in comp.split("_") if len(w) >= 3]
                    if words and not any(w.lower() in body.lower() for w in words):
                        issues.append(
                            f"Spec mismatch: critical competency '{comp}' "
                            "not reflected in lesson text"
                        )

                for mm in spec_data.get("mental_models", []):
                    mm_id = mm.get("id", "") if isinstance(mm, dict) else str(mm)
                    words = [w for w in mm_id.split("_") if len(w) >= 3]
                    if words and not any(w.lower() in body.lower() for w in words):
                        issues.append(
                            f"Spec mismatch: mental model '{mm_id}' not mentioned"
                        )

                # Lab artifacts
                lab = spec_data.get("lab") or {}
                lab_path_str = lab.get("path")
                if lab.get("exec") and lab_path_str:
                    lab_path = VAULT_ROOT / lab_path_str.rstrip("/")
                    issues.extend(check_lab_artifacts(lab_path, spec_data))

            except Exception as e:
                issues.append(f"Failed to parse spec {spec_file}: {e}")

    # Roadmap link
    if lesson_id and lesson_id != "?":
        issues.extend(check_roadmap_link(lesson_id, lesson_file.stem))

    # Quality report consistency
    issues.extend(check_quality_report(lesson_dir, fm))

    # Status verdict
    fail_count = len(issues)
    if fail_count == 0:
        status = "PASS"
    elif strict or fail_count >= 3:
        status = "FAIL"
    else:
        status = "WARN"

    return {
        "lesson_file": str(lesson_file.relative_to(VAULT_ROOT)),
        "lesson_id": lesson_id,
        "status": status,
        "strict": strict,
        "issue_count": fail_count,
        "issues": issues,
        "phase_a": "implemented",
        "phase_b": "not_implemented",
        "frontmatter_certification_status": fm.get("certification_status"),
    }


def cmd_certify(args: list[str]) -> None:
    strict = "--strict" in args
    targets = [a for a in args if not a.startswith("-")]

    if not LESSONS_DIR.exists():
        print(json.dumps({"error": f"Lessons directory {LESSONS_DIR} not found"}))
        sys.exit(1)

    if targets:
        target_files: list[Path] = []
        for tid in targets:
            target_files.extend(LESSONS_DIR.rglob(f"*{tid}*.md"))
    else:
        target_files = list(LESSONS_DIR.rglob("*.md"))

    results = []
    for lesson_file in sorted(set(target_files)):
        if lesson_file.name.endswith("-quality-audit.md"):
            continue
        if "certifier-audit" in lesson_file.name:
            continue
        results.append(check_lesson_quality(lesson_file, strict=strict))

    summary = {
        "certified_contract": "lesson-quality-contract-v1",
        "phase_a": "extended-static-gates",
        "phase_b": "NOT_IMPLEMENTED — use kb-blackbox for human quiz",
        "strict_mode": strict,
        "total_lessons_checked": len(results),
        "pass": sum(1 for r in results if r["status"] == "PASS"),
        "warn": sum(1 for r in results if r["status"] == "WARN"),
        "fail": sum(1 for r in results if r["status"] == "FAIL"),
        "reports": results,
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False, default=json_serial))

    if strict and any(r["status"] != "PASS" for r in results):
        sys.exit(1)


def main():
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    cmd_certify(sys.argv[1:])


if __name__ == "__main__":
    main()
