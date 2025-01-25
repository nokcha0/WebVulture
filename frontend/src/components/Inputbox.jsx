import React from 'react';
export default function ModernForm()
{   
    return (
        <div className="top-container">
            <form className="modern-form" >
            <input
                type="text"
                className="modern-input"
                placeholder="Enter a URL..."
            />
            <button type="submit" className="modern-button">
                <img src="./src/images/arrowSubmit.png" alt="Submit" className="modern-button-icon" />
            </button>
            </form>
        </div>
    );

      
}

