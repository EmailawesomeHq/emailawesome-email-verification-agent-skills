import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED = {
    "emailawesome",
    "emailawesome-list-cleaner",
    "emailawesome-hubspot-verification",
    "emailawesome-api-validation",
}
WORKFLOWS = EXPECTED - {"emailawesome"}


class SkillContractTests(unittest.TestCase):
    def test_expected_skill_set(self):
        self.assertEqual({path.name for path in SKILLS.iterdir() if path.is_dir()}, EXPECTED)

    def test_frontmatter_name_matches_folder(self):
        for folder in SKILLS.iterdir():
            content = (folder / "SKILL.md").read_text(encoding="utf-8")
            match = re.search(r"(?m)^name:\s*([a-z0-9-]+)$", content)
            self.assertIsNotNone(match, folder.name)
            self.assertEqual(match.group(1), folder.name)

    def test_core_routes_every_specialized_skill(self):
        core = (SKILLS / "emailawesome" / "SKILL.md").read_text(encoding="utf-8")
        for name in EXPECTED - {"emailawesome"}:
            self.assertIn(f"](../{name}/SKILL.md)", core)

    def test_workflow_readmes_match_skill_titles(self):
        for name in WORKFLOWS:
            skill = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
            readme = (SKILLS / name / "README.md").read_text(encoding="utf-8")
            skill_title = re.search(r"(?m)^# (.+)$", skill)
            readme_title = re.search(r"(?m)^# (.+)$", readme)
            self.assertIsNotNone(skill_title, name)
            self.assertIsNotNone(readme_title, name)
            self.assertEqual(skill_title.group(1), readme_title.group(1), name)

    def test_skill_instructions_are_model_neutral(self):
        for folder in SKILLS.iterdir():
            content = (folder / "SKILL.md").read_text(encoding="utf-8")
            self.assertNotIn("$emailawesome", content.lower(), folder.name)
            self.assertNotRegex(content.lower(), r"\b(?:codex|openai|claude|glm|deepseek)\b")
        for name in WORKFLOWS:
            content = (SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("](../emailawesome/SKILL.md)", content, name)

    def test_portability_contract_marks_adapter_optional(self):
        content = (ROOT / "COMPATIBILITY.md").read_text(encoding="utf-8").lower()
        self.assertIn("agents/openai.yaml", content)
        self.assertIn("optional", content)
        self.assertIn("ordinary python 3", content)

    def test_relative_references_exist(self):
        for folder in SKILLS.iterdir():
            content = (folder / "SKILL.md").read_text(encoding="utf-8")
            for target in re.findall(r"\]\(([^)]+)\)", content):
                if "://" not in target:
                    self.assertTrue((folder / target).exists(), f"{folder.name}: {target}")

    def test_openai_metadata_invokes_matching_skill(self):
        for folder in SKILLS.iterdir():
            content = (folder / "agents" / "openai.yaml").read_text(encoding="utf-8")
            self.assertIn(f"${folder.name}", content)
            match = re.search(r'(?m)^  short_description: "([^"]+)"$', content)
            self.assertIsNotNone(match, folder.name)
            self.assertGreaterEqual(len(match.group(1)), 25)
            self.assertLessEqual(len(match.group(1)), 64)

    def test_no_unfinished_placeholders(self):
        unfinished = "|".join(("TO" + "DO", "T" + "BD", r"\[" + "TO" + "DO:"))
        for path in ROOT.rglob("*"):
            if "tests" in path.parts or not path.is_file():
                continue
            if path.suffix.lower() in {".md", ".yaml", ".py"}:
                self.assertNotRegex(path.read_text(encoding="utf-8"), unfinished)


if __name__ == "__main__":
    unittest.main()
