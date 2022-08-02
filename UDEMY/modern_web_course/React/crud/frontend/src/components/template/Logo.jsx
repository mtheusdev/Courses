import './Logo.css'
import React from 'react'
import logo from '../../assets/imgs/logo.png'
const aux = (props) => {
    return(
        <aside className="logo">
            <a href="/" className="logo">
                <img src={logo} alt="logo"/>
            </a>
        </aside>
    )

}

export default aux;