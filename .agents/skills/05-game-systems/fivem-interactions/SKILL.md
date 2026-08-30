---
name: fivem-interactions
description: Design FiveM interaction systems using targets, zones, context actions, 3D prompts, entities, and keybinds with adapters for ox_target, qb-target, or custom implementations.
---
# fivem-interactions
## Purpose

Keep interaction discovery client-local but validate privileged actions server-side.
## Workflow
1. Choose interaction modality based on density, precision, and accessibility.
2. Normalize target system behind an adapter when multi-framework portability matters.
3. Use entity/zone identifiers that can be removed deterministically.
4. Apply distance/role/availability predicates locally for UX and revalidate server-side for authority.
5. Avoid registering duplicate targets on resource restart/state change.
6. Provide fallback interaction when optional target dependency is unavailable if required.

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
- Do not use client role predicates as security.
- Do not leak interaction registrations.
- Do not scan every world entity each frame.

## Done criteria
- Registration/removal is idempotent.
- Privileged actions are revalidated.
- Interaction cost scales with nearby content, not entire world.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
