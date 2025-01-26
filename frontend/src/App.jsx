import React from 'react'
import Header from "/src/components/Header"
import Inputbox from "/src/components/Inputbox"
import Page from "/src/components/Page"
import Footer from "/src/components/Footer"

export default function App() {
  let [onSubmit, setOnSubmit] = React.useState(false)
  return (
    <>
      <Header />
      <Inputbox />
  
      <Page />
      <Footer />
    </>
  )
}


