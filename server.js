const express = require('express');
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());

const baseRouter = express.Router();

//greeting endpoint
baseRouter.get('/greeting', (req, res) => {
    return res.status(200).json({"content":"Hello world!"});
});

//add endpoint
baseRouter.post('/add', (req, res) => {
    const {first,second}=req.body;
    const result=parseInt(first)+parseInt(second);
    res.status(200).json({ "result": result });
});

//subtract endpoint
baseRouter.post('/subtract', (req, res) => {
    const { first, second } = req.body;
    const diff = parseInt(first) - parseInt(second);
    res.status(200).json({ "result": diff });
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});