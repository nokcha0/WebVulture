import * as React from 'react';
import './checkbox.css'
import { Context } from '../context';
import  { useContext } from 'react';


export default function VerboseCheck() {
  // Access the context values
  const { isVerboseChecked, toggleVerboseCheckbox } = useContext(Context);

  return (
    <div className="checkContainer">

    <label class="container"> Verbose

      <input type="checkbox"
      checked={isVerboseChecked}  // Set the checkbox checked state from context
      onChange={toggleVerboseCheckbox}  // Toggle the checkbox when changed
      />
      <span className="checkmark"></span>

    </label>
      
      
    </div>
  );
}