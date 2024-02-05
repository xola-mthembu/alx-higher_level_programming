#!/usr/bin/python3
"""
Module 11-square - Contains a class Square that inherits from Rect.
Updates the string representation to specify 'Square'.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, inheriting functionalities from Rect.
    """
    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the Square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return the square description: [Square] <width>/<height>.
        """
        return f"[Square] {self.__size}/{self.__size}"
