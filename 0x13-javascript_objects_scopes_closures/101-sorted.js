#!/usr/bin/node
/*
 * Write a script that imports a di
 * ctionary of occurrences by user id
 * and computes a dictionary of user ids by occurrence.
 * Your script must import dict from the file 101-data.js
 * In the new dictionary:
 * A key is a number of occurrences
 * A value is the list of user ids
 * Print the new dictionary at the end
 */

const ndic = require('./101-data.js').dict;
// manipulate imported dictionary for sorted

// get list of values from object dictionary and make them unique
const values = Object.values(ndic);
// convert to set to make unique
const uniqueSet = new Set(values);
// convert back to unique list
const uvalues = [...uniqueSet];

// new object(dictionary) to be constucted
const nobj = {};

// loop through unique values contructing list of IDs
for (let i = 0; i < uvalues.length; i++) {
  nobj[String(uvalues[i])] = [];
  for (const key in ndic) {
    if (ndic[key] === uvalues[i]) {
      nobj[String(uvalues[i])].push(String(key));
    }
  }
}

// print dictionarry of Ids
console.log(nobj);
