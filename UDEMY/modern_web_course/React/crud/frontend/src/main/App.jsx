import './App.css'
import React from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'font-awesome/css/font-awesome.min.css'

import { HashRouter} from 'react-router-dom'
import Routes from './Routes'

import Logo from '../components/template/Logo'
import Footer from '../components/template/Footer'
import Nav from '../components/template/Nav'

const aux = (props) => {
    return (
        <HashRouter>
            <div className="app">
                <Logo/>
                <Nav/>
                <Routes/>
                <Footer/>
            </div>
        </HashRouter>
    )
   
}

export default aux;