#!/usr/bin/node
/** File:  6-completed_tasks.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */

const process = require('process');
const request = require('request');

const url = process.argv[2];
let data;
const collected = {};

request(url, function (error, response, body) {
  if (error != null) {
    console.log(error);
  } else {
    data = JSON.parse(body);
    data.forEach(function (result) {
      if (result.completed === true) {
        const userid = result.userId;
        if (!(userid in collected)) {
          collected[userid] = 0;
        }
        collected[userid] += 1;
      }
    });
    console.log(collected);
  }
});
