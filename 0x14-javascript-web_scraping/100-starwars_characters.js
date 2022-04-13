#!/usr/bin/node
/** File:  100-starwars_characters.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */

const process = require('process');
const request = require('request');

const movie = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movie;

function printCharName (charUrl) {
  request(charUrl, function (error, response, body) {
    if (error != null) {
      console.log(error);
    } else {
      const data = JSON.parse(body);
      console.log(data.name);
    }
  });
}

request(url, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.characters.forEach(function (charUrl) {
      printCharName(charUrl);
    });
  }
});
