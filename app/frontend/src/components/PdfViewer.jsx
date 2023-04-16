import React, { useState } from 'react';
import { Document, Page } from 'react-pdf';
import { extract } from "@openai/pdf-extractor";

function PdfViewer(props) {
    const [numPages, setNumPages] = useState(null);
    const [pageNumber, setPageNumber] = useState(1);
    const [pdfData, setPdfData] = useState("");

    async function onDocumentLoadSuccess({ numPages }) {
        setNumPages(numPages);
        const buffer = await props.file.arrayBuffer();
        const data = await extract(buffer);
        setPdfData(data.text);
    }

    return (
        <>
            <Document file={props.file} onLoadSuccess={onDocumentLoadSuccess}>
                <Page pageNumber={pageNumber} />
            </Document>
            <p>Page {pageNumber} of {numPages}</p>
            <p>{pdfData}</p>
        </>
    );
}

export default PdfViewer;