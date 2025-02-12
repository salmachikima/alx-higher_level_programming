#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, _res, body) {
  if (err) {
    console.log(err);
  } else {
    const completedTasksByUsers = {};
    body = JSON.parse(body);

    for (let s = 0; s < body.length; ++s) {
      const userId = body[s].userId;
      const completed = body[s].completed;

      if (completed && !completedTasksByUsers[userId]) {
        completedTasksByUsers[userId] = 0;
      }

      if (completed) ++completedTasksByUsers[userId];
    }

    console.log(completedTasksByUsers);
  }
});
