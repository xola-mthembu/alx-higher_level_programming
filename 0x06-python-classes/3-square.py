#!/usr/bin/python3
"""Module for Square class.

This module provides a Square class with a private instance attribute 'size'
and a public method to calculate the area of the square.
"""


class Square:
    """Class that defines a square.

    This class has a private instance attribute 'size' and a method to calculate
    the area of the square.

    Attributes:
        __size (int): The size of the square, must be an integer and >= 0.
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square, defaults to 0.

        Raises:
            TypeError: If 'size' is not an integer.
            ValueError: If 'size' is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
