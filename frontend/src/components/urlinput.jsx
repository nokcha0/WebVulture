
import * as React from 'react';
import './checkbox.css'

import { Context } from '../context';
import  { useContext } from 'react';


export default function UrlInput() {
  
  const { urlValue, handleUrlChange } = useContext(Context);

    return (
        <div className="top-container">
            <form className="modern-form" >
            <input
                type="text"
                className="input"
                placeholder="Enter a URL"
                value={urlValue}
                onChange={handleUrlChange}
            />
            </form>
        </div>
    );

      
}
