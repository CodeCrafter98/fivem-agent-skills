---
name: fivem-ui-design
description: 'Design premium, game-first FiveM UI/UX for HUDs, menus, MDTs, phones, inventories, garages, dispatch, vehicle controls, admin tools, and custom interfaces.'
---
# fivem-ui-design
## Purpose

Create polished interfaces that feel native to the game, preserve gameplay visibility, and remain fast under CEF.
## Workflow
1. Start from interaction goal, frequency, urgency, and whether gameplay continues underneath.
2. Use strong hierarchy, compact density, readable typography, tabular numerals for telemetry, and restrained effects.
3. Protect the gameplay focal area; avoid oversized SaaS-style cards and excessive modal stacking.
4. Design keyboard/controller escape paths and clear focus states.
5. Use motion for state/orientation feedback, not decoration alone.
6. Plan loading/empty/error/disabled/permission states.
7. Respect 16:9, ultrawide, high-DPI, safe edges, and scalable text.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not imitate copyrighted branded UI pixel-for-pixel unless authorized.
- Do not trade readability for glass/blur effects.
- Do not animate high-frequency telemetry with expensive layout thrashing.

## Done criteria
- Core tasks are reachable with few actions.
- All application states are designed.
- Visual polish does not compromise CEF performance or gameplay.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
