const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000

const baseUrl = '/calculator'
const bodyparser = require("body-parser");
app.use(bodyparser.urlencoded({extended:true}));
app.use(express.json());

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    return res.send('Hello!');
});

baseRouter.post('/add', (req, res) => {
    var a=parseInt(req.body.first);
     var b=parseInt(req.body.second);
     res.json({
        "result":a+b,
     }
     )
});


baseRouter.post('/subtract', (req, res) => {
    var a=parseInt(req.body.first);
    var b=parseInt(req.body.second);
    res.json({
       "result":a-b,
    }
    );
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});