import * as React from 'react';
import './checkbox.css'
import { Context } from '../context';
import  { useContext } from 'react';

export default function VerboseCheck() {
  const { isVerboseChecked, toggleVerboseCheckbox } = useContext(Context);

  return (
    <div className="checkContainer">
      <label class="container"> Verbose
        <input type="checkbox"
        checked={isVerboseChecked}
        onChange={toggleVerboseCheckbox}
        />
        <span className="checkmark"></span>
      </label>
    </div>
  );
}