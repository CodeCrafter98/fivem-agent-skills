---
name: fivem-onesync
description: 'Design OneSync-aware FiveM networking: server-created entities, network IDs, ownership migration, culling, routing buckets, population, synchronization, and large-player behavior.'
---
# fivem-onesync
## Purpose

Build networked systems that remain correct as players enter/leave scope and entity ownership changes.
## Workflow
1. Prefer server-created entities for authoritative/persistent shared entities when supported.
2. Pass network IDs across boundaries; resolve to local handles only where used.
3. Assume entities can leave scope and handles can disappear.
4. Avoid depending on a specific client retaining ownership.
5. Use routing buckets only for session/instance separation, not as a substitute for general dimension logic without design.
6. Choose entity lockdown mode intentionally for buckets when clients should not create entities.
7. Test with at least two clients and ownership migration for networked gameplay.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not assume all clients stream every entity.
- Do not store a client entity handle on the server as durable identity.
- Do not build correctness around a fixed owner.

## Done criteria
- Ownership migration is safe.
- Out-of-scope/re-entry behavior works.
- Server and clients agree on canonical entity identity/state.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. See `references/onesync-sources.md` in this skill for OneSync and state bag documentation. When documentation and installed project code disagree, target the installed version.
