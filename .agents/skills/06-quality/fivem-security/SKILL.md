---
name: fivem-security
description: Audit and harden FiveM resources against malicious clients, forged events/callbacks, economy abuse, permission bypass, entity spoofing, replay/race attacks, SQL injection, and exposed secrets.
---
# fivem-security
## Purpose

Assume an attacker can trigger client-accessible network events with arbitrary payloads and can modify local client/NUI code.
## Workflow
1. Enumerate every client→server network event/callback and every NUI→client→server path.
2. For each, define server-owned facts and validate source, permission, identifiers, ownership, state transition, values/ranges, proximity, cooldown, and replay/idempotency as relevant.
3. Rate-limit costly/abusable endpoints.
4. Use parameterized SQL and never expose DB/API secrets to client/shared/NUI.
5. Validate entity NetIDs and expected type/state before mutation.
6. Prefer allowlists/capabilities over deny-by-obscurity.
7. Log anomalous denials with enough context for investigation but no secrets.

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

Run `python scripts/scan_attack_surface.py <repo-root>` to enumerate likely event/NUI entry points. It does not prove a vulnerability; trace and review validation around each server endpoint.

## Skill-specific guardrails
- Do not rely on renamed events, minification, or UI restrictions for security.
- Do not trust client coordinates blindly for rewards/actions.
- Do not patch exploit symptoms without closing the authority gap.

## Done criteria
- All externally triggerable valuable operations are validated.
- Replay/race/abuse behavior is addressed.
- No secrets or privileged database access are client-exposed.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
