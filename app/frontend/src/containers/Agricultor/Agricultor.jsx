import React, { useState } from 'react';
import { Navbar, Pop } from '../../components'
import images from '../../constants'
import { MdOutlineClose } from 'react-icons/md';

import './Agricultor.css'

function Agricultor() {
    const [dados] = useState([
        { data: "16/04", estado: "T" },
        { data: "10/04", estado: "F" },
    ]);
    const [produtos] = useState([
        { produto: "Batata", quant: "100 kg", preco: "3€/kg" },
        { produto: "Couve", quant: "35 kg", preco: "2€/kg" },
        { produto: "Cenoura", quant: "10 kg", preco: "2€/kg" },
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
        <div className="app_agricultor">
            <Navbar />
            <div className='app_agricultor-lado2'>
                <div className='app_agricultor-lado'>
                    <div className='app_agricultor-foto'>
                        <img src={images.pino} alt="Productor" />
                    </div>
                    <div className='app_agricultor-margin1'>
                        <div className='app_agricultor-nome'>
                            João Pino
                        </div>
                        <div className='app_agricultor-loc'>
                            Aveiro
                        </div>
                        <div className='app_agricultor-email'>
                            joaopinao@gmail.com
                        </div>
                    </div>
                </div>
                <div className='app_agricultor-center'>
                    <div className='app_agricultor-icon'><img src={images.farmer} alt="Productor_icon" /></div>
                    <div className='app_agricultor-star'>
                        <ul>
                            {
                                (() => {
                                    var d = [];
                                    for (let i = 0; i < 4; i++) {
                                        d.push(<img src={images.star_brown} alt="star" />)
                                    }
                                    return d;

                                })()}
                        </ul>

                        <ul>
                            {
                                (() => {
                                    var d = [];
                                    for (let i = 0; i < 1; i++) {
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
                                    <td width={"300rem"} className='app_agricultor-prod app_agricultor-prod2' onClick={handlePopUp}>Encomenda</td>
                                    <td width={"170rem"} className='app_agricultor-desc'>{item.data}</td>
                                    {item.estado === "T" ? (
                                        <div>
                                            <td width={"300rem"}>
                                                <button className='app_agricultor-button'>Aceitar</button>
                                            </td>
                                            <td width={"300rem"}>
                                                <button className='app_agricultor-button'>Eliminar</button>
                                            </td>
                                        </div>
                                    ) : (
                                        <td width={"300rem"}>
                                            <button className='app_agricultor-button-emcurso'>Em curso</button>
                                        </td>
                                    )}
                                </tr>
                            ))}
                        </tbody>
                    </table>

                    <br /><br /><br /><br /><br />

                    <div className='app_agricultor-title'>
                        Anuncios
                    </div>
                    <table style={{ lineHeight: "5" }}>
                        <tbody>
                            {produtos.map((item) => (
                                <tr key={item.produto}>
                                    <td width={"250rem"} className='app_agricultor-prod'>{item.produto}</td>
                                    <td width={"200rem"} className='app_agricultor-desc'>{item.quant}</td>
                                    <td width={"200rem"} className='app_agricultor-prod'>{item.preco}</td>
                                    <td width={"300rem"}>
                                        <button className='app_agricultor-button'>Editar</button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                    <br />
                    <button className='app_agricultor-button-emcurso app_agricultor-adicionar'>Adicionar</button>
                </div>
            </div>

            <Pop trigger={btnPopUp} setTrigger={setBtnPopUp}>
                <MdOutlineClose fontSize={27} className='close-btn' onClick={() => { setBtnPopUp(false) }} />
                <div className='app_agricultor-pop'>
                    <div className="app_agricultor-pop-header">
                        <span className='app_agricultor-pop-title'>Mega Leguminosas</span>
                        <span className='app_agricultor-pop-local'>Aveiro</span>
                        <span className='app_agricultor-pop-email'>vendemoslegumes@gmail.com</span>
                    </div>
                    <div className='app_agricultor-pop-desc'>
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
                    </div>
                    <div className='app_agricultor-pop-desc-footer'>
                        <div className='app_agricultor-pop-desc-footer-data'>
                            <span className='app_agricultor-pop-desc-footer-total'>Total: </span>
                            <span className='app_agricultor-pop-desc-footer-quant'>400€</span>

                        </div>
                        <div className='app_agricultor-pop-desc-footer-buttons'>
                            <button className='app_agricultor-button'>Aceitar</button>
                            <button className='app_agricultor-button'>Eliminar</button>
                        </div>
                    </div>
                </div>
            </Pop>
        </div>
    )
}

export default Agricultor