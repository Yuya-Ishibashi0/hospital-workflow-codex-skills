# Hospital Workflow Codex Skills

[日本語](README.md) | English

Hospital Workflow Codex Skills is a lightweight Codex agent harness for non-clinical hospital workflow improvement.

It is not just a collection of Skills. It combines `AGENTS.md`, Codex Skills, workflow templates, task routing, safety boundaries, output contracts, human review rules, and maintenance tools so Codex can work safely and consistently on non-clinical hospital operations tasks.

## Scope

Supported:

- duplicate-entry and transfer-work reduction
- paper / Excel / Word workflow organization
- existing hospital template organization
- meeting summaries
- department manuals
- proposal drafts
- requirements and workflow documentation
- training and operations documents

Not supported:

- diagnosis
- treatment decisions
- patient-specific medical advice
- patient explanations
- clinical records
- handoff notes
- EHR content analysis
- patient personal information processing

## Structure

| Directory | Role |
| --- | --- |
| `.codex-plugin/` | Codex plugin manifest |
| `AGENTS.md` | Top-level rules for Codex |
| `.agents/skills/` | Repo-local Codex Skills |
| `skills/` | Plugin orchestrator and task Skills |
| `harness/` | Execution control layer for Codex |
| `templates/` | Reusable output templates |
| `use-cases/` | Representative workflow improvement scenarios |
| `tools/` | Maintenance scripts |
| `evals/` | Future evaluation cases and rubrics |
| `outputs/` | Default location for generated deliverable files |

## Output Policy

Skill outputs should be created as files by default, not pasted into chat.

- Documents, reports, manuals, and minutes: `.docx` or `.md`
- Tables, checklists, and survey summaries: `.xlsx` or `.csv`
- Training materials and slide outlines: `.pptx` or `.md`

Chat responses should only summarize the created files, their paths, and human-review points.

## Important distinction

- `harness/` defines how Codex should operate.
- `evals/` defines how outputs may be evaluated in the future.
- `tools/` contains repository maintenance utilities.

## Usage

```bash
git clone https://github.com/Yuya-Ishibashi0/hospital-workflow-codex-skills.git
cd hospital-workflow-codex-skills
codex
```

Use `$hospital-workflow-harness` as the primary entrypoint. It applies safety gates, selects the working mode and task Skill, determines file deliverables, and performs the final human-review handoff.

For user-level installation:

```bash
python3 tools/install_user_harness.py --dry-run
python3 tools/install_user_harness.py
```

Validate the harness with:

```bash
python3 tools/harness_doctor.py
```

## Maintenance

```bash
python3 tools/validate_skill_metadata.py
python3 tools/validate_skill_sections.py
python3 tools/generate_skill_index.py
```
