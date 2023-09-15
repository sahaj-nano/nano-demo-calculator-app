const express = require('express');

const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    return res.send('Hello world!');
});

baseRouter.post('/add', (req, res) => {
    let first= req.body.first;
    let second = req.body.second;
    console.log(first);
    res.json({ "result": first+second });
});


baseRouter.post('/subtract', (req, res) => {
    let first= req.body.first;
    let second = req.body.second;
    console.log(first);
    res.json({ "result": first-second });
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});