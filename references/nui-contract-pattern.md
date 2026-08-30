# NUI Contract Pattern

Recommended envelope:

```ts
export type NuiResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: { code: string; message: string } };
```

Browser request helper should:
1. Resolve `GetParentResourceName()` in FiveM; allow a dev fallback only in development.
2. POST JSON to `https://${resource}/${callback}`.
3. Apply timeout/abort handling.
4. Parse a stable result envelope.

Lua callback should:
1. Runtime-validate the payload.
2. Perform local presentation work or forward the minimal request to the server.
3. Call `cb(...)` exactly once on every path.
4. Never treat UI visibility/disabled controls as authorization.
