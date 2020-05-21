const jwt = require('jsonwebtoken');

class JWT {
  constructor(secret) {
    this.secret = secret;
  }

  sign = (payload, options) => new Promise((resolve, reject) => {
    jwt.sign(payload, this.secret, options, (err, result) => {
      if (err) return reject(err);
      return resolve(result);
    });
  });

  verify = (token, options) => new Promise((resolve, reject) => {
    jwt.verify(token, this.secret, options, (err, result) => {
      if (err) return reject(err);
      return resolve(result);
    });
  });
}

module.exports = JWT;