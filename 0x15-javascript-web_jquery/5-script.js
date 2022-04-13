/** File:  5-script.js
*   Author: Alex Orland Arévalo Tribaldos
*   email: <3915@holbertonschool.com> */
$(() => {
  $('DIV#add_item').click(() => {
    const newItem = document.createElement('li');

    newItem.textContent = 'Item';
    $('UL.my_list').append(newItem);
  });
});
