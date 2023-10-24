#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
let present = 0;

// query number of movies by character Wedge Antilles
request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else
    if (!error && response.statusCode === 200) {
      const jsonObject = JSON.parse(body);
      for (const film of jsonObject.results) {
        for (const url of film.characters) {
          if (url === 'https://swapi-api.alx-tools.com/api/people/18/') {
            present++;
          }
        }
      }
      console.log(present);
    }
}
);
