import React, { useRef, useEffect } from 'react'
import './Pop.css'


const Pop = ({ name, location, email, description, total }) => {

  // const parsedDescriptions = description.map(desc => {
  //   const [name, quantidade] = desc.split(',');
  //   return { name, quantidade };
  // });

  const popupRef = useRef(null);

  // useEffect(() => {
  //   // const handleClickOutside = (event) => {
  //   //   if (popupRef.current && !popupRef.current.contains(event.target)) {
  //   //     onClose();
  //   //   }
  //   // };

  //   document.addEventListener("click", handleClickOutside);

  //   return () => {
  //     document.removeEventListener("click", handleClickOutside);
  //   };
  // }, [onClose]);


  return (
    <div className="popup_container" >
      <div className="popup" ref={popupRef}>
        <div className='popup_items'>
          <h1>&#8203;</h1>
          <h1>&#8203;</h1>
          <h1>{name}</h1>
          <h2>{location}</h2>
          <h2>{email}</h2>
          <div className='popup_info'>
            <p style={{ color: "var(--color-green)" }}>Encomenda</p>
            {/* {parsedDescriptions.map((desc, index) => (
              <div key={index}>
                <span>{desc.name} {desc.quantidade}</span>
              </div>
            ))} */}
            <div className="popup_total">
              <p style={{ color: "var(--color-green)" }}>Total:</p>
              <p>{total}€</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};


export default Pop;