#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

// readding and printing content od a file
request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    console.log('code: 200');
  } else {
    console.log('code: 404');
  }
}
);
