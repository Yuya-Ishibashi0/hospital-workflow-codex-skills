#!/usr/bin/env python3
"""Check whether the lightweight Codex harness is structurally usable."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_HARNESS_FILES = [
    "README.md",
    "operating-model.md",
    "task-routing.md",
    "safety-boundaries.md",
    "output-contracts.md",
    "artifact-output-policy.md",
    "artifact-generation.md",
    "run-lifecycle.md",
    "human-review-policy.md",
    "workflow-modes.md",
]

REQUIRED_TEMPLATES = [
    "workflow-hearing-sheet.md",
    "workflow-map.md",
    "template-document-mapping.md",
    "survey-summary-report.md",
    "proposal-outline.md",
    "meeting-minutes.md",
    "department-manual.md",
    "operation-design.md",
    "task-brief.md",
]


def check_file(path: Path, errors: list[str]) -> None:
    if not path.is_file():
        errors.append(f"missing file: {path.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []

    check_file(ROOT / "AGENTS.md", errors)
    check_file(ROOT / ".codex-plugin" / "plugin.json", errors)
    check_file(ROOT / "skills" / "hospital-workflow-harness" / "SKILL.md", errors)

    for name in REQUIRED_HARNESS_FILES:
        check_file(ROOT / "harness" / name, errors)

    for name in REQUIRED_TEMPLATES:
        check_file(ROOT / "templates" / name, errors)

    plugin_path = ROOT / ".codex-plugin" / "plugin.json"
    if plugin_path.is_file():
        try:
            plugin = json.loads(plugin_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            errors.append("invalid JSON: .codex-plugin/plugin.json")
        else:
            if plugin.get("skills") != "./skills/":
                errors.append("plugin skills path must be ./skills/")

    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if len(skill_files) != 10:
        errors.append(
            f"expected orchestrator plus 9 task skills under skills/, found {len(skill_files)}"
        )

    installed_distribution = (ROOT / ".install-manifest.json").is_file()
    if not installed_distribution:
        mirror_check = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "sync_repo_skills.py"), "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if mirror_check.returncode != 0:
            errors.append("repo-local .agents/skills mirror is out of sync")

    bundle_check = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "sync_harness_bundle.py"), "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if bundle_check.returncode != 0:
        errors.append("orchestrator reference/template bundle is out of sync")

    manifest_check = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "validate_plugin_manifest.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if manifest_check.returncode != 0:
        errors.append("plugin manifest validation failed")

    contract_check = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "validate_harness_contracts.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if contract_check.returncode != 0:
        errors.append("harness contract validation failed")

    if errors:
        print("Harness doctor found problems:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Harness doctor: OK")
    print(f"- plugin manifest: {plugin_path.relative_to(ROOT)}")
    print(f"- plugin skills: {len(skill_files)}")
    if installed_distribution:
        print("- distribution mode: user-level install")
    else:
        print("- repo-local skill mirror: synchronized")
    print("- orchestrator bundle: synchronized")
    print("- plugin manifest: valid")
    print("- routing, templates, evals, and scope terms: valid")
    print(f"- harness documents: {len(REQUIRED_HARNESS_FILES)}")
    print(f"- templates: {len(REQUIRED_TEMPLATES)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
