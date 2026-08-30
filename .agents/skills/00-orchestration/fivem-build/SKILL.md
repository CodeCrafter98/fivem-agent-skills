---
name: fivem-build
description: 'Execute a production-minded BUILD workflow for a new FiveM feature or resource. Use when implementing new functionality end-to-end.'
---
# fivem-build
## Purpose

Coordinate design, implementation, integration, and verification for a new feature while keeping authority boundaries and runtime costs explicit.
## Workflow
1. Inspect the project and requirements.
2. Define acceptance criteria and authority/data-flow diagram.
3. Design resource/module boundaries and public contracts before implementation.
4. Implement the smallest vertical slice first.
5. Add server validation, lifecycle cleanup, NUI contracts, persistence, and framework adapters as required.
6. Run static checks, focused tests, restart/disconnect scenarios, security review, and performance checks.
7. Document configuration, dependencies, exports/events, and operational notes.

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
- Do not build speculative abstractions without a current use case.
- Do not accept client-supplied rewards/ownership/permissions as truth.
- Do not leave TODO placeholders in the requested production path.

## Done criteria
- Acceptance criteria are met.
- Feature survives resource restart and relevant disconnect/entity-loss cases.
- Security and performance risks are explicitly checked.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
