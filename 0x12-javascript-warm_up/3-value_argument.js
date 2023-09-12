#!/usr/bin/node
// determine if script contains argument or not
if (!process.argv[2]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
