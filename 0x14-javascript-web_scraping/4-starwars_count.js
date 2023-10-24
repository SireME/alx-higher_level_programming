#!/usr/bin/node
// A script that prints the number of movies where the character Wedge Antilles is present

const filmsUrl = process.argv[2];

const request = require('request');
request(filmsUrl, (error, response, body) => {
  const jsonObject = JSON.parse(body);
  const results = jsonObject.results;
  let count = 0;
  if (error) {
    console.log(error);
    return;
  }
  for (let i = 0; i < results.length; i++) {
    const character = (results[i].characters);
    for (let j = 0; j < character.length; j++) {
      const check = character[j].endsWith('18/');
      if (check) {
        count++;
      }
    }
  }
  console.log(count);
});
