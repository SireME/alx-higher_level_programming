#!/usr/bin/node
// determine if script contains argument or not
if (process.argv.length < 3) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
