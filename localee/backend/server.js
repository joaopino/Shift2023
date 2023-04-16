import express from "express";
import dotenv from "dotenv";
import cors from "cors";
import { StatusCodes } from "http-status-codes";
import { MongoClient } from "mongodb";
import mongoose from "mongoose";

import Farmer from "./models/Farmer.js";

dotenv.config({ path: './.env', debug: process.env.DEBUG });

// App Environment
const HOST = process.env.HOST !== undefined ? process.env.HOST : "localhost";
const PORT = process.env.PORT || 5000;

// Web App URL (cors)
const FRONTEND_URL = process.env.FRONTEND_URL;

const uri = `mongodb+srv://${process.env.DB_USER}:${process.env.DB_PASS}@localeedb.xulgqx4.mongodb.net/?retryWrites=true&w=majority`;

// MongoDB Client
const client = new MongoClient(uri, {
	useNewUrlParser: true,
	useUnifiedTopology: true,
});

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cors({ origin: FRONTEND_URL, credentials: true }));
//------------Esquema de dados
const userSchema = new mongoose.Schema({
	name: {
		type: String,
		required: true
	},
	location: {
		type: String,
		required: true
	},
	contact: {
		type: String,
		required: true
	},
	isProducer: {
		type: Boolean,
		default: false
	},
	isRetailer: {
		type: Boolean,
		default: false
	},
	email: {
		type: String,
		required: true,
		unique: true
	},
	password: {
		type: String,
		required: true
	}
});

const adSchema = new mongoose.Schema({
	productType: {
		type: String,
		required: true
	},
	price: {
		type: Number,
		required: true
	},
	maxQuantity: {
		type: Number,
		required: true
	},
	farmer: {
		type: mongoose.Schema.Types.ObjectId,
		ref: 'User'
	}
});

const orderSchema = new mongoose.Schema({
	products: [{
		product: {
			type: mongoose.Schema.Types.ObjectId,
			ref: 'Ad'
		},
		quantity: {
			type: Number,
			required: true
		}
	}],
	retailer: {
		type: mongoose.Schema.Types.ObjectId,
		ref: 'User'
	},
	deliveryDate: {
		type: Date,
		required: true
	},
	isDelivered: {
		type: Boolean,
		default: false
	}
});

const User = mongoose.model('User', userSchema);
const Ad = mongoose.model('Ad', adSchema);
const Order = mongoose.model('Order', orderSchema);

module.exports = { User, Ad, Order };

//-----------------Rotas

const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const { User, Ad, Order } = require('./models');
const { authenticateUser } = require('./middleware');

const router = express.Router();

// Registro de usuário
router.post('/register', async (req, res) => {
	const { name, location, contact, isProducer, isRetailer, email, password } = req.body;
	const hashedPassword = await bcrypt.hash(password, 10);

	try {
		const user = await User.create({
			name,
			location,
			contact,
			isProducer,
			isRetailer,
			email,
			password: hashedPassword
		});

		const token = jwt.sign({ userId: user._id }, 'secret');

		res.status(201).json({ user: user._id, token });
	} catch (err) {
		res.status(400).json({ error: err.message });
	}
});

