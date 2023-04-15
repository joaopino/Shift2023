import React from 'react'
import images from '../../constants'
import './Navbar.css'

const Navbar = () => {
    return (
        <nav className='Navbar'>
            <div className="navbar-logo">
                <a href="/#"><img src={images.brown_logo} alt="localee_logo" /></a>
            </div>

            <div className="navbar-login">
                <a href="/#">
                    <img src={images.green_little_guy} alt="" />
                </a>
            </div>
        </nav>
    )
}

export default Navbar