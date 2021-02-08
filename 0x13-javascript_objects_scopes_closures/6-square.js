#!/usr/bin/node
/*
class Square
*/
const SquareBase = require('./5-square');

module.exports = class Square extends SquareBase {
  /* defines asquare and inherits from Square of 5-square.js */
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
