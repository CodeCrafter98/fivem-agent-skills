---
name: fivem-debugging
description: 'Systematically diagnose FiveM client/server/Lua/NUI/network/database/framework/resource errors and desynchronization.'
---
# fivem-debugging
## Purpose

Follow evidence from reproduction to root cause across process boundaries instead of making random patches.
## Workflow
1. Classify failure surface: resource load/manifest, Lua client, Lua server, NUI browser, network/OneSync, entity ownership, DB, framework, build asset.
2. Capture exact logs/stack traces and correlate timestamps/IDs.
3. Trace producer→transport→consumer for events/messages/callbacks.
4. Check entity existence/NetID/owner/scope for sync bugs.
5. Check callback completion and browser network errors for NUI.
6. Check query inputs/results/transactions for DB bugs.
7. Patch the root cause minimally and add regression verification.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not hide stack traces with broad `pcall` without handling.
- Do not add arbitrary delays as a permanent race fix without understanding ordering.
- Do not assume client and server see the same entity handle.

## Done criteria
- Reproduction is explained.
- Root cause is evidenced.
- Patch is verified against original and adjacent scenarios.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
