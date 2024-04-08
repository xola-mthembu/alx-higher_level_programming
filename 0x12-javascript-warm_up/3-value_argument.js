#!/usr/bin/node
// This script prints the first argument passed to it
const arg = process.argv[2];

console.log(arg || 'No argument');
