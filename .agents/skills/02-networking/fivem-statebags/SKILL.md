---
name: fivem-statebags
description: Use FiveM state bags efficiently and safely for replicated entity/player/global attributes, including ownership, replication direction, change handlers, namespacing, and serialization cost.
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

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
