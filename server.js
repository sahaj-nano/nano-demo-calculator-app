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
    var x = parseInt(req.body.first)+parseInt(req.body.second);
    console.log(x);
    if(isNaN(x)) res.status(400).json({message: "Bad Request"});
    else res.status(200).json({ "result": x});
});


baseRouter.post('/subtract', (req, res) => {
    var x = parseInt(req.body.first)-parseInt(req.body.second);
    console.log(x);
    if(isNaN(x)) res.status(400).json({message: "Bad Request"});
    else res.status(200).json({ "result": x});
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});