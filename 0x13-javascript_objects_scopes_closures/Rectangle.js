#!/usr/bin/node
/* Rectangle class definition */
class Rectangle {
  constructor (width, height) {
    this.width = width;
    this.height = height;
  }

  area () {
    return (this.width * this.height);
  }
}

module.exports = Rectangle;
