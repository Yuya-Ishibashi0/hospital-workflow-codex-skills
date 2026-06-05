#!/usr/bin/env python3
"""Validate generated document, workbook, slide, Markdown, and CSV artifacts."""

from __future__ import annotations

import argparse
import csv
import zipfile
from pathlib import Path


OOXML_REQUIRED = {
    ".docx": {"[Content_Types].xml", "word/document.xml"},
    ".xlsx": {"[Content_Types].xml", "xl/workbook.xml"},
    ".pptx": {"[Content_Types].xml", "ppt/presentation.xml"},
}
SUPPORTED = set(OOXML_REQUIRED) | {".md", ".csv"}
IGNORED_NAMES = {"README.md", "task-brief.md"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate generated artifacts under a file or task directory."
    )
    parser.add_argument("path", type=Path)
    return parser.parse_args()


def validate_ooxml(path: Path) -> list[str]:
    errors: list[str] = []
    if not zipfile.is_zipfile(path):
        return [f"{path}: not a valid OOXML ZIP package"]
    with zipfile.ZipFile(path) as archive:
        names = set(archive.namelist())
    missing = OOXML_REQUIRED[path.suffix.lower()] - names
    if missing:
        errors.append(f"{path}: missing package entries: {', '.join(sorted(missing))}")
    return errors


def validate_text(path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return [f"{path}: not valid UTF-8 text"]
    if not text.strip():
        return [f"{path}: empty file"]
    return []


def validate_csv(path: Path) -> list[str]:
    errors = validate_text(path)
    if errors:
        return errors
    try:
        with path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.reader(handle))
    except (OSError, csv.Error) as exc:
        return [f"{path}: invalid CSV: {exc}"]
    if not rows:
        return [f"{path}: CSV has no rows"]
    return []


def collect(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(
        candidate
        for candidate in path.rglob("*")
        if candidate.is_file()
        and candidate.name not in IGNORED_NAMES
        and candidate.name != "run.json"
    )


def main() -> int:
    args = parse_args()
    target = args.path.expanduser().resolve()
    if not target.exists():
        print(f"Artifact validation failed: path does not exist: {target}")
        return 1

    files = collect(target)
    artifacts = [path for path in files if path.suffix.lower() in SUPPORTED]
    if not artifacts:
        print("Artifact validation failed: no supported artifacts found")
        return 1

    errors: list[str] = []
    for artifact in artifacts:
        if artifact.stat().st_size == 0:
            errors.append(f"{artifact}: empty file")
            continue
        suffix = artifact.suffix.lower()
        if suffix in OOXML_REQUIRED:
            errors.extend(validate_ooxml(artifact))
        elif suffix == ".csv":
            errors.extend(validate_csv(artifact))
        else:
            errors.extend(validate_text(artifact))

    if errors:
        print("Artifact validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Artifact validation passed: {len(artifacts)} file(s)")
    for artifact in artifacts:
        print(f"- {artifact}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
