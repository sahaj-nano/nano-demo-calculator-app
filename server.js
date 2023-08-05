const express = require('express');
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    return res.status(200).send("Hello world!")
});

baseRouter.post('/add', (req, res) => {
    const {first,second}=req.body;
    const addition=parseInt(first)+parseInt(second);
    res.status(200).json({ "result": addition });
});


baseRouter.post('/subtract', (req, res) => {
    const { first, second } = req.body;
    const difference = parseInt(first) - parseInt(second);
    res.status(200).json({ "result": difference });
});
app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});