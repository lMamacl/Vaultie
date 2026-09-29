import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "vaultie-lint.py"
spec = importlib.util.spec_from_file_location("vaultie_lint", SCRIPT)
linter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(linter)


class VaultieLintTests(unittest.TestCase):
    def make_vault(self, note: str, extra: dict[str, str] | None = None) -> Path:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)
        (root / "10_Libraries").mkdir()
        (root / "10_Libraries" / "sample.md").write_text(note, encoding="utf-8")
        for name, content in (extra or {}).items():
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
        return root

    def test_valid_note_and_existing_wikilink_pass(self):
        note = """---
type: library
title: Sample
created: 2026-09-29
updated: 2026-09-29
tags: [test]
aliases: []
up: "[[index]]"
---
See [[other]].
"""
        valid_target = """---\ntype: pattern\ntitle: Other\ncreated: 2026-09-29\nupdated: 2026-09-29\ntags: []\naliases: []\nup: \"[[index]]\"\n---\n# Other\n"""
        root = self.make_vault(note, {"90_Meta/index.md": "# Index", "20_Patterns/other.md": valid_target})
        report = linter.lint(root)
        self.assertEqual(report["summary"]["errors"], 0)

    def test_missing_required_field_is_error(self):
        note = """---
type: concept
title: Sample
created: 2026-09-29
updated: 2026-09-29
tags: []
aliases: []
---
Body
"""
        report = linter.lint(self.make_vault(note))
        self.assertTrue(any(e["code"] == "required_field" and "up" in e["message"] for e in report["errors"]))

    def test_invalid_date_is_error(self):
        note = """---
type: concept
title: Sample
created: 29-09-2026
updated: 2026-09-29
tags: []
aliases: []
up: "[[index]]"
---
Body
"""
        report = linter.lint(self.make_vault(note))
        self.assertTrue(any(e["code"] == "invalid_date" for e in report["errors"]))

    def test_dead_wikilink_is_error_but_example_in_comment_is_ignored(self):
        note = """---
type: concept
title: Sample
created: 2026-09-29
updated: 2026-09-29
tags: []
aliases: []
up: "[[index]]"
---
<!-- Example [[not-a-real-note]] -->
See [[also-missing]].
"""
        root = self.make_vault(note, {"90_Meta/index.md": "# Index"})
        report = linter.lint(root)
        dead = [e["message"] for e in report["errors"] if e["code"] == "broken_wikilink"]
        self.assertEqual(dead, ["target not found: [[also-missing]]"])

    def test_invalid_yaml_is_rejected_when_pyyaml_is_available(self):
        if linter.yaml is None:
            self.skipTest("PyYAML is installed in CI; optional for local runs")
        note = """---\ntype: [broken\ntitle: Sample\ncreated: 2026-09-29\nupdated: 2026-09-29\ntags: []\naliases: []\nup: \"[[index]]\"\n---\nBody\n"""
        report = linter.lint(self.make_vault(note))
        self.assertTrue(any(e["code"] == "frontmatter" for e in report["errors"]))

    def test_raw_inbox_sources_are_not_schema_gated(self):
        root = self.make_vault("---\ntype: concept\ntitle: Sample\ncreated: 2026-09-29\nupdated: 2026-09-29\ntags: []\naliases: []\nup: \"[[index]]\"\n---\nBody\n")
        raw = root / "00_Inbox" / "_raw" / "source.md"
        raw.parent.mkdir(parents=True)
        raw.write_text("Unmodified source capture", encoding="utf-8")
        report = linter.lint(root)
        self.assertEqual(report["files_checked"], 1)


if __name__ == "__main__":
    unittest.main()
