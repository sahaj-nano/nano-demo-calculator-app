const express = require('express');
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    res.status(200);
    //res.sendStatus(200);
    res.end("Hello world!");
});

baseRouter.post('/add', (req, res) => {
    res.status(200);
    res.setHeader("Content-Type", "application/json");
    let num1 = req.body.first;
    let num2 = req.body.second;
    res.json({ "result": num1 + num2 });
    res.end();
});


baseRouter.post('/subtract', (req, res) => {
    res.status(200);
    res.setHeader("Content-Type", "application/json");
    res.json({ "result": req.body.first - req.body.second });
    res.end();
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});