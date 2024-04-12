#!/usr/bin/node
// This module defines a function that executes another function x times

function callMeMoby (x, theFunction) { // Added space before the parentheses
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports.callMeMoby = callMeMoby;
