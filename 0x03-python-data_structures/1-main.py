#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 10
idx2 = -2
idx3 = 2
print(my_list)
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
print("Element at index {:d} is {}".format(idx2, element_at(my_list, idx2)))
print("Element at index {:d} is {}".format(idx3, element_at(my_list, idx3)))
