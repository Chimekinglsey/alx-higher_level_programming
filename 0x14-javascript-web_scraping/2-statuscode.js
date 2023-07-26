#!/usr/bin/node
const req = require('request');
const url = process.argv[2];
req.get(url).on('response', (response) => {
  console.log(`code: ${response.statusCode}`);
});
