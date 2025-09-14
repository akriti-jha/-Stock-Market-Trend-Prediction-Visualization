import React, { useState } from 'react';
import axios from 'axios';

function UploadForm({ onResults }) {
  const [file, setFile] = useState();
  const [isTrained, setIsTrained] = useState(false);

  const handleTrain = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append('file', file);
    await axios.post('http://localhost:8000/train', formData);
    setIsTrained(true);
    alert('Model trained! Now upload a file for prediction.');
  };

  const handlePredict = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append('file', file);
    const res = await axios.post('http://localhost:8000/predict', formData);
    onResults(res.data);
  };

  return (
    <div>
      <input type="file" accept=".csv" onChange={e => setFile(e.target.files[0])} />
      <button onClick={handleTrain}>Train Model</button>
      <button onClick={handlePredict} disabled={!isTrained}>Predict & Visualize</button>
    </div>
  );
}

export default UploadForm;