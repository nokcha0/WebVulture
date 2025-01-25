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
            <form action={onSubmit} className="modern-form" >
            <input
                type="text"
                className="modern-input"
                placeholder="Enter a URL..."
                name="website"
            />
            <button type="submit" className="modern-button">
                <img src="./src/images/arrowSubmit.png" alt="Submit" className="modern-button-icon" />
            </button>
            </form>
        </div>
    );

      
}

