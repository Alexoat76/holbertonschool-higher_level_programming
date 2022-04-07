#!/usr/bin/node
/** File: : 10-converter.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
