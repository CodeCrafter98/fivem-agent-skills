---
name: fivem-peds-ai
description: 'Build FiveM ped AI with task sequences, follow/escort/guard/combat/flee/scenario behavior, relationships, animations, perception, networking, and cleanup.'
---
# fivem-peds-ai
## Purpose

Use native task systems and relationship configuration while accounting for network ownership and task interruption.
## Workflow
1. Define ped ownership/persistence.
2. Load model/animations safely.
3. Configure relationship groups and combat/flee attributes intentionally.
4. Use task sequences for multi-step behavior where suitable.
5. Supervise at a modest cadence for death/stuck/target loss.
6. Handle player proximity, scope/ownership migration, and cancellation.
7. Clean relationship/task/entity state on teardown.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not issue tasks every frame.
- Do not assume a task remains active after ownership migration.
- Do not create uncontrolled ambient ped counts.

## Done criteria
- Behavior is interruptible/recoverable.
- Network migration does not corrupt state.
- Entity/task cleanup is complete.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
