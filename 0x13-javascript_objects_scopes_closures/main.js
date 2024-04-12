#!/usr/bin/node
/* Importing the Rectangle class */
const Rectangle = require('./Rectangle');

/* Creating a Rectangle object */
const myRectangle = new Rectangle(2, 3);

console.log(`Area: ${myRectangle.area()}`);
