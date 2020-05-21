require('dotenv').config({});
const http = require('http');
const app = require('./app');
const { connect } = require('./db');

const server = http.createServer(app);

server.listen(8000, () => {
  // console.log(process.env.foo)
  console.log('mango is coming');
  connect(() => {
    console.log('mongo is coming');
  });
});