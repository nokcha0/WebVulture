import Slider from '@mui/material/Slider';
import { Context } from '../context';
import React, { useContext } from 'react';

export const ThreadSlide = (props) => {
  const { threadValue, handleThreadChange } = useContext(Context);

  return (
    <div>
      <p className="sliderText">Number of Threads: {threadValue}</p>
      <Slider
        aria-label="Number of Threads"
        defaultValue={1}
        valueLabelDisplay="off"
        onChange={handleThreadChange}
        shiftStep={1}
        step={1}
        marks
        min={1}
        max={10}
        sx={{ width: 400, height: '10px', borderRadius: '0px',

        color: '#ff5733',
        
        '& .MuiSlider-track': {
          opacity: 0,
        },

        '& .MuiSlider-rail': {
          background: 'rgb(166, 166, 166)',
          opacity: 1,
          border: '0px solid #162521',
          width: '100%',
          borderRadius: '6px',
        },  

        '& .MuiSlider-thumb': {
          background: '#000000', 
          boxShadow: '0px 0px 8px rgba(0, 0, 0, 0.3)',
          border: '1px solid #162521',
          height: '10px',
          width: '10px',
        },

        '& .MuiSlider-mark': {
          display: 'none', 
        },

        }}
      />
    </div>
  );
};

export default ThreadSlide
