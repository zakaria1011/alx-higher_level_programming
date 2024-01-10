#!/usr/bin/node
const Data = require('./101-data').dict;
occurDict = {};
for (key in Data) {
  const val = Data[key];
  if (!(val in occurDict)) {
    occurDict[val] = [];
  }
  occurDict[val].push(key.toString());
}
console.log(occurDict);
