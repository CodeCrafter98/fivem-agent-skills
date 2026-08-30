---
name: fivem-documentation
description: 'Write operator and developer documentation for FiveM resources: installation, dependencies, configuration, permissions, events/exports, database, UI build, troubleshooting, security, and upgrade guidance.'
---
# fivem-documentation
## Purpose

Document the stable contract and operational behavior, not implementation trivia.
## Workflow
1. Include prerequisites and supported environment matrix.
2. Document install/start order and config with safe examples.
3. Document public exports/events/callbacks with direction, payload, result, and authority notes.
4. Document database migrations/backups.
5. Document NUI build workflow if source is shipped.
6. Document common errors and diagnostic commands.
7. Document security assumptions and which values are server authoritative.

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
- Do not expose secrets in examples.
- Do not document internal implementation as guaranteed API.
- Do not claim tested compatibility without evidence.

## Done criteria
- A new operator can install and configure resource.
- A developer can integrate via documented contracts.
- Troubleshooting covers known failure surfaces.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
