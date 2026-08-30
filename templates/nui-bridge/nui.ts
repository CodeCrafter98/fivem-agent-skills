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

    if (!response.ok) {
      return { ok: false, error: { code: 'http_error', message: `HTTP ${response.status}` } };
    }

    let body: unknown;
    try {
      body = await response.json();
    } catch {
      return { ok: false, error: { code: 'invalid_response', message: 'Response is not valid JSON' } };
    }

    // Validate the response matches the expected NuiResult shape
    if (typeof body === 'object' && body !== null && 'ok' in body) {
      return body as NuiResult<TRes>;
    }

    return { ok: false, error: { code: 'invalid_response', message: 'Unexpected response shape' } };
  } catch (err: unknown) {
    if (err instanceof DOMException && err.name === 'AbortError') {
      return { ok: false, error: { code: 'timeout', message: `Request timed out after ${timeoutMs}ms` } };
    }
    return { ok: false, error: { code: 'network_error', message: 'Network request failed' } };
  } finally {
    clearTimeout(timer);
  }
}
