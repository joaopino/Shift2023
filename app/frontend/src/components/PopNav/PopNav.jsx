import React from 'react'
import './PopNav.css'

function PopNav(props) {
  return (props.trigger) ? (
    <div className='popup1'>
        <div className='popup-inner1'>
            {props.children}
        </div>
    </div>
  ) : "";
}

export default PopNav