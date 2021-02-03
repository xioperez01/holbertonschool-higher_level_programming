#!/usr/bin/node
const argument = parseInt(process.argv[2], 10);
if (isNaN(argument)) {
  console.log('Missing number of occurences');
} else {
  for (let i = argument; i > 0; i -= 1) {
    console.log('C is fun');
  }
}
