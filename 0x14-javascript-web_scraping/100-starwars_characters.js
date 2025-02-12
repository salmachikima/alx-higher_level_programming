#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const fullUrl = baseUrl.concat(movieId);

request(fullUrl, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
    // variable where to store the num of chars processed
    let charactersProcessed = 0;
    // storing the characters name by creating an empty array
    const characterNames = [];
    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (!error) {
          const charName = JSON.parse(body).name;
          // character name
          characterNames.push(charName);
        }
        // Incrementing the processed chars
        charactersProcessed++;
        // Checking the processed chars
        if (charactersProcessed === characters.length) {
          // when all the chars have been processed, log the char
          characterNames.forEach((actor) => {
            console.log(actor);
          });
        }
      });
    });
  } else {
    console.log(error);
  }
});
