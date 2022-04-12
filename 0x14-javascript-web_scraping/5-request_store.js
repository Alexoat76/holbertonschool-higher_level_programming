#!/usr/bin/node
/** File:  5-request_store.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */

const process = require('process');
const request = require('request');
const filesystem = require('fs');

const url = process.argv[2];
const filepath = process.argv[3];

request(url, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    filesystem.writeFile(filepath, body, 'utf8', function (err, data) {
      if (err != null) {
        console.log(error);
      }
    });
  }
});
