// ── Request payloads ──────────────────────────────────────────────────────────

export interface HeatParams {
  alpha: number;
  L: number;
  T: number;
  Nx: number;
  Nt: number;
}

export interface PINNOptions {
  load_pretrained: boolean;
  train: boolean;
  epochs: number;
  lr: number;
  use_lbfgs: boolean;
}

export interface CompareRequest extends HeatParams {
  pinn_load_pretrained: boolean;
  pinn_train: boolean;
  pinn_epochs: number;
  pinn_lr: number;
  pinn_use_lbfgs: boolean;
}

// ── Response payloads ─────────────────────────────────────────────────────────

export interface SolutionData {
  x: number[];
  t: number[];
  u: number[][];
}

export interface FDMSolution extends SolutionData {
  fourier_number: number;
  stable: boolean;
  warning?: string;
}

export interface PINNSolution extends SolutionData {
  loss_history: number[];
  training_time: number;
  loaded_pretrained: boolean;
}

export interface MethodMetrics {
  l2_error: number;
  linf_error: number;
  execution_time: number;
}

export interface CompareResponse {
  analytic: SolutionData;
  fdm: FDMSolution;
  pinn?: PINNSolution;
  metrics: Record<string, MethodMetrics>;
}

// ── UI state ──────────────────────────────────────────────────────────────────

export type TabId = 'analytic' | 'fdm' | 'pinn' | 'compare';
