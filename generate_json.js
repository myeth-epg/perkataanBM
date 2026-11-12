const fs = require('fs');
const path = require('path');

const dataPath = path.join(__dirname, 'perkataan_bm_data.json');
const data = JSON.parse(fs.readFileSync(dataPath, 'utf8'));

console.log(`Loaded ${data.length} vocabulary words.`);

// Example verification
console.log('Sample item:', data[0]);
