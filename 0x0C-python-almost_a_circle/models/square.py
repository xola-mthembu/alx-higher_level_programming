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

    @property
    def size(self):
        """
        Gets the size of the Square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the Square, applying the same validation as width.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns the string representation of the Square instance.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """
        Updates the Square attributes with non-keyword
        arguments first, then keyword arguments.
        """
        # Implementation of update method unchanged...

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
