const express = require("express");
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = "/calculator";

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get("/greeting", (req, res) => {
  return res.json({
    code: 200,
    content: "Hello world!",
  });
});

baseRouter.post("/add", (req, res) => {
  const { first, second } = req.body;
  const sum = first + second;
  res.json({
    "Status code": 200,
    result: sum,
  });
});

baseRouter.post("/subtract", (req, res) => {
  const { first, second } = req.body;
  const sub = first - second;
  res.json({ 
    "Status code": 200,
    result: sub });
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
  console.log("Server running at PORT", PORT);
});
