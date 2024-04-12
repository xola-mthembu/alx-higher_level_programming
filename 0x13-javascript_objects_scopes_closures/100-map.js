#!/usr/bin/node
/* Script that imports an array and computes a new array using map */
const { list } = require('./100-data.js');

console.log(list);
const newList = list.map((element, index) => element * index);
console.log(newList);
