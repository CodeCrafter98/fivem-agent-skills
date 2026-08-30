---
name: fivem-statebags
description: 'Use FiveM state bags efficiently and safely for replicated entity/player/global attributes, including ownership, replication direction, change handlers, namespacing, and serialization cost.'
---
# fivem-statebags
## Purpose

Represent small replicated facts, not arbitrary application databases, in state bags.
## Workflow
1. Choose Player/Entity/GlobalState based on ownership and audience.
2. Use flat/namespaced keys rather than deep nested mutation.
3. Keep values compact and JSON/serialization friendly.
4. Define which side may write each key and whether writes replicate.
5. Use change handlers for reactions instead of polling when appropriate.
6. Avoid high-frequency state bag churn for telemetry that can be local or batched.
7. Treat replicated state as observable, not secret.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not store secrets in state bags.
- Do not continuously rewrite large nested tables.
- Do not use state bags as authoritative proof of client-owned facts without server validation.

## Done criteria
- Keys have owners and meanings.
- Update frequency is bounded.
- Change-handler cleanup and entity disappearance are handled.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. See `references/onesync-sources.md` in this skill for state bag documentation. When documentation and installed project code disagree, target the installed version.
