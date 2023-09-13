#!/usr/bin/node

const oldArray = require('./100-data.js').list;

// print imported old array
console.log(oldArray);

// compute new array
let idx = 0;
const newArray = oldArray.map((x) => x * idx++);

// print modified list
console.log(newArray);
