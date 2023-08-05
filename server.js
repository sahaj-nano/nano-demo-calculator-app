const express = require('express');
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator'

app.use(express.json());

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    return res.send('Hello World!');
});

baseRouter.post('/add', (req, res) => {
    const { first, second } = req.body;
    if (typeof first !== 'number' || typeof second !== 'number') {
        return res.status(400).json({ error: 'Invalid input. Both first and second must be numbers.' });
    }

    const result = first + second;
    res.status(200).json({ result: result });
});

baseRouter.post('/subtract', (req, res) => {
    const { first, second } = req.body;
    if (typeof first !== 'number' || typeof second !== 'number') {
        return res.status(400).json({ error: 'Invalid input. Both first and second must be numbers.' });
    }

    const result = first - second;
    res.status(200).json({ result: result });
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});
