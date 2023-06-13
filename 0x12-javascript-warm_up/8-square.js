#!/usr/bin/node

const myArgs = process.argv[2];
const parsed = parseInt(myArgs);
const k = 'X';
if (parsed) {
  for (let i = 0; i < parsed; i++) {
    console.log(k.repeat(parsed));
  }
} else if (!parsed) {
  console.log('Missing size');
}
