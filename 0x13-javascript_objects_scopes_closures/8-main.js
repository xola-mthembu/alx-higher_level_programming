#!/usr/bin/node
/* Test script for the esrever function */
const esrever = require('./8-esrever').esrever;

console.log(esrever([1, 2, 3, 4, 5]));
console.log(esrever(['School', 89, { id: 12 }, 'String']));
