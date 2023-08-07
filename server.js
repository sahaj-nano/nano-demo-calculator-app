const express = require('express');
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    return res.send('Hello World!');
});

baseRouter.post('/add', (req, res) => {
    const a = req.body.first;
    const b = req.body.second;
    const sum = a+b;
    res.json({ "result": sum });
});


baseRouter.post('/subtract', (req, res) => {
    const a = req.body.first;
    const b = req.body.second;
    const diff = a-b;
    res.json({ "result": diff });
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});