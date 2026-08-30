---
name: fivem-fix
description: 'Run a root-cause-first FIX workflow for FiveM bugs. Use for errors, regressions, desync, NUI failures, event failures, entity issues, database problems, or performance regressions.'
---
# fivem-fix
## Purpose

Reproduce and isolate before patching. Prefer the smallest correction that fixes the root cause and add regression protection.
## Workflow
1. Capture exact symptom, logs, F8/server/NUI error, and reproduction steps when available.
2. Trace the failing path across UI/client/server/database/network boundaries.
3. Form a root-cause hypothesis and verify it against code or runtime evidence.
4. Implement a minimal patch that preserves unrelated behavior.
5. Add or update a regression test/check.
6. Verify resource restart, player reconnect, and ownership/state transitions when relevant.
7. Run security/performance review if the failure path is externally triggerable or hot.

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
- Do not apply random defensive guards without explaining the root cause.
- Do not silence errors that should be handled.
- Do not broaden refactors during a bug fix unless required.

## Done criteria
- Root cause is identified.
- Regression is covered.
- Original reproduction no longer fails and adjacent paths still work.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
