---
name: fivem-audit
description: 'Perform a comprehensive FiveM resource audit across architecture, security, networking, performance, persistence, UI, framework compatibility, lifecycle, testing, and release readiness.'
---
# fivem-audit
## Purpose

Review an existing resource systematically and prioritize findings by exploitability, correctness impact, performance cost, and maintenance risk.
## Workflow
1. Inspect the project first.
2. Audit trust boundaries and externally triggerable events/callbacks.
3. Audit OneSync/state bags/entity lifecycle and routing buckets.
4. Audit NUI contracts, focus handling, message frequency, and UI runtime cost.
5. Audit database queries, transactions, indexes, and framework APIs.
6. Audit hot loops/native calls/event traffic and cleanup handlers.
7. Audit resource restart, player disconnect, missing dependency, and partial-failure behavior.
8. Report findings as BLOCKER/HIGH/MEDIUM/LOW with file/line evidence, impact, and remediation.

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
- Do not report style preferences as security findings.
- Do not claim performance issues without identifying the hot path or expected cost.
- Do not rewrite code unless the user asked for remediation.

## Done criteria
- Every finding is evidenced and actionable.
- Severity is consistent.
- False-positive risk and verification method are stated for uncertain findings.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
