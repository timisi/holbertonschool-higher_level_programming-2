#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    if (!(size <= 0) && size) {
      this.size = size;
    }
  }
};
