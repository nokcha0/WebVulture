
import Slider from '@mui/material/Slider';

import { Context } from '../context';
import React, { useContext } from 'react';


export const AttackSlide = (props) => {
  const { attackValue, handleAttackChange } = useContext(Context);
  var attackText = "Attack Level 1: Basic Scanning, Minimal Payloads"

    if (attackValue === 1) {
        attackText = "Attack Level 1: Basic Scanning, Minimal Payloads"
    }
    if (attackValue === 2) {
        attackText = "Attack Level 2: Basic Scanning, Moderate Payloads"
    }
    if (attackValue === 3) {
        attackText = "Attack Level 3: Balanced Intrusion"
    }
    if (attackValue === 4) {
        attackText = "Attack Level 4: Aggressive Intrusion"
    }
    if (attackValue === 5) {
        attackText = "Attack Level 5: Maximum Strength, High Risk"
    }

  return (
    <div>
      <p className="sliderText">{attackText}</p>
      <Slider
        aria-label="Attack Level"
        defaultValue={1}
        valueLabelDisplay="off"
        onChange={handleAttackChange}
        shiftStep={1}
        step={1}
        marks
        min={1}
        max={5}
        sx={{ width: 400, left: 50, height: '10px', borderRadius: '0px',

        color: '#ff5733', // Change the color of the slider
        '& .MuiSlider-track': {
          opacity: 0,
          //background: 'linear-gradient(to right,rgb(0, 255, 42),rgb(255, 0, 0))', // Gradient for the track
        },
        '& .MuiSlider-rail': {
          background: 'linear-gradient(to right, #00CA4E, #FFBD44 , #FF605C)',
          opacity: 1, // Background for the rail
          border: '0px solid #0f100f',
          width: '100%',
          borderRadius: '6px',
        },  

        '&:focus, &:hover, &.Mui-focusVisible': {
          boxShadow: 'none', // Remove the focus outline (blue glow)
        },
        
        '& .MuiSlider-thumb': {
          background: '#000000', // Gradient for the thumb
          boxShadow: '0px 0px 8px rgba(0, 0, 0, 0.3)', // Optional glow
          border: '1px solid #162521',
          height: '10px',
          width: '10px',
        },

        '& .MuiSlider-mark': {
      display: 'none', // Hide the discrete marker dots
        },
         }}
      />
    </div>
  );
};

export default AttackSlide