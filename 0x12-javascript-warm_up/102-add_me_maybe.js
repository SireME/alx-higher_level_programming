#!/usr/bin/node

// execute theFunction x times

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
