import React from 'react'
import { Navbar } from '../../components'
import images from '../../constants'


import './Landing.css'

function Landing() {

    return (
        <div className="app_landing">
            <Navbar showLogin={true} />
            <section className="app_landing-body">
                <img src={images.logo} alt="Localee_logo" />
            </section>
        </div>
    )
}

export default Landing