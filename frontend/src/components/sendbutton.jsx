import React from 'react';
import { Context } from '../context';
import  { useContext } from 'react';

const ButtonComponent = () => {

  const { handleSend } = useContext(Context);
  const ScrollButton = () => {
      handleSend()
      window.scrollTo({
        top: document.documentElement.scrollHeight,
        behavior: 'smooth',
      });
    }

  return (
      <button type="submit" className="input-button" onClick={ScrollButton}>
        <img src="./src/images/arrowSubmit.png" alt="Submit" className="input-button-icon" />
      </button>
  );
};

export default ButtonComponent;
