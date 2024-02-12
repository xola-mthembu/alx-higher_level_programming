#!/usr/bin/python3
"""
This module provides a Square class that inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, inheriting from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns the string representation of the Square instance.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
