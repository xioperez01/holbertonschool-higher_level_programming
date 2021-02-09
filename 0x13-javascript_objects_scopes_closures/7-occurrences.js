#!/usr/bin/node
/*
nbOccurences function
*/
module.exports.nbOccurences = function (list, searchElement) {
  // Returns the number of occurrences in a list
  let counter = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      counter += 1;
    }
  }
  return counter;
};
