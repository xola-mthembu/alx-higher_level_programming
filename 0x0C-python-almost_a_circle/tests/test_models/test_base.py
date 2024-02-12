#!/usr/bin/python3
"""
Unit test for the Base class.
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Tests the functionality of the Base class.
    """
    def test_instance(self):
        """
        Test instantiation of the Base class.
        """
        instance = Base()
        self.assertIsInstance(instance, Base)


if __name__ == "__main__":
    unittest.main()
