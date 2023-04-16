import React, { useState } from 'react';
import { Navbar, Pop } from '../../components'
import images from '../../constants'
import { saveAs } from 'file-saver';

import './List.css'

function List() {
    const [dados, setDados] = useState([
        { produto: "Batata", quant: "10kg", nome: "António Silva", preco: "20€" },
        { produto: "Cenoura", quant: "5kg", nome: "Manuel Machado", preco: "25€" },
        { produto: "Couve", quant: "20kg", nome: "Manuel Santos", preco: "40€" },
        { produto: "Batata", quant: "10kg", nome: "António Silva", preco: "20€" },
        { produto: "Cenoura", quant: "5kg", nome: "Manuel Machado", preco: "25€" },
        { produto: "Couve", quant: "20kg", nome: "Manuel Santos", preco: "40€" },
    ]);

    return (
        <div className="app_list">
            <Navbar />
            <div className='app_list-margin'>
                <div className='app_list-header'>
                    <p className='app_agricultor-title'>Total:</p>
                    <p style={{color: "var(--color-green-button)"}} className='app_agricultor-title'>450€</p>
                    <p className='app_agricultor-title app_list-sep'>Data de entrega:</p>
                    <p style={{color: "var(--color-green-button)"}} className='app_agricultor-title'>25 de abril</p>
                </div>
                <table style={{ lineHeight: "20" }}>
                    <tbody>
                        <div className="app_list-box">
                        {dados.map((item) => (
                            <div className="app_list-linha">
                                <tr key={item.data}>
                                    <td width={"400rem"} className='app_agricultor-prod app_list-pad'>{item.produto}</td>
                                    <td width={"300rem"} className='app_agricultor-desc'>{item.quant}</td>
                                    <td width={"500rem"} className='app_agricultor-desc'>{item.nome}</td>
                                    <td className='app_agricultor-prod app_list-pad2'>{item.preco}</td>
                                </tr>
                            </div>
                        ))}
                        </div>
                    </tbody>
                </table>
            </div>
        </div>
    )
}

export default List