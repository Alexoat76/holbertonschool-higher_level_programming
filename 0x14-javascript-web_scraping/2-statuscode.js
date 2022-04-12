#!/usr/bin/node
/** File:  2-statuscode.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */

const process = require('process');
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
