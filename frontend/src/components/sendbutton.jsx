import React from 'react';
import Button from '@mui/material/Button'; // Import Button component from Material UI
import { Context } from '../context';
import  { useContext } from 'react';


const ButtonComponent = () => {


  const { handleSend } = useContext(Context);

  
  return (
  <button type="submit" className="input-button" onClick={handleSend}>
    <img src="./src/images/arrowSubmit.png" alt="Submit" className="input-button-icon" />
  </button>
  );
};

export default ButtonComponent;
