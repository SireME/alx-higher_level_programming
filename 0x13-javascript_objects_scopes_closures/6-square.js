#!/usr/bin/node
// import Rectangle
const Rectangle = require('./4-rectangle.js');

// create square class and inherite from Recatngle
class Square extends Rectangle {
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
