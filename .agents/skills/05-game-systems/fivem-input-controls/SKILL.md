---
name: fivem-input-controls
description: Design FiveM keyboard/controller input, command/key mapping, control disabling, focus interactions, hold/tap behavior, and conflict-safe cleanup.
---
# fivem-input-controls
## Purpose

Make controls configurable, reversible, and compatible with NUI focus/gameplay states.
## Workflow
1. Prefer registered commands/key mappings for user-configurable actions where suitable.
2. Centralize control state and enable/disable reasons.
3. Distinguish tap, hold, repeat, and continuous actions.
4. Coordinate NUI focus so controls are restored on close/error/stop.
5. Avoid globally disabling broad control sets unless necessary.
6. Document default bindings and conflicts.

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
- Do not hard-code inaccessible bindings without remapping path.
- Do not leave controls disabled after resource stop.
- Do not use per-frame input polling for events that command/key mapping can provide.

## Done criteria
- Bindings are configurable where appropriate.
- Focus/control cleanup works.
- Controller/keyboard behavior is intentional.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
