#!/usr/bin/node
/** File: : 100-map.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */
const list = require('./100-data.js').list;

const newList = list.map((item, index) => item * index);
console.log(list);
console.log(newList);
