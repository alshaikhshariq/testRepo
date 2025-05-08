// src/limiter.js
const redis = require('./redisClient');
require('dotenv').config();

const WINDOW_SIZE_IN_MS = parseInt(process.env.WINDOW_SIZE) || 60000; // 1 minute
const MAX_REQUESTS = parseInt(process.env.RATE_LIMIT) || 200;

module.exports = async function rateLimiter(req, res, next) {
    const apiKey = req.header('X-API-Key');
    if (!apiKey) {
        return res.status(400).send('Missing API key');
    }

    const currentTimestamp = Date.now();
    const windowStartTimestamp = currentTimestamp - WINDOW_SIZE_IN_MS;
    const redisKey = `rate:${apiKey}`;

    try {
        // Remove old requests outside the window
        await redis.zRemRangeByScore(redisKey, 0, windowStartTimestamp);

        // Get the number of requests in the current window
        const requestCount = await redis.zCard(redisKey);

        if (requestCount >= MAX_REQUESTS) {
            return res.status(429).send('Too Many Requests');
        }

        // Add current request timestamp
        await redis.zAdd(redisKey, {
            score: currentTimestamp,
            value: `${currentTimestamp}-${Math.random()}` // unique entry
        });

        // Optional: Set TTL to auto-cleanup Redis keys
        await redis.expire(redisKey, Math.ceil(WINDOW_SIZE_IN_MS / 1000) + 5);

        next();
    } catch (err) {
        console.error('⚠️ Rate limiter error:', err);
        // Allow request on Redis failure
        next();
    }
};
