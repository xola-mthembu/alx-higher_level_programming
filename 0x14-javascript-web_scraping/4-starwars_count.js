#!/usr/bin/node

const request = require('request');

if (process.argv.length <= 2) {
  console.log('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const films = JSON.parse(body).results;
  let wedgeCount = 0;
  films.forEach(film => {
    if (film.characters.some(character => character.includes('/18/'))) {
      wedgeCount++;
    }
  });
  console.log(wedgeCount);
});
