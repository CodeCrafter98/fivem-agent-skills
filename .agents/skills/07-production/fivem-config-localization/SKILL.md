---
name: fivem-config-localization
description: 'Design FiveM configuration and localization for safe defaults, environment-specific values, feature flags, locale files, validation, and backwards-compatible upgrades.'
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

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

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

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
