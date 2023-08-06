const express = require("express");
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = "/calculator";

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get("/greeting", (req, res) => {
  return res.send("Hello world!");
});

baseRouter.post("/add", (req, res) => {
  // adding logic here
  const { first, second } = req.body;
  const result = parseInt(first) + parseInt(second);
  res.json({ result: result });
});

baseRouter.post("/subtract", (req, res) => {
  const { first, second } = req.body;
  const result = parseInt(first) - parseInt(second);
  res.json({ result: result });
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
  console.log("Server running at PORT", PORT);
});
