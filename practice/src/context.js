// SliderContext.js
import React, { createContext, useState } from 'react';

export const Context = createContext();

export const ContextProvider = ({ children }) => {
  // Define state for slider value, button click count, and theme
  const [sliderValue, setSliderValue] = useState(3);

  // Handlers to update the values
  const handleSliderChange = (event, newValue) => {
    setSliderValue(newValue);
  };

  // Code for checkboxes context

  const [boxChecked, setBoxChecked] = useState(false); // Initial state is false (unchecked)
  
  const handleBoxChange = (event) => {
      setBoxChecked(event.target.checked); // Update the state when the checkbox is clicked
  }
  // send button context

  const handleSend= () => {
    console.log('Button clicked!');
  };


  return (
    <Context.Provider
      value={{
        sliderValue,
        handleSliderChange,
        boxChecked,
        handleBoxChange,
        handleSend,
      }}
    >
      {children}
    </Context.Provider>
  );
};
