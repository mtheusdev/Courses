import './styles.css'
import { Component } from 'react'
export class Button extends Component {
    render () {
        const {disabled, text, loadMoreClick} = this.props
        return (
            <button
                disabled={disabled}
                className="button"
                onClick={loadMoreClick}
            >{text}</button>
        )
    }
}