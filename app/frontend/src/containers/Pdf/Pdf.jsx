import React, { useState } from 'react';
import { Navbar, Pop } from '../../components'
import images from '../../constants'

import './Pdf.css'

function Pdf() {
    return (
        <div className="app_pdf">
            <Navbar />
            <div className='app_pdf-center'>
                <button className='app_pdf-button'>Ficheiro PDF</button>
            </div>
        </div>
    )
}

export default Pdf