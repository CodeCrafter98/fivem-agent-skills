# FiveM Security Checklist

For every externally triggerable server endpoint:

- [ ] Validate `source` / loaded player/session.
- [ ] Validate payload types, size, enum/range, and required fields.
- [ ] Derive money, reward, price, job/role, item definitions, permissions, and ownership from server-owned state.
- [ ] Validate entity NetID exists, is expected type, and is in an allowed state.
- [ ] Validate proximity/zone on the server when location affects authorization/reward.
- [ ] Validate state transition (e.g. cannot complete before start).
- [ ] Add cooldown/rate limit where spam can create cost or advantage.
- [ ] Define replay/idempotency behavior for purchases/rewards/claims.
- [ ] Use parameterized SQL and transactions for valuable multi-step operations.
- [ ] Do not expose secrets in client/shared/NUI code or replicated state.
- [ ] Log meaningful denied attempts without secrets.
