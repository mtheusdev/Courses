//action creator recebe novo numoero
export function alterarNumeroMinimo(novoNumero) {
  //retornar action
  return {
    type: 'NUM_MIN_ALTERADO',
    payload: novoNumero
  }

}
export function alterarNumeroMaximo(novoNumero) {
  //retornar action
  return {
    type: 'NUM_MAX_ALTERADO',
    payload: novoNumero
  }

}