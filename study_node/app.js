const express = require("express");
const app = express();
const userRoutes = require('./routes/user');

app.use(express.json());

app.use('./user', userRoutes);

app.get("/user/:id/:name", (req, res, next) => {
  console.log("id", req.params);
  res.json({
    query: req.query,
    params: req.params,
    url: req.url,
  });
});

module.exports = app;
