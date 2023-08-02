const express = require('express');
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    res.status(200).send("Hello world!")
});

baseRouter.post('/add', (req, res) => {
    if(req.body.first==null || req.body.second==null)
    res.status(400).json({ "result": "Wrong input" });
    
    let {first,second} =req.body;
    res.status(200).json({ "result": first+second });
});


baseRouter.post('/subtract', (req, res) => {
    if(req.body.first==null || req.body.second==null)
    res.status(400).json({ "result": "Wrong input" });

    const {first,second} =req.body;
     res.status(200).json({ "result": first-second });
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});