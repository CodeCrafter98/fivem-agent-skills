---
name: fivem-compatibility
description: Assess FiveM compatibility across server artifacts/game builds, GTA5 legacy/enhanced considerations, OneSync modes, frameworks, dependencies, and resource versions.
---
# fivem-compatibility
## Purpose

State explicit support boundaries and avoid accidental reliance on environment-specific behavior.
## Workflow
1. Inspect current target artifact/build/framework/dependency versions.
2. Verify natives/features against target game/runtime when version-sensitive.
3. Test optional dependencies absent/present as designed.
4. Document required OneSync or routing behavior.
5. Use feature/capability detection where practical.
6. Provide migration notes for breaking dependency/API changes.
7. Avoid broad compatibility claims without test evidence.

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
- Do not promise support for untested forks/builds.
- Do not add legacy compatibility code that harms current runtime without a requirement.
- Do not suppress dependency version errors.

## Done criteria
- Supported matrix is explicit.
- Unsupported environments fail clearly.
- Version-specific branches are isolated and documented.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
