#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

// readding and printing content od a file
request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const jsonObject = JSON.parse(body);
    console.log(jsonObject.title);
  }
}
);
