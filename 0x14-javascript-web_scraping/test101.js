const request = require('request');

function makeRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode === 200) {
        resolve(JSON.parse(body).name);
      } else {
        resolve(null);
      }
    });
  });
}

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const charac = JSON.parse(body).characters;

    const promises = charac.map(makeRequest);

    Promise.all(promises)
      .then((characters) => {
        for (const character of characters) {
          if (character) {
            console.log(character);
          }
        }
      })
      .catch((err) => {
        console.error(err);
      });
  }
});

