---
name: fivem-client-gameplay
description: 'Implement FiveM client gameplay systems: player/ped/vehicle interaction, cameras, animations, props, blips, markers, particles, audio, controls, and local presentation logic.'
---
# fivem-client-gameplay
## Purpose

Keep the client responsive and presentation-focused while delegating trusted state changes to the server.
## Workflow
1. Separate input/presentation from authoritative decisions.
2. Use proximity/adaptive loops for world interactions.
3. Manage model/anim/ptfx loading with timeouts and cleanup.
4. Handle player death, ped change, teleport, resource restart, and entity loss when relevant.
5. Keep cameras/focus/input state reversible.
6. Batch or throttle UI updates generated from gameplay state.
7. Send requests to server with minimal evidence; let server revalidate critical facts.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not grant money/items/permissions client-side.
- Do not leave controls/focus/cameras stuck after cancel/error/stop.
- Do not run expensive scans every frame.

## Done criteria
- Gameplay feels responsive.
- Cleanup is complete.
- Authoritative mutations are server validated.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
