import React, { useState, useEffect } from 'react';
import axios from 'axios';

function HelloWorld() {
  const [message, setMessage] = useState('');
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = () => {
    if (!selectedFile) {
      alert('Please select a file to upload.');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    axios.post('http://localhost:8000/api/upload-spreadsheet/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    })
    .then(response => {
      // Handle response as needed
      console.log(response.data);
    })
    .catch(error => {
      console.error('Error uploading file:', error);
    });
  };

  useEffect(() => {
    axios.get('http://localhost:8000/api/hello-world/')
      .then(response => {
        setMessage(response.data.message);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <div>
      <h1>Spreadsheet file upload</h1>
      <p>{message}</p>
      <br></br>
      <input type="file" onChange={handleFileChange} />
      <br></br>
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}

export default HelloWorld;
