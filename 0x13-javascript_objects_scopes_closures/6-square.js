#!/usr/bin/node
// import Rectangle
const square = require('./5-square.js');

// create square class and inherite from Recatngle
class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let pr = c;
    if (pr === undefined) {
      pr = 'X';
    }
    for (let i = 1; i <= this.height; i++) {
      console.log(pr.repeat(this.height));
    }
  }
}

module.exports = Square;
