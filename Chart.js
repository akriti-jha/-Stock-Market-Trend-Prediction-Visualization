import React from 'react';
import Plot from 'react-plotly.js';

function Chart({ dates, predicted, actual }) {
  return (
    <Plot
      data={[
        {
          x: dates,
          y: actual,
          type: 'scatter',
          mode: 'lines+markers',
          name: 'Actual',
          line: { color: 'blue' }
        },
        {
          x: dates,
          y: predicted,
          type: 'scatter',
          mode: 'lines+markers',
          name: 'Predicted',
          line: { color: 'red' }
        }
      ]}
      layout={{ title: 'Stock Price Prediction', xaxis: { title: 'Date' }, yaxis: { title: 'Price' } }}
      style={{ width: "100%", height: "500px" }}
    />
  );
}

export default Chart;