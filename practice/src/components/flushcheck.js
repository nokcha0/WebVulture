import * as React from 'react';
import './checkbox.css'
import { Context } from '../context';
import  { useContext } from 'react';


export default function FlushCheck() {
  // Access the context values
  const { isFlushChecked, toggleFlushCheckbox } = useContext(Context);

  return (
    <div className="checkContainer">

      <label class="container"> Flush Session

      <input type="checkbox"
      checked={isFlushChecked}  // Set the checkbox checked state from context
      onChange={toggleFlushCheckbox}  // Toggle the checkbox when changed
      />
      <span class="checkmark"></span>

      </label>
      
    </div>
  );
}