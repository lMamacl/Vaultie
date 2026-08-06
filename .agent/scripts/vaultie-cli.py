#!/usr/bin/env python3
"""
Vaultie CLI — Transaction & Integrity Helper
Pure Python standard library script for SHA-256 integrity, transaction planning, and vault linting.
"""

import sys
import os
import json
import hashlib
import re
from pathlib import Path

def compute_sha256(file_path):
    """Computes SHA-256 digest of a given file."""
    sha = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(65536):
            sha.update(chunk)
    return sha.hexdigest()

def cmd_hash(args):
    """Returns hash of specified file."""
    if not args:
        print("Usage: vaultie-cli.py hash <filepath>")
        sys.exit(1)
    file_path = Path(args[0])
    if not file_path.exists():
        print(f"Error: File {file_path} not found.")
        sys.exit(1)
    digest = compute_sha256(file_path)
    print(json.dumps({"path": str(file_path), "sha256": digest}, indent=2))

def cmd_lint(args):
    """Scans the vault for orphaned files, missing frontmatter, and broken wikilinks."""
    vault_dir = Path(args[0]) if args else Path.cwd()
    print(f"Scanning vault at: {vault_dir}")
    
    md_files = list(vault_dir.rglob("*.md"))
    results = {
        "total_md_files": len(md_files),
        "missing_frontmatter": [],
        "orphans": [],
        "broken_wikilinks": []
    }
    
    existing_stems = {f.stem for f in md_files}
    wikilink_pattern = re.compile(r'\[\[([^\]\|#]+)(?:[\|#][^\]]+)?\]\]')
    
    for f in md_files:
        if ".agent" in f.parts or "99_Archive" in f.parts:
            continue
        try:
            content = f.read_text(encoding='utf-8')
        except Exception:
            continue
        
        # Check frontmatter
        if not content.startswith("---"):
            results["missing_frontmatter"].append(str(f.relative_to(vault_dir)))
        else:
            if "up:" not in content and f.name != "_index.md":
                results["orphans"].append(str(f.relative_to(vault_dir)))
                
        # Check wikilinks
        matches = wikilink_pattern.findall(content)
        for link in matches:
            clean_link = link.strip()
            if clean_link not in existing_stems and clean_link != "90_Meta/_index":
                results["broken_wikilinks"].append({
                    "file": str(f.relative_to(vault_dir)),
                    "target": clean_link
                })
                
    print(json.dumps(results, indent=2, ensure_ascii=False))

def cmd_plan(args):
    """Generates an atomic transaction plan JSON for proposed modifications."""
    if len(args) < 2:
        print("Usage: vaultie-cli.py plan <target_file> <new_content_file>")
        sys.exit(1)
        
    target_path = Path(args[0])
    new_content_path = Path(args[1])
    
    old_hash = compute_sha256(target_path) if target_path.exists() else None
    new_hash = compute_sha256(new_content_path)
    
    plan = {
        "operation_id": f"tx-{os.urandom(4).hex()}",
        "target": str(target_path),
        "expected_old_sha256": old_hash,
        "proposed_new_sha256": new_hash,
        "action": "overwrite" if target_path.exists() else "create"
    }
    
    plan_json = json.dumps(plan, indent=2)
    plan_hash = hashlib.sha256(plan_json.encode('utf-8')).hexdigest()
    plan["plan_sha256"] = plan_hash
    
    print(json.dumps(plan, indent=2))

def main():
    if len(sys.argv) < 2:
        print("Vaultie CLI v1.0.0")
        print("Commands: hash, lint, plan")
        sys.exit(0)
        
    command = sys.argv[1]
    args = sys.argv[2:]
    
    if command == "hash":
        cmd_hash(args)
    elif command == "lint":
        cmd_lint(args)
    elif command == "plan":
        cmd_plan(args)
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
