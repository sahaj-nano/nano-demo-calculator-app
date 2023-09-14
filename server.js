const express = require('express');
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    res.status(200)
    return res.send('Hello World!');
});

baseRouter.post('/add', (req, res) => {
    res.status(200)
    res.json({ "result":req.body.first+req.body.second});
});


baseRouter.post('/subtract', (req, res) => {
    res.status(200)
    res.json({ "result":req.body.first-req.body.second});
});




app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});