#!/usr/bin/node
/*
Module that defines a rectangle
*/

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    /* Print a rectangle */
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    /* exchanges the width and the height of the rectangle */
    const new_ = this.width;
    this.width = this.height;
    this.height = new_;
  }

  double () {
    /* multiples the width and the height  by 2 */
    this.width *= 2;
    this.height *= 2;
  }
};
