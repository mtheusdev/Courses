import PageTitle from '../../components/layout/PageTitle'
import React, { useState } from 'react';
import SectionTitle from '../../components/layout/SectionTitle';

const UseState = (props) => {
    const [count, setCount] = useState(0)
    const [name, setName] = useState('')
    return (
        <div className="UseState">
            <PageTitle
                title="Hook UseState"
                subtitle="Estado em componentes funcionais!"
            />
            <SectionTitle title="Exercicio #1"/>
            <div className="center">
                <span className="text">{count}</span>
                <div>
                    <button onClick={() => setCount(count-1)} className="btn">-1</button>
                    <button onClick={() => setCount(c => c +1)} className="btn">+1</button>
                </div>
            </div>
            <SectionTitle title="Exercicio #2"/>
            <input type="text" className="input" value={name} onChange={e => setName(e.target.value)}/>
            <span className="text">{name}</span>
        </div>
    )
}

export default UseState
