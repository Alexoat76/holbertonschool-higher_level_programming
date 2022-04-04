#!/usr/bin/node
/** File: 5-to_integer.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */
const num = Number.parseInt(process.argv[2]);
console.log(Number.isNaN(num) ? 'Not a number' : 'My number: ' + num);
