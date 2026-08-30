export type NuiResult<T> =
  | { ok: true; data: T }
  | { ok: false; error: { code: string; message: string } };

export async function nuiFetch<TReq, TRes>(event: string, payload: TReq, timeoutMs = 5000): Promise<NuiResult<TRes>> {
  const resource = typeof GetParentResourceName === 'function' ? GetParentResourceName() : 'dev-resource';
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    const response = await fetch(`https://${resource}/${event}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json; charset=UTF-8' },
      body: JSON.stringify(payload),
      signal: controller.signal,
    });
    return await response.json();
  } finally {
    clearTimeout(timer);
  }
}
