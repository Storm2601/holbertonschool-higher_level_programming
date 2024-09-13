#!/usr/bin/python3
"""Unit tests for the max_integer function from 6-max_integer.py"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test case for the max_integer function"""

    def test_empty_list(self):
        """Test when the list is empty; should return None"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test when the list contains only one element"""
        self.assertEqual(max_integer([2]), 2)

    def test_same(self):
        """Test when all values in the list are the same"""
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_with_floats(self):
        """Test when the list contains floating-point numbers"""
        self.assertEqual(max_integer([1.32, 1.21, 3.45]), 3.45)

    def test_string(self):
        """Test when the input is a string;
        should return the highest character"""
        self.assertEqual(max_integer("test"), "t")

    def test_negative_and_positive(self):
        """Test when the list contains both negative and positive values"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_negative(self):
        """Test when all values in the list are negative"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_at_beginning(self):
        """Test when the maximum value is at the beginning of the list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_at_middle(self):
        """Test when the maximum value is in the middle of the list"""
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_max_at_end(self):
        """Test when the maximum value is at the end of the list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
