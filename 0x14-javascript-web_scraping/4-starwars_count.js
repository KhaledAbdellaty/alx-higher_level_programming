#!/usr/bin/node
const request = require("request");
request(process.argv[2], (err, response, body) => {
	if (err) console.error(err);
	else {
		if (response.statusCode == 200) {
			const results = JSON.parse(body).results;
			console.log(results.reduce((count, movie) => {
				return movie.characters.find((character) => character.endsWith('/18/'))
					? count + 1
					: count;
			}, 0));
		}
		else console.error('Error code: ' + response.statusCode);
	}
});
