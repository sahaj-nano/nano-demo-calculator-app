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
  const dat = req.body;
  let f = dat["first"];
  let s = dat["second"];

  res.json({ result: f + s });
});

baseRouter.post("/subtract", (req, res) => {
  const dat = req.body;
  let f = dat["first"];
  let s = dat["second"];
  res.json({ result: f - s });
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
  console.log("Server running at PORT", PORT);
});
