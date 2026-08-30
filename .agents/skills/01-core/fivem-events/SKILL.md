---
name: fivem-events
description: Design and review FiveM local/network event contracts, handlers, callbacks, exports, cancellation, payload validation, naming, rate limits, and versioning.
---
# fivem-events
## Purpose

Make event-driven systems explicit, secure, traceable, and cheap enough for their expected frequency.
## Workflow
1. Classify each channel as local event, network event, NUI callback, export, or framework callback.
2. Use local events for same-context internal communication when networking is unnecessary.
3. For network events, define request/response semantics and validate all fields.
4. Namespace public event names consistently.
5. Avoid broadcasting when only one target needs data.
6. Add rate limiting/debouncing for abuse-prone or high-frequency calls.
7. Remove dynamically registered handlers when lifecycle requires it.

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
- Do not use `RegisterNetEvent` where a local event/export suffices.
- Do not send huge object graphs repeatedly.
- Do not assume event order across independent network messages.

## Done criteria
- Event ownership and direction are clear.
- Payload schema is minimal and validated.
- Frequency and abuse behavior are controlled.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
