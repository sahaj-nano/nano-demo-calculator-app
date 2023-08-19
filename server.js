const express = require("express");
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = "/calculator";

app.use(express.json());

const baseRouter = express.Router();

function CheckIfParamIsNum(req, res, next) {
  if (isNaN(req.body.first) || isNaN(req.body.second)) {
    return res.status(400).json({ error: "Invalid parameters" });
  }
  next();
}

baseRouter.get("/greeting", (req, res) => {
  return res.send("Hello world!");
});

baseRouter.post("/add", CheckIfParamIsNum, (req, res) => {
  const { first, second } = req.body;
  return res.json({ result: first + second });
});

baseRouter.post("/subtract", CheckIfParamIsNum, (req, res) => {
  const { first, second } = req.body;
  return res.json({ result: first - second });
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
  console.log("Server running at PORT", PORT);
});
