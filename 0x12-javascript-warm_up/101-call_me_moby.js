#!/usr/bin/node

// execute theFunction x times

exports.callMeMoby = function (x, theFunction) {
  for (let i = 1; i <= x; i++) {
    theFunction();
  }
};
