# AGENTS.md

This repository is a lightweight Codex agent harness for non-clinical hospital workflow improvement.

It is designed for Codex only. Do not add Claude Code, OpenCode, or other agent-runtime compatibility layers unless explicitly requested.

## Repository intent

This is not only a Codex Skills collection. It is an operating package that gives Codex:

- operating assumptions
- safety boundaries
- task routing rules
- skill selection guidance
- output contracts
- human review points
- reusable templates
- maintenance tools

The harness exists so Codex can support hospital workflow improvement tasks safely, consistently, and with clear limits.

## Required scope

- Work only on non-clinical hospital operations, administration, education, documentation, and workflow improvement.
- Support tasks such as duplicate-entry reduction, paper / Excel / Word transfer reduction, meeting summaries, proposal drafts, manuals, training materials, survey summaries, and operational documentation.
- Do not create patient-facing explanations, clinical records, handoff notes, diagnosis, treatment advice, medication decisions, or patient-specific medical guidance.
- Do not process patient personal information or electronic medical record contents.

## Safety rules

- Treat all outputs as drafts for human review.
- Create deliverables as files by default, not as long chat responses.
- Use `.docx`, `.xlsx`, `.pptx`, `.md`, or `.csv` according to the task. Chat responses should only summarize what was created and where it is saved.
- Never create fake Office files by renaming Markdown, text, or CSV files. Use the appropriate document, spreadsheet, or presentation generation capability and validate the resulting package.
- Treat generated deliverables as `review_pending` until a human has reviewed them.
- State assumptions when source information is incomplete.
- Preserve unknowns instead of inventing facts.
- Prefer low-risk, small-start improvements before complex automation.
- Consider safety, operational workload, maintainability, staff adoption, and local rules.
- Escalate to human review when legal, privacy, information security, vendor, or medical safety judgment is needed.

## Harness execution rules

- Automatically apply `hospital-workflow-harness` to every in-scope request about non-clinical hospital operations, even when the user does not name a Skill or use a `$` command.
- Never require non-technical users to select, remember, or type a Skill name.
- Treat ordinary Japanese requests such as "マニュアルを作って", "会議メモを整理して", or "業務を改善したい" as sufficient invocation.
- Select specialist Skills internally. Do not ask the user to choose a Skill unless they explicitly want to control the routing.
- If the user names a specialist Skill directly, still apply the scope gate, artifact policy, and human-review policy before completing the task.
- Do not create a deliverable when the request fails the non-clinical scope gate.
- For substantive work, create an `outputs/YYYYMMDD-task-name/` workspace with `task-brief.md` and `run.json`.
- Read the selected specialist Skill before execution; use no more than two supporting Skills unless the user explicitly requests otherwise.
- Validate generated artifacts before handoff.
- Leave the run in `review_pending` until a human confirms it.

## Repository structure rules

- Treat `skills/` as the canonical source for all Codex Skills.
- Keep `.agents/skills/` as a generated repo-local mirror.
- After changing `harness/` or `templates/`, run `python3 tools/sync_harness_bundle.py --write`.
- After changing any Skill or its bundle, run `python3 tools/sync_repo_skills.py --write`.
- Keep the Codex operating model and control layer under `harness/`.
- Keep reusable output templates under `templates/`.
- Keep generated working deliverables under `outputs/` unless the user specifies another path.
- Keep repository maintenance scripts under `tools/`.
- Keep future quality checks and regression cases under `evals/`.
- Do not put maintenance scripts or evaluation rubrics in `harness/`.

## Skill rules

Every Skill must include `SKILL.md` with YAML frontmatter containing `name` and `description`.

Skill bodies should include:

- Purpose
- When to use
- When not to use
- Inputs
- Process
- Output format
- Safety constraints
- Examples
- Escalation / human review notes

## Content rules

- Use Japanese as the primary language for hospital users.
- Use short English summaries only when useful for repository navigation.
- Use fictional, anonymized, non-clinical examples only.
- Do not include real patient information, real hospital names, or real staff names.
- If adding a new use case, first map it to an existing Skill before creating a new Skill.
