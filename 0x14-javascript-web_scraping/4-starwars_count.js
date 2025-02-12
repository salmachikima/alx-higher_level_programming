#!/usr/bin/node

const request = require('request');
const starWarsUri = process.argv[2];
let times = 0;

request(starWarsUri, function (_err, _res, body) {
  body = JSON.parse(body).results;

  for (let s = 0; s < body.length; ++s) {
    const characters = body[s].characters;

    for (let r = 0; r < characters.length; ++r) {
      const character = characters[r];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        times += 1;
      }
    }
  }

  console.log(times);
});
