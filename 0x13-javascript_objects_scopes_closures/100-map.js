#!/usr/bin/node
const { list } = require('./100-data');

const nlist = list.map((value, index) => value * index);

console.log("Initial list:", list);
console.log("New list:", nlist);
