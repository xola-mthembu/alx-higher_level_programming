#!/usr/bin/python3
"""Module for Square class.

This module provides a Square class with a private instance attribute 'size'.
"""


class Square:
    """Class that defines a square.

    This class has a private instance attribute 'size' which is crucial for
    various computations and functionalities of a square.

    Attributes:
        __size (int): The size of a square.
    """

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
