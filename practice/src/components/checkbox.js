import * as React from 'react';
import Checkbox from '@mui/material/Checkbox';


import { Context } from '../context';


export default function Checkboxes() {

  const { boxChecked, handleBoxChange } = useContext(Context);

  return (
    <div>
      <Checkbox
        checked={boxChecked} // Set the checkbox state to the current state value
        onChange={handleBoxChange} // Update state on change
        color="black"

      />
    </div>
  );
}