---
name: fivem-testing
description: Test FiveM resources with static checks, pure-Lua unit tests, frontend tests, integration tests, in-game multi-client scenarios, restart/disconnect cases, and regression matrices.
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

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
