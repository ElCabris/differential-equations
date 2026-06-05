import type { MethodMetrics } from '../types';

interface Props {
  metrics: Record<string, MethodMetrics>;
}

const LABELS: Record<string, string> = {
  fdm: 'FTCS',
  pinn: 'PINN',
};

function fmt(v: number, decimals = 4) {
  return v.toExponential(decimals);
}

export default function MetricsTable({ metrics }: Props) {
  const methods = Object.keys(metrics);

  return (
    <div className="metrics-wrapper">
      <h3 className="metrics-title">Métricas de error vs. solución analítica</h3>
      <table className="metrics-table">
        <thead>
          <tr>
            <th>Método</th>
            <th>Error L²</th>
            <th>Error L∞</th>
            <th>Tiempo (s)</th>
          </tr>
        </thead>
        <tbody>
          {methods.map((m) => (
            <tr key={m}>
              <td>{LABELS[m] ?? m}</td>
              <td>{fmt(metrics[m].l2_error)}</td>
              <td>{fmt(metrics[m].linf_error)}</td>
              <td>{metrics[m].execution_time.toFixed(4)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
