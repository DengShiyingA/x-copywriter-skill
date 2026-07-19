from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(text: str, needle: str, source: str) -> None:
    if needle not in text:
        raise AssertionError(f"{source}: missing {needle!r}")


skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
readme = (ROOT / "README.md").read_text(encoding="utf-8")
readme_en_path = ROOT / "README.en.md"
appeals_path = ROOT / "references" / "x-appeals.md"

if not readme_en_path.exists():
    raise AssertionError("README.en.md: file is missing")

if not appeals_path.exists():
    raise AssertionError("references/x-appeals.md: file is missing")

readme_en = readme_en_path.read_text(encoding="utf-8")
appeals = appeals_path.read_text(encoding="utf-8")

for needle in (
    "references/x-appeals.md",
    "Appeal or review request",
    "X account/content/feature/monetization appeals",
):
    require(skill, needle, "SKILL.md")

for needle in (
    "## Fact Ledger",
    "## Appeal Stages",
    "## Output Contract",
    "## Safety And Integrity",
    "initial appeal",
    "no substantive response",
    "reconsideration after rejection",
    "supplemental evidence",
    "account suspension",
    "post-level enforcement",
    "feature restriction",
    "monetization",
    "requested language",
    "Do not fabricate",
    "Do not provide ban-evasion",
    "Do not recommend a fixed resubmission cadence",
    "contradiction",
):
    require(appeals, needle, "references/x-appeals.md")

require(readme, "申诉与合规自查", "README.md")
require(readme_en, "X appeals", "README.en.md")
print("Appeals contract is valid")
