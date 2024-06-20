import React, { useState } from 'react';
import axios from 'axios';
import './OCRUpload.css';

function OCRUpload() {
    const [file, setFile] = useState(null);
    const [text, setText] = useState('');
    const [uploadError, setUploadError] = useState('');

    const handleFileChange = (event) => {
        setFile(event.target.files[0]);
        setText('');  // Clear the text when a new file is selected
        setUploadError('');
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        if (!file) {
            setUploadError('Please select a file first.');
            return;
        }
        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('http://127.0.0.1:8000/ocr/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            console.log('Server response:', response.data);  // Debug: Log the response
            if (response.data.error) {
                setUploadError(response.data.error);
            } else {
                setText(response.data.text);
                setUploadError('');
            }
        } catch (error) {
            console.error('Error uploading file:', error);
            setUploadError('Error uploading file.');
        }
    };

    return (
        <div className="container">
            <h1>OCR Upload Tool</h1>
            <form onSubmit={handleSubmit} className="form">
                <input type="file" onChange={handleFileChange} className="file-input" />
                <button type="submit" className="button">Upload</button>
            </form>
            {file && <p>Selected file: {file.name}</p>}
            {uploadError && <p className="error">{uploadError}</p>}
            <div className="text-container">
                <h2>Extracted Text</h2>
                <textarea value={text} readOnly rows={10} cols={50} />
            </div>
        </div>
    );
}

export default OCRUpload;
