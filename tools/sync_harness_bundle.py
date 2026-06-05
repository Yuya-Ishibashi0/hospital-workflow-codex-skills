#!/usr/bin/env python3
"""Bundle harness references and templates into the orchestrator Skill."""

from __future__ import annotations

import argparse
import filecmp
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "hospital-workflow-harness"
REFERENCE_SOURCE = ROOT / "harness"
REFERENCE_TARGET = SKILL_ROOT / "references"
TEMPLATE_SOURCE = ROOT / "templates"
TEMPLATE_TARGET = SKILL_ROOT / "assets" / "templates"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync harness docs and templates into the orchestrator Skill."
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    return parser.parse_args()


def differences(source: Path, target: Path, label: str) -> list[str]:
    if not target.is_dir():
        return [f"missing bundled directory: {label}"]
    result: list[str] = []

    def walk(node: filecmp.dircmp, relative: Path) -> None:
        for name in node.left_only:
            result.append(f"missing in bundle: {relative / name}")
        for name in node.right_only:
            result.append(f"extra in bundle: {relative / name}")
        for name in node.diff_files:
            result.append(f"bundle differs: {relative / name}")
        for name, child in node.subdirs.items():
            walk(child, relative / name)

    walk(filecmp.dircmp(source, target), Path(label))
    return result


def sync_tree(source: Path, target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    source_files = {
        path.relative_to(source)
        for path in source.rglob("*")
        if path.is_file() and path.name != ".DS_Store"
    }
    target_files = {
        path.relative_to(target)
        for path in target.rglob("*")
        if path.is_file() and path.name != ".DS_Store"
    }

    for relative in sorted(target_files - source_files):
        (target / relative).unlink()
    for relative in sorted(source_files):
        source_file = source / relative
        target_file = target / relative
        target_file.parent.mkdir(parents=True, exist_ok=True)
        if not target_file.exists() or not filecmp.cmp(
            source_file, target_file, shallow=False
        ):
            shutil.copy2(source_file, target_file)

    for directory in sorted(
        (path for path in target.rglob("*") if path.is_dir()),
        key=lambda path: len(path.parts),
        reverse=True,
    ):
        if not any(directory.iterdir()):
            directory.rmdir()


def main() -> int:
    args = parse_args()
    if args.write:
        sync_tree(REFERENCE_SOURCE, REFERENCE_TARGET)
        sync_tree(TEMPLATE_SOURCE, TEMPLATE_TARGET)
        print("Updated orchestrator reference and template bundle")

    issues = differences(REFERENCE_SOURCE, REFERENCE_TARGET, "references")
    issues.extend(differences(TEMPLATE_SOURCE, TEMPLATE_TARGET, "assets/templates"))
    if issues:
        print("Orchestrator bundle is out of sync:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("Orchestrator bundle: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
