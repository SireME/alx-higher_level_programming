#!/usr/bin/node

// print number of elements already printed and new argument value
let printed = 0;
exports.logMe = function (item) {
  console.log(`${printed}: ${item}`);
  printed++;
};
