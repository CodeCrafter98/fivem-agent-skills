# Performance Checklist

## Client
- Measure idle/active `resmon` for changed resources.
- Find unconditional `Wait(0)` loops; justify each.
- Reduce native calls and world scans by proximity/event/adaptive sleep/caching.
- Avoid allocation-heavy tables/strings in frame loops.
- Throttle NUI messages and state bag writes.

## Server
- Profile hot handlers/threads.
- Bound event fanout and payload size.
- Avoid repeated/N+1 DB queries; inspect indexes.
- Bound entity creation and cleanup work.

## NUI
- Check long tasks, rerenders, layout/paint churn, large images/fonts, and animation cost.
- Prefer transform/opacity for motion.
- Avoid high-frequency full-state replacement when deltas suffice.

## Evidence
Record the before/after measurement or the exact reproducible measurement plan.
