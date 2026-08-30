---
name: fivem-server-authority
description: Design secure server-authoritative FiveM logic for permissions, economy, inventory, ownership, proximity, cooldowns, state mutation, spawning, and validation.
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

## Non-negotiable engineering rules

- Treat every client and NUI payload as untrusted input. Security-sensitive state is server authoritative.
- Target current CfxLua / Lua 5.4. Do not add `lua54 'yes'`; it is deprecated and unnecessary.
- Prefer `fxmanifest.lua` with `fx_version 'cerulean'` for modern resources unless compatibility evidence requires otherwise.
- Never invent natives, exports, events, framework APIs, SQL columns, or configuration keys. Verify uncertain APIs against project code or authoritative documentation.
- Keep client, server, shared, UI, persistence, and framework-adapter responsibilities explicit.
- Minimize polling and frame loops. `Wait(0)` is reserved for work that genuinely must execute every rendered frame.
- Across network boundaries, use network-safe identifiers and validate existence/ownership/state before mutation.
- Design every entity workflow for create → network/own → use → migration → cleanup/delete, including resource stop and player disconnect.
- NUI callbacks must always return a response; use JSON-encodable contracts and explicit error shapes.
- Prefer small, typed/validated event payloads over large replicated blobs or implicit shared state.
- Do not refactor unrelated code during a focused fix. Preserve existing architecture unless a change is necessary and justified.
- Completion means verification: syntax/static checks, relevant tests, runtime/restart cases, security review, and performance checks proportional to the change.

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

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
