// SliderContext.js
import React, { createContext, useState } from 'react';

export const Context = createContext();

export const ContextProvider = ({ children }) => {

  // Define state for slider value, button click count, and theme
  const [attackValue, setAttackValue] = useState(1);

  // Handlers to update the values
  const handleAttackChange = (event, newValue) => {
    setAttackValue(newValue);
  };

  //THREADS
  const [threadValue, setThreadValue] = useState(1);

  // Handlers to update the values
  const handleThreadChange = (event, newValue) => {
    setThreadValue(newValue);
  };

  // Code for checkboxes context
  const [isFlushChecked, setIsFlushChecked] = useState(false);

  const toggleFlushCheckbox = () => {
      console.log('flushchecked')
      setIsFlushChecked((prev) => !prev);
  };


  // Code for checkboxes context
  const [isDumpChecked, setIsDumpChecked] = useState(false);

  const toggleDumpCheckbox = () => {
      console.log('dumpchecked')
      setIsDumpChecked((prev) => !prev);
  };


  //Code for url input
  const [urlValue, setUrlValue] = useState("");

  const handleUrlChange = (event) => {
    setUrlValue(event.target.value);
  }

  //Code for manual command input
  const [cmdValue, setCmdValue] = useState("");

  const handleCmdChange = (event) => {
    setCmdValue(event.target.value);
  }


  //send button context
  const handleSend= () => {
    console.log('Button clicked!');
    console.log(attackValue);
    console.log(threadValue);
    console.log(isFlushChecked);
    console.log(isDumpChecked);
    console.log(urlValue);
    console.log(cmdValue);
  };


  return (
    <Context.Provider
      value={{
        attackValue,
        handleAttackChange,

        threadValue,
        handleThreadChange,

        isFlushChecked,
        toggleFlushCheckbox,
        
        isDumpChecked,
        toggleDumpCheckbox,

        urlValue,
        handleUrlChange,

        cmdValue,
        handleCmdChange,

        handleSend,
      }}
    >
      {children}
    </Context.Provider>
  );
};
