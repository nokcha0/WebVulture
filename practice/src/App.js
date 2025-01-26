import './App.css';
import AttackSlide from './components/attacklvl';
import { ContextProvider } from './context';
import ButtonComponent from './components/sendbutton';
import ThreadSlide from './components/threads';
import UrlInput from './components/urlinput';
import CmdInput from './components/cmdinput';
import DumpCheck from './components/dumpcheck';
import FlushCheck from './components/flushcheck';

function App() {
  return (
    <div className="App">
      <ContextProvider>
      <FlushCheck></FlushCheck>
      <DumpCheck></DumpCheck>
      <UrlInput></UrlInput>
      <CmdInput></CmdInput>
      <AttackSlide></AttackSlide>
      <ThreadSlide></ThreadSlide>
      <ButtonComponent></ButtonComponent>
      </ContextProvider>
    </div>
  );
}

export default App;
