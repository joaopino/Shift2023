import React from 'react'
import images from '../../constants'
import './Navbar.css'

const Navbar = () => {
    // const [toggleMenu, setToggleMenu] = React.useState(false);

    return (
        <nav className='Navbar'>
            <div className="navbar-logo">
                <a href="/#"><img src={images.brown_logo} alt="localee_logo" /></a>
            </div>

            <div className="navbar-login">
                <img src={images.green_little_guy} alt="" />
            </div>
        </nav>
    )
}

export default Navbar