import type { HeatParams, PINNOptions } from '../types';

interface Props {
  params: HeatParams;
  pinnOpts: PINNOptions;
  loading: boolean;
  onParamsChange: (p: Partial<HeatParams>) => void;
  onPINNOptsChange: (o: Partial<PINNOptions>) => void;
  onSolve: () => void;
  onCompare: () => void;
}

interface NumFieldProps {
  label: string;
  value: number;
  min?: number;
  max?: number;
  step?: number;
  onChange: (v: number) => void;
  disabled?: boolean;
}

function NumField({ label, value, min, max, step = 1, onChange, disabled }: NumFieldProps) {
  return (
    <div className="field">
      <label className="field-label">{label}</label>
      <input
        type="number"
        className="field-input"
        value={value}
        min={min}
        max={max}
        step={step}
        disabled={disabled}
        onChange={(e) => onChange(parseFloat(e.target.value))}
      />
    </div>
  );
}

export default function Sidebar({
  params,
  pinnOpts,
  loading,
  onParamsChange,
  onPINNOptsChange,
  onSolve,
  onCompare,
}: Props) {
  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <span className="sidebar-title">Ecuación de Calor 1D</span>
        <span className="sidebar-subtitle">∂u/∂t = α ∂²u/∂x²</span>
      </div>

      <section className="sidebar-section">
        <h4 className="section-title">Parámetros físicos</h4>
        <NumField
          label="α (difusividad)"
          value={params.alpha}
          min={0.001}
          max={1}
          step={0.001}
          onChange={(v) => onParamsChange({ alpha: v })}
        />
        <NumField
          label="L (longitud)"
          value={params.L}
          min={0.1}
          max={10}
          step={0.1}
          onChange={(v) => onParamsChange({ L: v })}
        />
        <NumField
          label="T (tiempo total)"
          value={params.T}
          min={0.1}
          max={10}
          step={0.1}
          onChange={(v) => onParamsChange({ T: v })}
        />
        <NumField
          label="Nx (puntos espaciales)"
          value={params.Nx}
          min={10}
          max={500}
          step={10}
          onChange={(v) => onParamsChange({ Nx: v })}
        />
        <NumField
          label="Nt (pasos temporales)"
          value={params.Nt}
          min={10}
          max={500}
          step={10}
          onChange={(v) => onParamsChange({ Nt: v })}
        />
      </section>

      <section className="sidebar-section">
        <h4 className="section-title">PINN</h4>
        <div className="field">
          <label className="checkbox-label">
            <input
              type="checkbox"
              checked={pinnOpts.load_pretrained}
              onChange={(e) => onPINNOptsChange({ load_pretrained: e.target.checked })}
            />
            Cargar modelo preentrenado
          </label>
        </div>
        <div className="field">
          <label className="checkbox-label">
            <input
              type="checkbox"
              checked={pinnOpts.train}
              onChange={(e) => onPINNOptsChange({ train: e.target.checked })}
            />
            Entrenar modelo nuevo
          </label>
        </div>
        <NumField
          label="Épocas (Adam)"
          value={pinnOpts.epochs}
          min={100}
          max={10000}
          step={100}
          disabled={!pinnOpts.train}
          onChange={(v) => onPINNOptsChange({ epochs: v })}
        />
        <NumField
          label="Learning rate"
          value={pinnOpts.lr}
          min={0.0001}
          max={0.01}
          step={0.0001}
          disabled={!pinnOpts.train}
          onChange={(v) => onPINNOptsChange({ lr: v })}
        />
        <div className="field">
          <label className="checkbox-label">
            <input
              type="checkbox"
              checked={pinnOpts.use_lbfgs}
              disabled={!pinnOpts.train}
              onChange={(e) => onPINNOptsChange({ use_lbfgs: e.target.checked })}
            />
            Refinamiento LBFGS
          </label>
        </div>
      </section>

      <div className="sidebar-actions">
        <button className="btn btn-primary" onClick={onSolve} disabled={loading}>
          {loading ? 'Calculando…' : 'Resolver'}
        </button>
        <button className="btn btn-secondary" onClick={onCompare} disabled={loading}>
          {loading ? 'Calculando…' : 'Comparar métodos'}
        </button>
      </div>
    </aside>
  );
}
