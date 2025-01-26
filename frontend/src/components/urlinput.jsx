
import * as React from 'react';
import './checkbox.css'

import { Context } from '../context';
import  { useContext } from 'react';


export default function UrlInput() {
  
  const { urlValue, handleUrlChange } = useContext(Context);

    return (
        <div >
            <input
                type="text"
                className="input2"
                placeholder="Enter a URL"
                value={urlValue}
                onChange={handleUrlChange}
            />
        </div>
    );

      
}
