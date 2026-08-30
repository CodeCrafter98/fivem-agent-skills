---
name: fivem-build
description: 'Execute a production-minded BUILD workflow for a new FiveM feature or resource. Use when implementing new functionality end-to-end.'
---
# fivem-build
## Purpose

Coordinate design, implementation, integration, and verification for a new feature while keeping authority boundaries and runtime costs explicit.
## Workflow
1. Inspect the project and requirements.
2. Define acceptance criteria and authority/data-flow diagram.
3. Design resource/module boundaries and public contracts before implementation.
4. Implement the smallest vertical slice first.
5. Add server validation, lifecycle cleanup, NUI contracts, persistence, and framework adapters as required.
6. Run static checks, focused tests, restart/disconnect scenarios, security review, and performance checks.
7. Document configuration, dependencies, exports/events, and operational notes.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not build speculative abstractions without a current use case.
- Do not accept client-supplied rewards/ownership/permissions as truth.
- Do not leave TODO placeholders in the requested production path.

## Done criteria
- Acceptance criteria are met.
- Feature survives resource restart and relevant disconnect/entity-loss cases.
- Security and performance risks are explicitly checked.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
