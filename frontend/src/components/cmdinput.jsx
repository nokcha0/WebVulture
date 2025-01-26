import * as React from 'react';
import { Context } from '../context';
import  { useContext } from 'react';

export default function CmdInput() {
  
  const { cmdValue, handleCmdChange } = useContext(Context);

    return (
        <div >
            <input
                type="text"
                className="input"
                placeholder="Enter a manual command"
                value={cmdValue}
                onChange={handleCmdChange}
            />
        </div>
    );
}
      