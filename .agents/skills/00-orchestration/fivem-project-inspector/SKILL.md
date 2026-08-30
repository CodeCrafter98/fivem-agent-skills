---
name: fivem-project-inspector
description: 'Inspect an existing FiveM project before modification. Use to identify framework, dependencies, resource boundaries, events, exports, database access, NUI stack, conventions, and risk areas.'
---
# fivem-project-inspector
## Purpose

Build a factual project map before changing code. Prefer repository evidence over assumptions.
## Workflow
1. Locate `fxmanifest.lua`, resource roots, server config references, and package manifests.
2. Identify framework: standalone, Qbox, QBCore, ESX, custom, or mixed.
3. Identify ox ecosystem and other dependencies.
4. Map client/server/shared scripts, exports, registered events, NUI callbacks/messages, state bags, entities, and database repositories.
5. Identify UI technology and build output path.
6. Record existing naming, error, logging, config, localization, and test conventions.
7. Produce a concise change-impact map: files to touch, contracts affected, migrations, restart risks, and verification commands.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Deterministic helper

For a fast factual inventory, run `python scripts/scan_project.py <repo-root>` from this skill directory. Treat its regex output as leads, then inspect surrounding code before conclusions.

## Skill-specific guardrails
- Do not infer framework from filenames alone.
- Do not rewrite architecture before understanding it.
- Do not search-replace event names without tracing producers and consumers.

## Done criteria
- Framework/dependencies are evidenced.
- Affected boundaries and contracts are listed.
- Planned edits are scoped to the requested outcome.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
