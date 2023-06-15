#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
if (args.length === 4) {
const readFile1 = fs.readFileSync(args[2], "utf-8");
const readFile2 = fs.readFileSync(args[3], "utf-8");
const fileC = readFile1 + readFile2;
fs.writeFileSync('fileC.txt', fileC, "utf-8");
}


