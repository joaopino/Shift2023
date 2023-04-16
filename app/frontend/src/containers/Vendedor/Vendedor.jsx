import React, { useState } from 'react';
import { Navbar, Pop } from '../../components'
import images from '../../constants'
import { MdOutlineClose } from 'react-icons/md';

import './Vendedor.css'

function Vendedor() {
    const [dados] = useState([
        { data: "16/04", estado: "T" },
        { data: "10/04", estado: "F" },
    ]);

    const [list] = useState([
        { produto: "Batata", quant: "100 Kg" },
        { produto: "Cenoura", quant: "15 Kg" },
        { produto: "Cebola", quant: "30 Kg" },
    ]);

    const [btnPopUp, setBtnPopUp] = useState(false);

    function handlePopUp() {
        setBtnPopUp(!btnPopUp);
    }

    return (
        <div className="app_vendedor">
            <Navbar />
            <div className='app_agricultor-lado2'>
                <div className='app_agricultor-lado'>
                    <div className='app_agricultor-foto'>
                        <img src={images.store} alt="Productor" />
                    </div>
                    <div className='app_agricultor-margin1'>
                        <div className='app_agricultor-nome'>
                            Mega Leguminosas
                        </div>
                        <div className='app_agricultor-loc'>
                            Aveiro
                        </div>
                        <div className='app_agricultor-email'>
                            vendemoslegumes@gmail.com
                        </div>
                    </div>
                </div>
                <div className='app_agricultor-center'>
                    <div className='app_agricultor-icon'><img src={images.reseller} alt="Resseller_icon" /></div>
                    <div className='app_agricultor-star'>
                        <ul>
                            {
                                (() => {
                                    var d = [];
                                    for (let i = 0; i < 3; i++) {
                                        d.push(<img src={images.star_brown} alt="star" />)
                                    }
                                    return d;

                                })()}
                        </ul>

                        <ul>
                            {
                                (() => {
                                    var d = [];
                                    for (let i = 0; i < 2; i++) {
                                        d.push(<img src={images.star_green} alt="star" />)
                                    }
                                    return d;

                                })()}
                        </ul>
                    </div>
                </div>
            </div>
            <div className='app_agricultor-green'>
                <div className='app_agricultor-margin'>
                    <div className='app_agricultor-title'>
                        Painel de controlo
                    </div>
                    <table style={{ lineHeight: "5" }}>
                        <tbody>
                            {dados.map((item) => (
                                <tr key={item.data}>
                                    <td width={"350rem"} className='app_agricultor-prod app_agricultor-prod2' onClick={handlePopUp}>Encomendado</td>
                                    <td width={"180rem"} className='app_agricultor-desc'>{item.data}</td>
                                    {item.estado === "T" ? (
                                        <div>
                                            <td width={"300rem"}>
                                                <button className='app_vendedor-button'>Por aceitar</button>
                                            </td>
                                        </div>
                                    ) : (
                                        <td width={"300rem"}>
                                            <button className='app_agricultor-button-emcurso'>Em distribuição</button>
                                        </td>
                                    )}
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>

            <Pop trigger={btnPopUp} setTrigger={setBtnPopUp}>
                <MdOutlineClose fontSize={27} className='close-btn' onClick={() => { setBtnPopUp(false) }} />
                <div className='app_agricultor-pop'>
                    <span className='app_agricultor-pop-desc-header'>Encomenda</span>
                    <table style={{ lineHeight: "1.5" }}>
                        <tbody>
                            {list.map((item) => (
                                <tr key={item.prod}>
                                    <td width={"180rem"} style = {{textAlign: 'left'}} className='app_agricultor-pop-text'>{item.produto}</td>
                                    <td style = {{textAlign: 'left'}} className='app_agricultor-pop-text'>{item.quant}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                    <div className='app_agricultor-pop-desc-footer'>
                        <div className='app_agricultor-pop-desc-footer-data'>
                            <span className='app_agricultor-pop-desc-footer-total'>Total: </span>
                            <span className='app_agricultor-pop-desc-footer-quant'>400€</span>

                        </div>
                    </div>
                </div>
            </Pop>

        </div>
    )
}

export default Vendedor