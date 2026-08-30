---
name: fivem-qbcore
description: 'Implement QBCore integrations for players, jobs, money, items, metadata, callbacks, vehicles, permissions, notifications, and lifecycle using the installed server version.'
---
# fivem-qbcore
## Purpose

Use QBCore APIs through a narrow adapter and validate all externally triggered economic/gameplay operations server-side.
## Workflow
1. Inspect installed QBCore version and local conventions.
2. Acquire core object using the project-supported pattern.
3. Normalize player/job/money/item operations behind adapter functions.
4. Use server callbacks/events with runtime payload validation.
5. Respect inventory/vehicle resource boundaries; use their APIs rather than direct table mutation where required.
6. Handle player loaded/unloaded lifecycle and missing player objects.

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
- Do not assume every QBCore fork exposes identical APIs.
- Do not trust client-provided item/money/job data.
- Do not spread QBCore globals through domain modules.

## Done criteria
- Adapter matches installed APIs.
- Economy/inventory mutations are authoritative.
- Fork/version assumptions are documented.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