// Login de usuário
router.post('/login', async (req, res) => {
	const { email, password } = req.body;

	const user = await User.findOne({ email });

	if (!user) {
		return res.status(400).json({ error: 'Usuário não encontrado' });
	}

	const isMatch = await bcrypt.compare(password, user.password);

	if (!isconst(express = require('express')));
	const bcrypt = require('bcrypt');
	const jwt = require('jsonwebtoken');
	const { User, Ad, Order } = require('./models');
	const { authenticateUser } = require('./middleware');

	const router = express.Router();

	// Registro de usuário
	router.post('/register', async (req, res) => {
		const { name, location, contact, isProducer, isRetailer, email, password } = req.body;
		const hashedPassword = await bcrypt.hash(password, 10);

		try {
			const user = await User.create({
				name,
				location,
				contact,
				isProducer,
				isRetailer,
				email,
				password: hashedPassword
			});

			const token = jwt.sign({ userId: user._id }, 'secret');

			res.status(201).json({ user: user._id, token });
		} catch (err) {
			res.status(400).json({ error: err.message });
		}
	});

	// Login de usuário
	router.post('/login', async (req, res) => {
		const { email, password } = req.body;

		const user = await User.findOne({ email });

		if (!user) {
			return res.status(400).json({ error: 'Usuário não encontrado' });
		}

		const isMatch = await bcrypt.compare(password, user.password);

		if (!isconst(express = require('express')));
		const bcrypt = require('bcrypt');
		const jwt = require('jsonwebtoken');
		const { User, Ad, Order } = require('./models');
		const { authenticateUser } = require('./middleware');

		const router = express.Router();

		// Registro de usuário
		router.post('/register', async (req, res) => {
			const { name, location, contact, isProducer, isRetailer, email, password } = req.body;
			const hashedPassword = await bcrypt.hash(password, 10);

			try {
				const user = await User.create({
					name,
					location,
					contact,
					isProducer,
					isRetailer,
					email,
					password: hashedPassword
				});

				const token = jwt.sign({ userId: user._id }, 'secret');

				res.status(201).json({ user: user._id, token });
			} catch (err) {
				res.status(400).json({ error: err.message });
			}
		});

		// Login de usuário
		router.post('/login', async (req, res) => {
			const { email, password } = req.body;

			const user = await User.findOne({ email });

			if (!user) {
				return res.status(400).json({ error: 'Usuário não encontrado' });
			}

			const isMatch = await bcrypt.compare(password, user.password);

			if (!isMatch) {
				return res.status(400).json({ error: 'Email ou senha inválidos' });
			}

			const token = jwt.sign({ userId: user._id }, 'secret');

			res.json({ user: user._id, token });
		});

		// Criação de anúncio
		router.post('/ads', authenticateUser, async (req, res) => {
			const { productType, price, maxQuantity } = req.body;
			const { userId } = req;

			if (!req.user.isProducer) {
				return res.status(401).json({ error: 'Você não tem permissão para criar anúncios' });
			}

			try {
				const ad = await Ad.create({
					productType,
					price,
					maxQuantity,
					farmer: userId
				});

				res.status(201).json({ ad });
			} catch (err) {
				res.status(400).json({ error: err.message });
			}
		});

		// Gerenciamento de encomendas
		router.get('/orders', authenticateUser, async (req, res) => {
			if (!req.user.isRetailer) {
				return res.status(401).json({ error: 'Você não tem permissão para gerenciar encomendas' });
			}

			try {
				const orders = await Order.find({ retailer: req.userId })
					.populate({
						path: 'products.product',
						model: 'Ad',
						populate: {
							path: 'farmer',
							model: 'User'
						}
					});
				res.json({ orders });
			} catch (err) {
				res.status(400).json({ error: err.message });
			}
		});

		router.post('/orders', authenticateUser, async (req, res) => {
			const { products, deliveryDate } = req.body;
			const { userId } = req;

			if (!req.user.isRetailer) {
				return res.status(401).json({ error: 'Você não tem permissão para criar encomendas' });
			}

			try {
				const order = await Order.create({
					products,
					retailer: userId,
					deliveryDate
				});

				res.status(201).json({ order });

			} catch (err) {
				res.status(400).json({ error: err.message });
			}
		});

		router.patch('/orders/:id', authenticateUser, async (req, res) => {
			const { id } = req.params;
			const { isDelivered } = req.body;

			if (!req.user.isRetailer) {
				return res.status(401).json({ error: 'Você não tem permissão para atualizar o status da encomenda' });
			}

			try {
				const order = await Order.findByIdAndUpdate(id, { isDelivered }, { new: true });

				res.json({ order });

			} catch (err) {
				res.status(400).json({ error: err.message });
			}
		});

		module.exports = router;

		//------------------Middleware de autenticação

		const jwt = require('jsonwebtoken');
		const { User } = require('./models');

		const authenticateUser = async (req, res, next) => {
			const { authorization } = req.headers;

			if (!authorization) {
				return res.status(401).json({ error: 'Você precisa estar autenticado para acessar este recurso' });
			}

			const token = authorization.replace('Bearer ', '');

			try {
				const { userId } = jwt.verify(token, 'secret');
				const user = await User.findById(userId);

				if (!user) {
					throw new Error();
				}

				req.userId = userId;
				req.user = user;

				next();

			} catch (err) {
				res.status(401).json({ error: 'Você precisa estar autenticado para acessar este recurso' });
			}
		};

		module.exports = authenticateUser;

		app.listen(PORT, HOST, () =>
			console.log(`Server is live on port http://${HOST}:${PORT}`)
		);
	});
});
