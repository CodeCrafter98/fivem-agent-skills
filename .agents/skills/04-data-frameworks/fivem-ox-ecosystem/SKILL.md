---
name: fivem-ox-ecosystem
description: 'Integrate ox_lib, ox_target, ox_inventory, and oxmysql deliberately in FiveM resources, using current APIs and avoiding unnecessary lock-in.'
---
# fivem-ox-ecosystem
## Purpose

Use ox components when they materially improve the resource and match the existing server stack.
## Workflow
1. Inspect which ox resources and versions are already present.
2. Use ox_lib modules for UI/callback/cache utilities only where they simplify established patterns.
3. Abstract target/inventory integration when portability matters.
4. Use oxmysql parameterization/transactions through the database layer.
5. Respect inventory ownership/metadata semantics rather than direct DB edits.
6. Provide graceful feature disablement when optional ox integrations are absent.

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
- Do not introduce ox dependencies merely for convenience.
- Do not manipulate ox inventory tables directly.
- Do not mix multiple target/inventory systems without an adapter plan.

## Done criteria
- Dependencies are explicit.
- Integrations use current project APIs.
- Standalone/core behavior remains isolated when portability is a goal.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
