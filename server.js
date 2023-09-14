const express = require('express');
const app = express();

const PORT = process.env.PORT || 3000

const baseUrl = '/calculator'

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    return res.send('service is availble');
});

baseRouter.post('/add', (req, res) => {
    var a=parseInt(req.body.first);
     var b=parseInt(req.body.second);
     res.send({
        "result":a+b,
     }
     ).json();
});


baseRouter.post('/subtract', (req, res) => {
    var a=parseInt(req.body.first);
    var b=parseInt(req.body.second);
    res.send({
       "result":a-b,
    }
    ).json();
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});