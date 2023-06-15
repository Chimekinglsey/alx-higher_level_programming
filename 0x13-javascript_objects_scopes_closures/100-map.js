#!/usr/bin/node
const { list } = require('./100-data');
const newList = list.map((ele, index, list) => ele * index);

console.log(list);
console.log(newList);
