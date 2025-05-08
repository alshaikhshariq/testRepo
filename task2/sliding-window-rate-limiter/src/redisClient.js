// src/redisClient.js
const { createClient } = require('redis');
require('dotenv').config();

const redisClient = createClient({
    socket: {
        host: process.env.REDIS_HOST || 'localhost',
        port: process.env.REDIS_PORT || 6379
    }
});

redisClient.on('error', (err) => {
    console.error('Redis connection error:', err);
});

(async () => {
    try {
        await redisClient.connect();
        console.log('Connected to Redis');
    } catch (err) {
        console.error('Redis connect failed:', err);
    }
})();

module.exports = redisClient;
