import '../App.css';
import Slider from '@mui/material/Slider';

import { Context } from '../context';
import React, { useContext } from 'react';


export const AttackSlide = (props) => {
  const { sliderValue, handleSliderChange } = useContext(Context);

  return (
    <div>
      <Slider
        aria-label="Attack Level"
        defaultValue={3}
        valueLabelDisplay="auto"
        onChange={handleSliderChange}
        shiftStep={1}
        step={1}
        marks
        min={1}
        max={5}
        sx={{ width: 300, left: 50, height: '10px', borderRadius: '0px',

        color: '#ff5733', // Change the color of the slider
        '& .MuiSlider-track': {
          opacity: 0,
          //background: 'linear-gradient(to right,rgb(0, 255, 42),rgb(255, 0, 0))', // Gradient for the track
        },
        '& .MuiSlider-rail': {
          background: 'linear-gradient(to right,rgb(0, 255, 0), rgb(255, 255, 0) ,rgb(255, 0, 0))',
          opacity: 1, // Background for the rail
          border: '2px solid #162521',
          width: '100%',
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