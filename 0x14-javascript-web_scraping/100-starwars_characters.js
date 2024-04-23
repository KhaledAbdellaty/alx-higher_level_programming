#!/usr/bin/node
const request = require('request');
request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, response, body) => {
  if (err) console.error(err);
  else {
    if (response.statusCode === 200) {
      const data = JSON.parse(body);
      data.characters.forEach((character) => {
        request(character, (err, response, body) => {
          if (err) {
            console.error(err);
          } else if (response) {
            const data = JSON.parse(body);
            console.log(data.name);
          }
        });
      });
    }
  }
});
