const express = require('express');
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    return res.send('hello world!');
});

baseRouter.post('/add', (req, res) => {
    var num1 = req.body.first;
    var num2 = req.body.second;
    res.json({ "result": num1+num2 });
});


baseRouter.post('/subtract', (req, res) => {
    var num1 = req.body.first;
    var num2 = req.body.second;
    res.json({ "result": num1-num2 });
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});