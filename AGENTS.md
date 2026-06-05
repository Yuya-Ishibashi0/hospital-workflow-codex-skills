# AGENTS.md

This repository provides Codex Skills for non-clinical hospital workflows in Japanese hospital contexts.

## Repository rules

- Keep all Codex Skills under `.agents/skills/`.
- Every skill must include a `SKILL.md` file with YAML frontmatter containing `name` and `description`.
- Each skill should include clear scope, trigger conditions, inputs, outputs, safety constraints, examples, and references.
- Do not create or modify skills for diagnosis, treatment decisions, patient-specific medical advice, clinical documentation, patient handoffs, or patient explanation documents.
- Do not include real patient information in examples.
- Use fictional, anonymized, non-clinical examples only.
- Prefer Japanese content for healthcare users, with short English summaries where useful.
- If you modify a skill, update related examples, references, and harness cases when appropriate.
- If you add a new use case, map it to one or more existing skills instead of creating a new skill by default.
- Keep skills focused on one job.
- Do not add web apps, Docker, local LLM environments, API integrations, or EHR integrations in the initial version.

