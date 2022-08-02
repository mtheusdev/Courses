import React from 'react'
import ReactDOM from 'react-dom'
import BomDia from './componentes/BomDia'
import {BoaTarde, BoaNoite} from './componentes/Multiplos'
import Saudacao from './componentes/Saudacao'
import Pai from "./componentes/Pai"
import Filho from './componentes/Filho'
ReactDOM.render( 
    <Pai nome="Arecio" sobrenome="Santos">
        <Filho nome="Matheus"/> 
        <Filho nome="Ana"/>
        <Filho nome="Carla"/> 
    </Pai> , 
document.getElementById('root'))