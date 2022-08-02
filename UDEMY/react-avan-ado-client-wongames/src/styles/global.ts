import { createGlobalStyle, css } from 'styled-components'

const GlobalStyles = createGlobalStyle`

  @font-face {
    font-family: 'Poppins';
    font-style: normal;
    font-weight: 300;
    font-display: swap; /* Carregar font parecida caso a Poppins ainda não tenha carregado (impedir pagina em branco) */
    src: local(''),
        url('/fonts/poppins-v15-latin-300.woff2') format('woff2'); /* Chrome 26+, Opera 23+, Firefox 39+ */
  }

  @font-face {
    font-family: 'Poppins';
    font-style: normal;
    font-weight: 400;
    font-display: swap; /* Carregar font parecida caso a Poppins ainda não tenha carregado (impedir pagina em branco) */
    src: local(''),
        url('/fonts/poppins-v15-latin-regular.woff2') format('woff2'); /* Chrome 26+, Opera 23+, Firefox 39+ */
  }

  @font-face {
    font-family: 'Poppins';
    font-style: normal;
    font-weight: 600;
    font-display: swap; /* Carregar font parecida caso a Poppins ainda não tenha carregado (impedir pagina em branco) */
    src: local(''),
        url('/fonts/poppins-v15-latin-600.woff2') format('woff2'); /* Chrome 26+, Opera 23+, Firefox 39+ */
  }

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    -webkit-font-smoothing: antialiased; /* Tirar serrilhado do Mac */
    -moz-osx-font-smoothing: grayscale; /* Tirar serrilhado do Firefox */
  }


  ${({ theme }) => css`
    html {
      font-size: 62.5%;
    }

    body {
      font-family: ${theme.font.family};
      font-size: ${theme.font.sizes.medium};
    }
  `}

`

export default GlobalStyles
