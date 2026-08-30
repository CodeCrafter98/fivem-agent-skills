---
name: fivem-server-authority
description: 'Design secure server-authoritative FiveM logic for permissions, economy, inventory, ownership, proximity, cooldowns, state mutation, spawning, and validation.'
---
# fivem-server-authority
## Purpose

Treat clients as untrusted requesters and make the server the source of truth for valuable or shared state.
## Workflow
1. Define what the server can independently verify for each request.
2. Validate source/player/session existence and permission.
3. Validate identifiers, ownership, state transitions, quantities, ranges, coordinates/proximity, and cooldowns as applicable.
4. Derive prices/rewards/roles from server-owned configuration/database, not client payloads.
5. Use transactions/locks/idempotency for multi-step valuable operations.
6. Return explicit success/error results instead of silent mutation.
7. Log security-relevant denials without leaking secrets.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Never trust client money, inventory, job, permission, reward, price, or ownership claims.
- Do not rely on obscured event names as security.
- Do not perform non-idempotent operations twice on retry.

## Done criteria
- Every critical mutation has server validation.
- Race/replay behavior is defined.
- Failure leaves state consistent.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
