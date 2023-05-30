const express = require('express');
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    res.send('Hello world');
    res.sendStatus(200);    
});

baseRouter.post('/add', (req, res) => {
    const data = req.body;
    let result = data['first'] + data['second'];
    res.json({ "result": result });
});


baseRouter.post('/subtract', (req, res) => {
    const data = req.body;
    let result = data['first'] - data['second'];
    res.json({ "result": result }); 
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});
