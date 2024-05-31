#!/usr/bin/node

/* global $ */

$(document).ready(function () {
  function fetchHello () {
    const lang = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${lang}`, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(fetchHello);

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchHello();
    }
  });
});
