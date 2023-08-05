const express = require('express');
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    return res.send('Hello World');
});

baseRouter.post('/add', (req, res) => {
    var first=req.body.first;
    var second=req.body.second;
    var result=first+second;
    res.json({ "result": result });
});


baseRouter.post('/subtract', (req, res) => {
    var first=req.body.first;
    var second=req.body.second;
    var result=first-second;
    res.json({ "result": result });
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});