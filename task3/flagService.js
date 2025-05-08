// flagService.js
const fs = require('fs');
const chokidar = require('chokidar');
const path = require('path');

const FLAGS_PATH = path.join(__dirname, 'flags.json');

let flags = {};

function loadFlags() {
    try {
        const raw = fs.readFileSync(FLAGS_PATH);
        flags = JSON.parse(raw);
        console.log('Flags reloaded:', new Date().toISOString());
    } catch (err) {
        console.error('Failed to load flags:', err.message);
    }
}

// Load initially
loadFlags();

// Watch for changes
chokidar.watch(FLAGS_PATH).on('change', () => {
    setTimeout(loadFlags, 100); // Debounce reload
});

// Evaluation function
function isFeatureEnabled(feature, userId, region) {
    const f = flags[feature];
    if (!f) return false;

    const userOverrides = f.overrides?.users || {};
    const regionOverrides = f.overrides?.regions || {};

    if (userOverrides.hasOwnProperty(userId)) {
        return userOverrides[userId];
    }

    if (regionOverrides.hasOwnProperty(region)) {
        return regionOverrides[region];
    }

    return f.enabled;
}

module.exports = { isFeatureEnabled };
