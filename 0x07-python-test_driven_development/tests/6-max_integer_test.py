#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ unnitest testing """
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([2, 2, 2, 2, 2]), 2)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1000000, 999999, 10000000]), 10000000)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

if __name__ == '__main__':
    unittest.main()
