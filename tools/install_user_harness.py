#!/usr/bin/env python3
"""Safely install, update, or uninstall the harness in a user's Codex home."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CODEX_HOME = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
PLUGIN_NAME = "hospital-workflow-codex-skills"
INSTALL_DIR_NAME = "hospital-workflow-harness"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install or remove Hospital Workflow Harness in a Codex home."
    )
    parser.add_argument(
        "--codex-home",
        type=Path,
        default=DEFAULT_CODEX_HOME,
        help="Codex home directory. Defaults to CODEX_HOME or ~/.codex.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show the planned operation without writing files.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Back up and replace conflicting same-named user Skills.",
    )
    parser.add_argument(
        "--uninstall",
        action="store_true",
        help="Remove only files and links owned by this installer.",
    )
    return parser.parse_args()


def plugin_name(path: Path) -> str | None:
    manifest = path / ".codex-plugin" / "plugin.json"
    try:
        payload = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    value = payload.get("name")
    return value if isinstance(value, str) else None


def canonical_skill_names() -> list[str]:
    return sorted(
        path.name
        for path in (ROOT / "skills").iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    )


def managed_link(path: Path, install_root: Path) -> bool:
    if not path.is_symlink():
        return False
    try:
        resolved = path.resolve(strict=False)
        resolved.relative_to(install_root.resolve(strict=False))
    except (OSError, ValueError):
        return False
    return True


def copy_source(target: Path) -> None:
    shutil.copytree(
        ROOT,
        target,
        ignore=shutil.ignore_patterns(
            ".git",
            ".agents",
            ".DS_Store",
            "outputs",
            "tmp",
            "__pycache__",
        ),
    )


def unique_backup_root(codex_home: Path, timestamp: str) -> Path:
    base = codex_home / "backups" / f"{INSTALL_DIR_NAME}-{timestamp}"
    candidate = base
    counter = 1
    while candidate.exists():
        candidate = Path(f"{base}-{counter}")
        counter += 1
    return candidate


def uninstall(codex_home: Path, dry_run: bool) -> int:
    install_root = codex_home / INSTALL_DIR_NAME
    skill_root = codex_home / "skills"
    owned = []
    for name in canonical_skill_names():
        target = skill_root / name
        if managed_link(target, install_root):
            owned.append(target)

    print(f"Remove harness: {install_root}")
    for target in owned:
        print(f"Remove managed Skill link: {target}")

    if dry_run:
        return 0

    for target in owned:
        target.unlink()
    if install_root.exists():
        if plugin_name(install_root) != PLUGIN_NAME:
            print("Refusing to remove an install directory not owned by this harness.")
            return 1
        shutil.rmtree(install_root)
    print("Uninstallation complete.")
    return 0


def main() -> int:
    args = parse_args()
    codex_home = args.codex_home.expanduser().resolve()
    install_root = codex_home / INSTALL_DIR_NAME
    skill_root = codex_home / "skills"

    if args.uninstall:
        return uninstall(codex_home, args.dry_run)

    names = canonical_skill_names()
    conflicts: list[Path] = []
    for name in names:
        target = skill_root / name
        if not target.exists() and not target.is_symlink():
            continue
        if managed_link(target, install_root):
            continue
        conflicts.append(target)

    if install_root.exists() and plugin_name(install_root) != PLUGIN_NAME:
        print(f"Installation failed: unmanaged directory exists: {install_root}")
        return 1

    print(f"Harness destination: {install_root}")
    print(f"User Skill directory: {skill_root}")
    print(f"Skills to install: {len(names)}")
    if conflicts:
        print("Conflicting same-named Skills:")
        for conflict in conflicts:
            print(f"- {conflict}")
        if not args.force:
            print("Re-run with --force to back up and replace these conflicts.")
            return 1

    timestamp = datetime.now().astimezone().strftime("%Y%m%dT%H%M%S")
    backup_root = unique_backup_root(codex_home, timestamp)
    if args.force or install_root.exists():
        print(f"Backup destination: {backup_root}")

    if args.dry_run:
        return 0

    codex_home.mkdir(parents=True, exist_ok=True)
    skill_root.mkdir(parents=True, exist_ok=True)
    staging = codex_home / f".{INSTALL_DIR_NAME}.staging-{os.getpid()}"
    if staging.exists():
        shutil.rmtree(staging)

    moved_install = False
    moved_conflicts: list[tuple[Path, Path]] = []
    try:
        copy_source(staging)
        manifest = {
            "plugin": PLUGIN_NAME,
            "source": str(ROOT),
            "installed_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "skills": names,
        }
        (staging / ".install-manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

        if install_root.exists() or conflicts:
            backup_root.mkdir(parents=True, exist_ok=False)
        if install_root.exists():
            shutil.move(str(install_root), str(backup_root / "harness"))
            moved_install = True
        for conflict in conflicts:
            skills_backup = backup_root / "skills"
            skills_backup.mkdir(parents=True, exist_ok=True)
            backup_target = skills_backup / conflict.name
            shutil.move(str(conflict), str(backup_target))
            moved_conflicts.append((conflict, backup_target))

        staging.rename(install_root)

        for name in names:
            target = skill_root / name
            if target.exists() or target.is_symlink():
                if managed_link(target, install_root):
                    target.unlink()
                else:
                    raise RuntimeError(f"unexpected Skill conflict after backup: {target}")
            target.symlink_to(
                install_root / "skills" / name,
                target_is_directory=True,
            )
            print(f"Installed Skill: {name}")
    except Exception as exc:
        if staging.exists():
            shutil.rmtree(staging)
        if install_root.exists():
            shutil.rmtree(install_root)
        if moved_install and (backup_root / "harness").exists():
            shutil.move(str(backup_root / "harness"), str(install_root))
        for original, backup in moved_conflicts:
            if original.exists() or original.is_symlink():
                if original.is_dir() and not original.is_symlink():
                    shutil.rmtree(original)
                else:
                    original.unlink()
            if backup.exists() or backup.is_symlink():
                shutil.move(str(backup), str(original))
        print(f"Installation failed: {exc}")
        print("The previous installation and conflicting Skills were restored.")
        return 1

    print("Installation complete. Restart Codex before using the harness.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
