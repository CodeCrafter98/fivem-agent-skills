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

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

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

Prefer project source and authoritative documentation over memory for version-sensitive APIs. See `references/performance-checklist.md` in this skill for the profiling checklist. When documentation and installed project code disagree, target the installed version.
