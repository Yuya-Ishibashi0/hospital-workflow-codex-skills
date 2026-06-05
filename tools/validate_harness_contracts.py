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
REQUIRED_SCENARIO_HEADINGS = [
    "想定する場面",
    "最初の依頼",
    "作成されるファイル",
    "人が確認する点",
]
MINIMUM_SCENARIOS = 8
MINIMUM_DEPARTMENT_FILES = 8
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
    use_cases = ROOT / "use-cases"
    scenarios = use_cases / "scenarios"
    departments = use_cases / "departments"

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

    unexpected_root_use_cases = [
        path.name for path in use_cases.glob("*.md") if path.name != "README.md"
    ]
    for name in unexpected_root_use_cases:
        errors.append(
            f"use-cases/{name} must be placed under scenarios/ or departments/"
        )

    scenario_files = [
        path for path in sorted(scenarios.glob("*.md")) if path.name != "README.md"
    ]
    if len(scenario_files) < MINIMUM_SCENARIOS:
        errors.append(
            f"use-cases/scenarios requires at least {MINIMUM_SCENARIOS} scenarios"
        )
    for scenario in scenario_files:
        text = scenario.read_text(encoding="utf-8")
        for heading in REQUIRED_SCENARIO_HEADINGS:
            if not re.search(rf"^##\s+{re.escape(heading)}\s*$", text, re.MULTILINE):
                errors.append(
                    f"{scenario.relative_to(ROOT)} missing heading: {heading}"
                )

    department_files = [
        path for path in sorted(departments.glob("*.md")) if path.name != "README.md"
    ]
    if len(department_files) < MINIMUM_DEPARTMENT_FILES:
        errors.append(
            "use-cases/departments requires at least "
            f"{MINIMUM_DEPARTMENT_FILES} department files"
        )

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
    print(f"- representative scenarios checked: {len(scenario_files)}")
    print(f"- department indexes checked: {len(department_files)}")
    print(
        f"- eval cases checked: {len(list((ROOT / 'evals' / 'cases').rglob('*.md')))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
