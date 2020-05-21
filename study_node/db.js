const mongoose = require('mongoose');

const connect = async (callback) => {
  const connection = await mongoose.connect(process.env.MONGODB_LOCATION, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    useFindAndModify: false,
    useCreateIndex: true,
  });
  callback();
}

module.exports = {
  connect
}