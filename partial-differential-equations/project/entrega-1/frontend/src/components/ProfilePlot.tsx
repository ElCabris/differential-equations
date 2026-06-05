import Plot from 'react-plotly.js';
import type { Data } from 'plotly.js';
import type { SolutionData } from '../types';

interface Props {
  datasets: { data: SolutionData; name: string; color: string }[];
  title?: string;
  /** Fraction of T at which to show profiles [0..1] */
  timeFractions?: number[];
}

const DEFAULT_FRACTIONS = [0, 0.25, 0.5, 0.75, 1.0];
const DASHES = ['solid', 'dash', 'dot', 'dashdot', 'longdash'] as const;

export default function ProfilePlot({
  datasets,
  title = 'Perfiles de temperatura',
  timeFractions = DEFAULT_FRACTIONS,
}: Props) {
  const traces: Data[] = [];

  datasets.forEach(({ data, name, color }, di) => {
    timeFractions.forEach((frac, fi) => {
      const tIdx = Math.round(frac * (data.t.length - 1));
      const tVal = data.t[tIdx].toFixed(2);
      traces.push({
        type: 'scatter',
        mode: 'lines',
        x: data.x,
        y: data.u[tIdx],
        name: `${name} t=${tVal}`,
        line: {
          color,
          dash: DASHES[fi % DASHES.length],
          width: di === 0 ? 2 : 1.5,
        },
      } as Data);
    });
  });

  return (
    <Plot
      data={traces}
      layout={{
        title: { text: title, font: { size: 15 } },
        xaxis: { title: 'Posición x', showgrid: true, gridcolor: '#eee' },
        yaxis: { title: 'Temperatura u', showgrid: true, gridcolor: '#eee' },
        legend: { orientation: 'v', font: { size: 11 } },
        margin: { t: 50, r: 20, b: 50, l: 60 },
        paper_bgcolor: 'transparent',
        plot_bgcolor: '#fafafa',
      }}
      style={{ width: '100%', height: '420px' }}
      config={{ responsive: true, displayModeBar: false }}
      useResizeHandler
    />
  );
}
