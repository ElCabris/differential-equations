import type {
  CompareRequest,
  CompareResponse,
  FDMSolution,
  HeatParams,
  PINNOptions,
  PINNSolution,
  SolutionData,
} from '../types';

const BASE = import.meta.env.VITE_API_URL ?? '';

async function post<T>(path: string, body: unknown): Promise<T> {
  const res = await fetch(`${BASE}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const detail = await res.json().catch(() => ({ detail: res.statusText }));
    throw new Error(detail.detail ?? res.statusText);
  }
  return res.json() as Promise<T>;
}

export const api = {
  analytic: (params: HeatParams) =>
    post<SolutionData>('/solve/analytic', params),

  fdm: (params: HeatParams) =>
    post<FDMSolution>('/solve/fdm', params),

  pinn: (params: HeatParams & PINNOptions) =>
    post<PINNSolution>('/solve/pinn', params),

  compare: (req: CompareRequest) =>
    post<CompareResponse>('/compare', req),
};
