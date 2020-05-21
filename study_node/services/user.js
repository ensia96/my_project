const path = require('path');
const User = require('../models/users');
const bcrypt = require('bcrypt');
const JWT = require('../utils/jwt');

const jwt = new JWT(process.env.TOKEN_SECRET);

exports.createUser = async params => {
  const hashedPassword = await bcrypt.hash(params.password, 10);

  const user = await User.create({
    username: params.username,
    password: hashedPassword,
    name: params.name,
  });

  return user;
};

exports.login = async (username, password) => {
  const user = await User.findOne({ username });
  if (!user) return Promise.reject('로그인에 실패했습니다.');

  const result = await bcrypt.compare(password, user.password);
  if (!result) return Promise.reject('로그인에 실패했습니다.');

  const { password: _, ...restUserData } = user;

  return restUserData;
}

// exports.createToken = async (user) => {
//   const token = await jwt.sign(user, {
//     expiresIn: '1d'
//   });
//   return token
// }

exports.createToken = user => jwt.sign(user, {
  expiresIn: '1d'
});

// const GetPath = root => name => {
//   return path.join(__dirname, root, `${name}.txt`)
// }

// const getPath = GetPath('userfiles');

// exports.createUserFile = (name, data) => {
//   const filePath = getPath(name);
//   return writeFile(filePath, data);
// }

// // export const readUserFile = () => {}

// exports.readUserFile = (name) => {
//   const filePath = getPath(name);
//   return readFile(filePath)
// }

// module.exports = {
//   createUserFile,
//   readUserFile,
// }