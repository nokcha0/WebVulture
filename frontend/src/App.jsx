import React from 'react'
import Header from "/src/components/Header"
import Inputbox from "/src/components/Inputbox"
import Terminal from "/src/components/Terminal"

export default function App() {
  let [onSubmit, setOnSubmit] = React.useState(false)
  return (
    <>
      <Header />
      <Inputbox />
      {<Terminal />}
    </>
  )
}


