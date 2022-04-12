#!/usr/bin/node
/** File:  4-starwars_count.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */

const process = require('process');
const request = require('request');

const url = process.argv[2];
let data;

request(url, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    let movies = 0;
    data = JSON.parse(body);
    data.results.forEach(function (result) {
      result.characters.forEach(function (character) {
        const urlSplit = character.split('/');
        if (urlSplit[urlSplit.length - 2] === '18') {
          movies++;
        }
      });
    });
    console.log(movies);
  }
});
