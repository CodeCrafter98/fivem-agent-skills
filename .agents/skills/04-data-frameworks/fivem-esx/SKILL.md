---
name: fivem-esx
description: 'Implement ESX integrations for xPlayer, jobs, accounts, inventory, callbacks, vehicles, permissions, notifications, and lifecycle using the installed ESX version.'
---
# fivem-esx
## Purpose

Use current ESX APIs through a contained adapter while accounting for differences among ESX versions/forks.
## Workflow
1. Inspect installed ESX version and initialization pattern.
2. Normalize xPlayer access and account/job/item operations behind adapter functions.
3. Use server-side validation around callbacks/events.
4. Use addon/inventory/vehicle APIs appropriate to the installed stack.
5. Avoid retaining stale xPlayer objects across disconnect/reload.
6. Document fork-specific behavior.

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
- Do not assume Legacy/fork APIs are identical.
- Do not trust client-provided economy or job claims.
- Do not directly edit framework-owned DB state unless explicitly documented as supported.

## Done criteria
- Adapter is version-aware.
- Player lifecycle is safe.
- Critical state changes remain server authoritative.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
