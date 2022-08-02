import React from 'react'
import Main from '../template/Main'

const aux = (props) => {
    return (
        <Main icon="home" title="Início" subtitle="Projeto Crud de Users em ReactJS">
            <div className="display-4">Bem Vindo!</div>
            <hr/>
            <p className="mb-0">Sistema para exemplificar a construção de um cadastro desenvolvido em ReactJS!</p>
        </Main>
    )
}

export default aux;