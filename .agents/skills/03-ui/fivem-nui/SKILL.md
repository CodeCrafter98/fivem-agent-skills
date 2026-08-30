---
name: fivem-nui
description: Build and review FiveM fullscreen NUI using CEF, `ui_page`, resource files, focus, messages, callbacks, development tooling, responsive layout, and safe teardown.
---
# fivem-nui
## Purpose

Create game-native interfaces that load reliably, release focus correctly, and communicate through explicit contracts.
## Workflow
1. Declare `ui_page` and all packaged UI assets in `fxmanifest.lua`.
2. Use the secure `https://cfx-nui-<resource>/...` resource scheme where needed.
3. Centralize open/close/focus behavior and always release focus on close/error/resource stop.
4. Use `SendNUIMessage` for client→UI messages with small event envelopes.
5. Use NUI callbacks for UI→client requests; always return a response.
6. Keep the UI functional at common FiveM resolutions/aspect ratios.
7. Use NUI devtools for console/network/performance diagnosis.

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
- Do not put trusted secrets or authority in browser code.
- Do not leave focus enabled after UI closes.
- Do not spam UI with per-frame messages unless unavoidable and measured.

## Done criteria
- UI loads from packaged build.
- Focus/escape/cancel behavior is correct.
- Callbacks resolve on all paths.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
