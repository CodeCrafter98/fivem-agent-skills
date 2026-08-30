---
name: fivem-routing-buckets
description: 'Design and review routing bucket usage, population settings, entity lockdown modes, player/entity assignment, and instance teardown in OneSync.'
---
# fivem-routing-buckets
## Purpose

Use buckets as deliberate isolation domains with safe entry/exit and teardown.
## Workflow
1. Define bucket allocation and collision strategy.
2. Move required entities and players consistently.
3. Choose population enabled/disabled intentionally.
4. Choose lockdown mode intentionally, favoring stricter modes when clients should not create entities.
5. Define return-to-default behavior on disconnect/error/resource stop.
6. Delete or migrate bucket-owned entities during teardown.
7. Prevent cross-instance data/event leakage at application level.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not assume buckets provide authorization by themselves.
- Do not reuse bucket IDs without teardown/reconciliation.
- Do not strand players in non-default buckets after failure.

## Done criteria
- Instance lifecycle is complete.
- Security assumptions are explicit.
- Teardown restores players/entities safely.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
