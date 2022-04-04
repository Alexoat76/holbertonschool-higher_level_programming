#!/usr/bin/node
/** File: 7-multi_c.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */
const num = parseInt(process.argv[2], 10);
if (isNaN(num)) {
  console.log('Missing number of occurences');
} else {
  for (let i = num; i > 0; i -= 1) {
    console.log('C is fun');
  }
}
