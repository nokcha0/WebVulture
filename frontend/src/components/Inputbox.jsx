import React from 'react';
export default function InputBox()
{   
    const [outputShown, setOutputShown] = React.useState(false)

    function onSubmit(formData)
    {
        console.log(3)
    }

    return (
        <div className="top-container">
            <form action={onSubmit} className="input-form" >
            <input
                type="text"
                className="input"
                placeholder="Enter a URL..."
                name="website"
            />
            <button type="submit" className="input-button">
                <img src="./src/images/arrowSubmit.png" alt="Submit" className="input-button-icon" />
            </button>
            </form>
        </div>
    );

      
}

