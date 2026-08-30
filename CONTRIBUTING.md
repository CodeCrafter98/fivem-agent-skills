# Contributing to FiveM Agent Skills

Thank you for your interest in improving FiveM Agent Skills! This toolkit relies on community expertise to ensure AI coding agents make sound engineering decisions.

## High-Value Contributions

We particularly welcome:
- Corrections to outdated FiveM behavior or native documentation
- New regression evals that capture recurring AI mistakes
- Improved security patterns and exploit mitigation
- Improved OneSync and state bag guidance
- Framework compatibility updates (Qbox, QBCore, ESX, ox)
- New deterministic analysis tools (`scripts/*.py`)
- Missing specialist skills

## Adding a New Skill

A new skill should solve a specific engineering problem rather than duplicate generic instructions.

1. **Focus:** Avoid giant catch-all skills. Prefer a focused specialist.
2. **Structure:** Create a directory under the appropriate domain in `.agents/skills/`.
3. **SKILL.md:** Must contain valid YAML frontmatter with `name` and `description` (description must be single-quoted if it contains colons).
4. **Required sections:** Include `## Purpose`, `## Workflow`, `## Standalone safety`, `## Done criteria`, and `## Output contract`.
5. **Portability:** If you reference official docs, create a `references/` directory in your skill and include a small markdown file with the links. Do not point to global reference files.
6. **Manifest:** Add the new skill to `skills-manifest.json` and increment `skill_count`.

## Making Changes to Existing Skills

When modifying existing skills:
- **Do not add large duplicated blocks** (e.g., repeating the entire `AGENTS.md` content). Keep skills concise.
- **Ensure standalone safety:** Each skill should retain the critical invariants (untrusted input, no inventing APIs, verification).
- **Run the validator:** Always run `python scripts/validate_skills.py` before submitting a PR.

## Evals

If you are fixing a recurring agent failure, please consider adding a regression eval in `evals/cases/`.
An eval is a simple JSON file containing:
- `prompt`: The user request that triggers the failure
- `expected_skills`: The skills the router should select
- `assertions`: What the agent must do correctly
- `forbidden_patterns`: What the agent must avoid

## Pull Request Process

1. Create a branch for your feature/fix.
2. Ensure `python scripts/validate_skills.py` passes completely.
3. Open a Pull Request using the provided template.
4. Maintainers will review the engineering advice for safety and accuracy.
