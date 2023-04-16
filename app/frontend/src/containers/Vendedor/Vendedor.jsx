import React, { useState, useNavigate } from 'react';
import { Navbar, Pop } from '../../components'
import images from '../../constants'
import useFetch from '../../hooks/useFetch.js'

import './Vendedor.css'

function Vendedor() {
    const [dados, setDados] = useState([
        { data: "16/04", estado: "T" },
        { data: "10/04", estado: "F" },
    ]);

    const {loading:userLoading,error:userError,data:userData} = useFetch("http://localhost:1337/api/users/6?filters[tipo][$eq]=Revendedor")
    const {loading: encomendasloading,error: encomendaserror,data: encomendasData} = useFetch("http://localhost:1337/api/encomendas?populate=anuncios")


    if(userLoading | encomendasloading) return <p>Loading...</p>
    if(userError | encomendaserror ) return <p>ERROR</p>
    //console.log(encomendasData.data[0])

    encomendasData.data.map((encomendas) => {
        const array =  encomendas.attributes.anuncios.data
        array.forEach(element => {
            console.log(element.attributes.tipo_de_produto + " " + element.attributes.quantidade )
        });

    })

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
                            {userData.username}
                        </div>
                        <div className='app_agricultor-loc'>
                            {userData.localizacao}
                        </div>
                        <div className='app_agricultor-email'>
                            {userData.email}
                        </div>
                    </div>
                </div>
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
            <div className='app_agricultor-green'>
                <div className='app_agricultor-margin'>
                    <div className='app_agricultor-title'>
                        Painel de controlo
                    </div>
                    <table style={{ lineHeight: "5" }}>
                        <tbody>
                            {dados.map((item) => (


                                <tr key={item.data}>
                                    <td width={"350rem"} className='app_agricultor-prod'><a href=''>Encomendado</a></td>
                                    <td width={"180rem"} className='app_agricultor-desc'>{item.data}</td>
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