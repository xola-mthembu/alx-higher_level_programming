#!/usr/bin/node

/* global $ */

$(document).ready(function () {
  $('#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
});
