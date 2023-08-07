const express = require('express');
const app = express();

const PORT = process.env.PORT || 3000;


app.use(express.json());

const baseRouter = express.Router();

app.get('/', (req, res) => {
    return res.json({data:"Hello guys"});
});

app.post('/add', (req, res) => {
    res.json({ "": null });
});


app.post('/subtract', (req, res) => {
    res.json({ "": null });
});

app.listen(PORT, () => {
    console.log("Server running at PORT", PORT);
});