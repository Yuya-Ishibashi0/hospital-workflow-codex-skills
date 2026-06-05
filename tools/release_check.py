#!/usr/bin/env python3
"""Run all repository release gates in a stable order."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable
CHECKS = [
    ("orchestrator bundle", ["tools/sync_harness_bundle.py", "--check"]),
    ("repo-local Skill mirror", ["tools/sync_repo_skills.py", "--check"]),
    ("Skill metadata", ["tools/validate_skill_metadata.py"]),
    ("Skill sections", ["tools/validate_skill_sections.py"]),
    ("plugin manifest", ["tools/validate_plugin_manifest.py"]),
    ("harness contracts", ["tools/validate_harness_contracts.py"]),
    ("documentation links", ["tools/validate_markdown_links.py"]),
    ("harness doctor", ["tools/harness_doctor.py"]),
    ("isolated smoke tests", ["tools/smoke_test_harness.py"]),
]


def main() -> int:
    for label, arguments in CHECKS:
        print(f"\n== {label} ==")
        result = subprocess.run(
            [PYTHON, *arguments],
            cwd=ROOT,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            print(f"\nRelease check failed at: {label}")
            return result.returncode

    print("\n== Python syntax ==")
    result = subprocess.run(
        [PYTHON, "-m", "compileall", "-q", "tools"],
        cwd=ROOT,
        check=False,
    )
    if result.returncode != 0:
        print("\nRelease check failed at: Python syntax")
        return result.returncode

    print("\nRelease check: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
