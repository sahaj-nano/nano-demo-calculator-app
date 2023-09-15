const express = require('express');
const bodyParser = require('body-parser');

const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());
app.use(bodyParser.urlencoded({ extended: false }))
app.use(express.json())

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    return res.send('Hello world!');
});

baseRouter.post('/add', (req, res) => {
    const {first, second} = req.body;
    res.json({ "result": parseInt(first)+parseInt(second) });
});


baseRouter.post('/subtract', (req, res) => {
    const {first, second} = req.body;
    res.json({ "result": parseInt(first)-parseInt(second) });
});

app.use(baseUrl, baseRouter);
