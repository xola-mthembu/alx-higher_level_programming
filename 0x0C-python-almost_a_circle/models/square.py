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
        attrs = ['id', 'size', 'x', 'y']
        if args and len(args) > 0:
            for attr, arg in zip(attrs, args):
                if attr == 'size':
                    setattr(self, 'width', arg)
                    setattr(self, 'height', arg)
                else:
                    setattr(self, attr, arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                elif key in attrs:
                    setattr(self, key, value)
