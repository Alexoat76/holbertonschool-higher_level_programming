#!/usr/bin/node
/** File: : 7-occurrences.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
