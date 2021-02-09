#!/usr/bin/node
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    body = JSON.parse(body);
    for (const i in body.characters) {
      request(body.characters[i], function (error, response, body) {
        if (error) {
          console.error(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
