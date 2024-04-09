#!/usr/bin/node
/* Function that logs the number of arguments printed and the new argument value */
let count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
