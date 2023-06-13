#!/usr/bin/node

const myArgV = process.argv;
if (!myArgV[2]) {
  console.log('No argument');
} else if (myArgV[2]) {
  console.log(myArgV[2]);
}
