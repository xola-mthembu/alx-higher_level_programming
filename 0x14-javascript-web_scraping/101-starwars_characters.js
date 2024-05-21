#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const characters = JSON.parse(body).characters;
  printCharacters(characters, 0);
});

function printCharacters (characters, index) {
  if (index >= characters.length) {
    return;
  }
  request(characters[index], (err, response, body) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(JSON.parse(body).name);
    printCharacters(characters, index + 1);
  });
}
