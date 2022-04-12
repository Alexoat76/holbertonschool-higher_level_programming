#!/usr/bin/node
/** File:  1-writeme.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */

const process = require('process');
const filesystem = require('fs');

const file = process.argv[2];
const text = process.argv[3];

filesystem.writeFile(file, text, 'utf8', function (err, data) {
  if (err != null) {
    console.log(err);
  }
});
