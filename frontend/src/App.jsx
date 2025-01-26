import React from 'react'
import Header from "/src/components/Header"
import Inputbox from "/src/components/Inputbox"
import Page from "/src/components/Page"
import { ContextProvider } from './context'


import AllForms from "./components/AllForms";
import Footer from "./components/Footer";

export default function App() {
  return (
    <>
      <Header />
      <Inputbox />
      <ContextProvider>
        <AllForms />
      </ContextProvider>
      <Page />
      <Footer />
      
      
    </>
  )
}


