#!/usr/bin/node
const fs = require('fs');
const url = process.argv[2];

// query a url and write its content to a file
const request = require('request');
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  if (response.statusCode === 200) {
    fs.writeFile(process.argv[3], body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
