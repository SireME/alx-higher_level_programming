#!/usr/bin/node

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;
let charac;

// query a url and write its content to a file
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return 7;
  }
  if (response.statusCode === 200) {
    charac = JSON.parse(body).characters;
    for (let i = 0; i < charac.length; i++) {
      request(charac[i], (error, response, bd) => {
        if (error) {
          console.log(error);
          return;
        }
        if (response.statusCode === 200) {
          console.log(JSON.parse(bd).name);
        }
      });
    }
  }
});
