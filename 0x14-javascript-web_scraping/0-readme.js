#!/usr/bin/node
const fs = require('fs');
const arg1 = process.argv[2];
fs.readFile(arg1, 'utf-8', function (error, data) {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
