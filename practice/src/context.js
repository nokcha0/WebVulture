// SliderContext.js
import React, { createContext, useState } from 'react';
import api from "./api.js";

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
    console.log(attackValue); // int
    console.log(threadValue); // int
    console.log(isFlushChecked); // bool
    console.log(isDumpChecked); // bool
    console.log(urlValue); // str
    console.log(cmdValue); // str

    api.post('/submitted', { clicked: true })
    .then(response => {
      console.log("Submit state sent to backend:", response.data);
    })
    .catch(error => {
      console.error("Error submitting state:", error);
    });

    api.post('/attackValue', { value: attackValue })
    .then(response => {
      console.log("attackValue updated on backend:", response.data);
    })
    .catch(error => {
      console.error("Error updating attackValue:", error);
    });

    api.post('/threadValue', { value: threadValue })
    .then(response => {
      console.log("threadValue updated on backend:", response.data);
    })
    .catch(error => {
      console.error("Error updating threadValue:", error);
    });
    
    api.post('/isFlushChecked', { toggle: isFlushChecked })
    .then(response => {
      console.log("isFlushChecked updated on backend:", response.data);
    })
    .catch(error => {
      console.error("Error updating isFlushChecked:", error);
    });

    api.post('/isDumpChecked', { toggle: isDumpChecked })
    .then(response => {
      console.log("isDumpChecked updated on backend:", response.data);
    })
    .catch(error => {
      console.error("Error updating isDumpChecked:", error);
    });

    api.post('/urlValue', { text: urlValue })
    .then(response => {
      console.log("urlValue updated on backend:", response.data);
    })
    .catch(error => {
      console.error("Error updating urlValue:", error);
    });

    api.post('/cmdValue', { text: cmdValue })
    .then(response => {
      console.log("cmdValue updated on backend:", response.data);
    })
    .catch(error => {
      console.error("Error updating cmdValue:", error);
    });
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
