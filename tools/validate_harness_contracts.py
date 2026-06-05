#!/usr/bin/env python3
"""Validate cross-file harness routing, templates, eval cases, and scope terms."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROUTING = ROOT / "harness" / "task-routing.md"
REQUIRED_CASE_HEADINGS = [
    "入力例",
    "使うべきSkill",
    "期待する出力",
    "安全上の注意",
    "NG出力例",
    "評価観点",
]
LEGACY_TERMS = ["AI-OCR", "RPA", "FAX", "PoC"]
SCOPE_PATHS = [
    ROOT / "README.md",
    ROOT / "AGENTS.md",
    ROOT / "harness",
    ROOT / "templates",
    ROOT / "use-cases",
    ROOT / "skills",
    ROOT / "docs",
    ROOT / "evals",
]


def markdown_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(path.rglob("*.md"))


def main() -> int:
    errors: list[str] = []
    skills = {
        path.name
        for path in (ROOT / "skills").iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }
    templates = {path.name for path in (ROOT / "templates").glob("*.md")}

    routing_text = ROUTING.read_text(encoding="utf-8")
    for line in routing_text.splitlines():
        if not line.startswith("|") or line.startswith("| ---"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) != 4 or cells[0] == "依頼種別":
            continue
        route_skills = re.findall(r"`([a-z0-9-]+)`", cells[1])
        route_templates = re.findall(r"`([^`]+\.md)`", cells[2])
        for name in route_skills:
            if name not in skills:
                errors.append(f"unknown routed Skill: {name}")
        for name in route_templates:
            if name not in templates:
                errors.append(f"unknown routed template: {name}")

    for case in sorted((ROOT / "evals" / "cases").rglob("*.md")):
        text = case.read_text(encoding="utf-8")
        for heading in REQUIRED_CASE_HEADINGS:
            if not re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.MULTILINE):
                errors.append(f"{case.relative_to(ROOT)} missing heading: {heading}")

    for scope_path in SCOPE_PATHS:
        for path in markdown_files(scope_path):
            text = path.read_text(encoding="utf-8")
            for term in LEGACY_TERMS:
                if term in text:
                    errors.append(
                        f"legacy out-of-scope term '{term}' in {path.relative_to(ROOT)}"
                    )

    if errors:
        print("Harness contract validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Harness contract validation: OK")
    print(f"- routed Skills available: {len(skills)}")
    print(f"- templates available: {len(templates)}")
    print(
        f"- eval cases checked: {len(list((ROOT / 'evals' / 'cases').rglob('*.md')))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
