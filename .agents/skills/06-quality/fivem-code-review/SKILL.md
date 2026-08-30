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

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

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

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
