import React from 'react'
import './Button.css'

const aux = (props) => {
    let classes = 'button '

    classes += props.operation ? 'operation' : ''
    classes += props.double ? 'double' : ''
    classes += props.triple ? 'triple' : ''

    return (
        <React.StrictMode>
            <button 
                onClick={e => props.click && props.click(props.label)}
                className={classes}>
                {props.label}
            </button>
        </React.StrictMode>
    )
}
    
export default aux