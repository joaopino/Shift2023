import React from 'react'
import { Navbar } from '../../components'
import images from '../../constants'

import './Register.css'

function Register() {
	return (
		<div className="app_register">
			<Navbar />
			<div className="app_register-container">
				<div className="app_register-container-form">
					<h1>Registar</h1>
					<form action="">
						<div className="app_register-container-form-input">
							<label htmlFor="name">Nome</label>
							<input type="text" name="name" id="name" />

							<label htmlFor="email">Email</label>
							<input type="email" name="email" id="email" />

							<label htmlFor="password">Password</label>
							<input type="password" name="password" id="password" />

							<label htmlFor="confirmPassword">Confirmar Password</label>
							<input type="password" name="confirmPassword" id="confirmPassword" />

							<button type="submit">Registar</button>

							<div className="app_register-container-form-input-footer">
								<p>Já tem uma conta? <a href="/login">Entrar</a></p>
							</div>
						</div>
					</form>
				</div>
			</div>
		</div>
	)
}

export default Register