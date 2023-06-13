#!/usr/bin/node

const args = process.argv;
if (!args[2] || (parseInt(args[2], 10) === 'NaN')) {
  console.log('Not a number');
} else if (parseInt(args[2], 10)) {
  console.log('My Number: ' + parseInt(args[2], 10));
}
