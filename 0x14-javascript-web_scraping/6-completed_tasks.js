#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error', error);
    return;
  }
  const todos = JSON.parse(body);
  const completedTask = {};
  todos.forEach(todo => {
    if (todo.completed) {
      if (completedTask[todo.userId]) {
        completedTask[todo.userId]++;
      } else {
        completedTask[todo.userId] = 1;
      }
    }
  });
  console.log(completedTask);
});
