---
name: fivem-documentation
description: 'Write operator and developer documentation for FiveM resources: installation, dependencies, configuration, permissions, events/exports, database, UI build, troubleshooting, security, and upgrade guidance.'
---
# fivem-documentation
## Purpose

Document the stable contract and operational behavior, not implementation trivia.
## Workflow
1. Include prerequisites and supported environment matrix.
2. Document install/start order and config with safe examples.
3. Document public exports/events/callbacks with direction, payload, result, and authority notes.
4. Document database migrations/backups.
5. Document NUI build workflow if source is shipped.
6. Document common errors and diagnostic commands.
7. Document security assumptions and which values are server authoritative.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not expose secrets in examples.
- Do not document internal implementation as guaranteed API.
- Do not claim tested compatibility without evidence.

## Done criteria
- A new operator can install and configure resource.
- A developer can integrate via documented contracts.
- Troubleshooting covers known failure surfaces.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
