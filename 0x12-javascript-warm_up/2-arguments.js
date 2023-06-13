#!/usr/bin/node

const proc = process.argv;
// console.log(proc);
const myArgLen = proc.length;
if (myArgLen === 2) {
  console.log('No argument');
} else if (myArgLen === 3) {
  console.log('Argument found');
} else if (myArgLen > 3) {
  console.log('Arguments found');
}
