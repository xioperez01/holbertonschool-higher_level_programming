#!/usr/bin/node
/*
Reverse Function
*/
exports.esrever = function (list) {
  // Returns the reversed version of a list
  const esrever = [];
  let j = list.length - 1;
  for (let i = 0; i < list.length; i++) {
    esrever[i] = list[j];
    j--;
  }
  return esrever;
};
