---
name: fivem-database
description: Design FiveM persistence with oxmysql or project-specific database libraries: queries, prepared parameters, repositories, transactions, indexes, migrations, caching, and failure handling.
---
# fivem-database
## Purpose

Keep persistence server-only, safe, efficient, and isolated behind a small data-access layer.
## Workflow
1. Identify the project database library and existing query conventions.
2. Use parameterized queries; never concatenate untrusted SQL values.
3. Place SQL behind repository/service functions rather than scattered handlers.
4. Use transactions for multi-row/multi-step invariants.
5. Add indexes based on actual lookup/join patterns.
6. Avoid N+1 queries and DB calls inside hot/tick loops.
7. Make migrations reversible or safely forward-only with documented backup implications.
8. Define cache invalidation and stale-data tolerance when caching.

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
- Do not access SQL from client/NUI.
- Do not directly mutate framework-owned core tables when framework APIs are required.
- Do not hide database failures by returning empty success.

## Done criteria
- Queries are parameterized.
- Transactions preserve invariants.
- Migration and indexes match access patterns.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
