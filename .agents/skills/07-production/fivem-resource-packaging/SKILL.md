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

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

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

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
