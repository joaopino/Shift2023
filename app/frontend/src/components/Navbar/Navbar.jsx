import React from 'react'
import { PopNav } from '../index'
import { MdOutlineClose } from 'react-icons/md';
import images from '../../constants'
import './Navbar.css'

const Navbar = (props) => {
    const [btnPopUp, setBtnPopUp] = React.useState(false);

    function handlePopUp() {
        setBtnPopUp(!btnPopUp);
    }
    return (
        <nav className='Navbar'>
            <div className="navbar-logo">
                <a href="/#"><img src={images.brown_logo} alt="localee_logo" /></a>
            </div>
            {props.showLogin ? (
                <div className="navbar-login">
                    <a href="/#">
                        <img src={images.green_little_guy} alt="" onClick={handlePopUp} />
                    </a>
                </div>
            ) : (
                <div className="navbar-login">
                    <a href="/#">
                        <img src={images.green_little_guy} alt="" style={{ opacity: "0" }} />
                    </a>
                </div>

            )}
            <PopNav trigger={btnPopUp} setTrigger={setBtnPopUp} color="var(--color-green)">
                <MdOutlineClose fontSize={27} className='close-btn' onClick={() => { setBtnPopUp(false) }} />
                <div className='navbar-pop'>
                    <div className="navbar-container-form">
                        <form action="">
                            <div className="navbar-email">
                                <label htmlFor="email">Email</label>
                                <input type="email" name="email" id="email" />
                            </div>

                            <div className="navbar-password">
                                <label htmlFor="password">Pass</label>
                                <input type="password" name="password" id="password" />
                            </div>
                        </form>
                        <div className="navbar-container-submit">
                            <button type="submit">Entrar</button>
                            <button type="submit">Registar</button>
                        </div>
                    </div>
                </div>
            </PopNav>
        </nav>
    )
}

export default Navbar