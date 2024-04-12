#!/usr/bin/node
/* Script that imports a dictionary of occurrences and computes a dictionary
   of user ids by occurrence */
const { dict } = require('./101-data.js');

const newDict = {};
Object.keys(dict).forEach(key => {
  const value = dict[key];
  if (!newDict[value]) {
    newDict[value] = [];
  }
  newDict[value].push(key);
});

console.log(newDict);
