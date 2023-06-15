#!/usr/bin/node
const { dict } = require('./101-data.js');

const newDict = Object.entries(dict).reduce((acc, [userId, occurrence]) => {
  if (acc[occurrence]) {
    acc[occurrence].push(userId);
  } else {
    acc[occurrence] = [userId];
  }
  return acc;
}, {});

console.log(newDict);

