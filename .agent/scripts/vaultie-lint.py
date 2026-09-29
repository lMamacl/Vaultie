#!/usr/bin/env python3
"""Read-only structural lint for Vaultie notes (Python standard library only).

Checks frontmatter and local wikilinks in 00_Inbox and the production note folders.
Exit code 1 means at least one blocking error; warnings do not fail the run.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

try:
    import yaml  # Optional locally; CI installs it for full YAML syntax validation.
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[2]
CONTENT_DIRS = ("00_Inbox", "10_Libraries", "20_Patterns", "30_Decisions", "40_Snippets", "50_Concepts")
REQUIRED = ("type", "title", "created", "updated", "tags", "up")
ALLOWED_TYPES = {"library", "pattern", "decision", "snippet", "concept", "clip", "moc", "raw-extract", "comparison", "deep-analysis", "review", "proposal"}
LINK_RE = re.compile(r"(?<!!)\[\[([^\]]+)\]\]")


def frontmatter(text: str):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "missing opening ---"
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return None, "missing closing ---"
    raw_frontmatter = "\n".join(lines[1:end])
    if yaml is not None:
        try:
            parsed = yaml.safe_load(raw_frontmatter)
            if not isinstance(parsed, dict):
                return None, "frontmatter must be a YAML mapping"
        except Exception as exc:
            return None, f"invalid YAML frontmatter: {exc}"
    values = {}
    for line in lines[1:end]:
        if not line or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:\s*(.*))?$", line)
        if not match:
            # Continuation lines (e.g. YAML lists) are permitted; malformed top-level
            # lines are not. Indented lines belong to the preceding key.
            if line[:1].isspace():
                continue
            return None, f"invalid frontmatter line: {line[:80]}"
        key, value = match.group(1), (match.group(2) or "").strip()
        if key in values:
            return None, f"duplicate frontmatter key: {key}"
        values[key] = value
    return values, None


def unquote(value: str) -> str:
    value = value.split(" #", 1)[0].strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def find_markdown(root: Path):
    ignored = {".git", ".venv", "node_modules", "__pycache__", ".obsidian"}
    return [p for p in root.rglob("*.md") if not any(part in ignored for part in p.parts)]


def lint(root: Path):
    files = find_markdown(root)
    targets = []
    for p in files:
        parts = p.relative_to(root).parts
        if not parts:
            continue
        top = parts[0]
        if top in CONTENT_DIRS[1:]:
            targets.append(p)
        elif top == "00_Inbox" and len(parts) > 1 and parts[1] in {"_clips", "_proposals"} and (len(parts) == 2 or parts[1] == "_clips"):
            targets.append(p)
    # Raw captures are intentionally exempt: they preserve source material and may
    # not yet have been normalized into a knowledge-note schema.
    by_path = {p.relative_to(root).with_suffix("").as_posix().casefold(): p for p in files}
    by_stem: dict[str, list[Path]] = {}
    for p in files:
        by_stem.setdefault(p.stem.casefold(), []).append(p)
    errors, warnings = [], []
    for path in targets:
        rel = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append({"file": rel, "code": "read_error", "message": str(exc)})
            continue
        fm, problem = frontmatter(text)
        if problem:
            errors.append({"file": rel, "code": "frontmatter", "message": problem})
            continue
        for key in REQUIRED:
            if key not in fm or not unquote(fm[key]):
                errors.append({"file": rel, "code": "required_field", "message": f"missing or empty '{key}'"})
        if "aliases" not in fm:
            warnings.append({"file": rel, "code": "missing_aliases", "message": "frontmatter omits aliases; add [] when this note is next revised"})
        if "type" in fm:
            typ = unquote(fm["type"])
            if typ not in ALLOWED_TYPES:
                errors.append({"file": rel, "code": "invalid_type", "message": f"unsupported type '{typ}'"})
        for key in ("created", "updated"):
            val = unquote(fm.get(key, ""))
            if val:
                try:
                    date.fromisoformat(val)
                except ValueError:
                    errors.append({"file": rel, "code": "invalid_date", "message": f"'{key}' must be YYYY-MM-DD"})
        link_text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
        link_text = re.sub(r"```.*?```|~~~.*?~~~", "", link_text, flags=re.S)
        for link in LINK_RE.findall(link_text):
            target = link.split("|", 1)[0].split("#", 1)[0].strip()
            if not target or target.startswith("http") or "<%" in target or "placeholder" in target.casefold() or target.casefold() in {"notatka", "nazwa", "todo"}:
                continue
            norm = target.removesuffix(".md").casefold()
            exists = norm in by_path or bool(by_stem.get(norm)) or any(key.endswith("/" + norm) for key in by_path)
            if not exists:
                errors.append({"file": rel, "code": "broken_wikilink", "message": f"target not found: [[{target}]]"})
        # Empty sections are a review warning: some headings are intentionally brief.
        headings = list(re.finditer(r"^##\s+.+$", text, re.M))
        for i, heading in enumerate(headings):
            end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
            section = text[heading.end():end]
            meaningful = [ln.strip() for ln in section.splitlines() if ln.strip() and not ln.strip().startswith("<!--") and not ln.strip().endswith("-->")]
            if not meaningful:
                warnings.append({"file": rel, "code": "empty_section", "message": heading.group(0).strip()})
    return {"root": str(root), "files_checked": len(targets), "errors": errors, "warnings": warnings, "summary": {"errors": len(errors), "warnings": len(warnings)}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=ROOT, help="Vault root (defaults to this repository)")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    args = parser.parse_args()
    report = lint(args.root.resolve())
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"Vaultie lint: {report['files_checked']} plików; {report['summary']['errors']} błędów; {report['summary']['warnings']} ostrzeżeń")
        for category in ("errors", "warnings"):
            for item in report[category]:
                print(f"{category[:-1].upper():7} {item['file']}: {item['message']}")
    return 1 if report["errors"] else 0

if __name__ == "__main__":
    raise SystemExit(main())
