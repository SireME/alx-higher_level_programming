#!/usr/bin/node

const fs = require('fs');

// readding and printing content od a file
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
