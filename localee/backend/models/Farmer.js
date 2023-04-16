import { Schema, model } from 'mongoose';

const farmerSchema = new Schema({
  email: String,
  password: String,
  name: String,
  address: String,
  contact: Number
});

const Farmer = model('Farmer', farmerSchema);

export default Farmer;