#!/usr/bin/python3
"""
Module 10-square - Contains a class Square that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    A class that represents a square, inheriting from Rectangle.
    """
    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)  # Initialize Rectangle with size as both width and height
        self.__size = size

    def area(self):
        """
        Calculate the area of the Square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return the Square description as a Rectangle format.
        """
        return super().__str__()
