---
name: fivem-nui-bridge
description: 'Design typed, validated communication contracts between FiveM Lua and NUI frontends, including request/response envelopes, errors, timeouts, message routing, and rate limits.'
---
# fivem-nui-bridge
## Purpose

Make the Lua↔browser boundary explicit and mechanically consistent rather than a collection of magic strings.
## Workflow
1. Define canonical event/callback names in one place per side.
2. Use small request/response schemas with explicit success/error envelopes.
3. Validate browser payloads before server forwarding.
4. Always call the NUI callback response exactly once on every path.
5. Wrap browser `fetch` with timeout/error handling and resource-name resolution.
6. Throttle high-frequency game→UI telemetry; send deltas when practical.
7. Document which NUI action may trigger a server request and the server validation required.

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

## Deterministic helper

Run `python scripts/scan_nui.py <repo-root>` to map obvious Lua callbacks, browser fetches, and NUI messages before tracing contract mismatches manually.

## Skill-specific guardrails
- Do not let TypeScript types substitute for runtime validation.
- Do not trust hidden/disabled UI controls as authorization.
- Do not leave unresolved browser promises.

## Done criteria
- Contracts match on both sides.
- Errors are recoverable and user-visible where appropriate.
- No callback can hang.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
