#!/usr/bin/env python3
"""Create a standard task workspace for the hospital workflow harness."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value or "hospital-workflow-task"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create outputs/YYYYMMDD-task-name with a task brief and run metadata."
    )
    parser.add_argument("task_name", help="Short ASCII task name used for the folder")
    parser.add_argument(
        "--title",
        help="Human-readable Japanese title. Defaults to task_name.",
    )
    parser.add_argument(
        "--workspace",
        type=Path,
        default=Path.cwd(),
        help="Workspace where outputs/ will be created. Defaults to the current directory.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    today = datetime.now().strftime("%Y%m%d")
    slug = slugify(args.task_name)
    title = args.title or args.task_name
    workspace = args.workspace.expanduser().resolve()
    task_dir = workspace / "outputs" / f"{today}-{slug}"

    if task_dir.exists():
        print(f"Task workspace already exists: {task_dir}")
        return 1

    task_dir.mkdir(parents=True)
    template = ROOT / "templates" / "task-brief.md"
    if not template.is_file():
        template = (
            ROOT
            / "skills"
            / "hospital-workflow-harness"
            / "assets"
            / "templates"
            / "task-brief.md"
        )
    shutil.copy2(template, task_dir / "task-brief.md")

    metadata = {
        "title": title,
        "task_name": slug,
        "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "status": "discovery",
        "primary_skill": None,
        "supporting_skills": [],
        "deliverables": [],
        "human_review_required": True,
    }
    (task_dir / "run.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Created task workspace: {task_dir}")
    print("- task-brief.md")
    print("- run.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
