#!/usr/bin/node
// print first argument if number
if (isNaN(Number(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${process.argv[2] | 0}`);
}
