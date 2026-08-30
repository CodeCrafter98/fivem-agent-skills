---
name: fivem-vehicles
description: 'Implement robust FiveM vehicle systems: creation, persistence, seats, doors, engine, damage, mods, extras, liveries, trailers, towing, ownership, synchronization, and cleanup.'
---
# fivem-vehicles
## Purpose

Treat vehicles as networked lifecycle objects with validated ownership and bounded native work.
## Workflow
1. Decide whether vehicle is local, temporary networked, or persistent server-owned.
2. Load model with timeout and validity checks.
3. Create at safe coordinates/heading and obtain stable NetID where networked.
4. Apply properties in a deterministic order; normalize serialization format.
5. Validate ownership/permission server-side for valuable operations.
6. Handle driver/passenger transitions and ownership migration.
7. Delete/cleanup on explicit lifecycle and reconcile persistent vehicles on restart.

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
- Do not trust client vehicle properties as ownership proof.
- Do not continuously reapply handling/properties every frame.
- Do not leak temporary vehicles.

## Done criteria
- Spawn/property flow is deterministic.
- Ownership and persistence are validated.
- Cleanup/restart behavior is correct.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
