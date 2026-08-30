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

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

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

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
