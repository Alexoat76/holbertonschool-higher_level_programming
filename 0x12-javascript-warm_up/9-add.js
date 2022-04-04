#!/usr/bin/node
/** File: 9-add.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */
/**
* add - Computes the sum of 2 numbers.
* @param {Number} a - The first number.
* @param {Number} b - The second number.
* @returns The sum of the 2 numbers.
*/
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return (NaN);
  } else {
    return a + b;
  }
}
console.log(
  add(Number.parseInt(process.argv[2]), Number.parseInt(process.argv[3]))
);
