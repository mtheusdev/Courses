import './Header.css'
import React from 'react'

const aux = (props) => {
    return(
        <header className="header d-none d-sm-flex flex-column">
            <h1 className="mt3">
                <i className={`fa fa-${props.icon}`}></i> {props.title}
            </h1>
            <p className="lead text-muted">{props.subtitle}</p>
        </header>
    )
}

export default aux;