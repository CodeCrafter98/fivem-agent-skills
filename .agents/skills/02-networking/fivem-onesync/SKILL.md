---
name: fivem-onesync
description: 'Design OneSync-aware FiveM networking: server-created entities, network IDs, ownership migration, culling, routing buckets, population, synchronization, and large-player behavior.'
---
# fivem-onesync
## Purpose

Build networked systems that remain correct as players enter/leave scope and entity ownership changes.
## Workflow
1. Prefer server-created entities for authoritative/persistent shared entities when supported.
2. Pass network IDs across boundaries; resolve to local handles only where used.
3. Assume entities can leave scope and handles can disappear.
4. Avoid depending on a specific client retaining ownership.
5. Use routing buckets only for session/instance separation, not as a substitute for general dimension logic without design.
6. Choose entity lockdown mode intentionally for buckets when clients should not create entities.
7. Test with at least two clients and ownership migration for networked gameplay.

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
- Do not assume all clients stream every entity.
- Do not store a client entity handle on the server as durable identity.
- Do not build correctness around a fixed owner.

## Done criteria
- Ownership migration is safe.
- Out-of-scope/re-entry behavior works.
- Server and clients agree on canonical entity identity/state.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
