#!/usr/bin/node
/*
class Square
*/
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  /* defines a square and inherits from Rectangle of 4-rectangle.js: */
  constructor (size) {
    super(size, size);
  }
};
