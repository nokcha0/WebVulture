import React from 'react';
import Button from '@mui/material/Button'; // Import Button component from Material UI
import { Context } from '../context';
import  { useContext } from 'react';


const ButtonComponent = () => {


  const { handleSend } = useContext(Context);

  return (
    <Button variant="contained" color="primary" onClick={handleSend}>
      Click Me
    </Button>
  );
};

export default ButtonComponent;
