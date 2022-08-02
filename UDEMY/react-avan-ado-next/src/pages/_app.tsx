import { AppProps } from 'next/dist/shared/lib/router/router'
import Head from 'next/head'
import GlobalStyles from 'styles/global'

function App({ Component, pageProps }: AppProps) {
  return (
    <>
      <Head>
        <title>React Avançado - Boilerplate</title>
        <link rel="shortcut icon" href="/img/logo.svg" />
        <link rel="apple-touch-icon" href="/img/logo.svg" />
        <link rel="manifest" href="/manifest.json" />
        <meta
          name="description"
          content="A simple project to work with TypeScript, React, NextJS and Styled Components"
        />
      </Head>
      <GlobalStyles />
      <Component {...pageProps} />
    </>
  )
}

export default App
