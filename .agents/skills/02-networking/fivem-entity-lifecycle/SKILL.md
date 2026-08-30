---
name: fivem-entity-lifecycle
description: 'Manage FiveM entity lifecycle reliably across model loading, creation, networking, ownership, persistence, migration, deletion, resource stop, and player disconnect.'
---
# fivem-entity-lifecycle
## Purpose

Prevent leaked, orphaned, duplicated, or stale entities and NetIDs.
## Workflow
1. Define who creates and who is allowed to delete each entity.
2. Record stable identifiers separately from transient local handles.
3. Guard all operations with existence checks appropriate to context.
4. Handle spawn failure/model timeout.
5. Handle ownership migration and scope loss.
6. Clean entities on cancellation, resource stop, session teardown, and invalid owner cases as designed.
7. Make cleanup idempotent so repeated calls are safe.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not assume DeleteEntity always succeeds immediately across network ownership boundaries.
- Do not retain stale handles after deletion/scope loss.
- Do not respawn duplicates after resource restart without reconciliation.

## Done criteria
- No orphaned entities remain.
- Cleanup is idempotent.
- Restart/reconnect does not duplicate persistent objects.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
