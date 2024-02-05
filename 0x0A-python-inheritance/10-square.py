#!/usr/bin/python3
"""
Module 10-square - Contains a class Square that inherits from Rect.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, inheriting from Rectangle.
    """
    def __init__(self, size):
        """
        Initialize a new Square with size validated by int_validator.
        """
        # Validate and initialize Square as Rectangle with equal sides
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
        Return the Square description as Rectangle format.
        """
        return super().__str__()
