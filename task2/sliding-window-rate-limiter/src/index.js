// src/index.js
const express = require('express');
const rateLimiter = require('./limiter');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 8080;

app.use(rateLimiter); // apply rate limiter middleware

app.get('/resource', (req, res) => {
    res.status(200).send('✅ Request allowed.');
});

app.listen(PORT, () => {
    console.log(`🚀 Server is running on http://localhost:${PORT}`);
});
