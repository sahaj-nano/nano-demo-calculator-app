const express = require("express");
const app = express();
const cors = require("cors");
app.use(cors());
const PORT = process.env.PORT || 8080;

const baseUrl = "/calculator";

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get("/greeting", (req, res) => {
  res.status(200);
  res.end("Hello world!");
});

baseRouter.post("/add", (req, res) => {
  const ans = parseFloat(req.body.first) + parseFloat(req.body.second);
  res.json({ result: ans });
});

baseRouter.post("/subtract", (req, res) => {
  const ans = parseFloat(req.body.first) - parseFloat(req.body.second);
  res.json({ result: ans });
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
  console.log("Server running at PORT", PORT);
});
