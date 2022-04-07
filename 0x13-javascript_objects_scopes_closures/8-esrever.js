#!/usr/bin/node
/** File: : 8-esrever.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */
exports.esrever = function (list) {
  const rev = [];
  for (let i = 0; i < list.length; i++) {
    rev.unshift(list[i]);
  }
  return rev;
};
