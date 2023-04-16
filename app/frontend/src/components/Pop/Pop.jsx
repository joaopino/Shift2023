import React from 'react'
import './Pop.css'

function Pop(props) {
  return (props.trigger) ? (
    <div className='popup'>
        <div className='popup-inner'>
            {props.children}
        </div>
    </div>
  ) : "";
}

export default Pop