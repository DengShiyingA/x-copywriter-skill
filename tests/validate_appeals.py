from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(text: str, needle: str, source: str) -> None:
    if needle not in text:
        raise AssertionError(f"{source}: missing {needle!r}")


skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
readme = (ROOT / "README.md").read_text(encoding="utf-8")
appeals_path = ROOT / "references" / "x-appeals.md"

if not appeals_path.exists():
    raise AssertionError("references/x-appeals.md: file is missing")

appeals = appeals_path.read_text(encoding="utf-8")

for needle in (
    "references/x-appeals.md",
    "Appeal or review request",
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

require(readme, "X appeals", "README.md")
print("Appeals contract is valid")
