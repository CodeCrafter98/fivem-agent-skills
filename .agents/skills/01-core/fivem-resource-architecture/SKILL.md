---
name: fivem-resource-architecture
description: 'Design and review FiveM resource architecture, fxmanifest metadata, module boundaries, exports, dependencies, lifecycle, configuration, and multi-resource composition.'
---
# fivem-resource-architecture
## Purpose

Create cohesive resources with explicit public contracts and minimal coupling.
## Workflow
1. Use `fxmanifest.lua`; keep manifest declarative and minimal.
2. Separate client, server, shared, configuration, UI, and adapters by responsibility.
3. Prefer internal modules/services over globally exposed events for same-resource calls.
4. Expose exports/events only as intentional public API.
5. Declare dependencies explicitly when startup order matters.
6. Plan resource start/stop behavior, cleanup, and idempotent initialization.
7. Avoid circular dependencies; introduce a small interface/adapter boundary instead.
8. Version public contracts when external resources consume them.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not use `lua54 'yes'`.
- Do not put secrets or privileged logic in shared/client files.
- Do not create a monolithic `client.lua`/`server.lua` once responsibilities become distinct.

## Done criteria
- Manifest is valid and complete.
- Public API and dependencies are explicit.
- Start/stop/restart behavior is safe.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. See `references/cfxlua-sources.md` in this skill for resource manifest documentation. When documentation and installed project code disagree, target the installed version.
