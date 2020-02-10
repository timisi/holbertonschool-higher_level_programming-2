#!/usr/bin/node

const list = require('./100-main.js').list;

console.log(list);
const newList = list.map(function (num, index) {
  return num * index;
});
console.log(newList);
