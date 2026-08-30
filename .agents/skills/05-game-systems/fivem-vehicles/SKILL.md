---
name: fivem-vehicles
description: 'Implement robust FiveM vehicle systems: creation, persistence, seats, doors, engine, damage, mods, extras, liveries, trailers, towing, ownership, synchronization, and cleanup.'
---
# fivem-vehicles
## Purpose

Treat vehicles as networked lifecycle objects with validated ownership and bounded native work.
## Workflow
1. Decide whether vehicle is local, temporary networked, or persistent server-owned.
2. Load model with timeout and validity checks.
3. Create at safe coordinates/heading and obtain stable NetID where networked.
4. Apply properties in a deterministic order; normalize serialization format.
5. Validate ownership/permission server-side for valuable operations.
6. Handle driver/passenger transitions and ownership migration.
7. Delete/cleanup on explicit lifecycle and reconcile persistent vehicles on restart.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not trust client vehicle properties as ownership proof.
- Do not continuously reapply handling/properties every frame.
- Do not leak temporary vehicles.

## Done criteria
- Spawn/property flow is deterministic.
- Ownership and persistence are validated.
- Cleanup/restart behavior is correct.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
