---
name: fivem-dui
description: Implement and review Direct-rendered UI (DUI) for in-world screens, terminals, vehicle displays, signs, TVs, and runtime textures.
---
# fivem-dui
## Purpose

Use DUI when an interface must exist on a world surface, while managing browser/runtime-texture lifecycle carefully.
## Workflow
1. Confirm DUI is actually needed versus fullscreen NUI.
2. Create browser/DUI objects and runtime textures with explicit ownership.
3. Map the texture to the intended render target/material.
4. Define update/input strategy and interaction distance.
5. Throttle updates for offscreen/far-away displays.
6. Destroy DUI/runtime resources on teardown and resource stop.
7. Handle missing texture/model targets without leaking browser instances.

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
- Do not create one expensive DUI browser per entity without capacity analysis.
- Do not leave DUI handles alive after entity/resource destruction.
- Do not assume world-screen input maps automatically.

## Done criteria
- DUI lifecycle is bounded.
- Render/update cost is measured.
- Fallback behavior is defined.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
