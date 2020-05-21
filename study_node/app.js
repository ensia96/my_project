const express = require('express');
const app = express();

const userRoutes = require('./routes/users');

// const path = require('path')
// const file = require('./file');
// const { readFile, writeFile } = require('./file');

app.use(express.json());

app.use('/user', userRoutes);

app.use((err, req, res, next) => {
  console.error(err);
  res.status(err.status || 500).json({
    message: err.message || 'Unknown Error',
  });
});

// app.get('/user/:id', (req, res, next) => {
//   res.json({
//     id: req.params.id,
//     url: req.url,
//   });
// });

// app.post('/file/:name', (req, res, next) => {
//   const filename = `${req.params.name}.txt`;
//   const filePath = path.join(__dirname, filename);
//   const data = req.body.data;
  
//   writeFile(filePath, data)
//     .then(result => {
//       res.json({
//         message: '성공'
//       })
//     }).catch(err => {
//       res.status(500).json({
//         message: '실패'
//       })
//     });
// })

// app.get('/file/:name', (req,res,next) => {
//   const filename = `${req.params.name}.txt`;
//   const filePath = path.join(__dirname, filename);

//   readFile(filePath)
//     .then(data => {
//       res.json({
//         message: '성공',
//         data,
//       })
//     }).catch(err => {
//       res.status(500).json({
//         message: '실패'
//       })
//     })
// })

module.exports = app;