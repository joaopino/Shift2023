import React, { useState, useNavigate } from 'react';
import { Navbar, Pop } from '../../components'
import images from '../../constants'

import './Vendedor.css'

function Vendedor() {
    const [dados, setDados] = useState([
        { produto: "Batata", quant: "100 kg", preco: "300€", estado: "T" },
        { produto: "Cenoura", quant: "10 kg", preco: "20€", estado: "F" },
    ]);

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
            <div className='app_agricultor-green'>
                <div className='app_agricultor-margin'>
                    <div className='app_agricultor-title'>
                        Painel de controlo
                    </div>
                    <table style={{ lineHeight: "5" }}>
                        <tbody>
                            {dados.map((item) => (
                                <tr key={item.produto}>
                                    <td width={"400rem"} className='app_agricultor-prod'><a href=''>Encomendado</a></td>
                                    <td width={"300rem"} className='app_agricultor-desc'>{item.produto}</td>
                                    <td width={"300rem"} className='app_agricultor-desc'>{item.quant}</td>
                                    {item.estado === "T" ? (
                                        <div>
                                            <td width={"300rem"}>
                                                <button className='app_agricultor-button'>Por aceitar</button>
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
        </div>
    )
}

export default Vendedor