import React from 'react'
import { PopNav } from '../index'
import { MdOutlineClose } from 'react-icons/md';
import images from '../../constants'
import './Navbar.css'
import { useNavigate } from 'react-router-dom';

const Navbar = (props) => {
    const [btnPopUp, setBtnPopUp] = React.useState(false);

    function handlePopUp() {
        setBtnPopUp(!btnPopUp);
    }

    const navigate = useNavigate();


    return (
        <nav className='Navbar'>
            <div className="navbar-logo">
                <a href="/#"><img src={images.brown_logo} alt="localee_logo" /></a>
            </div>
            {/* <div className='navbar-rightside'> */}

            {props.showBasket ? (
                <div className="navbar-basket">
                    <img src={images.basket} alt="" onClick={() => {
                        navigate('/pdf')
                    }} />
                </div>
            ) : (
                <div className="navbar-basket">
                    <img src={images.basket} alt="" style={{ opacity: "0" }} />
                </div>

            )}

            {props.showLogin ? (
                <div className="navbar-login">
                    <img src={images.green_little_guy} alt="" onClick={handlePopUp} />
                </div>
            ) : (
                <div className="navbar-login">
                    <a href="/#">
                        <img src={images.green_little_guy} alt="" style={{ opacity: "0" }} />
                    </a>
                </div>

            )}
            {/* </div> */}
            <PopNav trigger={btnPopUp} setTrigger={setBtnPopUp} color="var(--color-green)">
                <MdOutlineClose fontSize={27} className='close-btn1' onClick={() => { setBtnPopUp(false) }} />
                <div className='navbar-pop'>
                    <div className="navbar-container-form">
                        <form action="">
                            {/* if email is manel then redirect to /produtor */}
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
                            <button onClick={() => {
                                // navigate to /produtor using react router 6.10
                                // if email is manel then redirect to /produtor

                                if (document.getElementById('email').value === 'manel@gmail.com') {
                                    navigate('/produtor')
                                }

                                if (document.getElementById('email').value === 'geral@sonae.pt') {
                                    navigate('/revendedor')
                                }


                            }} type="submit">Entrar</button>
                            <button onClick={
                                () => {
                                    navigate('/register')
                                }
                            } type="submit">Registar</button>
                        </div>
                    </div>
                </div>
            </PopNav>
        </nav>
    )
}

export default Navbar