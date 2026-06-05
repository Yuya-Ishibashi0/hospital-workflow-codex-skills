#!/usr/bin/env python3
"""Validate local Markdown and simple HTML links in repository documentation."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ROOT / "README.md",
    ROOT / "README.en.md",
    ROOT / "AGENTS.md",
    ROOT / "CHANGELOG.md",
    ROOT / "SECURITY.md",
    ROOT / "docs",
    ROOT / "harness",
    ROOT / "templates",
    ROOT / "use-cases",
    ROOT / "examples",
    ROOT / "evals",
    ROOT / ".github",
]
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_LINK = re.compile(r"""(?:href|src)=["']([^"']+)["']""")


def source_files() -> list[Path]:
    files: list[Path] = []
    for source in SOURCES:
        if source.is_file():
            files.append(source)
        elif source.is_dir():
            files.extend(source.rglob("*.md"))
    return sorted(set(files))


def local_target(raw: str) -> str | None:
    target = raw.strip().strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    target = target.split("#", 1)[0].split("?", 1)[0]
    return unquote(target) if target else None


def main() -> int:
    errors: list[str] = []
    checked = 0
    for document in source_files():
        text = document.read_text(encoding="utf-8")
        raw_targets = MARKDOWN_LINK.findall(text) + HTML_LINK.findall(text)
        for raw in raw_targets:
            target = local_target(raw)
            if target is None:
                continue
            checked += 1
            path = (document.parent / target).resolve()
            try:
                path.relative_to(ROOT)
            except ValueError:
                errors.append(
                    f"{document.relative_to(ROOT)} links outside repository: {target}"
                )
                continue
            if not path.exists():
                errors.append(
                    f"{document.relative_to(ROOT)} has broken link: {target}"
                )

    if errors:
        print("Markdown link validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Markdown link validation: OK ({checked} local links)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
