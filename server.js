const express = require('express');
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    return res.status(200).send('Hello world!');
});

baseRouter.post('/add', (req, res) => {
    let num1 = parseInt(req.body.first);
    let num2 = parseInt(req.body.second);
    res.status(200).json({ "result":  num1+num2});
});

baseRouter.post('/subtract', (req, res) => {
    let num1 = parseInt(req.body.first);
    let num2 = parseInt(req.body.second);
    res.status(200).json({ "result":  num1-num2});
});
    
app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});