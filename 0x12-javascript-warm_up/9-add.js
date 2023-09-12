#!/usr/bin/node
// function to print addition of two numbers
// from input

function add (a, b) {
  return a + b;
}
// print addition to stdout
console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
