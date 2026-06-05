#!/usr/bin/env python3
"""Update and validate a harness task run.json lifecycle."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATUSES = [
    "discovery",
    "planned",
    "in_progress",
    "review_pending",
    "completed",
    "cancelled",
]
TRANSITIONS = {
    "discovery": {"planned", "cancelled"},
    "planned": {"in_progress", "cancelled"},
    "in_progress": {"review_pending", "cancelled"},
    "review_pending": {"in_progress", "completed", "cancelled"},
    "completed": set(),
    "cancelled": set(),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update a harness task run.")
    parser.add_argument("task_directory", type=Path)
    parser.add_argument("--status", choices=STATUSES)
    parser.add_argument("--primary-skill")
    parser.add_argument("--supporting-skill", action="append", default=[])
    parser.add_argument("--deliverable", type=Path, action="append", default=[])
    parser.add_argument("--purpose", action="append", default=[])
    parser.add_argument(
        "--human-reviewed",
        action="store_true",
        help="Required when moving from review_pending to completed.",
    )
    return parser.parse_args()


def load_run(path: Path) -> dict:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"unable to read run.json: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError("run.json must contain a JSON object")
    return payload


def validate_artifacts(task_dir: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "validate_artifacts.py"), str(task_dir)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise ValueError(result.stdout.strip() or result.stderr.strip())


def main() -> int:
    args = parse_args()
    task_dir = args.task_directory.expanduser().resolve()
    run_path = task_dir / "run.json"

    try:
        run = load_run(run_path)
        current = run.get("status")
        if current not in STATUSES:
            raise ValueError(f"unknown current status: {current}")

        if args.primary_skill:
            run["primary_skill"] = args.primary_skill

        supporting = list(run.get("supporting_skills") or [])
        for skill in args.supporting_skill:
            if skill not in supporting:
                supporting.append(skill)
        run["supporting_skills"] = supporting

        if len(args.purpose) > len(args.deliverable):
            raise ValueError("--purpose cannot be provided more times than --deliverable")

        deliverables = list(run.get("deliverables") or [])
        known_paths = {
            item.get("path")
            for item in deliverables
            if isinstance(item, dict) and isinstance(item.get("path"), str)
        }
        for index, raw_path in enumerate(args.deliverable):
            path = raw_path
            if path.is_absolute():
                try:
                    path = path.resolve().relative_to(task_dir)
                except ValueError as exc:
                    raise ValueError("deliverables must be inside the task directory") from exc
            normalized = path.as_posix()
            if normalized in known_paths:
                continue
            full_path = task_dir / path
            if not full_path.is_file():
                raise ValueError(f"deliverable does not exist: {full_path}")
            purpose = args.purpose[index] if index < len(args.purpose) else ""
            deliverables.append(
                {
                    "path": normalized,
                    "format": full_path.suffix.lower().lstrip("."),
                    "purpose": purpose,
                    "validated": False,
                }
            )
            known_paths.add(normalized)
        run["deliverables"] = deliverables

        if args.status and args.status != current:
            if args.status not in TRANSITIONS[current]:
                raise ValueError(f"invalid status transition: {current} -> {args.status}")
            if args.status in {"planned", "in_progress"} and not run.get("primary_skill"):
                raise ValueError("primary_skill is required before planning or execution")
            if args.status == "review_pending":
                if not deliverables:
                    raise ValueError("at least one deliverable is required")
                validate_artifacts(task_dir)
                for item in deliverables:
                    item["validated"] = True
            if args.status == "completed":
                if not args.human_reviewed:
                    raise ValueError("--human-reviewed is required to complete a task")
                run["human_reviewed_at"] = datetime.now().astimezone().isoformat(
                    timespec="seconds"
                )
            run["status"] = args.status

        run["updated_at"] = datetime.now().astimezone().isoformat(timespec="seconds")
        run_path.write_text(
            json.dumps(run, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    except ValueError as exc:
        print(f"Task run update failed: {exc}")
        return 1

    print(f"Updated task run: {run_path}")
    print(f"- status: {run['status']}")
    print(f"- primary skill: {run.get('primary_skill')}")
    print(f"- deliverables: {len(run.get('deliverables') or [])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
