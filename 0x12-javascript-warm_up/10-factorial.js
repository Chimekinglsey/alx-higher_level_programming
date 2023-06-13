#!/usr/bin/node

function fact (a) {
  if (a === 1) { return 1; } else {
    return (a * fact(a - 1));
  }
}
const args = process.argv;
const a = parseInt(args[2]);
if (!args[2] || !a) {
  console.log(1);
} else {
  console.log(fact(a));
}
