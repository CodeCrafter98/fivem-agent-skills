---
name: fivem-cfxlua
description: 'Write and review modern CfxLua for FiveM using Lua 5.4 semantics, Cfx extensions, coroutine/thread patterns, efficient tables, vectors, errors, and hot-path discipline.'
---
# fivem-cfxlua
## Purpose

Produce idiomatic, allocation-conscious Lua that fits FiveM runtime semantics rather than generic Lua-only patterns.
## Workflow
1. Use locals aggressively for scoped state and frequently referenced functions when it improves hot paths.
2. Choose `CreateThread`, `Wait`, timeouts, promises, and events based on actual scheduling needs.
3. Prefer event-driven or adaptive-sleep loops over unconditional frame polling.
4. Use Cfx vector/quaternion support where it simplifies spatial logic.
5. Keep mutation ownership clear; avoid hidden globals.
6. Handle nil/deleted entities and resource shutdown explicitly.
7. For CPU-heavy pure logic, isolate functions so they can be unit tested outside GTA runtime.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not add Lua 5.3 compatibility workarounds without evidence.
- Do not busy-loop.
- Do not allocate large temporary tables every frame.
- Do not swallow errors that indicate invariant violations.

## Done criteria
- Code targets current CfxLua.
- Thread cadence matches gameplay need.
- Hot paths avoid unnecessary native calls/allocations.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. See `references/cfxlua-sources.md` in this skill for CfxLua and manifest documentation. When documentation and installed project code disagree, target the installed version.
