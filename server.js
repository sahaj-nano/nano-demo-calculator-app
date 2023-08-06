const express = require('express');
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator';

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    return res.send('Hello world!');
});

baseRouter.post('/add', (req, res) => {
    const { num1, num2 } = req.body;
    if (num1 === undefined || num2 === undefined) {
        return res.status(400).json({ error: 'Both num1 and num2 are required.' });
    }
    
    const sum = num1 + num2;
    res.json({ result: sum });
});

baseRouter.post('/subtract', (req, res) => {
    const { num1, num2 } = req.body;
    if (num1 === undefined || num2 === undefined) {
        return res.status(400).json({ error: 'Both num1 and num2 are required.' });
    }
    
    const difference = num1 - num2;
    res.json({ result: difference });
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});
