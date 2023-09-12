#!/usr/bin/node
// print square first argument is the size
if (isNaN(Number(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= (process.argv[2] | 0); i++) {
  // do not attempt if argument is negative
    if (i < 0) {
      break;
    }

    // print lines for square
    console.log('X'.repeat(process.argv[2] | 0));
  }
}
