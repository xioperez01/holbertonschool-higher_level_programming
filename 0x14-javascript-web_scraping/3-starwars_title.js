#!/usr/bin/node
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } /*else if (response.statusCode !== 200) {
    console.log(response.statusCode);
  }*/ else {
    body = JSON.parse(body);
    console.log(body['title']);
  }
});
