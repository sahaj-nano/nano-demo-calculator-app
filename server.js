const express = require('express');
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {

    return res.status(200).json('Hello World!');
});

baseRouter.post('/add', (req, res) => {
    const { first, second } = req.body;
    if (!first || !second) {
      return res.status(400).json({ error: 'Both num1 and num2 are required.' });
    }
    const result = first + second;
    res.json({ result });
  });
  
  baseRouter.post('/subtract', (req, res) => {
    const { first, second } = req.body;
    if (!first || !second) {
      return res.status(400).json({ error: 'Both num1 and num2 are required.' });
    }
    const result = first - second;
    res.json({ result });
  });


app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});