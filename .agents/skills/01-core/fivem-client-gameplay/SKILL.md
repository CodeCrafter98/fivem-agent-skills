---
name: fivem-client-gameplay
description: Implement FiveM client gameplay systems: player/ped/vehicle interaction, cameras, animations, props, blips, markers, particles, audio, controls, and local presentation logic.
---
# fivem-client-gameplay
## Purpose

Keep the client responsive and presentation-focused while delegating trusted state changes to the server.
## Workflow
1. Separate input/presentation from authoritative decisions.
2. Use proximity/adaptive loops for world interactions.
3. Manage model/anim/ptfx loading with timeouts and cleanup.
4. Handle player death, ped change, teleport, resource restart, and entity loss when relevant.
5. Keep cameras/focus/input state reversible.
6. Batch or throttle UI updates generated from gameplay state.
7. Send requests to server with minimal evidence; let server revalidate critical facts.

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
- Do not grant money/items/permissions client-side.
- Do not leave controls/focus/cameras stuck after cancel/error/stop.
- Do not run expensive scans every frame.

## Done criteria
- Gameplay feels responsive.
- Cleanup is complete.
- Authoritative mutations are server validated.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
