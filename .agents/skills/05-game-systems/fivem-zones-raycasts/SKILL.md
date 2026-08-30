---
name: fivem-zones-raycasts
description: Implement spatial queries, zones, raycasts, shape tests, line-of-sight, proximity, and world targeting efficiently in FiveM.
---
# fivem-zones-raycasts
## Purpose

Use the cheapest spatial technique that satisfies interaction accuracy and run it at an appropriate cadence.
## Workflow
1. Use coarse proximity/zone checks before expensive raycasts when possible.
2. Choose raycast/shape test type and flags intentionally.
3. Handle asynchronous shape-test results correctly.
4. Filter self/irrelevant entities.
5. Cache stable zone geometry and avoid rebuilding it per tick.
6. Use adaptive sleep when the player is far from interactable areas.
7. Validate critical server actions independently of client hit results.

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
- Do not raycast multiple times per frame without measured need.
- Do not treat client raycast result as authorization.
- Do not keep stale entity hits without existence checks.

## Done criteria
- Spatial accuracy matches UX.
- Hot-loop cost is bounded.
- Critical actions remain authoritative.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
