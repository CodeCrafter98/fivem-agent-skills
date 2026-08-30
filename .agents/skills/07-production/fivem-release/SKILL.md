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

## Non-negotiable engineering rules

- Treat every client and NUI payload as untrusted input. Security-sensitive state is server authoritative.
- Target current CfxLua / Lua 5.4. Do not add `lua54 'yes'`; it is deprecated and unnecessary.
- Prefer `fxmanifest.lua` with `fx_version 'cerulean'` for modern resources unless compatibility evidence requires otherwise.
- Never invent natives, exports, events, framework APIs, SQL columns, or configuration keys. Verify uncertain APIs against project code or authoritative documentation.
- Keep client, server, shared, UI, persistence, and framework-adapter responsibilities explicit.
- Minimize polling and frame loops. `Wait(0)` is reserved for work that genuinely must execute every rendered frame.
- Across network boundaries, use network-safe identifiers and validate existence/ownership/state before mutation.
- Design every entity workflow for create → network/own → use → migration → cleanup/delete, including resource stop and player disconnect.
- NUI callbacks must always return a response; use JSON-encodable contracts and explicit error shapes.
- Prefer small, typed/validated event payloads over large replicated blobs or implicit shared state.
- Do not refactor unrelated code during a focused fix. Preserve existing architecture unless a change is necessary and justified.
- Completion means verification: syntax/static checks, relevant tests, runtime/restart cases, security review, and performance checks proportional to the change.

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

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
