const express = require('express');
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    return res.send("Hello world!");
});

baseRouter.post('/add', (req, res) => {
    const fnum = req.body.first * 1;
    const snum = req.body.second * 1;
    res.json({ "":  fnum + snum});
});


baseRouter.post('/subtract', (req, res) => {
    const fnum = req.body.first * 1;
    const snum = req.body.second * 1;
    res.json({ "":  fnum - snum});
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});