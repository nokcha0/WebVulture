import React from 'react';

export default function InputBox()
{   
    const [outputShown, setOutputShown] = React.useState(false)

    return (
        <div className="top-container">
            <input
                type="text"
                className="input"
                placeholder="Enter a URL..."
                name="website"
            />
            <button className="input-button">
                <img src="./src/images/arrowSubmit.png" alt="Submit" className="input-button-icon" />
            </button>
        </div>
    );
}

