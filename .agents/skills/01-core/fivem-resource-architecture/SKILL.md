---
name: fivem-resource-architecture
description: Design and review FiveM resource architecture, fxmanifest metadata, module boundaries, exports, dependencies, lifecycle, configuration, and multi-resource composition.
---
# fivem-resource-architecture
## Purpose

Create cohesive resources with explicit public contracts and minimal coupling.
## Workflow
1. Use `fxmanifest.lua`; keep manifest declarative and minimal.
2. Separate client, server, shared, configuration, UI, and adapters by responsibility.
3. Prefer internal modules/services over globally exposed events for same-resource calls.
4. Expose exports/events only as intentional public API.
5. Declare dependencies explicitly when startup order matters.
6. Plan resource start/stop behavior, cleanup, and idempotent initialization.
7. Avoid circular dependencies; introduce a small interface/adapter boundary instead.
8. Version public contracts when external resources consume them.

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
- Do not use `lua54 'yes'`.
- Do not put secrets or privileged logic in shared/client files.
- Do not create a monolithic `client.lua`/`server.lua` once responsibilities become distinct.

## Done criteria
- Manifest is valid and complete.
- Public API and dependencies are explicit.
- Start/stop/restart behavior is safe.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
