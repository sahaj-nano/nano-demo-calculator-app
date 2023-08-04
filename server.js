const express = require('express');
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    return res.send('Hello Wolrd');
});

baseRouter.post('/add', (req, res) => {
    const {first,second} = req.body;
    const result = first+second;
    res.json({ "result": result });
});


baseRouter.post('/subtract', (req, res) => {
     const {first,second} = req.body;
    const result = first-second;
    res.json({ "result": result });
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});
