#!/usr/bin/node

const fs = require('fs');

// readding and printing content od a file
fs.writeFile(process.argv[2], process.argv[3], 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
}
);
