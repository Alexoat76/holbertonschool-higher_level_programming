#!/usr/bin/node
/** File: 3-value_argument.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */
const arg0 = process.argv[2];
console.log(arg0 !== undefined ? arg0 : 'No argument');
