---
name: fivem-qbcore
description: 'Implement QBCore integrations for players, jobs, money, items, metadata, callbacks, vehicles, permissions, notifications, and lifecycle using the installed server version.'
---
# fivem-qbcore
## Purpose

Use QBCore APIs through a narrow adapter and validate all externally triggered economic/gameplay operations server-side.
## Workflow
1. Inspect installed QBCore version and local conventions.
2. Acquire core object using the project-supported pattern.
3. Normalize player/job/money/item operations behind adapter functions.
4. Use server callbacks/events with runtime payload validation.
5. Respect inventory/vehicle resource boundaries; use their APIs rather than direct table mutation where required.
6. Handle player loaded/unloaded lifecycle and missing player objects.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not assume every QBCore fork exposes identical APIs.
- Do not trust client-provided item/money/job data.
- Do not spread QBCore globals through domain modules.

## Done criteria
- Adapter matches installed APIs.
- Economy/inventory mutations are authoritative.
- Fork/version assumptions are documented.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. See `references/framework-sources.md` in this skill for QBCore documentation. When documentation and installed project code disagree, target the installed version.
