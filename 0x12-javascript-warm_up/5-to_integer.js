#!/usr/bin/node
const firstArg = process.argv[2];
const converArg = parseInt(firstArg);
if (!isNaN(converArg)) {
  console.log(`My number: ${converArg}`);
} else {
  console.log('Not a number');
}
