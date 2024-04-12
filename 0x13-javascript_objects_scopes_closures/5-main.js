#!/usr/bin/node
/* Test script for the Square class */
const Square = require('./5-square');

const s1 = new Square(4);
console.log('Normal:');
s1.print();

console.log('Double:');
s1.double();
s1.print();
