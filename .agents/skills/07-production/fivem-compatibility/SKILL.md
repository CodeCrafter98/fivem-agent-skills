---
name: fivem-compatibility
description: 'Assess FiveM compatibility across server artifacts/game builds, GTA5 legacy/enhanced considerations, OneSync modes, frameworks, dependencies, and resource versions.'
---
# fivem-compatibility
## Purpose

State explicit support boundaries and avoid accidental reliance on environment-specific behavior.
## Workflow
1. Inspect current target artifact/build/framework/dependency versions.
2. Verify natives/features against target game/runtime when version-sensitive.
3. Test optional dependencies absent/present as designed.
4. Document required OneSync or routing behavior.
5. Use feature/capability detection where practical.
6. Provide migration notes for breaking dependency/API changes.
7. Avoid broad compatibility claims without test evidence.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not promise support for untested forks/builds.
- Do not add legacy compatibility code that harms current runtime without a requirement.
- Do not suppress dependency version errors.

## Done criteria
- Supported matrix is explicit.
- Unsupported environments fail clearly.
- Version-specific branches are isolated and documented.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
