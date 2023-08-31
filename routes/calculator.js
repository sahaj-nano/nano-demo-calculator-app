const express = require("express");
const router = express.Router();

router.get("/greeting", (req, res) => {
  return res.send("Hello world!");
});

router.post("/add", (req, res) => {
  const { first, second } = req.body;
  const result = first + second;
  res.json({ result });
});

router.post("/subtract", (req, res) => {
  const { first, second } = req.body;
  const result = first - second;
  res.json({ result });
});

module.exports = router;
