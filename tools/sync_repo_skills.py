#!/usr/bin/env python3
"""Synchronize canonical plugin skills into the repo-local skill directory."""

from __future__ import annotations

import argparse
import filecmp
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"
TARGET = ROOT / ".agents" / "skills"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync canonical skills/ into .agents/skills/."
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Fail when the trees differ.")
    mode.add_argument("--write", action="store_true", help="Replace the repo-local mirror.")
    return parser.parse_args()


def compare_dirs(source: Path, target: Path) -> list[str]:
    if not target.is_dir():
        return [f"missing directory: {target.relative_to(ROOT)}"]

    comparison = filecmp.dircmp(source, target)
    differences: list[str] = []

    def walk(node: filecmp.dircmp, relative: Path) -> None:
        for name in node.left_only:
            differences.append(f"missing in mirror: {relative / name}")
        for name in node.right_only:
            differences.append(f"extra in mirror: {relative / name}")
        for name in node.diff_files:
            differences.append(f"content differs: {relative / name}")
        for name in node.funny_files:
            differences.append(f"unable to compare: {relative / name}")
        for name, child in node.subdirs.items():
            walk(child, relative / name)

    walk(comparison, Path(".agents/skills"))
    return differences


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
        TARGET.parent.mkdir(parents=True, exist_ok=True)
        sync_tree(SOURCE, TARGET)
        print(f"Synced {SOURCE.relative_to(ROOT)} -> {TARGET.relative_to(ROOT)}")

    differences = compare_dirs(SOURCE, TARGET)
    if differences:
        print("Repo-local skill mirror is out of sync:")
        for difference in differences:
            print(f"- {difference}")
        return 1

    print("Repo-local skill mirror: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
