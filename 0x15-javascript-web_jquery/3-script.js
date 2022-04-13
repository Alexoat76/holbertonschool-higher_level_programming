#!/usr/bin/node
/** File:  3-script.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */

$(() => {
  $('DIV#red_header').click(() => {
    if (!$('header').hasClass('red')) {
      $('header').addClass('red');
    }
  });
});
