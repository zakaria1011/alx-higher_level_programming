#!/usr/bin/node
const request = require('request');
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error', error);
    return;
  }
  const description = JSON.parse(body);
  const actors = description.characters;
  actors.forEach(actor => {
    request(actor, (error, response, body) => {
      if (error) {
        console.error('Error', error);
        return;
      }
      actor_name = JSON.parse(body).name;
      console.log(actor_name);
    });
  });
});
