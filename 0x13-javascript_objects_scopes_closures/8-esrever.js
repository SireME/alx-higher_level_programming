#!/usr/bin/node

// return reversed version of list

exports.esrever = function (list) {
  let temp, end;
  end = list.length - 1;
  for (let i = 0; i < parseInt(list.length / 2); i++) {
    temp = list[i];
    list[i] = list[end];
    list[end] = temp;
    end--;
  }
  return list;
};
