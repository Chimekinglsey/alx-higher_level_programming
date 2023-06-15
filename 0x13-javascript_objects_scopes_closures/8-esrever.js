#!/usr/bin/node
exports.esrever = function (list) {
  let last = list.length - 1;
  const reversed = [];
  for (let i = 0; i < list.length; i++) {
    reversed[i] = list[last];
    last--;
  }
  return reversed;
};
