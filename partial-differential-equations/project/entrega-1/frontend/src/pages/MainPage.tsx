import { useState, type ReactNode } from 'react';
import Sidebar from '../components/Sidebar';
import HeatmapPlot from '../components/HeatmapPlot';
import ProfilePlot from '../components/ProfilePlot';
import LossPlot from '../components/LossPlot';
import MetricsTable from '../components/MetricsTable';
import { useSolver } from '../hooks/useSolver';
import type { HeatParams, PINNOptions, TabId } from '../types';

const DEFAULT_PARAMS: HeatParams = {
  alpha: 0.01,
  L: 1.0,
  T: 1.0,
  Nx: 100,
  Nt: 100,
};

const DEFAULT_PINN: PINNOptions = {
  load_pretrained: true,
  train: false,
  epochs: 2000,
  lr: 0.001,
  use_lbfgs: true,
};

const TABS: { id: TabId; label: string }[] = [
  { id: 'analytic', label: 'Analítica' },
  { id: 'fdm', label: 'FTCS' },
  { id: 'pinn', label: 'PINN' },
  { id: 'compare', label: 'Comparación' },
];

export default function MainPage() {
  const [params, setParams] = useState<HeatParams>(DEFAULT_PARAMS);
  const [pinnOpts, setPINNOpts] = useState<PINNOptions>(DEFAULT_PINN);
  const [activeTab, setActiveTab] = useState<TabId>('analytic');

  const { solutions, loading, errors, solveAnalytic, solveFDM, solvePINN, solveAll } =
    useSolver();

  const anyLoading = Object.values(loading).some(Boolean);

  function handleParamsChange(partial: Partial<HeatParams>) {
    setParams((p) => ({ ...p, ...partial }));
  }

  function handlePINNOptsChange(partial: Partial<PINNOptions>) {
    setPINNOpts((p) => ({ ...p, ...partial }));
  }

  function handleSolve() {
    switch (activeTab) {
      case 'analytic':
        solveAnalytic(params);
        break;
      case 'fdm':
        solveFDM(params);
        break;
      case 'pinn':
        solvePINN(params, pinnOpts);
        break;
      case 'compare':
        solveAll(params, pinnOpts);
        break;
    }
  }

  function handleCompare() {
    setActiveTab('compare');
    solveAll(params, pinnOpts);
  }

  return (
    <div className="layout">
      <Sidebar
        params={params}
        pinnOpts={pinnOpts}
        loading={anyLoading}
        onParamsChange={handleParamsChange}
        onPINNOptsChange={handlePINNOptsChange}
        onSolve={handleSolve}
        onCompare={handleCompare}
      />

      <main className="main">
        {/* Tab bar */}
        <div className="tabs">
          {TABS.map((tab) => (
            <button
              key={tab.id}
              className={`tab-btn${activeTab === tab.id ? ' active' : ''}`}
              onClick={() => setActiveTab(tab.id)}
            >
              {tab.label}
            </button>
          ))}
        </div>

        {/* Tab content */}
        <div className="tab-content">
          {/* ── Analítica ────────────────────────────────────────────────────── */}
          {activeTab === 'analytic' && (
            <TabPanel
              loading={loading.analytic}
              error={errors.analytic}
              hasData={!!solutions.analytic}
            >
              {solutions.analytic && (
                <>
                  <HeatmapPlot
                    data={solutions.analytic}
                    title="Solución analítica u*(x,t) = exp(-α(π/L)²t) · sin(πx/L)"
                  />
                  <ProfilePlot
                    datasets={[{ data: solutions.analytic, name: 'Analítica', color: '#2563eb' }]}
                    title="Perfiles espaciales — Solución analítica"
                  />
                </>
              )}
            </TabPanel>
          )}

          {/* ── FTCS ─────────────────────────────────────────────────────────── */}
          {activeTab === 'fdm' && (
            <TabPanel
              loading={loading.fdm}
              error={errors.fdm}
              hasData={!!solutions.fdm}
            >
              {solutions.fdm && (
                <>
                  {solutions.fdm.warning && (
                    <div className="alert alert-warning">⚠ {solutions.fdm.warning}</div>
                  )}
                  <div className="info-badge">
                    Número de Fourier Fo = {solutions.fdm.fourier_number.toFixed(4)}{' '}
                    {solutions.fdm.stable ? '✓ estable' : '✗ inestable'}
                  </div>
                  <HeatmapPlot
                    data={solutions.fdm}
                    title="Diferencias Finitas FTCS"
                    colorscale="Viridis"
                  />
                  <ProfilePlot
                    datasets={[{ data: solutions.fdm, name: 'FTCS', color: '#16a34a' }]}
                    title="Perfiles espaciales — FTCS"
                  />
                </>
              )}
            </TabPanel>
          )}

          {/* ── PINN ─────────────────────────────────────────────────────────── */}
          {activeTab === 'pinn' && (
            <TabPanel
              loading={loading.pinn}
              error={errors.pinn}
              hasData={!!solutions.pinn}
              loadingMsg={pinnOpts.train ? 'Entrenando PINN (puede tardar ~60 s)…' : undefined}
            >
              {solutions.pinn && (
                <>
                  <div className="info-badge">
                    {solutions.pinn.loaded_pretrained
                      ? '✓ Modelo preentrenado cargado'
                      : `✓ Entrenamiento completado en ${solutions.pinn.training_time.toFixed(1)} s`}
                  </div>
                  <HeatmapPlot
                    data={solutions.pinn}
                    title="PINN — û(x,t)"
                    colorscale="Plasma"
                  />
                  {solutions.pinn.loss_history.length > 0 && (
                    <LossPlot lossHistory={solutions.pinn.loss_history} />
                  )}
                  <ProfilePlot
                    datasets={[{ data: solutions.pinn, name: 'PINN', color: '#9333ea' }]}
                    title="Perfiles espaciales — PINN"
                  />
                </>
              )}
            </TabPanel>
          )}

          {/* ── Comparación ──────────────────────────────────────────────────── */}
          {activeTab === 'compare' && (
            <TabPanel
              loading={loading.compare}
              error={errors.compare}
              hasData={!!solutions.compare}
              loadingMsg="Ejecutando todos los métodos…"
            >
              {solutions.compare && (
                <>
                  <MetricsTable metrics={solutions.compare.metrics} />

                  <div className="grid-2">
                    <HeatmapPlot
                      data={solutions.compare.analytic}
                      title="Analítica"
                    />
                    <HeatmapPlot
                      data={solutions.compare.fdm}
                      title="FTCS"
                      colorscale="Viridis"
                    />
                  </div>

                  {solutions.compare.pinn && (
                    <HeatmapPlot
                      data={solutions.compare.pinn}
                      title="PINN"
                      colorscale="Plasma"
                    />
                  )}

                  <ProfilePlot
                    datasets={[
                      { data: solutions.compare.analytic, name: 'Analítica', color: '#2563eb' },
                      { data: solutions.compare.fdm,      name: 'FTCS',      color: '#16a34a' },
                      ...(solutions.compare.pinn
                        ? [{ data: solutions.compare.pinn, name: 'PINN', color: '#9333ea' }]
                        : []),
                    ]}
                    title="Comparación de perfiles"
                  />
                </>
              )}
            </TabPanel>
          )}
        </div>
      </main>
    </div>
  );
}

// ── Small helper ──────────────────────────────────────────────────────────────

interface TabPanelProps {
  loading: boolean;
  error: string | null;
  hasData: boolean;
  loadingMsg?: string;
  children: ReactNode;
}

function TabPanel({ loading, error, hasData, loadingMsg, children }: TabPanelProps) {
  if (loading) {
    return (
      <div className="placeholder">
        <div className="spinner" />
        <p>{loadingMsg ?? 'Calculando…'}</p>
      </div>
    );
  }
  if (error) {
    return <div className="alert alert-error">Error: {error}</div>;
  }
  if (!hasData) {
    return (
      <div className="placeholder">
        <p>Presiona <strong>Resolver</strong> para calcular la solución.</p>
      </div>
    );
  }
  return <>{children}</>;
}
