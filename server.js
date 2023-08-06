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
    const { first, second } = req.body;
    if (typeof first === 'number' && typeof second === 'number') {
        const result = first + second;
       return res.json({ result });
    } else {
       return res.status(400).json({ error: 'Invalid input. Both numbers must be valid.' });
    }
});

baseRouter.post('/subtract', (req, res) => {
    
    const { first, second } = req.body;

   
    if (typeof first === 'number' && typeof second === 'number') {
       
        const result = first - second;
        
        return res.json({ result });
    } else {
       
        return res.status(400).json({ error: 'Invalid input. Both numbers must be valid.' });
    }
});

app.use(baseUrl, baseRouter);
app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});
