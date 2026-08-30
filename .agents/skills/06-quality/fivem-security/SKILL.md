---
name: fivem-security
description: 'Audit and harden FiveM resources against malicious clients, forged events/callbacks, economy abuse, permission bypass, entity spoofing, replay/race attacks, SQL injection, and exposed secrets.'
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

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

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

Prefer project source and authoritative documentation over memory for version-sensitive APIs. See `references/security-checklist.md` and `references/security-sources.md` in this skill for checklists and official docs. When documentation and installed project code disagree, target the installed version.
