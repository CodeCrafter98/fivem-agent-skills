---
name: fivem-qbox
description: 'Implement FiveM integrations for current Qbox/QBX conventions, players, jobs, groups, money, callbacks, metadata, vehicles, inventory bridges, and framework lifecycle.'
---
# fivem-qbox
## Purpose

Use Qbox public APIs/exports and preserve Qbox-owned invariants rather than modifying core internals.
## Workflow
1. Inspect installed Qbox version and resources before assuming API availability.
2. Use supported exports/functions for player/group/money operations.
3. Use framework events only for documented lifecycle/integration points.
4. Keep Qbox specifics inside an adapter/service boundary.
5. Respect Qbox guidance not to mutate core database tables directly when an API owns the invariant.
6. Handle player unload/resource restart cleanly.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not edit Qbox core for resource-specific behavior.
- Do not use deprecated compatibility APIs when current Qbox APIs are available.
- Do not store framework player objects long-term.

## Done criteria
- Qbox calls are version-appropriate.
- No core DB invariant is bypassed.
- Adapter cleanup/reload behavior works.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. See `references/framework-sources.md` in this skill for Qbox documentation. When documentation and installed project code disagree, target the installed version.
