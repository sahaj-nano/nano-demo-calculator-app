const express = require("express");
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = "/calculator";

app.use(express.json());

const baseRouter = express.Router();

app.get("/", (req, res) => {
  res.send("This is a base url");
});

baseRouter.get("/", (req, res) => {
  res.send("This is a calculator");
});

baseRouter.get("/greeting", (req, res) => {
  return res.status(200).send("Hello world");
});

baseRouter.post("/add", (req, res) => {
  var num1 = req.body.first;
  var num2 = req.body.second;
  res.status(200).json({ result: `${num1 + num2}` });
});

baseRouter.post("/subtract", (req, res) => {
  var num1 = req.body.first;
  var num2 = req.body.second;
  res.status(200).json({ result: `${num1 - num2}` });
});

app.use(baseUrl, baseRouter);

app.listen(PORT, () => {
  console.log("Server running at PORT", PORT);
});
