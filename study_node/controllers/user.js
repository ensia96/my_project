const userService = require('../services/user');

exports.createUser = async (req, res, next) => {
  try {
    const {
      username,
      password,
      name,
    } = req.body

    const user = await userService.createUser({
      username,
      password,
      name,
    });

    res.json(user);
  } catch (err) {
    next(err);
  }
}

exports.login = async (req, res, next) => {
  try {
    const { username, password } = req.body
    const user = await userService.login(username, password);
    const token = await userService.createToken(user);
    res.json({ token });
  } catch (err) {
    next(err);
  }
}

// const createUserFile = async (req, res, next) => {
//   try {
//     // 요청 가공해서 필요한 정보를 요청에서 추출
//     const { name, data } = req.body;

//     // 실제 행동을 하는 로직인 서비스로직을 호출하면서,
//     // 가공된 정보를 넣어주고
//     const result = await userService.createUserFile(name, data);

//     // 서비스로직 결과를 기반으로 응답
//     res.json({
//       name,
//     })
//   } catch (err) {
//     res.status(500).json({
//       message: err.message,
//     })
//   }
// }

// const readUserFile = async (req, res, next) => {
//   try {
//     const name = req.params.name;
//     const result = await userService.readUserFile(name);
    
//     res.json({
//       name,
//       content: result,
//     });
//   } catch (err) {
//     res.status(500).json({
//       message: err.message,
//     })
//   }
// }

// module.exports = {
//   createUserFile,
//   readUserFile,
// };
