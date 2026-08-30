---
name: fivem-cfxlua
description: 'Write and review modern CfxLua for FiveM using Lua 5.4 semantics, Cfx extensions, coroutine/thread patterns, efficient tables, vectors, errors, and hot-path discipline.'
---
# fivem-cfxlua
## Purpose

Produce idiomatic, allocation-conscious Lua that fits FiveM runtime semantics rather than generic Lua-only patterns.
## Workflow
1. Use locals aggressively for scoped state and frequently referenced functions when it improves hot paths.
2. Choose `CreateThread`, `Wait`, timeouts, promises, and events based on actual scheduling needs.
3. Prefer event-driven or adaptive-sleep loops over unconditional frame polling.
4. Use Cfx vector/quaternion support where it simplifies spatial logic.
5. Keep mutation ownership clear; avoid hidden globals.
6. Handle nil/deleted entities and resource shutdown explicitly.
7. For CPU-heavy pure logic, isolate functions so they can be unit tested outside GTA runtime.

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
- Do not add Lua 5.3 compatibility workarounds without evidence.
- Do not busy-loop.
- Do not allocate large temporary tables every frame.
- Do not swallow errors that indicate invariant violations.

## Done criteria
- Code targets current CfxLua.
- Thread cadence matches gameplay need.
- Hot paths avoid unnecessary native calls/allocations.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
