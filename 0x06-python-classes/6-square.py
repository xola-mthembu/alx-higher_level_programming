#!/usr/bin/python3
"""Module for Square class.

This module provides a Square class with private instance attr 'size'
and 'position', and methods to retrieve, update, calculate the area, and
print the square.
"""


class Square:
    """Class that defines a square.

    This class has private instance attr 'size' and 'position' with
    properties and property setters. The size must be an integer >= 0, and
    position must be a tuple of 2 positive integers.

    Attributes:
        __size (int): The size of the square, must be an integer and >= 0.
        __position (tuple): The position of the square as a tuple of 2 ints.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of new square, defaults to 0.
            position (tuple): The position of new square, defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Update the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If 'value' is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character #.

        Prints the square using the '#' character at its position. If the size
        is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            [print() for _ in range(self.__position[1])]
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
