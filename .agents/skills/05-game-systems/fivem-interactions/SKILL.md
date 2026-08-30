---
name: fivem-interactions
description: 'Design FiveM interaction systems using targets, zones, context actions, 3D prompts, entities, and keybinds with adapters for ox_target, qb-target, or custom implementations.'
---
# fivem-interactions
## Purpose

Keep interaction discovery client-local but validate privileged actions server-side.
## Workflow
1. Choose interaction modality based on density, precision, and accessibility.
2. Normalize target system behind an adapter when multi-framework portability matters.
3. Use entity/zone identifiers that can be removed deterministically.
4. Apply distance/role/availability predicates locally for UX and revalidate server-side for authority.
5. Avoid registering duplicate targets on resource restart/state change.
6. Provide fallback interaction when optional target dependency is unavailable if required.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not use client role predicates as security.
- Do not leak interaction registrations.
- Do not scan every world entity each frame.

## Done criteria
- Registration/removal is idempotent.
- Privileged actions are revalidated.
- Interaction cost scales with nearby content, not entire world.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
