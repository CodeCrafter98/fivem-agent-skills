---
name: fivem-project-inspector
description: Inspect an existing FiveM project before modification. Use to identify framework, dependencies, resource boundaries, events, exports, database access, NUI stack, conventions, and risk areas.
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

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
