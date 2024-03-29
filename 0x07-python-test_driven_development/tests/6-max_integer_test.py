#!/usr/bin/python3
"""Unittest for max_integer([..])."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test with an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with the max integer at the beginning."""
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)

    def test_one_element(self):
        """Test with a single element in the list."""
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Test with a list of negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_non_integers(self):
        """Test with a list of non-integer elements."""
        with self.assertRaises(TypeError):
            max_integer(["Hello", "World"])


if __name__ == "__main__":
    unittest.main()
