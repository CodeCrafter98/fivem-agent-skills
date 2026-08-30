---
name: fivem-code-review
description: 'Review FiveM code changes for correctness, architecture, security, networking, lifecycle, performance, persistence, UI, compatibility, and maintainability with evidence-based severity.'
---
# fivem-code-review
## Purpose

Act as a senior reviewer: prioritize defects and regression risks over stylistic preferences.
## Workflow
1. Read the diff plus enough surrounding code to understand contracts.
2. Trace changed events/callbacks across both ends.
3. Check authority and validation for every new/changed client→server path.
4. Check entity/state lifecycle and cleanup.
5. Check loops/event rates/NUI messages/DB calls for runtime cost.
6. Check framework API/version assumptions and migration compatibility.
7. Check tests against the changed risk surface.
8. Report BLOCKER/HIGH/MEDIUM/LOW with concise remediation.

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
- Do not manufacture findings to fill severity buckets.
- Do not flag formatting already enforced by tooling.
- Do not approve unverified security-sensitive paths.

## Done criteria
- Findings cite exact code.
- Severity matches realistic impact.
- Approval is conditional on concrete verification evidence.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
