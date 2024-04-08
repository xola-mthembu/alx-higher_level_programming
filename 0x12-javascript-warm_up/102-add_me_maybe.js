#!/usr/bin/node
// This module defines a function that increments a number and then calls a function

function addMeMaybe (number, theFunction) {
  theFunction(number + 1);
}

module.exports.addMeMaybe = addMeMaybe;
