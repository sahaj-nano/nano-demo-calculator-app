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
    var n1=req.body.first;
    var n2=req.body.second;
    res.json({ "result": n1+n2 });
});


baseRouter.post('/subtract', (req, res) => {
    var n1=req.body.first;
    var n2=req.body.second;
    res.json({ "result": n1-n2 });
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});