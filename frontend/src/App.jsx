import React from 'react'
import Header from "/src/components/Header"
import Inputbox from "/src/components/Inputbox"
import Page from "/src/components/Page"
import { ContextProvider } from './context'
import ButtonComponent from './components/sendbutton'

import AttackSlide from './components/attacklvl';
import ThreadSlide from './components/threads';
import UrlInput from './components/urlinput';
import CmdInput from './components/cmdinput';
import DumpCheck from './components/dumpcheck';
import FlushCheck from './components/flushcheck';

export default function App() {
  return (
    <>
      <Header />
      <Inputbox />
      <ContextProvider>
        <FlushCheck></FlushCheck>
        <DumpCheck></DumpCheck>
        <UrlInput></UrlInput>
        <CmdInput></CmdInput>
        <AttackSlide></AttackSlide>
        <ThreadSlide></ThreadSlide>
        <ButtonComponent></ButtonComponent>
      </ContextProvider>
      <Page />
      
    </>
  )
}


