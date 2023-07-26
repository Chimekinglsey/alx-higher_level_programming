#!/usr/bin/node
const fs = require('fs');
const arg = process.argv[2]; // process.argv[0] is "node", process.argv[1] is the script file, so the first argument is at index 2.

fs.readFile(arg, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
