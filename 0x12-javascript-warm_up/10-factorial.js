#!/usr/bin/node
// This script computes and prints the factorial of a number recursively
function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else if (n < 0) {
    return 'Undefined'; // Factorial for negative numbers is undefined
  } else {
    return n * factorial(n - 1);
  }
}

const arg = parseInt(process.argv[2]);
console.log(factorial(arg));
