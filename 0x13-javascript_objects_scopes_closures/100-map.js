#!/usr/bin/node
const importedList = require('./100-data');
const newList = importedList.list.map((num, index) => {
  return num * index;
});
console.log(importedList.list);
console.log(newList);
