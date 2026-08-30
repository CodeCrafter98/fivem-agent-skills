---
name: fivem-resource-packaging
description: 'Package distributable FiveM resources with clean manifests, production UI assets, licenses, source/build separation, optional escrow-aware boundaries, and no secrets or local artifacts.'
---
# fivem-resource-packaging
## Purpose

Create a minimal runtime package while preserving the source repository for development and review.
## Workflow
1. Define which files are runtime-required versus development-only.
2. Ensure manifest files/globs include all runtime assets and exclude irrelevant source when desired.
3. Build NUI before packaging and verify asset paths/case sensitivity.
4. Exclude `.env`, credentials, local logs, node_modules, caches, test fixtures, and editor files.
5. Include license/readme/version/changelog as appropriate.
6. Verify package on a clean server/resource directory.
7. Generate checksums/release archive if distribution workflow uses them.

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
- Do not package credentials or local server data.
- Do not ship `node_modules` when static UI build is sufficient.
- Do not remove source/license notices contrary to dependency licenses.

## Done criteria
- Archive contains only intended files.
- Clean install starts successfully.
- No secret/local artifacts are present.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
