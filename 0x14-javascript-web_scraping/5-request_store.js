#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const getUrl = process.argv[2];
const storeIn = process.argv[3];

request(getUrl, (err, resp, body) => {
  if (err) { console.log(err); } else {
    fs.writeFile(storeIn, body, 'utf-8', (error) => {
      if (error) { console.log(error); }
    });
  }
});
