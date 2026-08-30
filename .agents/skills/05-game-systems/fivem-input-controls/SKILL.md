---
name: fivem-input-controls
description: 'Design FiveM keyboard/controller input, command/key mapping, control disabling, focus interactions, hold/tap behavior, and conflict-safe cleanup.'
---
# fivem-input-controls
## Purpose

Make controls configurable, reversible, and compatible with NUI focus/gameplay states.
## Workflow
1. Prefer registered commands/key mappings for user-configurable actions where suitable.
2. Centralize control state and enable/disable reasons.
3. Distinguish tap, hold, repeat, and continuous actions.
4. Coordinate NUI focus so controls are restored on close/error/stop.
5. Avoid globally disabling broad control sets unless necessary.
6. Document default bindings and conflicts.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not hard-code inaccessible bindings without remapping path.
- Do not leave controls disabled after resource stop.
- Do not use per-frame input polling for events that command/key mapping can provide.

## Done criteria
- Bindings are configurable where appropriate.
- Focus/control cleanup works.
- Controller/keyboard behavior is intentional.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
