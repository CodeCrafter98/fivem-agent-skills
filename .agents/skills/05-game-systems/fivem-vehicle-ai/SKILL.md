---
name: fivem-vehicle-ai
description: 'Build FiveM vehicle AI for following, escort, convoy, pathfinding, driving styles, speed/gap control, recovery, obstruction handling, and player/AI handover.'
---
# fivem-vehicle-ai
## Purpose

Prefer GTA task natives for baseline driving and layer lightweight supervisory logic on top instead of fighting vehicle physics every frame.
## Workflow
1. Define leader/target identity using network-safe references.
2. Choose appropriate driving task and documented driving-style flags.
3. Use desired speed and following distance with hysteresis rather than constant micro-corrections.
4. Detect stalled/stuck/off-route states on a low-frequency supervisor loop.
5. Implement bounded recovery escalation: retask → reposition only if safe/allowed → fail gracefully.
6. Handle target deletion, scope loss, driver death, player takeover, and ownership migration.
7. Measure CPU/native-call cost with multiple AI vehicles.

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
- Do not set steering/velocity/coordinates every frame unless the design explicitly requires custom physics.
- Do not teleport vehicles as the first recovery strategy.
- Do not assume pathfinding can reach every surface.

## Done criteria
- Convoy remains stable under normal latency.
- Recovery is bounded and safe.
- AI cleans up or hands over predictably.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
