import React, { useState } from 'react';
import UploadForm from './components/UploadForm';
import Chart from './components/Chart';
import Insights from './components/Insights';
import './App.css';

function App() {
  const [data, setData] = useState(null);

  const handleResults = (results) => {
    setData(results);
  };

  return (
    <div className="App">
      <h1>Stock Market Trend Prediction & Visualization</h1>
      <UploadForm onResults={handleResults} />
      {data && (
        <>
          <Chart dates={data.dates} predicted={data.predicted} actual={data.actual} />
          <Insights dates={data.dates} signals={data.insights} />
        </>
      )}
    </div>
  );
}

export default App;