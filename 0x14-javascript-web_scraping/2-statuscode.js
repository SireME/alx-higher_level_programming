#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

// readding and printing content od a file
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  console.log(`code: ${response.statusCode}`);
}
);
