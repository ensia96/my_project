const {userService = require('../services/user')};

const createUserFile = (req, res, next) => {
  try {
    const {name, data} = req.body
    const result = await userService.createUserService(name, data);

    res.json({
      name,
    })
  } catch (err){
    res.status(500).json({
      message: err.message,
    })
  }
}

const readUserFile = async (req, res, next) => {
  try{
    const name = req.params.name;
    const result = await userService.readUserService(name);

    res.json({
      name,
      content: result,
    });
  } catch (err) {
    res.status(500).json({
      message: err.message,
    })
  }
}


module.exports = {
  createUserFile,
  readUserFile,
}
