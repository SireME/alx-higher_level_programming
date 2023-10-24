#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
let character;

// query number of movies by character Wedge Antilles
request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (!error && response.statusCode === 200) {
    const jsonObject = JSON.parse(body);
    for (const url of jsonObject.results[0].characters) {
      if (url === 'https://swapi-api.alx-tools.com/api/people/18/') {
        character = url;
      }
    }
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
