---
name: fivem-performance
description: 'Profile and optimize FiveM client/server/NUI performance: resmon, profiler, hot loops, native calls, allocations, events, state bags, entities, database queries, and frontend renders.'
---
# fivem-performance
## Purpose

Measure before optimizing and reduce work at the source: frequency × cost × fanout.
## Workflow
1. Identify the hot path and expected frequency/fanout.
2. Measure idle and active client resmon when possible; use server/client profiler for CPU hotspots.
3. Reduce unconditional `Wait(0)` loops via events, zones, adaptive sleeps, or caching.
4. Cache stable native results but invalidate correctly.
5. Batch/throttle events, NUI messages, and state updates.
6. Reduce entity churn and expensive world scans.
7. Eliminate N+1/repeated DB queries and add indexes as supported by workload.
8. Profile NUI long tasks/rerenders/layout thrash for complex UIs.

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

Run `python scripts/scan_hotpaths.py <repo-root>` as a static lead generator for loops, NUI messages, and state writes. Confirm runtime cost with resmon/profiler before calling something a performance defect.

## Skill-specific guardrails
- Do not optimize based only on line count.
- Do not cache dynamic values without invalidation design.
- Do not claim success without before/after evidence for material performance work.

## Done criteria
- Bottleneck is measured or strongly evidenced.
- Optimization preserves correctness.
- Before/after metrics or a reproducible measurement plan is provided.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Use project source and authoritative documentation before relying on memory for version-sensitive APIs. Start with `references/official-sources.md` in this package. When documentation and installed project code disagree, target the installed version and document the compatibility constraint.
