#!/usr/bin/python3
"""Module for Square class.

This module provides a Square class with a private instance attribute 'size'
and methods to retrieve, update, calculate the area, and print the square.
"""


class Square:
    """Class that defines a square.

    This class has a private instance attribute 'size' with a property and
    a property setter to retrieve and update its value. The size must be an
    integer and greater than or equal to 0. It also includes a method to
    calculate the area and print the square using the '#' character.

    Attributes:
        __size (int): The size of the square, must be an integer and >= 0.
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square, defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Update the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character #.

        Prints the square using the '#' character. If the size is 0, it prints
        an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
