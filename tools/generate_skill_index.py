#!/usr/bin/env python3
"""Generate a Markdown index of Codex Skills."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    metadata: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")
    return metadata


def main() -> int:
    if not SKILLS_DIR.exists():
        print(f"ERROR: skills directory not found: {SKILLS_DIR}", file=sys.stderr)
        return 1

    rows: list[tuple[str, str, str]] = []
    for skill_dir in sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir()):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            rows.append((skill_dir.name, "", "Missing SKILL.md"))
            continue
        metadata = parse_frontmatter(skill_md)
        rows.append(
            (
                metadata.get("name", skill_dir.name),
                f"skills/{skill_dir.name}/",
                metadata.get("description", ""),
            )
        )

    print("# Skill Index")
    print()
    print("| Skill | Path | Description |")
    print("| --- | --- | --- |")
    for name, path, description in rows:
        print(f"| `{name}` | `{path}` | {description} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
