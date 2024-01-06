#!/usr/bin/python3
"""Unit tests for the max_integer function."""

import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_value_positive_numbers(self):
        """Test max_integer with a list of positive integers."""
        result = max_integer([6, 7, 8, 9])
        self.assertEqual(result, 9)

    def test_max_value_empty_list(self):
        """Test max_integer with an empty list."""
        result = max_integer([])
        self.assertEqual(result, None)

    def test_max_value_single_element(self):
        """Test max_integer with a list containing a single element."""
        result = max_integer([2])
        self.assertEqual(result, 2)

    def test_max_value_single_negative_element(self):
        """Test max_integer with a list containing a single negative element."""
        result = max_integer([-10])
        self.assertEqual(result, -10)

    def test_max_value_mixed_positive_negative(self):
        """Test max_integer with a list containing both positive and negative numbers."""
        result = max_integer([1, -2, -3, -4])
        self.assertEqual(result, 1)

    def test_max_value_in_middle(self):
        """Test max_integer with the maximum value in the middle of the list."""
        result = max_integer([1, 3, 8, 2, 6])
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()

