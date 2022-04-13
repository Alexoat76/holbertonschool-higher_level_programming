/** File:  9-script.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */
$(() => {
  const url = 'https://fourtonfish.com';

  $.get(`${url}/hellosalut/?lang=fr`, (data, status) => {
    $('DIV#hello').html(data.hello);
  });
});
