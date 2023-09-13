#!/usr/bin/node

// compute and print factorial

function fac (n) {
  if (isNaN(n)) {
    return 1;
  }

  if (n === 1) {
    return n;
  }

  return n * fac(n - 1);
}

console.log(fac(process.argv[2]));
