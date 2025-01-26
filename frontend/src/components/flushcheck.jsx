import * as React from 'react';
import './checkbox.css'
import { Context } from '../context';
import  { useContext } from 'react';

export default function FlushCheck() {
  const { isFlushChecked, toggleFlushCheckbox } = useContext(Context);

  return (
    <div className="checkContainer">
      <label class="container"> Flush Session
        <input type="checkbox"
        checked={isFlushChecked} 
        onChange={toggleFlushCheckbox} 
        />
        <span class="checkmark"></span>
      </label>
    </div>
  );
}
