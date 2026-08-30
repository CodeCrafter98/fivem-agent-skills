---
name: fivem-entity-lifecycle
description: 'Manage FiveM entity lifecycle reliably across model loading, creation, networking, ownership, persistence, migration, deletion, resource stop, and player disconnect.'
---
# fivem-entity-lifecycle
## Purpose

Prevent leaked, orphaned, duplicated, or stale entities and NetIDs.
## Workflow
1. Define who creates and who is allowed to delete each entity.
2. Record stable identifiers separately from transient local handles.
3. Guard all operations with existence checks appropriate to context.
4. Handle spawn failure/model timeout.
5. Handle ownership migration and scope loss.
6. Clean entities on cancellation, resource stop, session teardown, and invalid owner cases as designed.
7. Make cleanup idempotent so repeated calls are safe.

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
- Do not assume DeleteEntity always succeeds immediately across network ownership boundaries.
- Do not retain stale handles after deletion/scope loss.
- Do not respawn duplicates after resource restart without reconciliation.

## Done criteria
- No orphaned entities remain.
- Cleanup is idempotent.
- Restart/reconnect does not duplicate persistent objects.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
