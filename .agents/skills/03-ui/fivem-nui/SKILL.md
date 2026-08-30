---
name: fivem-nui
description: 'Build and review FiveM fullscreen NUI using CEF, `ui_page`, resource files, focus, messages, callbacks, development tooling, responsive layout, and safe teardown.'
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

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

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

Prefer project source and authoritative documentation over memory for version-sensitive APIs. See `references/nui-sources.md` in this skill for NUI/CEF documentation links. When documentation and installed project code disagree, target the installed version.
