import { useState } from 'react';
import { api } from '../services/api';
import type {
  CompareResponse,
  FDMSolution,
  HeatParams,
  PINNOptions,
  PINNSolution,
  SolutionData,
} from '../types';

interface SolverState {
  analytic: SolutionData | null;
  fdm: FDMSolution | null;
  pinn: PINNSolution | null;
  compare: CompareResponse | null;
}

interface LoadingState {
  analytic: boolean;
  fdm: boolean;
  pinn: boolean;
  compare: boolean;
}

interface ErrorState {
  analytic: string | null;
  fdm: string | null;
  pinn: string | null;
  compare: string | null;
}

export function useSolver() {
  const [solutions, setSolutions] = useState<SolverState>({
    analytic: null,
    fdm: null,
    pinn: null,
    compare: null,
  });
  const [loading, setLoading] = useState<LoadingState>({
    analytic: false,
    fdm: false,
    pinn: false,
    compare: false,
  });
  const [errors, setErrors] = useState<ErrorState>({
    analytic: null,
    fdm: null,
    pinn: null,
    compare: null,
  });

  function setLoad(key: keyof LoadingState, v: boolean) {
    setLoading((s) => ({ ...s, [key]: v }));
  }
  function setError(key: keyof ErrorState, msg: string | null) {
    setErrors((s) => ({ ...s, [key]: msg }));
  }
  function setResult<K extends keyof SolverState>(key: K, v: SolverState[K]) {
    setSolutions((s) => ({ ...s, [key]: v }));
  }

  async function solveAnalytic(params: HeatParams) {
    setLoad('analytic', true);
    setError('analytic', null);
    try {
      const r = await api.analytic(params);
      setResult('analytic', r);
    } catch (e) {
      setError('analytic', (e as Error).message);
    } finally {
      setLoad('analytic', false);
    }
  }

  async function solveFDM(params: HeatParams) {
    setLoad('fdm', true);
    setError('fdm', null);
    try {
      const r = await api.fdm(params);
      setResult('fdm', r);
    } catch (e) {
      setError('fdm', (e as Error).message);
    } finally {
      setLoad('fdm', false);
    }
  }

  async function solvePINN(params: HeatParams, opts: PINNOptions) {
    setLoad('pinn', true);
    setError('pinn', null);
    try {
      const r = await api.pinn({ ...params, ...opts });
      setResult('pinn', r);
    } catch (e) {
      setError('pinn', (e as Error).message);
    } finally {
      setLoad('pinn', false);
    }
  }

  async function solveAll(params: HeatParams, pinnOpts: PINNOptions) {
    setLoad('compare', true);
    setError('compare', null);
    try {
      const r = await api.compare({
        ...params,
        pinn_load_pretrained: pinnOpts.load_pretrained,
        pinn_train: pinnOpts.train,
        pinn_epochs: pinnOpts.epochs,
        pinn_lr: pinnOpts.lr,
        pinn_use_lbfgs: pinnOpts.use_lbfgs,
      });
      setResult('compare', r);
      // Populate individual tabs from the compare response
      setResult('analytic', r.analytic);
      setResult('fdm', r.fdm);
      if (r.pinn) setResult('pinn', r.pinn);
    } catch (e) {
      setError('compare', (e as Error).message);
    } finally {
      setLoad('compare', false);
    }
  }

  return { solutions, loading, errors, solveAnalytic, solveFDM, solvePINN, solveAll };
}
