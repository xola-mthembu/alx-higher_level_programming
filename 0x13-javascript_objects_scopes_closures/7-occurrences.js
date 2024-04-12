#!/usr/bin/node
/* Function that returns the number of occurrences in a list */
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((count, current) => count + (current === searchElement ? 1 : 0), 0);
};
