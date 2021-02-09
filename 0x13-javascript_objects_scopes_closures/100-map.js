#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const listNew = list.map((i, index) => i * index);
console.log(listNew);
