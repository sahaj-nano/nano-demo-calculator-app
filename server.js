const express = require('express');
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());

const baseRouter = express.Router();


//Greeting route
baseRouter.get('/greeting', (req, res) => {
    return res.status(200).send('Hello world!');
});

baseRouter.post('/add', (req, res) => {
    var first = Number(req.body.first);
    var second = Number(req.body.second);
    var result = first + second;
    res.status(200).json({"result":  + JSON.stringify(result) });
});


baseRouter.post('/subtract', (req, res) => {
    var first = Number(req.body.first);
    var second = Number(req.body.second);
    var result = first - second;
    res.status(200).json({"result":  + JSON.stringify(result) });
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});