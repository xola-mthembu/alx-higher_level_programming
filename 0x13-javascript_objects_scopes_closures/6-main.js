#!/usr/bin/node
/* Test script for the enhanced Square class */
const Square = require('./6-square');

const s1 = new Square(4);
s1.charPrint(); // Should print the square using 'X'

s1.charPrint('C'); // Should print the square using 'C'
