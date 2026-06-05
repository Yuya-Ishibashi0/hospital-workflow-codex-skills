#!/usr/bin/env python3
"""Validate required sections in Codex Skill files."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = ROOT / ".agents" / "skills"
REQUIRED_SECTIONS = [
    "Purpose",
    "When to use",
    "When not to use",
    "Inputs",
    "Process",
    "Output format",
    "Safety constraints",
    "Examples",
    "Escalation / human review notes",
]


def has_heading(text: str, heading: str) -> bool:
    pattern = re.compile(rf"^#+\s+{re.escape(heading)}\s*$", re.MULTILINE)
    return bool(pattern.search(text))


def validate_skill(skill_dir: Path) -> list[str]:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return ["missing SKILL.md"]

    text = skill_md.read_text(encoding="utf-8")
    return [section for section in REQUIRED_SECTIONS if not has_heading(text, section)]


def main() -> int:
    if not SKILLS_DIR.exists():
        print(f"ERROR: skills directory not found: {SKILLS_DIR}")
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        print(f"ERROR: no skills found under {SKILLS_DIR}")
        return 1

    total_missing = 0
    print(f"Validating required sections for {len(skill_dirs)} skills")

    for skill_dir in skill_dirs:
        missing = validate_skill(skill_dir)
        status = "OK" if not missing else "ERROR"
        print(f"\n[{status}] {skill_dir.name}")
        for section in missing:
            total_missing += 1
            print(f"  MISSING: {section}")

    print(f"\nSummary: {total_missing} missing required sections")
    return 1 if total_missing else 0


if __name__ == "__main__":
    sys.exit(main())

