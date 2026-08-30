---
name: fivem-esx
description: 'Implement ESX integrations for xPlayer, jobs, accounts, inventory, callbacks, vehicles, permissions, notifications, and lifecycle using the installed ESX version.'
---
# fivem-esx
## Purpose

Use current ESX APIs through a contained adapter while accounting for differences among ESX versions/forks.
## Workflow
1. Inspect installed ESX version and initialization pattern.
2. Normalize xPlayer access and account/job/item operations behind adapter functions.
3. Use server-side validation around callbacks/events.
4. Use addon/inventory/vehicle APIs appropriate to the installed stack.
5. Avoid retaining stale xPlayer objects across disconnect/reload.
6. Document fork-specific behavior.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not assume Legacy/fork APIs are identical.
- Do not trust client-provided economy or job claims.
- Do not directly edit framework-owned DB state unless explicitly documented as supported.

## Done criteria
- Adapter is version-aware.
- Player lifecycle is safe.
- Critical state changes remain server authoritative.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. See `references/framework-sources.md` in this skill for ESX documentation. When documentation and installed project code disagree, target the installed version.
