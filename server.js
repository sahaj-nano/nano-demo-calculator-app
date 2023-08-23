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
    const a=req.body.first;
    const b=req.body.second;
    res.json({ "result": a+b }).status(200);
});


baseRouter.post('/subtract', (req, res) => {
    const a=req.body.first;
    const b=req.body.second;
    res.json({ "result": a-b }).status(200);
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});