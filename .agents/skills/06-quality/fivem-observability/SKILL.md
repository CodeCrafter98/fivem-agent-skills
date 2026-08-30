---
name: fivem-observability
description: 'Add practical FiveM observability: structured logs, debug modes, metrics/counters, event tracing, correlation IDs, diagnostics commands, and privacy-conscious telemetry.'
---
# fivem-observability
## Purpose

Make production issues diagnosable without flooding console or leaking sensitive player data.
## Workflow
1. Define log levels and a config-gated debug mode.
2. Add structured context: resource/module/action/source/entity/request ID.
3. Correlate NUI/client/server requests where debugging cross-boundary flows.
4. Count/rate important events and denials for abuse/performance diagnosis.
5. Provide admin/debug commands for state snapshots when useful.
6. Redact tokens, secrets, and unnecessary personal data.
7. Avoid per-frame logging.

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
- Do not log secrets or full sensitive identifiers unnecessarily.
- Do not turn debug logging on permanently by default.
- Do not spam high-frequency logs without sampling/rate limits.

## Done criteria
- Errors are traceable across boundaries.
- Production logging volume is bounded.
- Sensitive data is minimized.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
