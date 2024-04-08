#!/usr/bin/node
// This script prints "C is fun" x times, where x is the first argument of the script
const arg = process.argv[2];
const times = parseInt(arg);

if (isNaN(times)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
}
