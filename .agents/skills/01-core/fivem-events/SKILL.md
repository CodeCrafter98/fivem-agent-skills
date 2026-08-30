---
name: fivem-events
description: 'Design and review FiveM local/network event contracts, handlers, callbacks, exports, cancellation, payload validation, naming, rate limits, and versioning.'
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

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

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

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
