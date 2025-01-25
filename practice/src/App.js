import './App.css';
import Kalan from './components/kalan'
import Justin from './components/justin'
import Tyler from './components/tyler'
import Ryan from './components/ryan'
import NiceBox from './components/nicebox'
import Slider from '@mui/material/Slider';
import AttackSlide from './components/attacklvl';
import { ContextProvider } from './context';
import { Checkbox } from '@mui/material';
import ButtonComponent from './components/sendbutton';

function App() {
  return (
    <div className="App">
      <ContextProvider>
        <NiceBox></NiceBox>
        <Slider
        aria-label="Attack Level"
        defaultValue={3}
        valueLabelDisplay="auto"
        shiftStep={1}
        step={1}
        marks
        min={1}
        max={5}
        sx={{width:1000, color: '#000000', left: 50, height: 10}}
      />
      <Checkbox></Checkbox>
      <AttackSlide></AttackSlide>
      <ButtonComponent></ButtonComponent>


        <Kalan name="zaza">
          <p>this is a child</p>
        </Kalan>
        <Justin name='Azelf'>
        </Justin>
        <Tyler></Tyler>
        <Ryan></Ryan>

    </ContextProvider>
    </div>
  );
}

export default App;
