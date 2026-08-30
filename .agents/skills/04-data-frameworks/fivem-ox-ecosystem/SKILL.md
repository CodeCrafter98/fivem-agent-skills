---
name: fivem-ox-ecosystem
description: 'Integrate ox_lib, ox_target, ox_inventory, and oxmysql deliberately in FiveM resources, using current APIs and avoiding unnecessary lock-in.'
---
# fivem-ox-ecosystem
## Purpose

Use ox components when they materially improve the resource and match the existing server stack.
## Workflow
1. Inspect which ox resources and versions are already present.
2. Use ox_lib modules for UI/callback/cache utilities only where they simplify established patterns.
3. Abstract target/inventory integration when portability matters.
4. Use oxmysql parameterization/transactions through the database layer.
5. Respect inventory ownership/metadata semantics rather than direct DB edits.
6. Provide graceful feature disablement when optional ox integrations are absent.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not introduce ox dependencies merely for convenience.
- Do not manipulate ox inventory tables directly.
- Do not mix multiple target/inventory systems without an adapter plan.

## Done criteria
- Dependencies are explicit.
- Integrations use current project APIs.
- Standalone/core behavior remains isolated when portability is a goal.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. See `references/framework-sources.md` in this skill for Overextended documentation. When documentation and installed project code disagree, target the installed version.
