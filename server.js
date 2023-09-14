const express = require('express');
const app = express();

const bodyparser = require('body-parser');
app.use(bodyparser.urlencoded({extended : true}));

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    return res.send('Hello world!');
});

baseRouter.post('/add', (req, res) => {
    var a=parseInt(req.body["first"])+parseInt(req.body["second"]);
    res.json({ "result": a });
});


baseRouter.post('/subtract', (req, res) => {
    var a=parseInt(req.body["first"])-parseInt(req.body["second"]);
    res.json({ "result": a });
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});