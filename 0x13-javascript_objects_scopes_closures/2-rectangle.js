#!/usr/bin/node
/* Rectangle class that defines a rectangle,
   now with validation to ensure width and height are positive */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
