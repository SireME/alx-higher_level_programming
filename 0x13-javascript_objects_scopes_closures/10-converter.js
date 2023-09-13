#!.usr/bin/node

// convert number from base 10 to another

exports.converter = function (base) {
  function numberToConvert (nc) {
    return nc.toString(base);
  }
  return numberToConvert;
};
