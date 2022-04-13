/** File:  8-script.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */
$(() => {
  const url = 'https://swapi-api.hbtn.io/api';

  $.get(`${url}/films/?format=json`, (data, status) => {
    data.results.forEach(film => {
      $('UL#list_movies').append(`<li>${film.title}</li>`);
    });
  });
});
