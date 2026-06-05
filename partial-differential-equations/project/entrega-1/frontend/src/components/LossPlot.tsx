import Plot from 'react-plotly.js';
import type { Data } from 'plotly.js';

interface Props {
  lossHistory: number[];
}

export default function LossPlot({ lossHistory }: Props) {
  const iters = lossHistory.map((_, i) => i);

  const trace: Data = {
    type: 'scatter',
    mode: 'lines',
    x: iters,
    y: lossHistory,
    line: { color: '#6366f1', width: 2 },
    name: 'Loss total',
  } as Data;

  return (
    <Plot
      data={[trace]}
      layout={{
        title: { text: 'Curva de pérdida PINN', font: { size: 15 } },
        xaxis: { title: 'Iteración' },
        yaxis: { title: 'Loss', type: 'log' },
        margin: { t: 50, r: 20, b: 50, l: 70 },
        paper_bgcolor: 'transparent',
        plot_bgcolor: '#fafafa',
      }}
      style={{ width: '100%', height: '300px' }}
      config={{ responsive: true, displayModeBar: false }}
      useResizeHandler
    />
  );
}
