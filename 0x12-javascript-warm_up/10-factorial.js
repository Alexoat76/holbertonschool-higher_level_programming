#!/usr/bin/node
/** File: 10-factorial.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */

/*
 * factorial - Computes the factorial of a number.
 * @param {Number} num - The number.
 * @return: The factorial of the number.
 */
function factorial (num) {
  if (Number.isNaN(num) || (num <= 0)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

console.log(factorial(Number.parseInt(process.argv[2])));
