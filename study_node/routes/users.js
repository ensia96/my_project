const express = require('express');

const userController = require('../controllers/user');

const router = express.Router();

//router.get('/:id', userController.readUserFile)
router.post('/', userController.createUser)
router.post('/login', userController.login)

module.exports = router;