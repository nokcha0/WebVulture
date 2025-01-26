// context.jsx
import React, { createContext, useState } from "react";
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
    console.log("flushchecked");
    setIsFlushChecked((prev) => !prev);
  };

  // Code for  verbose checkboxes context
  const [isVerboseChecked, setIsVerboseChecked] = useState(false);

  const toggleVerboseCheckbox = () => {
    console.log("Verbose");
    setIsVerboseChecked((prev) => !prev);
  };

  //Code for url input
  const [urlValue, setUrlValue] = useState("");

  const handleUrlChange = (event) => {
    setUrlValue(event.target.value);
  };

  //Code for manual command input
  const [cmdValue, setCmdValue] = useState("");

  const handleCmdChange = (event) => {
    setCmdValue(event.target.value);
  };

  //send button context
  const handleSend = () => {
    console.log("Button clicked!");
    console.log(attackValue);
    console.log(threadValue);
    console.log(isFlushChecked);
    console.log(isVerboseChecked);
    console.log(urlValue);
    console.log(cmdValue);

    api
      .post("/attackValue", { value: attackValue })
      .then((response) => {
        console.log("attackValue updated on backend:", response.data);
      })
      .catch((error) => {
        console.error("Error updating attackValue:", error);
      });

    api
      .post("/threadValue", { value: threadValue })
      .then((response) => {
        console.log("threadValue updated on backend:", response.data);
      })
      .catch((error) => {
        console.error("Error updating threadValue:", error);
      });

    api
      .post("/isFlushChecked", { toggle: isFlushChecked })
      .then((response) => {
        console.log("isFlushChecked updated on backend:", response.data);
      })
      .catch((error) => {
        console.error("Error updating isFlushChecked:", error);
      });

    api
      .post("/isVerboseChecked", { toggle: isVerboseChecked })
      .then((response) => {
        console.log("isVerboseChecked updated on backend:", response.data);
      })
      .catch((error) => {
        console.error("Error updating isVerboseChecked:", error);
      });

    api
      .post("/urlValue", { text: urlValue })
      .then((response) => {
        console.log("urlValue updated on backend:", response.data);
      })
      .catch((error) => {
        console.error("Error updating urlValue:", error);
      });

    api
      .post("/cmdValue", { text: cmdValue })
      .then((response) => {
        console.log("cmdValue updated on backend:", response.data);
      })
      .catch((error) => {
        console.error("Error updating cmdValue:", error);
      });

    api
      .post("/submitted", { clicked: true })
      .then((response) => {
        console.log("Submit state sent to backend:", response.data);
      })
      .catch((error) => {
        console.error("Error submitting state:", error);
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

        isVerboseChecked,
        toggleVerboseCheckbox,

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
