#!/usr/bin/node
/** File:  4-script.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */

$(() => {
  $('DIV#toggle_header').click(() => {
    if ($('header').hasClass('red')) {
      $('header').removeClass('red');
      if (!$('header').hasClass('green')) {
        $('header').addClass('green');
      }
    } else if ($('header').hasClass('green')) {
      $('header').removeClass('green');
      if (!$('header').hasClass('red')) {
        $('header').addClass('red');
      }
    } else {
      $('header').addClass('red');
    }
  });
});
