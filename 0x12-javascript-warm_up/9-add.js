#!/usr/bin/node
// This script defines a function to add two integers and prints the result
function add (a, b) { // Note the space before the parentheses
  return a + b;
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

console.log(add(arg1, arg2));
