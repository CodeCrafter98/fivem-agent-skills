---
name: fivem-qbox
description: Implement FiveM integrations for current Qbox/QBX conventions, players, jobs, groups, money, callbacks, metadata, vehicles, inventory bridges, and framework lifecycle.
---
# fivem-qbox
## Purpose

Use Qbox public APIs/exports and preserve Qbox-owned invariants rather than modifying core internals.
## Workflow
1. Inspect installed Qbox version and resources before assuming API availability.
2. Use supported exports/functions for player/group/money operations.
3. Use framework events only for documented lifecycle/integration points.
4. Keep Qbox specifics inside an adapter/service boundary.
5. Respect Qbox guidance not to mutate core database tables directly when an API owns the invariant.
6. Handle player unload/resource restart cleanly.

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
- Do not edit Qbox core for resource-specific behavior.
- Do not use deprecated compatibility APIs when current Qbox APIs are available.
- Do not store framework player objects long-term.

## Done criteria
- Qbox calls are version-appropriate.
- No core DB invariant is bypassed.
- Adapter cleanup/reload behavior works.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
