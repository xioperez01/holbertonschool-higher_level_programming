#!/usr/bin/node
const fileName = process.argv[2];
const toWrite = process.argv[3];
const fs = require('fs');
fs.appendFile(fileName, toWrite, 'utf-8', function (error) {
  if (error) {
    console.error(error);
  }
});
