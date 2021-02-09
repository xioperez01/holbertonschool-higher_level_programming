#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    let count = 0;
    body = JSON.parse(body).results;
    for (const i in body) {
      const chars = body[i].characters;
      for (const j in chars) {
        if (chars[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
          count++;
        }
      }
    }
    console.log(count);
  }
});
