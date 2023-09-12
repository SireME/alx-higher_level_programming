#!/usr/bin/node
// print first argument if number
if (isNaN(Number(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= (process.argv[2] | 0); i++) {
  // don't print negatives
    if (i < 0) {
      break;
    }

    // print based on number of times
    console.log('C is fun');
  }
}
