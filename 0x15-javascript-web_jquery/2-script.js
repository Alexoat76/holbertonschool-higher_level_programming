#!/usr/bin/node
/** File:  2-script.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */

$(() => {
  $('DIV#red_header').click(() => {
    $('header').css('color', '#FF0000');
  });
});
