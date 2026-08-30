---
name: fivem-release
description: 'Prepare FiveM resources for release: versioning, changelog, migrations, dependency checks, build artifacts, packaging, upgrade notes, rollback, and release verification.'
---
# fivem-release
## Purpose

Ship reproducible, reviewable releases that operators can upgrade safely.
## Workflow
1. Choose semantic version impact based on public API/config/schema changes.
2. Build NUI production assets and verify manifest file paths.
3. Run skill/package validator and project tests.
4. Bundle migrations and document order/backup requirements.
5. Update changelog, compatibility matrix, configuration reference, and public exports/events.
6. Verify clean install and upgrade from previous supported version when feasible.
7. Define rollback limits, especially after destructive migrations.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not publish dev dependencies/source maps/secrets unintentionally.
- Do not change public event/export behavior without release notes.
- Do not call a migration reversible if it loses data.

## Done criteria
- Package starts cleanly.
- Upgrade notes are complete.
- Version/changelog match actual compatibility impact.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
