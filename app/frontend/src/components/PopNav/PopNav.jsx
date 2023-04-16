import React from 'react'
import './PopNav.css'

function PopNav(props) {
  return (props.trigger) ? (
    <div className='popup'>
        <div className='popup-inner'>
            {props.children}
        </div>
    </div>
  ) : "";
}

export default PopNav