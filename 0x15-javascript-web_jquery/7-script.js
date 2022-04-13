/** File:  7-script.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */
$(() => {
  const url = 'https://swapi-api.hbtn.io/api';

  $.get(`${url}/people/5/?format=json`, (data, status) => {
    $('DIV#character').html(data.name);
  });
});
