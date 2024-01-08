#!/usr/bin/node
function computeFactorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    return n * computeFactorial(n - 1);
  }
}

const num = parseInt(process.argv[2]);

console.log(computeFactorial(num));
