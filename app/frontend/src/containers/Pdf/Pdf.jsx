import React from 'react';
import { Navbar } from '../../components'
import { saveAs } from 'file-saver';

import './Pdf.css'

function Pdf() {
    const handleFileChange = (event) => {
        const file = event.target.files[0];

        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => {
            const pdfDataUrl = reader.result;
            const pdfFilename = file.name;

            saveAs(pdfDataUrl, pdfFilename);
        };
    };

    return (
        <div className="app_pdf">
            <Navbar />
            <div className="app_pdf-center">
                <input type="file" accept=".pdf" onChange={handleFileChange} id="import-pdf-input" />
                <label className="app_pdf-button">Ficheiro PDF</label>
            </div>
        </div>
    )
}


export default Pdf