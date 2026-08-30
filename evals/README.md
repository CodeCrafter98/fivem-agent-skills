# Evals

These routing/quality cases are harness-neutral. For each case, run the prompt in your target coding agent with this pack installed and score:

1. **Routing precision** — expected specialists are selected; irrelevant specialists are not all loaded.
2. **FiveM correctness** — no invented APIs/natives; client/server/network boundaries are correct.
3. **Security** — privileged client claims are rejected/revalidated.
4. **Lifecycle** — restart/disconnect/entity-loss cases appear where relevant.
5. **Performance** — high-frequency work is recognized and measured.
6. **Verification** — completion includes concrete checks rather than assertion-only confidence.

Case JSON files contain `expected_skills`, positive assertions, and forbidden patterns. Add project-specific evals as regressions are discovered.
