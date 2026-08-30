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

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
