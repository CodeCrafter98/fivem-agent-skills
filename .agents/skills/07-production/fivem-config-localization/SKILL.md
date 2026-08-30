---
name: fivem-config-localization
description: Design FiveM configuration and localization for safe defaults, environment-specific values, feature flags, locale files, validation, and backwards-compatible upgrades.
---
# fivem-config-localization
## Purpose

Separate deployer-tunable settings from code while keeping secrets server-only and configuration validated.
## Workflow
1. Classify config as shared, client-safe, server-only, or secret/external.
2. Validate required config at resource start with actionable errors.
3. Use feature flags for optional integrations.
4. Keep locale keys stable and namespace them by feature.
5. Support fallback locale and missing-key diagnostics.
6. Document breaking config changes and migration defaults.
7. Use ConVars/server config for deployment-specific values when appropriate.

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
- Do not place secrets in shared/client config.
- Do not silently accept invalid enum/range values.
- Do not bake framework-specific text into domain logic.

## Done criteria
- Invalid config fails clearly.
- Locale fallback works.
- Upgrade behavior is documented.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
