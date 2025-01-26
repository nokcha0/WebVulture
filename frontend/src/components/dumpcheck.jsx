import * as React from 'react';
import './checkbox.css'
import { Context } from '../context';
import  { useContext } from 'react';


export default function DumpCheck() {
  // Access the context values
  const { isDumpChecked, toggleDumpCheckbox } = useContext(Context);

  return (
    <div className="checkContainer">

      <label class="container"> Dump Database

      <input type="checkbox"
      checked={isDumpChecked}  // Set the checkbox checked state from context
      onChange={toggleDumpCheckbox}  // Toggle the checkbox when changed
      />
      <span class="checkmark"></span>

      </label>
      
    </div>
  );
}