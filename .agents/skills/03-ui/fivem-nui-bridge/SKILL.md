---
name: fivem-nui-bridge
description: 'Design typed, validated communication contracts between FiveM Lua and NUI frontends, including request/response envelopes, errors, timeouts, message routing, and rate limits.'
---
# fivem-nui-bridge
## Purpose

Make the Lua↔browser boundary explicit and mechanically consistent rather than a collection of magic strings.
## Workflow
1. Define canonical event/callback names in one place per side.
2. Use small request/response schemas with explicit success/error envelopes.
3. Validate browser payloads before server forwarding.
4. Always call the NUI callback response exactly once on every path.
5. Wrap browser `fetch` with timeout/error handling and resource-name resolution.
6. Throttle high-frequency game→UI telemetry; send deltas when practical.
7. Document which NUI action may trigger a server request and the server validation required.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Deterministic helper

Run `python scripts/scan_nui.py <repo-root>` to map obvious Lua callbacks, browser fetches, and NUI messages before tracing contract mismatches manually.

## Skill-specific guardrails
- Do not let TypeScript types substitute for runtime validation.
- Do not trust hidden/disabled UI controls as authorization.
- Do not leave unresolved browser promises.

## Done criteria
- Contracts match on both sides.
- Errors are recoverable and user-visible where appropriate.
- No callback can hang.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. See `references/nui-contract-pattern.md` in this skill for the canonical contract envelope. When documentation and installed project code disagree, target the installed version.
