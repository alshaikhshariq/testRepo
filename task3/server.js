const express = require('express');
const { isFeatureEnabled } = require('./flagService'); // Import the flag service
const app = express();
const port = 9000;

// Flag evaluation endpoint
app.get('/flags', (req, res) => {
    const userId = req.query.user;
    const region = req.query.region;

    if (!userId || !region) {
        return res.status(400).json({ error: 'User and Region are required parameters' });
    }

    const featureAEnabled = isFeatureEnabled('featureA', userId, region);
    const featureBEnabled = isFeatureEnabled('featureB', userId, region);

    return res.json({
        featureA: featureAEnabled,
        featureB: featureBEnabled
    });
});

app.listen(port, () => {
    console.log(`Feature Flag Service is running on http://localhost:${port}`);
});
