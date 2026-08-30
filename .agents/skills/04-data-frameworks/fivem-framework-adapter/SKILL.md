---
name: fivem-framework-adapter
description: Keep FiveM resources portable across standalone, Qbox, QBCore, ESX, or custom frameworks using narrow adapter interfaces and capability detection.
---
# fivem-framework-adapter
## Purpose

Separate domain/gameplay logic from framework-specific player, job, money, item, notification, and callback APIs.
## Workflow
1. Define a framework-neutral interface based on actual needed capabilities.
2. Keep detection/bootstrapping in one adapter layer.
3. Implement one adapter per supported framework.
4. Return normalized domain objects instead of leaking framework player objects.
5. Fail clearly when a required capability is unavailable.
6. Prefer optional integrations over hard dependencies when feasible.
7. Test the core with a fake/standalone adapter.

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
- Do not branch `if ESX ... elseif QBCore ...` throughout domain code.
- Do not call deprecated compatibility APIs when native framework APIs exist.
- Do not pretend frameworks have identical transaction/identity semantics.

## Done criteria
- Core logic has no unnecessary framework imports.
- Adapters expose consistent capabilities.
- Unsupported combinations fail explicitly.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
