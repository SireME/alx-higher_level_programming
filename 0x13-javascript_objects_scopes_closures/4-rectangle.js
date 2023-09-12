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

  print () { // print rectangle using width and height
    for (let i = 1; i <= this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () { // replace width by heightand vice versa
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () { // double width and height
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
