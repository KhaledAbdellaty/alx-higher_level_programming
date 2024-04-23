#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response) {
    const data = JSON.parse(body);
    const todos = {};
    data.forEach((task) => {
      if (task.completed) {
        if (!todos[task.userId]) {
          todos[task.userId] = 1;
        } else {
          todos[task.userId] += 1;
        }
      }
    });
    console.log(todos);
  }
});
