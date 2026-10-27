#!/usr/bin/env python3
"""Validate that each Vaultie skill is a discoverable Agent Skills package."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ROOT = Path(__file__).resolve().parents[1] / "skills"


def read_manifest(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, "SKILL.md must start with YAML frontmatter"
    try:
        end = text.index("\n---\n", 4)
    except ValueError:
        return None, "SKILL.md is missing the closing frontmatter delimiter"
    raw = text[4:end]
    if yaml is not None:
        try:
            data = yaml.safe_load(raw)
        except Exception as exc:
            return None, f"invalid YAML frontmatter: {exc}"
        if not isinstance(data, dict):
            return None, "frontmatter must be a YAML mapping"
        return data, None

    # Minimal stdlib fallback; CI installs PyYAML for full YAML parsing.
    data = {}
    for line in raw.splitlines():
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$", line)
        if match:
            key, value = match.groups()
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            data[key] = value
    return data, None


def validate_skills(skills_dir: Path):
    errors: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []
    skill_dirs = sorted(path for path in skills_dir.iterdir() if path.is_dir()) if skills_dir.exists() else []
    flat_defs = sorted(path.name for path in skills_dir.glob("kb-*.md")) if skills_dir.exists() else []
    for filename in flat_defs:
        errors.append({"path": str(skills_dir / filename), "message": "legacy flat skill file; move canonical instructions into <skill-name>/SKILL.md"})
    for folder in skill_dirs:
        manifest = folder / "SKILL.md"
        if not manifest.is_file():
            errors.append({"path": str(folder), "message": "skill folder has no SKILL.md"})
            continue
        data, problem = read_manifest(manifest)
        if problem:
            errors.append({"path": str(manifest), "message": problem})
            continue
        name = data.get("name")
        description = data.get("description")
        if not isinstance(name, str) or not NAME_RE.fullmatch(name):
            errors.append({"path": str(manifest), "message": "frontmatter 'name' must be a lowercase hyphenated skill id"})
        elif name != folder.name:
            errors.append({"path": str(manifest), "message": f"frontmatter name '{name}' does not match folder '{folder.name}'"})
        if not isinstance(description, str) or not description.strip():
            errors.append({"path": str(manifest), "message": "frontmatter 'description' is required for skill discovery"})
        elif len(description) > 1024:
            errors.append({"path": str(manifest), "message": "description exceeds 1024 characters"})
        if data.get("name") and data.get("name") != folder.name:
            continue
        if manifest.stat().st_size == 0:
            errors.append({"path": str(manifest), "message": "SKILL.md has no instructions"})
    if not skill_dirs:
        errors.append({"path": str(skills_dir), "message": "no skill directories found"})
    names = []
    for folder in skill_dirs:
        manifest = folder / "SKILL.md"
        if not manifest.is_file():
            continue
        data, _ = read_manifest(manifest)
        if data and isinstance(data.get("name"), str):
            names.append(data["name"])
    for name in sorted({name for name in names if names.count(name) > 1}):
        errors.append({"path": str(skills_dir), "message": f"duplicate skill name '{name}'"})
    return {"skills_dir": str(skills_dir), "skill_count": len(skill_dirs), "errors": errors, "warnings": warnings}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skills_dir", nargs="?", type=Path, default=ROOT)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = validate_skills(args.skills_dir.resolve())
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Skill registry: {report['skill_count']} skills, {len(report['errors'])} errors")
        for issue in report["errors"]:
            print(f"ERROR {issue['path']}: {issue['message']}")
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
