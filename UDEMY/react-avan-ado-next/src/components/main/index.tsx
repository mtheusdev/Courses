import * as S from './styles'
const Main = ({
  title = 'React Avançado',
  description = 'React, Types, Next e Styled'
}) => (
  <S.Wrapper>
    <S.logo
      src="/img/logo.svg"
      alt="Imagem de um átomo e React Avançado escrito ao lado"
    />
    <S.Title>{title}</S.Title>
    <S.Description>{description}</S.Description>
    <S.Illustration
      src="/img/hero-illustration.svg"
      alt="Desenvolvedor de frente para a tela com código"
    />
  </S.Wrapper>
)

export default Main
