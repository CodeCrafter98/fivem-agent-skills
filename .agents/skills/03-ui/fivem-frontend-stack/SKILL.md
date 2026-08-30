---
name: fivem-frontend-stack
description: Engineer modern FiveM NUI frontends with TypeScript and an appropriate framework/build tool while controlling bundle size, render frequency, state, accessibility, and CEF compatibility.
---
# fivem-frontend-stack
## Purpose

Choose React/Vue/Svelte/vanilla based on UI complexity, not habit, and ship a compact production build compatible with FiveM CEF.
## Workflow
1. Prefer TypeScript for non-trivial UI contracts.
2. Keep framework-independent NUI transport in a small module.
3. Use local component state for ephemeral UI and a store only when shared state warrants it.
4. Avoid SSR/server-only assumptions; NUI is a client-side embedded browser.
5. Code-split only when it meaningfully improves load/cost.
6. Use transform/opacity animations where possible.
7. Build to a deterministic directory declared by the resource manifest.

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
- Do not add a full framework for a tiny static HUD without reason.
- Do not depend on browser APIs unavailable in target CEF without verification.
- Do not ship source maps/secrets unintentionally.

## Done criteria
- Production build is reproducible.
- Bundle/runtime cost is reasonable.
- Transport, state, and presentation are separated.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
