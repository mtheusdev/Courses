import React, {useState, useEffect} from 'react'
import PageTitle from '../../components/layout/PageTitle'
import SectionTitle from '../../components/layout/SectionTitle';

function calcFatorial(num) {
    const n = parseInt(num)
    if (n < 0) return -1
    if(n === 0 ) return 1
    return calcFatorial(n - 1) * n
}
function calcPairOrOdd(num) {
    const n = parseInt(num)
    if (n % 2 === 0) return 'par'
    else return 'impar'
}
const UseEffect = (props) => {
    const [number, setNumber] = useState(1)
    const [fatorial, setFatorial] = useState(1)
    const [pairOrOdd, setPairOrOdd] = useState(1)
    useEffect(function () {
        setFatorial(calcFatorial(number))
    }, [number])

    useEffect(function () {
        setPairOrOdd(calcPairOrOdd(number))
    }, [number])
    return (
        <div className="UseEffect">
            <PageTitle
                title="Hook UseEffect"
                subtitle="Permite executar efeitos colaterais em componentes funcionais!"
            />
            <SectionTitle title="Exercicio #01"/>
            <div className="center">
                <div>
                    <span className="text">Fatorial: </span>
                    <span className="text red">{fatorial}</span>
                </div> 
                <input onChange={e => setNumber(e.target.value)} type="number" className="input" value={number}/>
            </div>
            <SectionTitle title="Exercicio #02"/>
            <div className="center">
                <div>
                    <span className="text">Par ou Impar: </span>
                    <span className="text red">{pairOrOdd}</span>
                </div>
            </div>
        </div>
    )
}

export default UseEffect
