const express = require('express');
const morgan = require('morgan');
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());

app.use(morgan("tiny"));

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    res.status(200).send("Hello world!");
});

baseRouter.post('/add', (req, res) => {
    let numbers=req.body;
    let num1= numbers.first;
    let num2= numbers.second;
    res.status(200).json({"result":num1+num2});
});


baseRouter.post('/subtract', (req, res) => {
    let numbers=req.body;
    let num1= numbers.first;
    let num2= numbers.second;
    res.status(200).json({"result":num1-num2});
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});