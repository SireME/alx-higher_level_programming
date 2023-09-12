#!/usr/bin/node
// import Rectangle
const Rectangle = require('./4-rectangle.js');

// create square class and inherite from Recatngle
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
