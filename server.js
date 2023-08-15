const express = require('express');
const app = express();

const PORT = process.env.PORT || 8080;

const baseUrl = '/calculator';

const baseRouter = express.Router();

baseRouter.get('/greeting', (req, res) => {
    return res.status(200).send('Hello world!');
});

baseRouter.post('/add', (req, res) => {
    const { first, second } = req.body;

    if (typeof first !== 'number' || typeof second !== 'number') {
        return res.status(400).json({ error: 'Invalid input. Both inputs should be numbers.' });
    }

    const result = first + second;
    return res.status(200).json({ result: result });
});

baseRouter.post('/subtract', (req, res) => {
    const { first, second } = req.body;

    if (typeof first !== 'number' || typeof second !== 'number') {
        return res.status(400).json({ error: 'Invalid input. Both inputs should be numbers.' });
    }

    const result = first - second;
    return res.status(200).json({ result: result });
});

app.use(express.json()); // Parse JSON bodies

app.use(baseUrl, baseRouter); // Mount the router under /calculator

app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});
