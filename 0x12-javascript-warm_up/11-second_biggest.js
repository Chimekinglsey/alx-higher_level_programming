#!/usr/bin/node

function sorter (array) {
  let temp;
  for (let k = 0; k < array.length - 1; k++) {
    for (let j = 0; j < array.length - 1; j++) {
      if (array[j] > array[j + 1]) {
        temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
      }
    }
  }
  return array;
}

const args = process.argv;
const newArray = [];
let j = 0;
if (args.length > 2) {
  for (let i = 2; i < args.length; i++) {
    newArray[i - 2] = Number(args[i]);
  }
  const arrays = sorter(newArray);
  while (j < arrays.length) {
    j++;
  }
  console.log(arrays[j - 2]);
} else {
  console.log(0);
}
