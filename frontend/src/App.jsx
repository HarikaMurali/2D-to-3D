import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [file, setFile] = useState(null);
  const [downloadUrl, setDownloadUrl] = useState("");

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("image", file);

    const response = await axios.post("http://localhost:8000/upload", formData, {
      responseType: 'blob'
    });

    const blob = new Blob([response.data]);
    const url = window.URL.createObjectURL(blob);
    setDownloadUrl(url);
  };

  return (
    <div className="App">
      <h2>Floorplan to 3D Model</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Generate 3D</button>
      {downloadUrl && <a href={downloadUrl} download="output.glb">Download 3D Model</a>}
    </div>
  );
}

export default App;
