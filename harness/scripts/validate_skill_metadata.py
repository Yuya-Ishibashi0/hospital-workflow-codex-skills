#!/usr/bin/env python3
"""Validate Codex Skill metadata without external dependencies."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
SKILLS_DIR = ROOT / ".agents" / "skills"
MIN_DESCRIPTION_LENGTH = 80


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    warnings: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, ["missing YAML frontmatter start"]

    metadata: dict[str, str] = {}
    end_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_index = index
            break
        if ":" not in line:
            warnings.append(f"invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")

    if end_index is None:
        warnings.append("missing YAML frontmatter end")

    return metadata, warnings


def validate_skill(skill_dir: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        errors.append("missing SKILL.md")
        return errors, warnings

    metadata, parse_warnings = parse_frontmatter(skill_md)
    warnings.extend(parse_warnings)

    name = metadata.get("name", "")
    description = metadata.get("description", "")

    if not name:
        errors.append("missing frontmatter name")
    elif name != skill_dir.name:
        warnings.append(f"name '{name}' does not match directory '{skill_dir.name}'")

    if not description:
        errors.append("missing frontmatter description")
    elif len(description) < MIN_DESCRIPTION_LENGTH:
        warnings.append(
            f"description is short ({len(description)} chars, expected at least {MIN_DESCRIPTION_LENGTH})"
        )

    return errors, warnings


def main() -> int:
    if not SKILLS_DIR.exists():
        print(f"ERROR: skills directory not found: {SKILLS_DIR}")
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        print(f"ERROR: no skills found under {SKILLS_DIR}")
        return 1

    total_errors = 0
    total_warnings = 0
    print(f"Validating {len(skill_dirs)} skills under {SKILLS_DIR.relative_to(ROOT)}")

    for skill_dir in skill_dirs:
        errors, warnings = validate_skill(skill_dir)
        status = "OK" if not errors else "ERROR"
        print(f"\n[{status}] {skill_dir.name}")
        for warning in warnings:
            total_warnings += 1
            print(f"  WARNING: {warning}")
        for error in errors:
            total_errors += 1
            print(f"  ERROR: {error}")

    print(f"\nSummary: {total_errors} errors, {total_warnings} warnings")
    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main())

