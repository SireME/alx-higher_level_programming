#!/usr/bin/node
// read contentf rom filea and send to another
const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 5) {
  console.error('Usage: node 102-concat.js <fileA> <fileB> <fileC>');
  process.exit(1);
}

// Get file paths from command line arguments
const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const fileCPath = process.argv[4];

// Read the contents of fileA and fileB
const fileAContent = fs.readFileSync(fileAPath, 'utf8');
const fileBContent = fs.readFileSync(fileBPath, 'utf8');

// Concatenate the contents of fileA and fileB
const concatenatedContent = fileAContent + fileBContent;

// Write the concatenated content to fileC
fs.writeFileSync(fileCPath, concatenatedContent);

// completion message
console.log('Concatenation complete. Check ' + fileCPath + ' for the result.');
