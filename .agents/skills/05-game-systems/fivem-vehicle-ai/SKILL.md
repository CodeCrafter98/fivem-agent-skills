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

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

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

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
