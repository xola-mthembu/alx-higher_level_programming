#!/usr/bin/node
// This script adds a function that increments the value of myObject

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

myObject.incr = function () { // YOUR CODE HERE
  this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
