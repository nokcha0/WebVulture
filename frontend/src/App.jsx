import React from 'react'
import Header from "/src/components/Header"
import Page from "/src/components/Page"
import { ContextProvider } from './context'
import AllForms from "./components/AllForms";
import Footer from "./components/Footer";

export default function App() {
  return (
    <>
      <Header />
      <ContextProvider>
        <AllForms />
      </ContextProvider>
      <Page />
      <Footer />
    </>
  )
}


