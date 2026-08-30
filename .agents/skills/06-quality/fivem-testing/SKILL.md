---
name: fivem-testing
description: 'Test FiveM resources with static checks, pure-Lua unit tests, frontend tests, integration tests, in-game multi-client scenarios, restart/disconnect cases, and regression matrices.'
---
# fivem-testing
## Purpose

Use layered testing because not every GTA runtime behavior is unit-testable outside FiveM.
## Workflow
1. Run syntax/lint/type/build checks for Lua/TS/UI.
2. Extract deterministic business logic into pure functions and unit test it.
3. Test NUI transport/schema functions independently where possible.
4. Test DB repositories against disposable/test schema when available.
5. Define in-game scenarios for join/leave, resource restart, entity loss, ownership migration, latency, cancellation, and permissions.
6. For networked systems, use at least two clients for ownership/scope cases.
7. Record expected observations and pass/fail evidence.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not call a feature tested because it compiles.
- Do not require GTA runtime for logic that can be pure-unit-tested.
- Do not skip negative/abuse paths for server endpoints.

## Done criteria
- Critical acceptance paths have tests/checks.
- Restart/disconnect paths are covered when relevant.
- Security negative cases are included for valuable operations.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
