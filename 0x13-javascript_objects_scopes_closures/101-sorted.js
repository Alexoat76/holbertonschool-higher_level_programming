#!/usr/bin/node
/** File: : 101-sorted.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */

const dict = require('./101-data').dict;

const newDic = {};
for (const key in dict) {
  if (newDic[dict[key]] === undefined) {
    newDic[dict[key]] = [];
  }
  newDic[dict[key]].push(key);
}

console.log(newDic);
