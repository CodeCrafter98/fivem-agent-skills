---
name: fivem-zones-raycasts
description: 'Implement spatial queries, zones, raycasts, shape tests, line-of-sight, proximity, and world targeting efficiently in FiveM.'
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

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

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

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
