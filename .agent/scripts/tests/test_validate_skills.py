import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "validate_skills.py"
spec = importlib.util.spec_from_file_location("validate_skills", SCRIPT)
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class ValidateSkillsTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name) / "skills"
        self.root.mkdir()

    def add_skill(self, folder: str, manifest: str):
        path = self.root / folder
        path.mkdir()
        (path / "SKILL.md").write_text(manifest, encoding="utf-8")

    def test_valid_skill_package_passes(self):
        self.add_skill("kb-query", """---\nname: kb-query\ndescription: Searches project knowledge when asked to find a pattern.\n---\n\n# Query\n""")
        report = validator.validate_skills(self.root)
        self.assertEqual(report["errors"], [])

    def test_missing_skill_manifest_is_error(self):
        (self.root / "kb-query").mkdir()
        report = validator.validate_skills(self.root)
        self.assertTrue(any("no SKILL.md" in e["message"] for e in report["errors"]))

    def test_missing_description_is_error(self):
        self.add_skill("kb-query", """---\nname: kb-query\n---\n\n# Query\n""")
        report = validator.validate_skills(self.root)
        self.assertTrue(any("description" in e["message"] for e in report["errors"]))

    def test_folder_name_must_match_manifest_name(self):
        self.add_skill("kb-search", """---\nname: kb-query\ndescription: Searches notes.\n---\n\n# Query\n""")
        report = validator.validate_skills(self.root)
        self.assertTrue(any("does not match folder" in e["message"] for e in report["errors"]))

    def test_flat_legacy_skill_definitions_are_flagged(self):
        (self.root / "kb-query.md").write_text("# Legacy", encoding="utf-8")
        self.add_skill("kb-query", """---\nname: kb-query\ndescription: Searches notes.\n---\n\n# Query\n""")
        report = validator.validate_skills(self.root)
        self.assertTrue(any("legacy flat skill" in e["message"] for e in report["errors"]))


if __name__ == "__main__":
    unittest.main()
