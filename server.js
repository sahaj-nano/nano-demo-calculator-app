const express = require('express');
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    return res.status(200).send("Hello world!");
});

baseRouter.post('/add', (req, res) => {
    const data = req.body;
    const { first: firstNumber, second: secondNumber } = data;
    const sum = firstNumber+ secondNumber;
    res.status(200).json({ "result": sum });
});


baseRouter.post('/subtract', (req, res) => {
    const data = req.body;
    const { first: firstNumber, second: secondNumber } = data;
    const difference = firstNumber - secondNumber;
    res.status(200).json({ "result": difference });
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});