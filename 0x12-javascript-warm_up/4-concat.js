#!/usr/bin/node
// This script prints two arguments in the format: "first is second"
const args = process.argv;

console.log(`${args[2] || 'undefined'} is ${args[3] || 'undefined'}`);
