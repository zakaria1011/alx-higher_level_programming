#!/usr/bin/node
const x = parseInt(Math.floor(Number(process.argv[2])));
if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
