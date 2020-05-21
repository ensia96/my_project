const fs = require('fs');

const readFile = path => {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        return reject(err);
      }
      return resolve(data)
    })
  })
};

const writeFile = (path, data) => {
  return new Promise((resolve, reject) => {
    fs.writeFile(path, data, 'utf-8', err => {
      if (err) {
        return reject(err)
      }
      return resolve(true)
    })
  })
}

module.exports = {
  readFile,
  writeFile,
}