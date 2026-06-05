#!/usr/bin/env python3
"""Validate the repository's Codex plugin manifest without external packages."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".codex-plugin" / "plugin.json"
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
HEX_COLOR = re.compile(r"^#[0-9A-Fa-f]{6}$")


def require_string(payload: dict, key: str, errors: list[str], prefix: str = "") -> None:
    value = payload.get(key)
    label = f"{prefix}{key}"
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label} must be a non-empty string")


def main() -> int:
    errors: list[str] = []
    try:
        payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Plugin manifest validation failed: {exc}")
        return 1

    if not isinstance(payload, dict):
        print("Plugin manifest validation failed: manifest must be an object")
        return 1

    for key in ("name", "version", "description", "skills"):
        require_string(payload, key, errors)

    version = payload.get("version")
    if isinstance(version, str) and not SEMVER.fullmatch(version):
        errors.append("version must use MAJOR.MINOR.PATCH")
    if payload.get("skills") != "./skills/":
        errors.append("skills must be ./skills/")

    author = payload.get("author")
    if not isinstance(author, dict):
        errors.append("author must be an object")
    else:
        require_string(author, "name", errors, "author.")

    interface = payload.get("interface")
    if not isinstance(interface, dict):
        errors.append("interface must be an object")
    else:
        for key in (
            "displayName",
            "shortDescription",
            "longDescription",
            "developerName",
            "category",
        ):
            require_string(interface, key, errors, "interface.")
        prompts = interface.get("defaultPrompt")
        if (
            not isinstance(prompts, list)
            or not 1 <= len(prompts) <= 3
            or not all(isinstance(item, str) and item.strip() for item in prompts)
        ):
            errors.append("interface.defaultPrompt must contain 1-3 strings")
        elif any(len(item) > 128 for item in prompts):
            errors.append("interface.defaultPrompt entries must be 128 characters or fewer")
        color = interface.get("brandColor")
        if color is not None and (
            not isinstance(color, str) or not HEX_COLOR.fullmatch(color)
        ):
            errors.append("interface.brandColor must use #RRGGBB")
        logo = interface.get("logo")
        if logo is not None:
            if not isinstance(logo, str) or not logo.startswith("./"):
                errors.append("interface.logo must be a relative ./ path")
            elif not (ROOT / logo[2:]).is_file():
                errors.append(f"interface.logo does not exist: {logo}")

    skill_dirs = sorted(
        path.name
        for path in (ROOT / "skills").iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    )
    if len(skill_dirs) != 10:
        errors.append(f"expected 10 plugin Skills, found {len(skill_dirs)}")
    if "hospital-workflow-harness" not in skill_dirs:
        errors.append("missing hospital-workflow-harness orchestrator Skill")

    if errors:
        print("Plugin manifest validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Plugin manifest validation: OK")
    print(f"- name: {payload['name']}")
    print(f"- version: {payload['version']}")
    print(f"- skills: {len(skill_dirs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
