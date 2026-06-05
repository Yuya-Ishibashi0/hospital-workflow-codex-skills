#!/usr/bin/env python3
"""Run isolated smoke tests for installation and task lifecycle behavior."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def run(*args: str, expect: int = 0) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        [PYTHON, *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != expect:
        raise RuntimeError(
            f"command failed ({result.returncode}, expected {expect}): {' '.join(args)}\n"
            f"{result.stdout}\n{result.stderr}"
        )
    return result


def test_task_lifecycle(base: Path) -> None:
    workspace = base / "workspace"
    workspace.mkdir()
    run(
        "tools/start_harness_task.py",
        "smoke-test",
        "--title",
        "スモークテスト",
        "--workspace",
        str(workspace),
    )
    task = workspace / "outputs" / f"{datetime.now():%Y%m%d}-smoke-test"
    (task / "result.md").write_text("# Result\n\nSmoke test.\n", encoding="utf-8")

    run(
        "tools/update_task_run.py",
        str(task),
        "--status",
        "planned",
        "--primary-skill",
        "hospital-document-drafter",
    )
    run("tools/update_task_run.py", str(task), "--status", "in_progress")
    run(
        "tools/update_task_run.py",
        str(task),
        "--deliverable",
        "result.md",
        "--purpose",
        "スモークテスト成果物",
        "--status",
        "review_pending",
    )
    run(
        "tools/update_task_run.py",
        str(task),
        "--status",
        "completed",
        "--human-reviewed",
    )
    payload = json.loads((task / "run.json").read_text(encoding="utf-8"))
    if payload.get("status") != "completed":
        raise RuntimeError("task lifecycle did not reach completed")
    if not payload.get("deliverables", [{}])[0].get("validated"):
        raise RuntimeError("task deliverable was not validated")


def test_installer_lifecycle(base: Path) -> None:
    codex_home = base / "codex-home"
    run("tools/install_user_harness.py", "--codex-home", str(codex_home))
    installed = codex_home / "hospital-workflow-harness"
    run(str(installed / "tools" / "harness_doctor.py"))
    if not (codex_home / "skills" / "hospital-workflow-harness").is_symlink():
        raise RuntimeError("orchestrator Skill link was not installed")

    run("tools/install_user_harness.py", "--codex-home", str(codex_home))
    run(
        "tools/install_user_harness.py",
        "--codex-home",
        str(codex_home),
        "--uninstall",
    )
    if installed.exists():
        raise RuntimeError("harness install directory remained after uninstall")


def test_conflict_protection(base: Path) -> None:
    codex_home = base / "conflict-home"
    conflict = codex_home / "skills" / "hospital-manual-builder"
    conflict.mkdir(parents=True)
    marker = conflict / "KEEP.txt"
    marker.write_text("user-owned\n", encoding="utf-8")

    run(
        "tools/install_user_harness.py",
        "--codex-home",
        str(codex_home),
        expect=1,
    )
    if not marker.is_file():
        raise RuntimeError("conflicting user Skill was modified without --force")

    run(
        "tools/install_user_harness.py",
        "--codex-home",
        str(codex_home),
        "--force",
    )
    backups = list((codex_home / "backups").rglob("KEEP.txt"))
    if len(backups) != 1:
        raise RuntimeError("conflicting user Skill was not backed up exactly once")


def main() -> int:
    try:
        with tempfile.TemporaryDirectory(prefix="hospital-harness-smoke-") as raw:
            base = Path(raw)
            test_task_lifecycle(base)
            test_installer_lifecycle(base)
            test_conflict_protection(base)
    except RuntimeError as exc:
        print(f"Harness smoke test failed: {exc}")
        return 1

    print("Harness smoke tests: OK")
    print("- task lifecycle")
    print("- install, update, and uninstall")
    print("- conflict protection and backup")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
