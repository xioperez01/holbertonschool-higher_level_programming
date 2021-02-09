#!/usr/bin/node
/*
logMe Function
*/
let count = 0;
exports.logMe = function (item) {
  // prints <number arguments already printed>: <current argument value>
  console.log(count + ': ' + item);
  count += 1;
};
