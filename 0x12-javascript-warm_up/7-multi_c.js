#!/usr/bin/node

const myArgs = process.argv[2];
const parsed = parseInt(myArgs);
if (parsed) {
  for (let i = 0; i < parsed; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
