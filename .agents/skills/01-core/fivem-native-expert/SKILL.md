---
name: fivem-native-expert
description: 'Select, verify, and use FiveM/GTA natives correctly, including client/server context, hashes, parameters, return values, entity validity, network implications, and safer alternatives.'
---
# fivem-native-expert
## Purpose

Prevent hallucinated or context-invalid native usage and choose the narrowest correct native/API for the job.
## Workflow
1. Search project wrappers first; then authoritative native docs when uncertain.
2. Confirm client/server availability and game build constraints.
3. Validate entity handles before native calls and network IDs after resolution.
4. Load/request models/anim dicts/resources before dependent natives and release them when appropriate.
5. Distinguish local entity handles from network IDs.
6. Prefer server setters or server authority when state must be trusted/replicated.
7. Document unusual flag bitmasks/driving styles with meaning, not magic numbers.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Never invent a native name or signature.
- Do not use client-only entity handles as cross-network identity.
- Do not call expensive natives repeatedly when the value can be safely cached.

## Done criteria
- Native exists and context is correct.
- Parameters/flags are understood.
- Ownership/replication implications are handled.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
