import React from 'react'
import { Navbar } from '../../components'
import images from '../../constants'

import './Register.css'

function Register() {
	const [clickedFarmer, setClickedFarmer] = React.useState(false);
	const [clickedReseller, setClickedReseller] = React.useState(false);

	const handleClickFarmer = () => {
		setClickedFarmer(!clickedFarmer);
		setClickedReseller(false);
	};

	const handleClickReseller = () => {
		setClickedReseller(!clickedReseller);
		setClickedFarmer(false);
	};

	return (
		<div className="app_register">
			<Navbar />
			<div className="app_register-container">
				<div className='app_register-container-header'>
					Registar
				</div>

				<div className="app_register-container-images">
					<div className="app_register-container-farmer">
						<div className="app_register-container-farmer-image">
							<img className={clickedFarmer ? 'farmer clicked' : 'farmer'} src={images.farmer} alt="farmer_img" onClick={handleClickFarmer} />
						</div>
						{clickedFarmer ? <h1 style={{ color: "var(--color-brown)" }}>Produtor</h1> : <h1 style={{ color: "var(--color-green)" }}>Produtor</h1>}
					</div>

					<div className="app_register-container-reseller">
						<div className="app_register-container-reseller-image">
							<img className={clickedReseller ? 'reseller clicked' : 'farmer'} src={images.reseller} alt="reseller_img" onClick={handleClickReseller} />
						</div>
						{clickedReseller ? <h1 style={{ color: "var(--color-brown)" }}>Vendedor</h1> : <h1 style={{ color: "var(--color-green)" }}>Vendedor</h1>}
					</div>
				</div>
				<div className="app_register-green">
					<div className="app_register-container-form">
						<div className='app_register-pois' />
						<form action="">

							<label htmlFor="name">Nome</label>
							<input type="text" name="name" id="name" />

							<label htmlFor="email">Email</label>
							<input type="email" name="email" id="email" />

							<label htmlFor="password">Password</label>
							<input type="password" name="password" id="password" />

							<label htmlFor="contact">Contacto</label>
							<input type="text" name="contact" id="contact" />

						</form>
						<div className="app_register-container-submit">
							<button type="submit">Registar</button>
						</div>
					</div>
				</div>
			</div>
		</div>
	)
}

export default Register