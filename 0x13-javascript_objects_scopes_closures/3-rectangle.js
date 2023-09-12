#!/usr/bin/node

// initialise empty class and initialise
// constructor except when values are invalid
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 1; i <= this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
