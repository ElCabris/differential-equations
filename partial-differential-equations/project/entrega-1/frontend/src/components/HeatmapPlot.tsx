import Plot from 'react-plotly.js';
import type { Data } from 'plotly.js';
import type { SolutionData } from '../types';

interface Props {
  data: SolutionData;
  title: string;
  colorscale?: string;
}

export default function HeatmapPlot({ data, title, colorscale = 'Magma' }: Props) {
  const trace: Data = {
    type: 'heatmap',
    x: data.x,
    y: data.t,
    z: data.u,
    colorscale,
    colorbar: { title: 'u(x,t)' },
  } as Data;

  return (
    <Plot
      data={[trace]}
      layout={{
        title: { text: title, font: { size: 15 } },
        xaxis: { title: 'Posición x', showgrid: false },
        yaxis: { title: 'Tiempo t', showgrid: false },
        margin: { t: 50, r: 20, b: 50, l: 60 },
        paper_bgcolor: 'transparent',
        plot_bgcolor: 'transparent',
      }}
      style={{ width: '100%', height: '420px' }}
      config={{ responsive: true, displayModeBar: false }}
      useResizeHandler
    />
  );
}
