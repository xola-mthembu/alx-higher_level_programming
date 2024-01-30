#!/usr/bin/python3
"""
This module provides an add_integer function that adds two numbers.
"""


def add_integer(a, b=98):
    """
    Return the addition of a and b as integers.
    Raises:
        TypeError: If a or b is neither an integer nor a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
