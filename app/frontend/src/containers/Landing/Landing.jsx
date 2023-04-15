import React from 'react'
import { Navbar } from '../../components'
import images from '../../constants'

import './Landing.css'

function Landing() {
    return (
        <div className="Landing">
            <div className="Landing-Nav">
                <Navbar />
            </div>
            <section className="Landing-Body">
                <img src={images.logo} alt="Localee_logo" />
            </section>
        </div>
    )
}

export default Landing