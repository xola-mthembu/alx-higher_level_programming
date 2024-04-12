#!/usr/bin/node
/* Function that returns a conversion function from base 10 to the specified base */
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
