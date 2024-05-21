#!/usr/bin/node

const request = require('request');

if (process.argv.length <= 2) {
  console.log('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const movies = JSON.parse(body).results;
  let count = 0;
  for (const movie of movies) {
    for (const characterUrl of movie.characters) {
      if (characterUrl.endsWith('/18/')) {
        count++;
        break;
      }
    }
  }
  console.log(count);
});
