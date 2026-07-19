from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(text: str, needle: str, source: str) -> None:
    if needle not in text:
        raise AssertionError(f"{source}: missing {needle!r}")


readme = (ROOT / "README.md").read_text(encoding="utf-8")
readme_en = (ROOT / "README.en.md").read_text(encoding="utf-8")
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
examples = (ROOT / "references" / "examples.md").read_text(encoding="utf-8")

for source, text in (
    ("README.md", readme),
    ("README.en.md", readme_en),
    ("SKILL.md", skill),
    ("references/examples.md", examples),
):
    require(text, "Xquik TweetClaw", source)

for needle in (
    "## Source Evidence Mode",
    "read-only grounding",
    "public engagement counts",
    "Do not use source evidence to:",
):
    require(skill, needle, "SKILL.md")

require(readme, "## 可选的来源证据", "README.md")
require(readme_en, "## Optional source evidence", "README.en.md")
require(examples, "## Example 8: Source-Grounded Draft", "references/examples.md")
print("Source evidence contract is valid")
