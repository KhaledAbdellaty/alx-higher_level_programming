#!/usr/bin/node
const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, response, body) => {
  if (err) console.error(err);
  else {
    if (response.statusCode === 200) console.log(JSON.parse(body).title);
    else console.error('Error code: ' + response.statusCode);
  }
});
