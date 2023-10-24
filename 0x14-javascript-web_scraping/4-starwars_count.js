#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
let character;

// query number of movies by character Wedge Antilles
request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const jsonObject = JSON.parse(body);
    character = jsonObject.results[0].characters[15];
  }

  request(character, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const numberFilm = JSON.parse(body).films.length;
      console.log(numberFilm);
    }
  }
  );
}
);
