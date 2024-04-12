#!/usr/bin/node
// This script prints "My number: <first argument converted to integer>"
// if the first argument can be converted to an integer, otherwise "Not a number"
const arg = process.argv[2];
const num = parseInt(arg);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
