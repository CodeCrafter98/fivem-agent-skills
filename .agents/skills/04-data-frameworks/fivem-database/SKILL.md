---
name: fivem-database
description: 'Design FiveM persistence with oxmysql or project-specific database libraries: queries, prepared parameters, repositories, transactions, indexes, migrations, caching, and failure handling.'
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

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

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

Prefer project source and authoritative documentation over memory for version-sensitive APIs. See `references/framework-sources.md` in this skill for oxmysql documentation. When documentation and installed project code disagree, target the installed version.
