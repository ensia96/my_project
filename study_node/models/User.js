const  { Schema, model } = require('mongoose');

const UserSchema = new Schema({
  username: { type: String, required: true, unique: true },
  password: { type: String, required: true, },
  name: { type: String },
  createdAt: { type: Date, default: Date.now() },
});

module.exports = model('User', UserSchema);