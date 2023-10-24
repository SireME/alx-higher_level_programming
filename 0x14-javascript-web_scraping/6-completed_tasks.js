#!/usr/bin/node
const url = process.argv[2];
const numCompleted = {};
let res;

// query a url and write its content to a file
const request = require('request');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return 7;
  }
  if (response.statusCode === 200) {
    res = JSON.parse(body);
    for (let i = 0; i < res.length; i++) {
      if (res[i].completed === true) {
        if (numCompleted[`${res[i].userId}`] === undefined) {
          numCompleted[`${res[i].userId}`] = 1;
        } else {
          numCompleted[`${res[i].userId}`] += 1;
        }
      }
    }
  }
  console.log(numCompleted);
});
