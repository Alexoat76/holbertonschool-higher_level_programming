#!/usr/bin/node
/** File: : 9-logme.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */
let num = 0;
exports.logMe = function (item) {
  console.log(num + ': ' + item);
  num++;
};
