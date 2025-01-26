import * as React from 'react';
import './checkbox.css'

import { Context } from '../context';
import  { useContext } from 'react';


export default function CmdInput() {
  
  const { cmdValue, handleCmdChange } = useContext(Context);

    return (
        <div className="manual-input">

            <input
                type="text"
                className="modern-input"
                placeholder="Enter a manual command..."
                value={cmdValue}
                onChange={handleCmdChange}
            />
        </div>
    );
}
      